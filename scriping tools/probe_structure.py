from playwright.sync_api import sync_playwright
import sys
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    page.goto("https://www.skool.com/cliefnotes/classroom/036893d9", timeout=15000)
    page.wait_for_timeout(4000)

    # Click each module to expand, then collect ALL lesson links
    modules_expanded = page.evaluate("""
    () => {
        const results = [];
        const moduleTitles = document.querySelectorAll('.styled__MenuItemTitle-sc-1wvgzj7-8');
        moduleTitles.forEach((title, idx) => {
            results.push({
                index: idx,
                text: title.textContent.trim()
            });
        });
        return results;
    }
    """)

    print("=== MODULES FOUND ===")
    for m in modules_expanded:
        print(f"  [{m['index']}] {m['text']}")

    # Click each module title to expand it
    module_divs = page.locator(".styled__MenuItemTitle-sc-1wvgzj7-8")
    count = module_divs.count()
    print(f"\nTotal module divs: {count}")

    # Click each one to expand
    for i in range(count):
        mod = module_divs.nth(i)
        text = mod.inner_text()
        print(f"\nClicking [{i}]: {text}")
        mod.click()
        page.wait_for_timeout(500)

    # Now get ALL lesson links from sidebar
    page.wait_for_timeout(2000)
    
    all_lessons = page.evaluate("""
    () => {
        const results = [];
        // Get all module wrappers
        const wrappers = document.querySelectorAll('.styled__MenuItemWrapper-sc-1wvgzj7-10');
        wrappers.forEach((wrapper) => {
            const titleEl = wrapper.querySelector('.styled__MenuItemTitle-sc-1wvgzj7-8');
            const moduleName = titleEl ? titleEl.textContent.trim() : 'Unknown';
            
            // Find lesson links within this wrapper
            const links = wrapper.querySelectorAll('a[href*="/classroom/"]');
            const lessons = [];
            links.forEach(link => {
                const href = link.getAttribute('href');
                const text = link.textContent.trim();
                if (href && text && !text.includes('Module') && !text.includes('SECTION')) {
                    const fullUrl = href.startsWith('/') ? 'https://www.skool.com' + href : href;
                    // Clean URL (remove utm params)
                    const cleanUrl = fullUrl.split('&utm_')[0];
                    lessons.push({title: text, url: cleanUrl});
                }
            });
            
            if (lessons.length > 0) {
                results.push({module: moduleName, lessons: lessons});
            }
        });
        return results;
    }
    """)

    print("\n=== MODULE STRUCTURE ===")
    for m in all_lessons:
        print(f"\n  {m['module']}:")
        for l in m['lessons']:
            print(f"    - {l['title']}")
            print(f"      {l['url']}")

    if not all_lessons:
        print("No lessons found. Let me try a broader approach...")
        all_links = page.evaluate("""
        () => {
            const results = [];
            const links = document.querySelectorAll('a');
            for (const link of links) {
                const href = link.getAttribute('href');
                const text = link.textContent.trim();
                if (href && href.includes('/classroom/036893d9') && text && text.length > 2 && text.length < 80) {
                    const parent = link.closest('.styled__MenuItemWrapper-sc-1wvgzj7-10');
                    const moduleName = parent ? 
                        (parent.querySelector('.styled__MenuItemTitle-sc-1wvgzj7-8')?.textContent?.trim() || 'Unknown') 
                        : 'Unknown';
                    results.push({module: moduleName, title: text, url: href});
                }
            }
            return results;
        }
        """)
        for l in all_links:
            print(f"  [{l['module']}] {l['title']} -> {l['url']}")

    browser.close()
