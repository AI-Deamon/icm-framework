# ICM Enhancements — QA, Evidence Architecture, Style Audit

**Source:** Self-generated during MBA_Research framework design session

## Core Insight
The ICM pipeline (Extract → Research → Produce) needs additional quality infrastructure to produce Distinction-level output consistently. The key gaps are: no independent verification, no claim-level reasoning, and weak source quality control.

## Changes Adopted in MBA_Research

### 1. Evidence Split (Evidence + Argument)
- `evidence_vault.md` — what sources say (passive collection)
- `argument_vault.md` — what position the report defends (active synthesis)

### 2. Source Traceability IDs
Every source gets `SRC-XXX`. Every claim in argument_vault references source IDs. Makes citation audits concrete.

### 3. Contradiction Detection
Surface disagreement between sources explicitly. High-distinction research resolves contradictions, not just summarizes consensus.

### 4. Insight Generation
`insights.md` — captures key insights before drafting, with business impact and strategic implication. Creates originality.

### 5. Light QA Gate (not a full room)
`qa/` subfolder in Production with:
- `citation_audit.md` — every claim verified against evidence
- `quality_score.md` — self-scored dimensions
- `final_checklist.md` — submission readiness

### 6. Style Audit (alongside Humanizer, not replacing it)
Humanizer handles AI-pattern removal (originality). Style audit handles writing quality (passive voice, repetition, weak transitions).

## Changes Deferred
- **Knowledge base** — build after 2-3 subjects prove the pipeline
- **Risk register** — over-engineered for single assignments
- **Full 7-room restructure** — too many empty rooms
- **Hard evidence score threshold** — use as guide, not gate

## Mental Model
A research workspace needs three layers:
1. **Collection** — what exists (evidence vault)
2. **Reasoning** — what it means (argument vault + insights)
3. **Verification** — is it sound (QA gate)

Most AI workspaces skip layers 2 and 3. That's the gap this addresses.
