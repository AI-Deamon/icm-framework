from playwright.sync_api import sync_playwright
from markdownify import markdownify as md
from pathlib import Path
import re, sys, json

sys.stdout.reconfigure(encoding='utf-8')
BASE = "https://www.skool.com"
OUTPUT_DIR = Path("./skool_lessons")

def sanitize(name):
    return re.sub(r'[<>:"/\\|?*]', '', name).strip().rstrip('. ')[:80]

def discover_courses(page):
    """Get list of accessible courses from the classroom page."""
    page.goto(f"{BASE}/cliefnotes/classroom", timeout=20000, wait_until="domcontentloaded")
    page.wait_for_timeout(5000)

    data = page.evaluate("""() => { const s = document.querySelectorAll('script[type="application/json"]'); for (const x of s) { try { return JSON.parse(x.textContent); } catch(e) {} } return {}; }""")
    courses = data.get('props', {}).get('pageProps', {}).get('renderData', {}).get('allCourses', [])

    result = []
    for c in courses:
        meta = c.get('metadata', {})
        name = meta.get('title', '')
        cid = c.get('name', '')
        has_access = meta.get('hasAccess', 0)
        if name and cid and has_access:
            result.append({"name": name, "slug": cid})
    return result

def expand_all_sidebar(page, course_slug):
    """Click all collapsed sidebar items to reveal hidden lessons."""
    for attempt in range(5):
        n = page.evaluate("""
        (slug) => {
            const wrappers = document.querySelectorAll('.styled__MenuItemWrapper-sc-1wvgzj7-10');
            let clicked = 0;
            for (const w of wrappers) {
                const clickable = w.querySelector('.styled__MenuItemTitleWrapper-sc-1wvgzj7-6');
                if (!clickable) continue;
                const text = clickable.textContent.trim();
                if (!text || text.length < 2 || text.length > 60) continue;
                const links = w.querySelectorAll('a[href*="/classroom/' + slug + '"]');
                if (links.length === 0) {
                    clickable.click();
                    clicked++;
                }
            }
            return clicked;
        }
        """, course_slug)
        if n == 0:
            break
        page.wait_for_timeout(600)

def get_structure(page, course_slug):
    """Extract module -> lessons structure from sidebar, handling all patterns."""
    return page.evaluate("""
    (slug) => {
        const wrappers = document.querySelectorAll('.styled__MenuItemWrapper-sc-1wvgzj7-10');
        const modules = [];
        let currentModule = null;

        for (const w of wrappers) {
            const titleEl = w.querySelector('.styled__MenuItemTitle-sc-1wvgzj7-8');
            const text = titleEl ? titleEl.textContent.trim() : '';
            if (!text || text.length < 2) continue;

            // Collect all classroom links in this wrapper
            const links = w.querySelectorAll('a');
            const lessonLinks = [];
            for (const l of links) {
                const h = l.getAttribute('href');
                if (h && (h.includes('/classroom/' + slug) || h.includes('classroom/' + slug + '?'))) {
                    lessonLinks.push({ text: l.textContent.trim(), href: h });
                }
            }

            // Determine if this wrapper IS a lesson (its title text matches one of its link texts)
            const isLesson = lessonLinks.some(link => link.text === text);

            if (isLesson) {
                if (!currentModule) {
                    // Create default module for orphan lessons
                    const prev = modules.length > 0 ? modules[modules.length - 1] : null;
                    if (prev && prev.name !== 'Module ' && !prev.name.startsWith('Module ') && !prev.name.startsWith('SECTION ')) {
                        currentModule = prev;
                    } else {
                        currentModule = { name: "Lessons", lessons: [] };
                        modules.push(currentModule);
                    }
                }
                // Find the exact link for this lesson
                const myLink = lessonLinks.find(l => l.text === text) || lessonLinks[0];
                let clean = myLink.href.startsWith('/') ? 'https://www.skool.com' + myLink.href : myLink.href;
                clean = clean.split('&utm_')[0];
                currentModule.lessons.push({ title: text, url: clean });
            } else if (lessonLinks.length > 0 || text.startsWith('Module ') || text.startsWith('SECTION ') || text.length < 50) {
                // This is a section/module header
                if (!text.startsWith('Module ') && !text.startsWith('SECTION ')) {
                    // Check all links inside to see if they're child items
                    // Section headers can contain links to their child lessons
                    // Only create a new module if the name is different from current
                }
                if (!currentModule || text !== currentModule.name) {
                    currentModule = { name: text, lessons: [] };
                    modules.push(currentModule);
                }
            }
        }

        // Remove empty modules and deduplicate
        const result = [];
        for (const mod of modules) {
            if (mod.lessons.length > 0) {
                const seen = new Set();
                mod.lessons = mod.lessons.filter(l => {
                    if (seen.has(l.url)) return false;
                    seen.add(l.url);
                    return true;
                });
                result.push(mod);
            }
        }
        return result;
    }
    """, course_slug)

def expand_and_get_structure(page, course_url, course_slug):
    """Navigate to course, expand modules, extract lesson structure."""
    page.goto(course_url, timeout=20000, wait_until="domcontentloaded")
    page.wait_for_timeout(5000)

    expand_all_sidebar(page, course_slug)
    page.wait_for_timeout(1000)

    structure = get_structure(page, course_slug)

    # Retry once if empty (some courses may need more clicks)
    if not structure or all(len(m['lessons']) == 0 for m in structure):
        page.wait_for_timeout(2000)
        expand_all_sidebar(page, course_slug)
        page.wait_for_timeout(1000)
        structure = get_structure(page, course_slug)

    return structure

def scrape_lesson(browser, url, retries=2):
    """Visit a lesson and return (title, markdown). Uses isolated context per call."""
    for attempt in range(retries + 1):
        ctx = None
        page = None
        try:
            ctx = browser.new_context(
                no_viewport=True,
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            page = ctx.new_page()
            page.goto(url, timeout=30000, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)

            title = page.evaluate("""() => { const h1 = document.querySelector('h1'); if (h1) return h1.textContent.trim(); return document.title.split('·')[0].trim(); }""")
            html = page.evaluate("""() => { const el = document.querySelector("[contenteditable='false'][translate='no'].tiptap.ProseMirror"); if (el) return el.innerHTML; const fb = document.querySelector('[class*="ModuleBody"]') || document.querySelector('[class*="EditorContent"]'); return fb ? fb.innerHTML : ''; }""")

            if not html:
                raise Exception("No content found")

            md_c = md(html, heading_style="ATX")
            md_c = re.sub(r'\n{3,}', '\n\n', md_c.strip())
            return title, md_c
        except Exception as e:
            if attempt == retries:
                raise
            print(f"    Retry {attempt+1}/{retries}: {e}")
        finally:
            if page:
                try: page.close()
                except: pass
            if ctx:
                try: ctx.close()
                except: pass
    raise Exception("All retries exhausted")

def with_new_page(browser):
    """Create a fresh page."""
    return browser.new_page(viewport={"width": 1280, "height": 900})

# ============================================================

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = with_new_page(browser)

    courses = discover_courses(page)
    page.close()
    print(f"Found {len(courses)} accessible courses:")
    for c in courses:
        print(f"  {c['name']:40s} [{c['slug']}]")

    total_lessons = 0
    for course in courses:
        course_slug = course['slug']
        course_name = course['name']
        course_url = f"{BASE}/cliefnotes/classroom/{course_slug}"
        course_dir = OUTPUT_DIR / sanitize(course_name)

        print(f"\n{'='*70}")
        print(f"COURSE: {course_name} ({course_slug})")
        print(f"{'='*70}")

        # Fresh page per course to avoid navigation conflicts
        page = with_new_page(browser)
        try:
            structure = expand_and_get_structure(page, course_url, course_slug)
        except Exception as e:
            print(f"  Failed to load course: {e}")
            page.close()
            continue
        page.close()

        if not structure:
            print("  No modules/lessons found!")
            continue

        lesson_count = sum(len(m['lessons']) for m in structure)
        total_lessons += lesson_count
        print(f"  {len(structure)} modules, {lesson_count} lessons")

        for mod in structure:
            print(f"    {mod['name']} ({len(mod['lessons'])} lessons)")

        # Scrape each lesson
        count = 0
        for mod in structure:
            mod_dir = course_dir / sanitize(mod['name'])
            mod_dir.mkdir(parents=True, exist_ok=True)

            for lesson in mod['lessons']:
                count += 1
                print(f"\n  [{count}/{lesson_count}] {lesson['title']}")
                try:
                    t, md_c = scrape_lesson(browser, lesson['url'])
                    (mod_dir / (sanitize(lesson['title']) + ".md")).write_text(
                        f"# {t}\n\n{md_c}", encoding="utf-8"
                    )
                    print(f"    SAVED")
                except Exception as e:
                    print(f"    FAILED: {e}")
                    (mod_dir / (sanitize(lesson['title']) + ".md")).write_text(
                        f"# {lesson['title']}\n\nERROR: {e}\nURL: {lesson['url']}", encoding="utf-8"
                    )

    browser.close()

    print(f"\n{'='*70}")
    print(f"ALL DONE! {total_lessons} lessons across {len(courses)} courses")
    print(f"{'='*70}")
    for course in courses:
        d = OUTPUT_DIR / sanitize(course['name'])
        if d.exists():
            mods = [p.name for p in d.iterdir() if p.is_dir()]
            print(f"  {course['name']}/ ({len(mods)} modules)")
