from playwright.sync_api import sync_playwright
import sys
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    for slug, name in [("f3fc312c", "Getting Started"), ("c7f102c7", "Davids Corner")]:
        print(f"\n{'='*60}")
        print(f"{name} ({slug})")
        print(f"{'='*60}")
        page.goto(f"https://www.skool.com/cliefnotes/classroom/{slug}", timeout=20000, wait_until="domcontentloaded")
        page.wait_for_timeout(5000)

        # Analyze sidebar structure
        sidebar_info = page.evaluate("""
        (slug) => {
            const wrappers = document.querySelectorAll('.styled__MenuItemWrapper-sc-1wvgzj7-10');
            const items = [];
            wrappers.forEach((w, i) => {
                const titleEl = w.querySelector('.styled__MenuItemTitle-sc-1wvgzj7-8');
                const text = titleEl ? titleEl.textContent.trim() : '';
                const links = w.querySelectorAll('a');
                const hrefs = [];
                links.forEach(l => {
                    const h = l.getAttribute('href');
                    if (h && h.includes('/classroom/' + slug)) hrefs.push(l.textContent.trim().substring(0, 40));
                });
                items.push({idx: i, text: text.substring(0, 50), links: hrefs.length, hrefList: hrefs.join(', ')});
            });
            return items;
        }
        """, slug)

        print("Sidebar structure:")
        for item in sidebar_info:
            link_info = f" [{item['links']} links: {item['hrefList']}]" if item['links'] > 0 else ""
            print(f"  [{item['idx']}] {item['text']}{link_info}")

        # Also check what happens when clicking sidebar items
        print("\nClicking sidebar items to reveal structure...")
        for attempt in range(3):
            n = page.evaluate("""
            (slug) => {
                const wrappers = document.querySelectorAll('.styled__MenuItemWrapper-sc-1wvgzj7-10');
                let clicked = 0;
                for (const w of wrappers) {
                    const titleEl = w.querySelector('.styled__MenuItemTitle-sc-1wvgzj7-8');
                    if (!titleEl) continue;
                    const text = titleEl.textContent.trim();
                    const links = w.querySelectorAll('a[href*="/classroom/' + slug + '"]');
                    if (text && text.length > 2 && text.length < 60 && links.length === 0) {
                        // Try clicking
                        const clickable = w.querySelector('.styled__MenuItemTitleWrapper-sc-1wvgzj7-6');
                        if (clickable) {
                            clickable.click();
                            clicked++;
                        }
                    }
                }
                return clicked;
            }
            """, slug)
            if n == 0:
                break
            page.wait_for_timeout(500)

        page.wait_for_timeout(1000)

        # Check again
        sidebar_info2 = page.evaluate("""
        (slug) => {
            const wrappers = document.querySelectorAll('.styled__MenuItemWrapper-sc-1wvgzj7-10');
            const items = [];
            wrappers.forEach((w, i) => {
                const titleEl = w.querySelector('.styled__MenuItemTitle-sc-1wvgzj7-8');
                const text = titleEl ? titleEl.textContent.trim() : '';
                const links = w.querySelectorAll('a[href*="/classroom/' + slug + '"]');
                const hrefs = [];
                links.forEach(l => hrefs.push(l.textContent.trim().substring(0, 40)));
                items.push({idx: i, text: text.substring(0, 50), links: links.length, hrefList: hrefs.join(', ')});
            });
            return items;
        }
        """, slug)

        print("\nAfter clicking:")
        for item in sidebar_info2:
            link_info = f" [{item['links']} links: {item['hrefList']}]" if item['links'] > 0 else ""
            print(f"  [{item['idx']}] {item['text']}{link_info}")

    browser.close()
