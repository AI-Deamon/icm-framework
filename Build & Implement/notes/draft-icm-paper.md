# Interpretable Context Methodology (ICM)

**Source:** Skool: The Foundation / Module 0 / 0.1 Where All Of This Leads

## Core Idea

ICM is the formal name for the folder-as-workspace system Jake published in his paper. 30,000+ people in his community and hundreds of GitHub stars use folders + markdown files instead of agent frameworks — and they get better results because context you can read is context you can debug.

## Why It Matters

- "Interpretable" is the key word. A traditional agent pipeline is a black box — prompts go in, actions come out, and you can't see why. A folder with markdown files is fully transparent — you can read every piece of context the AI is using.
- 30,000 people adopting this means it's not just Jake's opinion — it's a validated pattern. People tried agents, hit the same walls (cost, fragility, opacity), and switched to files.
- The paper formalizes what was previously implicit: your project's context should be human-readable AND AI-readable. If you can't read it, neither can the AI in a useful way.

## How I'll Apply It

Treat every folder in my workspace as a "context node" with its own CONTEXT.md. The folder hierarchy IS the context hierarchy — deep nesting means deep context, flat means broad. Use this to design better project structures.

## Cross-Reference

This is the formalization of everything in "Stop Building AI Agents. Use This Folder System Instead." The paper is the theory; the folder template is the practice. Connects to automation ladder — ICM operates above the automation layer (it organizes judgment).

Skool lesson 0.1 adds: the three layers of AI work — Layer 1 (Chat, copy-paste), Layer 2 (Skills, packaged prompts), Layer 3 (Folders & markdown, the full system). 30,000 people building this way. One agent, one workspace, structure on disk. Jake's demo: a full content pipeline (research → angles → scripts → voice → animation) running from one folder — "four or five startups" worth of production.
