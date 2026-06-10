# ICM Framework Knowledge Hub — AGENTS.md

## What This Is

**User:** Bhaskar · ICM Practitioner, Developer, and Content Researcher
**AI Role:** Knowledge Architect & Personal Librarian

Bhaskar's structured knowledge system for Jake Van Clief's **Interpretable Context Methodology (ICM)**. Converts 82+ Skool lessons and YouTube transcripts into mental models and playbooks. This is a knowledge management framework, not code.

**GEMINI.md** is the master map (always loaded). **CONTEXT.md** in each room routes you. This file is the overview.

## Folder Architecture

```
Framework/
├── GEMINI.md                        <- Master navigation map (Layer 1)
├── CONTEXT.md                       <- Root task router
├── AGENTS.md                        <- You are here
│
├── Foundation & Mindset/            <- Theory, mental models, principles
│   ├── CONTEXT.md (Theory Room)
│   └── notes/ (draft-* and final .md files)
│
├── Build & Implement/               <- Playbooks, scripts, automation
│   ├── CONTEXT.md (Action Room)
│   └── notes/
│
├── Reference & Insights/            <- Case studies, community insights
│   ├── CONTEXT.md (Archive Room)
│   └── notes/
│
├── skool_lessons/                   <- READ-ONLY: raw Skool curriculum
├── youtube_transcripts/             <- READ-ONLY: raw video transcripts
└── scriping tools/                  <- Python scraping utilities
```

## Task Routing

| User wants... | Load this room | Skip |
|---|---|---|
| Learn theory / mental models | `Foundation & Mindset/CONTEXT.md` + relevant `skool_lessons/` | Build & Implement, Reference & Insights |
| Build scripts / use playbooks | `Build & Implement/CONTEXT.md` + `skool_lessons/Implementation Playbooks/` | Foundation & Mindset, Reference & Insights |
| Research case studies / videos | `Reference & Insights/CONTEXT.md` + `youtube_transcripts/` + `skool_lessons/Davids Corner/` | Foundation & Mindset, Build & Implement |
| Manage the workspace | `GEMINI.md`, `scriping tools/` | All `notes/` subfolders |
| Cross-reference insights | `Foundation & Mindset/` + `Reference & Insights/` | Build & Implement, raw sources |

## Naming Conventions (The Lifecycle)

| Prefix | Meaning | Priority |
|---|---|---|
| `draft-[topic].md` | Initial brain dump, messy | LOW |
| `ref-[topic].md` | Curated external reference | MED |
| `[topic].md` | Finalized mental model (Ground Truth) | HIGH |
| `[topic]-v[n].md` | Iteration of final model | HIGH (use latest) |
| `poc-[topic].md` | Proof of concept / automation test | MED |

**All filenames must be `lowercase-kebab-case.md`. No spaces or underscores.**

## Principles

1. **Context Isolation** — never load files from unrelated rooms. Theory? Skip Build & Implement.
2. **Atomic Notes** — one mental model or playbook per note. No mega-notes.
3. **Draft-Refine-Final** — always start with `draft-`, iterate to `[topic].md`.
4. **Kebab-Case Enforcement** — `lowercase-kebab-case.md` only. No spaces or underscores.
5. **Cross-Referencing** — use standard Markdown links between related notes.

## SOP

1. `GEMINI.md` first for routing and rules.
2. Before writing final notes, create `notes/draft-[topic].md` first.
3. Source files in `skool_lessons/` and `youtube_transcripts/` are READ-ONLY.
4. **Token Management:** Only load the relevant room — skip everything else. Each room is siloed.

## Workspace Skills (Shortcuts)

| Command | What it does |
|---|---|
| `!extract` | Scan source → create `draft-[topic].md` with mental model |
| `!refine` | Format `draft-` → clean finalized `[topic].md` |
| `!audit` | Scan workspace for naming/principle violations |
| `!brain-sync` | Suggest 3 related notes in other rooms to link |
| `!summarize-video` | Extract 3 key takeaways from a transcript |

## Available Agent Skills

| Skill | When to use |
|---|---|
| `/graphify` | Cross-reference concepts, map connections across rooms, visualize the workspace |
| `/graphify-windows` | Re-query existing graph after `/graphify` has run once |
| `/understand` | Analyze codebase structure (any repo) into knowledge graph |
| `/humanizer` | Strip AI-writing patterns from notes before publishing |
| `/pdf` | Read/merge/split/create/OCR PDF files |

## Room Workflows

### Foundation & Mindset (Theory Room)
1. **Source:** Pick a lesson from `skool_lessons/The Foundation/`
2. **Absorb:** Read the material, identify the core mental model
3. **Draft:** `notes/draft-[topic].md` in your own words
4. **Refine:** Convert to `[topic].md` once the model clicks
5. **Iterate:** Use `[topic]-v[n].md` as understanding deepens

### Build & Implement (Action Room)
1. **Source:** Pick a playbook from `skool_lessons/Implementation Playbooks/`
2. **Plan:** Sketch in `notes/draft-[topic].md` before building
3. **Build:** Execute the automation/script
4. **Document:** Convert to `[topic].md` with decisions and outcomes

### Reference & Insights (Archive Room)
1. **Source:** `youtube_transcripts/` or `skool_lessons/Davids Corner/`
2. **Capture:** `notes/draft-[topic].md` with the key insight
3. **Connect:** Cross-reference to theoretical models in Foundation room
4. **Archive:** Finalize as `[topic].md` when insight is sharp

## Cross-Room Flow

```
Foundation (mental models)
    │
    ▼
Build & Implement (playbooks, scripts)
    │
    ▼
Reference & Insights (case studies, community insights — links back to Foundation)
```

## Foundation Room Rules

- **No Code in the Library** — implementation logic belongs in Build & Implement.
- **Source Truth Only** — if info isn't in provided `skool_lessons/` or `youtube_transcripts/`, mark as "(External AI Knowledge)" or omit.
- **No Generic Summaries** — produce mental model deconstructions, not overviews.

## Tools

- `scriping tools/skool_scraper.py` — Python/Playwright scraper for Skool.com lessons
- `scriping tools/download_transcripts.py` — yt-dlp wrapper for YouTube transcripts
- `scriping tools/Youtube_links.txt` — 29 video URLs to process
