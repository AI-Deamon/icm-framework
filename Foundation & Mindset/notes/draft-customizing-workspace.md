# Customizing the Folder Architecture

**Source:** Skool: The Foundation / Module 3 / 3.2 Customizing for Your Use Case

## Core Idea

The three-layer folder architecture (map, rooms, tools) stays the same regardless of what you're building. Only the labels, context files, and routing change. Three worked examples show exactly how: content creator, freelancer/consultant, and developer — each uses the same skeleton with different labels.

## Why It Matters

- The layers do not change. The labels do. This is the key insight — the system is not a template you copy, it's a pattern you apply.
- Mental mode test for workspace boundaries: "Do I shift mental modes between these tasks?" Writing and building are different mental modes. Drafting and editing are the same mental mode at different stages. If you don't shift modes, don't create a separate workspace.
- Example structures:
  - Content creator: `/script-lab` (ideas, drafts) + `/production` (briefs, builds) + `/distribution` (platform formatting)
  - Consultant: `/client-alpha`, `/client-beta`, `/templates`, `/business-dev` — clients never cross-reference
  - Developer: `/planning` (specs, ADRs) + `/src` (code + patterns) + `/docs` + `/ops`
- Four-step build process: (1) List 2-4 workspaces from mental modes, (2) Write short CONTEXT.md for each, (3) Write AGENTS.md with routing table, (4) Start working and adjust.

## How I'll Apply It

Run the mental mode test on my current Framework folder structure — do I actually shift modes between Foundation, Build, and Reference? If not, the workspaces may be wrong. Also: client folders should NEVER reference each other; each client gets its own isolated workspace with its own CONTEXT.md.

## Cross-Reference

Connects to Common Mistakes (3.3) which warns about over-building, too many workspaces, and never updating context files. Both lessons together are the "how to iterate" guide for the folder architecture from 3.1.
