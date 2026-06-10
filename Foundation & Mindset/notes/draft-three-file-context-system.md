# Three-Layer Folder Architecture

**Source:** Skool: The Foundation / Module 1 / 1.2 Your First Folder + Module 3 / 3.1–3.3 The Full Method

## The Problem

Every Claude conversation starts from zero. You spend half your messages explaining who you are, what you're working on, and what good looks like. Then you hit the token limit, start a new chat, and repeat everything. The output stays generic because Claude is always guessing.

## The Core Mental Model

**Folders are memory. Prompts are direction.**

A folder with structured markdown files replaces the overhead of re-explaining context every conversation. These files are persistent, editable, version-controllable, and model-agnostic — any AI tool can read them, any editor can edit them.

---

## Layer 1 — AGENTS.md (The Map)

**Job:** Routing file. Sits at the project root. Claude reads this first every time.

**What it contains:**
- **Identity** — Who you are, what you do, one-liner of the project
- **Folder structure** — ASCII tree showing every workspace
- **Routing table** — For each task type: which workspace to enter, which file to read, optionally which skill to load
- **Naming conventions** — How files are named per workspace (replaces databases — no SQL, no vector DB)
- **Token management rules** — What to skip for each type of task

**Length rule:** Fit on one screen. 40–50 lines max. Everything else belongs in a workspace CONTEXT.md.

**Routing table template:**

```
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| Write content | /script-lab | CONTEXT.md | humanizer |
| Build something | /production | CONTEXT.md | frontend-design |
| Publish or schedule | /distribution | CONTEXT.md | — |
```

The routing table is the most important pattern in the whole system. Without it, Claude either reads everything (wastes tokens), reads the wrong context (confused output), or guesses. With it, every task routes cleanly.

**Naming conventions example:**

```
- Drafts: topic-name_draft.md
- Final scripts: topic-name_final.md
- Published: YYYY-MM-platform-topic.md
- Demo versions: demo_v2.md, demo_v3.md
```

The AI knows how to find, organize, and move files because the naming tells it everything. You can say "pull my demo v2 and build a spec" and Claude knows exactly where to look and what to do next.

---

## Layer 2 — CONTEXT.md (The Rooms)

**Job:** Describe what happens in one workspace. One per workspace. Only loaded when Claude works in that room.

**What it contains (keep under one page):**

| Section | What goes there | Example |
|---|---|---|
| **What this workspace is for** | One-line purpose of this room | "Script Lab — where ideas become written drafts" |
| **The process** | The workflow steps in order | "First we brainstorm, then outline, then draft, then revise" |
| **File organization** | Subfolder structure and what goes where | "Ideas/ — raw concepts, Drafts/ — WIP, Final/ — finished scripts" |
| **What good looks like** | Quality standards specific to this room | "Output reads like me, not like a generic AI" |
| **What to avoid** | Common mistakes, constraints | "No jargon without explanation. No marketing fluff." |
| **Skills & tools** | Which Layer 3 skills to wire in here | "humanizer in review stage, web search for research" |
| **Hard rules** | Non-negotiable constraints | "Source files in skool_lessons/ are READ-ONLY. Never edit them." |

**Critical guideline:** Spend 80% of the content describing the work itself (project, audience, constraints, process), not Claude's personality. "You are a senior copywriter" gives Claude a role. "The audience is mid-market HR directors who have tried three other tools" gives it something to actually work with. The second changes the output more than the first.

**When to create a workspace:** Ask "Do I shift mental modes between these tasks?" Writing and building are different modes → two workspaces. Drafting and editing are the same mode at different stages → one workspace with a process inside it.

**Max workspaces:** Start with 2–3. If you're not sure whether something needs its own workspace, it doesn't. Subfolder it. Split later if the work grows.

---

## Layer 3 — Skills & Tools (Plug-and-Play)

**Job:** Reusable instruction sets that wire into specific workspaces. Not loaded everywhere — only where needed.

**How it works:**
- A skill is a set of files or a prompt that tells Claude how to do one specific thing
- Skills are referenced in the workspace CONTEXT.md where they're needed
- A Production workspace might wire in frontend-design and webapp-testing. A Writing Room wires in humanizer and doc-coauthoring. They don't cross-load.

**Types of skills:**
- **Workspace operations** — `!extract`, `!refine`, `!audit`, `!brain-sync`, `!summarize-video`
- **Agent skills** — `/graphify`, `/understand`, `/humanizer`, `/pdf`
- **MCP servers** — web search, external API access
- **Reusable prompts** — mad libs templates, process workflows

**Rule:** You can reference 15+ skills in a project, but each workspace only loads the ones it needs.

---

## Common Mistakes (From 3.3)

| Mistake | Fix |
|---|---|
| AGENTS.md too long (40+ lines of background) | Pull everything except routing into workspace CONTEXT.md files |
| No routing table | Add three-column table: Task / Go to / Read |
| Too many workspaces (8+ for a simple project) | Start with 2–3. Same mental mode = same workspace. |
| Context describes AI's personality instead of the work | 80% project context, 20% behavioral. Flip the ratio. |
| Never updating context files | Add "Last updated:" line. Edit when project changes. |
| Flat folder with 50 files, no subfolders | If 8–10+ files at the same level, add subfolders. |
| Building the whole system before using it | First version in 15 minutes. Grow from use. |

---

## Three Real Configurations (From 3.2)

### Content Creator

```
my-content-project/
├── AGENTS.md
├── script-lab/          <- Ideas, drafts, final scripts
│   ├── CONTEXT.md
│   ├── ideas/
│   ├── drafts/
│   └── final/
├── production/          <- Briefs, specs, builds, output
│   ├── CONTEXT.md
│   ├── briefs/
│   ├── specs/
│   ├── builds/
│   └── output/
└── distribution/        <- Platforms, scheduling, analytics
    ├── CONTEXT.md
    ├── platforms/
    ├── scheduling/
    └── analytics/
```

### Freelancer / Consultant

```
my-consulting-practice/
├── AGENTS.md
├── client-alpha/        <- One per client
│   ├── CONTEXT.md
│   ├── intake/
│   ├── deliverables/
│   └── communications/
├── client-beta/
│   └── (same structure)
├── templates/           <- Reusable proposals, reports
│   └── CONTEXT.md
└── business-dev/        <- Pipeline, outreach, case studies
    └── CONTEXT.md
```

### Developer

```
my-app/
├── AGENTS.md
├── planning/            <- Specs, architecture, decisions
├── src/                 <- Codebase with components, services, tests
├── docs/                <- API docs, guides, changelog
└── ops/                 <- Deploy, monitoring, scripts
```

Key difference for developers: the routing table gets a Skills column because code workspaces need testing skills, doc workspaces need authoring skills, etc.

---

## How Each File Should Be (Section-by-Section)

### AGENTS.md Checklist
- [ ] Identity: who you are, what you do
- [ ] Folder structure: ASCII tree
- [ ] Routing table: Task → Go to → Read (→ Skills)
- [ ] Naming conventions per workspace
- [ ] Token management: tell Claude what to skip
- [ ] Fits on one screen (~40 lines)

### CONTEXT.md Checklist (per workspace)
- [ ] Purpose: what this room is for
- [ ] Process: the workflow steps
- [ ] File organization: subfolders and their purpose
- [ ] Quality standards: what good looks like
- [ ] Constraints: what to avoid
- [ ] Skills & tools wired to this room
- [ ] Hard rules unique to this workspace
- [ ] Under one page
- [ ] "Last updated:" line at top

### Layer 3 Checklist (per skill)
- [ ] Single responsibility — one thing well
- [ ] Referenced only in workspaces that need it
- [ ] Not auto-loaded in every room

---

## Key Principles

1. **AGENTS.md is a map, not a brief.** Don't put project context in it. Put routing instructions.
2. **Context files describe the work, not the AI.** 80% project/audience/constraints, 20% behavioral.
3. **Start with 2–3 workspaces.** Add more only when the work demands it.
4. **Update context files when the project changes.** Stale context is worse than no context.
5. **Build in 15 minutes, iterate from use.** Don't build the perfect system before using it.

## Cross-Reference

This is the foundation for the entire ICM Framework. This repo (Framework/) is itself an implementation of this architecture — GEMINI.md is Layer 1, each CONTEXT.md is Layer 2, and the agent skills available are Layer 3. The naming conventions, routing table, and token management you see in this repo all follow Jake's pattern from 1.2 and 3.1.
