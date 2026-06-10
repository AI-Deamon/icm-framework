# Claude Design: Skills, Imports, and Local Handoff

**Source:** Skool: Implementation Playbooks / Module 1.5 Claude Design

## Core Idea

Claude Design is a separate product from Claude Code, focused on design and creative work. The key workflow: import a GitHub repo, apply skills (reusable prompt modules), and hand off to local models when you hit usage limits. Jake's big lesson: Claude hits limits fast on creative work, so you need a fallback.

## Why It Matters

- GitHub imports let Claude Design read your entire codebase or design system and work within it — same principle as AGENTS.md but for visual/design context.
- Skills are reusable instruction bundles. Instead of re-explaining your design system every session, you write it once as a skill and load it on demand. This is the same concept as plugins in the folder workspace system.
- Local model handoff is the escape valve. When Claude's usage limits block you (which happens fast on creative/design work), you switch to a local model running the same context. The context files stay the same — only the model changes. This is the portable-context principle in action.

## How I'll Apply It

- Create skills for my most common design/creative workflows (one for "explain this concept visually," one for "turn this into a slide deck")
- When building creative context files, make sure they're model-agnostic — usable by Claude, GPT, or a local model. The file format (markdown) guarantees this.

## Cross-Reference

Skills in Claude Design are the same concept as skills in the folder workspace system. The "portable context" idea connects to ICM (Build & Implement) — context that works with any model is the whole point.

Skool lesson adds: Claude Design is an automation of the ICM pattern itself — it generates folders, markdown files, and components from your assets, producing exportable design systems that run anywhere. It proves the pattern: design systems = folder systems.
