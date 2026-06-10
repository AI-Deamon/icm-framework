# The Template Pattern (Mad Libs for AI)

**Source:** Skool: The Foundation / Module 2 / 2.3 How a 1953 Word Game Explains AI Memory

## Core Idea

Mad Libs (1953) discovered the oldest pattern in computing: a fixed template with variable slots. AI prompts work the exact same way — you provide a structure with blanks, and the model fills them in. The template IS the interface.

## Why It Matters

- "Prompting" is just Mad Libs at scale. The template (system prompt + instruction structure) constrains the output, and the model fills the slots with probabilistically generated text. Understanding this makes prompt engineering less mystical.
- Jake's insight: the Mad Libs inventors stumbled onto something fundamental about how humans and computers communicate — we think in patterns with slots. Templates are how we make the unpredictable (AI output) useful.
- Templates reduce cognitive load for the AI. A well-structured template tells the model exactly what shape the answer should take, so it doesn't waste tokens figuring out format.

## How I'll Apply It

When writing prompts, start with the template structure first (what slots need filling?) before writing the instructions. The template IS the prompt — everything else is just decoration.

## Cross-Reference

This is the same pattern as Claude Code's AGENTS.md instructions: the file is a template that tells the AI "here's the structure of this project, now fill in the details as you work."

Skool lesson adds: prompting is the highest abstraction layer of programming. Your prompt is a Mad Libs template — the model fills the slots. Understanding this means you design prompts as template structures first (what slots need filling?), then write the framing text around them.
