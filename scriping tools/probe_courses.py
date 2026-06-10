from playwright.sync_api import sync_playwright
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    page.goto("https://www.skool.com/cliefnotes/classroom", timeout=15000)
    page.wait_for_timeout(4000)

    data = page.evaluate("""
    () => {
        const scripts = document.querySelectorAll('script[type="application/json"]');
        for (const s of scripts) {
            try {
                return JSON.parse(s.textContent);
            } catch(e) {}
        }
        return {};
    }
    """)

    courses = data.get('props', {}).get('pageProps', {}).get('renderData', {}).get('allCourses', [])

    print("=== ALL COURSES (accessible) ===")
    accessible = []
    for c in courses:
        meta = c.get('metadata', {})
        name = meta.get('title', c.get('name', 'Unknown'))
        cid = c.get('name', '')
        has_access = meta.get('hasAccess', 0)
        num_modules = meta.get('numModules', 0)
        if has_access and cid != '036893d9':
            accessible.append((name, cid, num_modules))
            print(f"  {name:40s} slug={cid}  modules={num_modules}")

    print(f"\n=== SKIPPING (no access) ===")
    for c in courses:
        meta = c.get('metadata', {})
        name = meta.get('title', c.get('name', 'Unknown'))
        cid = c.get('name', '')
        has_access = meta.get('hasAccess', 0)
        if not has_access:
            print(f"  {name:40s} slug={cid}")

    print(f"\n=== ALREADY DONE ===")
    print(f"  The Foundation (036893d9)")

    print(f"\nCourses to scrape next: {len(accessible)}")
    for name, cid, _ in accessible:
        print(f"  {name} -> /classroom/{cid}")

    browser.close()
