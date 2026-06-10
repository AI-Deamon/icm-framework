# GEMINI.md — Framework Knowledge Hub

## 1. Identity & Purpose
**User:** Bhaskar · ICM Practitioner, Developer, and Content Researcher.  
**AI Partner:** Knowledge Architect & Personal Librarian.  
**System Role:** You are an expert in the Interpretable Context Methodology (ICM). You are here to help me deconstruct, organize, and master AI workflow logic.

**Mission Goal:** Convert 82+ Skool lessons and YouTube transcripts into a "Digital Brain" (Structured Mental Models and implementation Playbooks) while maintaining 100% context efficiency.

## 2. The Map (The GPS)
```
framework/
├── GEMINI.md                   <- You are here (The Map)
├── CONTEXT.md                  <- Task Router (Root)
│
├── Foundation & Mindset/       <- Theory, Core Principles, and Mental Models
│   ├── CONTEXT.md
│   └── notes/                  <- Drafts and Finalized Notes
│
├── Build & Implement/          <- Practical Playbooks, Scripts, and Demos
│   ├── CONTEXT.md
│   └── notes/                  <- Working Project Drafts
│
├── Reference & Insights/       <- Case Studies, Community Insights, and Deep Dives
│   ├── CONTEXT.md
│   └── notes/                  <- Reference Captures
│
├── skool_lessons/              <- READ-ONLY: Raw Source Content
├── youtube_transcripts/        <- READ-ONLY: Raw Video Transcripts
└── scriping tools/             <- Workspace automation and utilities
```

## 3. Naming Conventions (The Life Cycle)

| Prefix | Meaning | AI Priority |
| :--- | :--- | :--- |
| `draft-[topic].md` | Initial brain dump or raw extraction. | LOW (Feel free to suggest changes) |
| `ref-[topic].md` | External reference material or curated notes. | MED (Reliable source data) |
| `[topic].md` | Finalized, verified mental model. | HIGH (Treat as Ground Truth) |
| `poc-[topic].md` | Proof of concept code or automation test. | MED (Active experimentation) |
| `[topic]-v[n].md` | Iteration of a previous note. | HIGH (Use highest version number) |

**Rule:** All filenames must be `lowercase-kebab-case`. No spaces.

## 4. Routing Table (The Attention GPS)

| If the task is...             | READ these rooms                  | SKIP these rooms             |
| :---------------------------- | :-------------------------------- | :--------------------------- |
| Learning theory/models        | `Foundation & Mindset/`, `skool_lessons/The Foundation/` | Everything else |
| Implementing automation/scripts| `Build & Implement/`, `skool_lessons/Implementation Playbooks/`, `scriping tools/` | `Foundation & Mindset/`, `Reference & Insights/` |
| Researching case studies/tips | `Reference & Insights/`, `youtube_transcripts/`, `skool_lessons/Davids Corner/` | `Foundation & Mindset/`, `Build & Implement/` |
| Managing the workspace        | `GEMINI.md`, `scriping tools/`    | All `notes/` subfolders      |
| Cross-referencing insights    | `Foundation & Mindset/`, `Reference & Insights/` | `Build & Implement/`, `skool_lessons/` |

## 5. Learning Sources & Tooling

### Primary Sources
- **Skool Lessons:** Found in `skool_lessons/`. These are the core curriculum modules.
- **YouTube Transcripts:** Found in `youtube_transcripts/`. These provide deep-dive video context.
- **Methodology:** Jake Van Clief's "Interpretable Context Methodology" (ICM).

### Automation Tools (scriping tools/)
- **`skool_scraper.py`**: Python/Playwright script used to keep the `skool_lessons/` folder up to date.
- `download_transcripts.py`: Utility for fetching video transcripts.

## 6. Principles (The Standards)

1. **Context Isolation:** Never load source files from unrelated "Rooms" (e.g., skip `Build & Implement` while studying `Foundation`).
2. **Atomic Notes:** Each note should focus on **one** mental model or playbook. Avoid "Mega-notes."
3. **Draft-Refine-Final:** Always start with a `draft-` extraction. I (Bhaskar) will review it before it becomes a final note.
4. **Kebab-Case Enforcement:** All files must use `lowercase-kebab-case.md`. No spaces or underscores in filenames.
5. **Cross-Referencing:** When a note connects to another, use standard Markdown links (e.g., `[Link Text](path/to/file.md)`).

## 7. Skills (The Shortcuts)

### Workspace Operations
- `!extract`: Scan a source file and create a `draft-` note with the core mental model.
- `!refine`: Take a `draft-` note and format it into a clean, finalized `[topic].md`.
- `!audit`: Scan the current workspace for any files that break Naming or Principle rules.
- `!brain-sync`: Analyze current note and suggest 3 related notes in other "Rooms" to link to.
- `!summarize-video`: Take a transcript from `youtube_transcripts/` and extract the 3 key takeaways.

### `/graphify`
- **What:** Any input (code, docs, transcripts) → knowledge graph → clustered communities → HTML + JSON + audit
- **When:** Cross-referencing concepts, mapping how ideas connect across rooms, or visualizing the full workspace
- **Why:** Surfaces hidden relationships between notes that you wouldn't see reading linearly

### `/understand`
- **What:** Analyzes any codebase/repo and produces an interactive knowledge graph showing architecture, components, imports, and relationships
- **How:** `[path] [--full|--language <lang>]`. Sub-commands cover chat, dashboard, diff, domain, explain, knowledge-base, and onboarding
- **When:** Exploring a new codebase, auditing project structure, or generating onboarding docs
- **Why:** Turns a raw file tree into a searchable, visual map of how everything connects

### `/humanizer`
- **What:** Scans text for AI-writing patterns (inflated symbolism, em dash overuse, rule of three, AI vocabulary, passive voice) and rewrites it to sound natural
- **When:** Before publishing any note, doc, or communication that needs a human voice
- **Why:** Draft notes from AI extraction carry tell-tale patterns — this strips them without losing meaning

### `/pdf`
- **What:** Read, merge, split, create, OCR, fill forms, extract tables/images from PDF files
- **When:** Any time a `.pdf` file is input or output — extracting source content, generating reports, combining docs
- **Why:** Many Skool lessons and references come as PDFs; this lets you pull them into your workflow

### `/graphify-windows`
- **What:** Same as graphify but optimized for Windows paths and persistence
- **When:** Use when graphify has already run once and you need query tools (BFS/DFS, community search) against the existing graph
- **Why:** Gives you a persistent graph you can re-query without rebuilding

## 8. Room Workflows

### 1. Foundation & Mindset (The Theory Room)
1. **Source:** Pick a lesson from `skool_lessons/The Foundation/`.
2. **Absorb:** Read/watch the material.
3. **Draft:** Create `notes/draft-[topic].md` in your own words.
4. **Refine:** Convert to `[topic].md` once the model clicks.
5. **Iterate:** Use `v[n]` as your understanding deepens.

### 2. Build & Implement (The Action Room)
1. **Source:** Pick a playbook from `skool_lessons/Implementation Playbooks/`.
2. **Plan:** Sketch the approach in `notes/draft-[topic].md` before building.
3. **Build:** Execute the automation/script.
4. **Document:** Convert to `[topic].md` with decisions and outcomes.

### 3. Reference & Insights (The Archive Room)
1. **Source:** Pick from `The Archive`, `Davids Corner`, or `youtube_transcripts/`.
2. **Capture:** Create `notes/draft-[topic].md` with the "Why it matters" insight.
3. **Connect:** Cross-reference to theoretical models in the Foundation room.
4. **Archive:** Finalize as `[topic].md` when the insight is sharp.







