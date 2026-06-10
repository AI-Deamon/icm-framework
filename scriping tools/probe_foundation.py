from playwright.sync_api import sync_playwright
import sys
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    page.goto("https://www.skool.com/cliefnotes/classroom/036893d9", timeout=15000)
    page.wait_for_timeout(5000)

    # Find module headers in the sidebar - elements that are headers for collapsible sections
    info = page.evaluate("""
    () => {
        const results = [];
        const allElements = document.querySelectorAll('div, span, h1, h2, h3, h4, button, a');
        for (const el of allElements) {
            const text = el.textContent.trim();
            if (!text || text.length < 3 || text.length > 100) continue;
            // Look for module patterns
            if (text.match(/^Module \d/) || text.match(/^SECTION \d/)) {
                const rect = el.getBoundingClientRect();
                const parent = el.parentElement;
                results.push({
                    text: text,
                    tag: el.tagName,
                    class: el.className.substring(0, 60),
                    rect: `${rect.width.toFixed(0)}x${rect.height.toFixed(0)}`,
                    parentTag: parent ? parent.tagName : '',
                    parentClass: parent ? parent.className.substring(0, 60) : '',
                    role: el.getAttribute('role') || '',
                    tabindex: el.getAttribute('tabindex') || '',
                    onclick: el.getAttribute('onclick') ? 'yes' : '',
                    cursor: getComputedStyle(el).cursor
                });
            }
        }
        return results;
    }
    """)

    print("=== MODULE HEADERS ===")
    for item in info:
        print(f"  {item['text']}")
        print(f"    Tag: {item['tag']}  Class: {item['class']}")
        print(f"    Parent: {item['parentTag']}  ParentClass: {item['parentClass']}")
        print(f"    Role: {item['role']}  TabIndex: {item['tabindex']}  Cursor: {item['cursor']}")
        print()

    # Get all lesson links from sidebar with their md params
    print("=== SIDEBAR LESSON LINKS ===")
    sidebar_lessons = page.evaluate("""
    () => {
        const results = [];
        const links = document.querySelectorAll('a');
        for (const link of links) {
            const href = link.getAttribute('href');
            const text = link.textContent.trim();
            if (href && href.includes('/classroom/036893d9') && text && text.length > 2) {
                results.push({text: text, href: href});
            }
        }
        return results;
    }
    """)
    for l in sidebar_lessons:
        print(f"  {l['text']:60s}  {l['href']}")

    browser.close()
