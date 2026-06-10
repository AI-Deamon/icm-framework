# Prompt: Recreate ICM Layer 1 & 2 for BSOL

Modeled after `ref-claude.md` (Jake's Acme CLAUDE.md template) for Layer 1,
and `Foundation & Mindset/CONTEXT.md` (room pattern) for Layer 2.

---

## Layer 1: AGENTS.md (The Map)

Create `AGENTS.md` in the project root. Follow the `ref-claude.md` template.

```markdown
# BSOL – Workspace Map

## What This Is

A penetration testing automation system. Orchestrates Nmap scanning, parses
results with service-specific rules, and generates comprehensive security
reports in PDF/HTML. Each pipeline phase (scanner → parser → reporter) has its
own CONTEXT.md so an agent drops into a module, reads its room, does its work,
and exits.

**CONTEXT.md** (root-level) routes you to the right phase. This file is the map.

---

## Folder Structure

```
test folder/
├── AGENTS.md                   <- You are here (always loaded)
├── CONTEXT.md                  <- Task router
├── targets.json                <- Target definitions
├── opencode.json               <- Agent configuration
│
├── bsol/                       <- Core application
│   ├── CONTEXT.md              <- App core room
│   ├── cli.py                  <- CLI entry point
│   ├── __main__.py
│   ├── config/                 <- Scan definitions & settings
│   ├── data/                   <- Data models & file I/O
│   ├── parser/                 <- Parsing rules engine
│   │   ├── CONTEXT.md          <- Parser room
│   │   └── rules/              <- Service-specific rules
│   ├── reporter/               <- Report generation
│   │   ├── CONTEXT.md          <- Reporter room
│   │   └── templates/          <- HTML templates
│   └── scanner/                <- Nmap orchestration
│       ├── CONTEXT.md          <- Scanner room
│       └── ...                 <- Orchestrator, discovery, executor
│
├── scripts/                    <- Convenience wrappers
│   └── CONTEXT.md              <- Scripts room
│
├── scans/                      <- Output organized by date
├── tests/                      <- Test scaffolding
│   └── CONTEXT.md              <- Tests room
│
└── graphify-out/               <- Knowledge graph (auto-generated)
```

---

## Quick Navigation

| Want to... | Go here |
|------------|---------|
| **Run a scan or change Nmap flags** | `bsol/scanner/CONTEXT.md` |
| **Fix a parsing rule for a service** | `bsol/parser/CONTEXT.md` |
| **Change report layout or styling** | `bsol/reporter/CONTEXT.md` |
| **Add/modify data models or config** | `bsol/CONTEXT.md` |
| **Update scan definitions** | `bsol/config/scans.py` |
| **Edit target list** | `targets.json` |
| **Read/add tests** | `tests/CONTEXT.md` |
| **Use convenience scripts** | `scripts/CONTEXT.md` |
| **Understand full architecture** | `graphify-out/` |

---

## Pipeline Flow

```
scanner (discovery -> service scans -> raw output)
    │
    ▼
parser (read raw -> match targets -> apply rules -> deduplicate -> findings.json)
    │
    ▼
reporter (load findings -> build sections -> render PDF/HTML -> reports/)
```

Each phase is independent — run them separately or as a pipeline. Output of
one phase is input to the next.

---

## Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Source files | `lowercase_with_underscores.py` | `pdf_builder.py` |
| Classes | `PascalCase` | `ScanOrchestrator` |
| Methods/functions | `snake_case` | `parse_findings()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_WORKERS` |

---

## File Placement Rules

### Scanner Phase
- Raw results: `scans/YYYY-MM-DD/raw/{target}_{scan_id}.txt`
- Discovery JSON: `scans/YYYY-MM-DD/{target}_discovery.json`
- Summary: `scans/YYYY-MM-DD/scan_summary.json`
- Log: `scans/YYYY-MM-DD/scanner.log`

### Parser Phase
- Input: `scans/YYYY-MM-DD/raw/*.txt`
- Output: `scans/YYYY-MM-DD/findings.json`

### Reporter Phase
- Input: `scans/YYYY-MM-DD/findings.json`
- Output: `scans/YYYY-MM-DD/reports/report_YYYY-MM-DD.pdf` (PDF)
- Output: `scans/YYYY-MM-DD/reports/report_YYYY-MM-DD.html` (HTML)
- Output: `scans/YYYY-MM-DD/reports/report_YYYY-MM-DD_client.pdf` (client PDF, if wkhtmltopdf)

---

## Token Management

**Each phase is siloed.** Don't load everything.

- Fixing a parser rule? → Load `bsol/parser/CONTEXT.md`. Skip scanner and reporter entirely.
- Tuning scan flags? → Load `bsol/scanner/CONTEXT.md`. Skip parser and reporter.
- Styling a report? → Load `bsol/reporter/CONTEXT.md`. Skip scanner and parser.

The CONTEXT.md files tell you what to load for each task. Trust them.

---

## Skills & Tools Available

| Tool | Type | Used In |
|------|------|---------|
| `/understand` | Skill | Root (Stage: onboard/audit) |
| `/humanizer` | Skill | Reporter (text polish for client reports) |
| `/pdf` | Skill | Reporter (PDF generation, merging, OCR) |
| `/graphify` | Skill | Root (cross-reference architecture) |
| Web Search | MCP | All phases (CVE lookups, research) |

See each room's CONTEXT.md for when and how these tools get invoked.
```

---

## Layer 2: CONTEXT.md Files (The Rooms)

Create one CONTEXT.md per room. All follow the `Foundation & Mindset/CONTEXT.md` pattern:

> `# [Room Name]`
> `## 1. What This Workspace Is`
> `## 2. What to Load (The Token Budget)` — table with Load These / Skip These
> `## 3. Folder Structure`
> `## 4. The Process` or workflow
> `## 5. Skills & Tools for This Room`
> `## 6. Hard Rules (The Contract)`

---

### Room 1: `bsol/CONTEXT.md`

```markdown
# Core Application Room

## 1. What This Workspace Is
The application root. Contains CLI entry points, configuration definitions,
data models, and file I/O. This is the central nervous system — it wires
scanner, parser, and reporter together.

## 2. What to Load (The Token Budget)

| Task | Load These | Skip These |
|------|------------|------------|
| **Add CLI command** | `cli.py`, `__main__.py` | All submodules |
| **Change data model** | `data/models.py`, `data/io.py` | `parser/`, `reporter/`, `scanner/` |
| **Modify scan definitions** | `config/scans.py` | `parser/`, `reporter/` |
| **Change app paths/behavior** | `config/settings.py` | All submodules |

## 3. Folder Structure
- `cli.py` — CLI dispatch (scanner/parser/reporter subcommands)
- `__main__.py` — Package entry for `python3 -m bsol`
- `config/` — `settings.py` (paths, targets) + `scans.py` (Nmap script definitions)
- `data/` — `models.py` (Target, Scan, Finding) + `io.py` (JSON I/O)

## 4. The Process
1. Config is read at startup and cached
2. `cli.py` parses args and dispatches to the correct phase module
3. Data models are shared across all phases — changes here ripple everywhere

## 5. Skills & Tools for This Room
| Tool | When | How |
|------|------|-----|
| `/understand` | Onboarding | Generate knowledge graph of full codebase |

## 6. Hard Rules (The Contract)
1. Keep CLI dispatch thin — logic lives in submodules
2. Data models are shared; test thoroughly before changing
3. Restart required for config changes (no hot-reload)
```

---

### Room 2: `bsol/scanner/CONTEXT.md`

```markdown
# Scanner Room

## 1. What This Workspace Is
Nmap scanning orchestration. Runs discovery (`-T4 -F --open`) to find live
hosts, then executes service-specific Nmap scripts. Manages parallel worker
pools, aggressive scan restrictions, and raw output storage.

## 2. What to Load (The Token Budget)

| Task | Load These | Skip These |
|------|------------|------------|
| **Change discovery logic** | `discovery.py`, `job.py` | `parser/`, `reporter/` |
| **Modify parallel execution** | `executor.py`, `orchestrator.py` | `parser/`, `reporter/` |
| **Add scan type** | `orchestrator.py`, `config/scans.py` (bsol root) | `parser/`, `reporter/` |
| **Debug scan failure** | All scanner files, target config | Everything else |

## 3. Folder Structure
- `orchestrator.py` — Top-level orchestration (loads targets, runs phases)
- `discovery.py` — Discovery phase Nmap command construction
- `executor.py` — Parallel job execution (6 workers)
- `job.py` — Scan job data class

## 4. The Process
1. Load targets from `targets.json`
2. Discovery phase: `nmap -T4 -F --open` for all targets
3. Service phase: For each open port, run configured Nmap scripts
4. Write raw results + summary JSON

## 5. Skills & Tools for This Room
| Tool | When | How |
|------|------|-----|
| Web Search | Research | Look up Nmap script flags or CVE data |

## 6. Hard Rules (The Contract)
1. All Nmap commands use `--open` — only report open ports
2. Aggressive scans (brute, dos) check `allow_aggressive` per target
3. Discovery is `-T4 -F` (fast), not full port range
4. Max 6 scan workers, 4 discovery workers
5. --dry-run shows planned actions without executing
```

---

### Room 3: `bsol/parser/CONTEXT.md`

```markdown
# Parser Room

## 1. What This Workspace Is
Service-specific parsing engine. Reads raw Nmap output, matches files to
targets using longest prefix matching, applies per-service rules (web,
database, infrastructure, crypto), deduplicates findings, and outputs
structured JSON.

## 2. What to Load (The Token Budget)

| Task | Load These | Skip These |
|------|------------|------------|
| **Add new service parser** | `rules/base.py`, create `rules/new.py` | `scanner/`, `reporter/` |
| **Modify existing rule** | Specific rule file (e.g. `rules/web.py`) | `scanner/`, `reporter/` |
| **Fix deduplication** | `engine.py`, `pipeline.py` | Rule files |
| **Debug parse failure** | `pipeline.py`, `reader.py`, all rules | Everything else |

## 3. Folder Structure
- `pipeline.py` — Main orchestrator (file discovery, matching, parsing)
- `reader.py` — Raw file reader
- `engine.py` — Deduplication engine
- `rules/` — Service-specific parsers
  - `base.py` — Abstract base class for all rules
  - `web.py` — HTTP/HTTPS rules
  - `database.py` — Database service rules
  - `infrastructure.py` — Infrastructure rules
  - `crypto.py` — Cryptographic service rules
  - `unknown_service.py` — Fallback handler

## 4. The Process
1. Discover raw scan files for the date
2. Match each file to a target (longest prefix matching)
3. Apply service-specific parsing rule
4. Deduplicate findings by `(host, title, port)`
5. Write `findings.json`

## 5. Skills & Tools for This Room
*(None specific to this room)*

## 6. Hard Rules (The Contract)
1. Each service type gets its own rule file
2. All rules implement `matches()` + `parse()` from `base.py`
3. Ignore discovery scan files — only parse service scan outputs
4. Dedup key: `(host, title, port)` — no duplicate findings
5. Reference `scan_summary.json` to only parse executed scans
```

---

### Room 4: `bsol/reporter/CONTEXT.md`

```markdown
# Reporter Room

## 1. What This Workspace Is
Report generation system. Loads parsed findings, processes through specialized
builders (exposure, PDF, HTML), and outputs formatted security reports.

## 2. What to Load (The Token Budget)

| Task | Load These | Skip These |
|------|------------|------------|
| **Change PDF layout** | `pdf_builder.py`, `pdf_styles.py`, `templates/pdf_config.py` | `scanner/`, `parser/` |
| **Change HTML design** | `html_builder.py`, `html_styles.py`, `templates/` | `scanner/`, `parser/` |
| **Add report section** | `exposure_builder.py`, relevant builder | `scanner/`, `parser/` |
| **Custom template** | `templates/`, `loader.py` | Everything else |

## 3. Folder Structure
- `runner.py` — Main execution (load data, trigger builders, write output)
- `loader.py` — Loads findings JSON and scan metadata
- `pdf_builder.py` — PDF construction (reportlab)
- `html_builder.py` — HTML construction (Chart.js)
- `exposure_builder.py` — Vulnerability exposure section
- `pdf_styles.py` — PDF color/font constants
- `html_styles.py` — HTML CSS constants
- `templates/` — HTML templates with `<!-- PLACEHOLDER -->` markers

## 4. The Process
1. Load findings from `scans/YYYY-MM-DD/findings.json`
2. Build exposure sections from findings
3. Render PDF (reportlab) and/or HTML (Chart.js)
4. Optionally generate client PDF via wkhtmltopdf
5. Write to `scans/YYYY-MM-DD/reports/`

## 5. Skills & Tools for This Room
| Tool | When | How |
|------|------|-----|
| `/humanizer` | Client reports | Polish finding descriptions to remove AI patterns |
| `/pdf` | Report processing | Merge, split, or OCR generated PDFs |

## 6. Hard Rules (The Contract)
1. HTML uses inline Chart.js from CDN — no local chart library
2. Templates use `<!-- PLACEHOLDER -->` for content injection
3. PDF uses reportlab — no LaTeX or WeasyPrint
4. Client PDF requires wkhtmltopdf (optional)
5. `--preview` generates HTML only, skips PDF
6. Review functionality removed — edit `findings.json` directly
```

---

### Room 5: `scripts/CONTEXT.md`

```markdown
# Scripts Room

## 1. What This Workspace Is
Convenience wrapper scripts for the bsol pipeline. Each wraps a
`python3 -m bsol <phase>` call with sensible defaults.

## 2. What to Load (The Token Budget)

| Task | Load These | Skip These |
|------|------------|------------|
| **Modify wrapper** | Specific script file | Core modules |
| **Add new wrapper** | All script files (reference pattern) | Core modules |

## 3. Folder Structure
- `scanner.py` — Wrapper for `python3 -m bsol scanner`
- `parser.py` — Wrapper for `python3 -m bsol parser`
- `reporter.py` — Wrapper for `python3 -m bsol reporter`

## 4. Hard Rules (The Contract)
1. Keep wrappers thin — no business logic
2. All real logic lives in `bsol/` modules
```

---

### Room 6: `tests/CONTEXT.md`

```markdown
# Tests Room

## 1. What This Workspace Is
Test scaffolding. Stubs for parser and scanner tests. To be built out.

## 2. What to Load (The Token Budget)

| Task | Load These | Skip These |
|------|------------|------------|
| **Add tests** | Test directory, relevant source module | All other rooms |
| **Run tests** | Test directory | Production code |

## 3. Folder Structure
- `test_parser/` — Parser test stubs
- `test_scanner/` — Scanner test stubs

## 4. Hard Rules (The Contract)
1. Tests are not yet implemented — stubs only
2. Match test file names to module names: `test_<module>.py`
3. Add tests before modifying existing parser/scanner logic
```
