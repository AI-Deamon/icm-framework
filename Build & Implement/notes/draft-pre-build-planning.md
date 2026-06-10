# Pre-Build Planning Sequence

**Source:** Skool: Implementation Playbooks / Module 3 / 3.3 Pre-Build Planning and Prompt Sequencing

## Core Idea

A five-step planning sequence that front-loads all thinking before Claude Code creates a single file: analyze existing → create briefing doc → research questions → prioritize → spec the build. The build is the easy part; the thinking is the work.

## Why It Matters

- Most people jump straight to prompting, then spend 90% of their time babysitting bad outputs. The five-step sequence inverts this — 80% of time on planning, 20% on building, and the build is clean on the first pass.
- The briefing doc is a markdown file in the planning workspace. It captures: what we're building, who it's for, what success looks like, constraints, and reference examples. This IS the spec that Claude Code reads.
- Prompt sequencing: you don't dump everything in one prompt. You sequence: (1) analyze reference, (2) create brief, (3) research and validate, (4) prioritize features, (5) build incrementally. Each prompt builds on the output of the last.
- The same pattern as the animation pipeline: scripts → specs → build → render. Planning is its own pipeline, not a step.

## How I'll Apply It

Before any build with Claude Code, create a planning workspace folder with the briefing doc. Walk through the five steps as separate prompts. Don't let Claude create anything until Step 4 is complete. The files survive the session; next time I pick up where I left off.

## Cross-Reference

Connects to "I run four phases before any AI builds anything" (Davids Corner) — Brainstorm, Plan, Hand-off Doc, Dispatch. Both are saying the same thing: thinking before AI generates.
