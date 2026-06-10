import subprocess
import re
import os
import json
import sys
from pathlib import Path

YT_DLP = "yt-dlp"
OUTPUT_DIR = Path("D:/Pen/Framework/youtube_transcripts")

def get_video_info(url):
    result = subprocess.run(
        [YT_DLP, "--skip-download", "--print-json", url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ERROR getting info: {result.stderr.strip()}")
        return None
    for line in result.stdout.strip().split("\n"):
        if line.startswith("{"):
            return json.loads(line)
    return None

def download_srt(url, output_template):
    result = subprocess.run(
        [YT_DLP, "--skip-download", "--write-auto-subs", "--sub-lang", "en",
         "--sub-format", "vtt", "--convert-subs", "srt",
         "--js-runtimes", "node",
         "-o", output_template, url],
        capture_output=True, text=True
    )
    return result.returncode == 0

def srt_to_markdown(srt_path):
    with open(srt_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"\n\s*\n", content.strip())
    lines = []
    prev_text = ""
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        match = re.match(r"\d+\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+)", block, re.DOTALL)
        if not match:
            continue
        start, end, text = match.groups()
        text = text.replace("\n", " ").strip()

        if text == prev_text:
            continue
        prev_text = text

        ts = start.split(",")[0]
        if ts.startswith("00:"):
            ts = ts[3:]
        lines.append(f"`{ts}` {text}")

    return "\n".join(lines)

def sanitize_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:120]

def process_urls(urls):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    for i, url in enumerate(urls, 1):
        url_clean = re.sub(r'\?si=.*', '', url.strip())
        print(f"\n[{i}/{len(urls)}] {url_clean}")

        info = get_video_info(url_clean)
        if not info:
            print("  SKIP (could not fetch info)")
            continue

        title = info.get("title", f"video_{info['id']}")
        safe_title = sanitize_filename(title)
        print(f"  Title: {title}")

        srt_template = str(OUTPUT_DIR / f"{safe_title}.%(ext)s")
        ok = download_srt(url_clean, srt_template)
        if not ok:
            print("  ERROR downloading subtitles")
            continue

        srt_files = list(OUTPUT_DIR.glob(f"{safe_title}.en.srt"))
        if not srt_files:
            print("  WARNING: no .srt file found")
            continue

        srt_path = srt_files[0]
        md_content = srt_to_markdown(str(srt_path))

        upload_date = info.get("upload_date", "")
        date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}" if len(upload_date) == 8 else ""
        channel = info.get("channel", "")
        duration = info.get("duration_string", "")
        video_url = info.get("webpage_url", url_clean)

        header = f"# {title}\n\n"
        if channel:
            header += f"**Channel:** {channel}  \n"
        if date_str:
            header += f"**Uploaded:** {date_str}  \n"
        if duration:
            header += f"**Duration:** {duration}  \n"
        header += f"**URL:** [{video_url}]({video_url})  \n\n"
        header += "---\n\n## Transcript\n\n"

        md_path = srt_path.with_suffix(".md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(header + md_content)

        print(f"  Saved: {md_path.name}")
        srt_path.unlink()

def main():
    script_dir = Path(__file__).parent
    link_file = str(script_dir / "Youtube_links.txt")
    if not os.path.exists(link_file):
        print(f"Links file not found: {link_file}")
        sys.exit(1)

    with open(link_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if re.search(r'https?://', line)]
    
    print(f"Found {len(urls)} URLs to process")
    process_urls(urls)
    print(f"\nDone! Transcripts saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
