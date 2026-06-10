# Computational Orchestration

**Source:** Skool: The Archive / Module 3 / 3.4 Computational Orchestration

## Core Idea

The capstone discipline of the entire course: knowing when to use AI, when to use traditional code, and when to keep a human in the loop. Not "how to use AI" but "how to know which type of computation fits which problem." The 60/30/10 framework is the answer: 60% traditional code, 30% rule-based logic, 10% AI.

## Why It Matters

- The 60/30/10 pattern restated: 60% traditional database queries (fast, cheap, deterministic), 30% if-then rules (de-buggable, auditable), 10% AI calls (only where semantic understanding matters). "The 10% made the whole thing feel magical. The 90% made it actually work."
- Three pillars of the discipline:
  1. **Abstraction Without Abandonment** — Adding a semantic layer on top (like Python on C), not replacing code with prompts. You still need the layers below.
  2. **Judgment AND Implementation** — "The hardest part of my job isn't making AI work. It's knowing when not to use it." Story: startup wanted an AI meeting scheduler; he built a Google Calendar integration instead. Boring beats brilliant.
  3. **Flow Over Features** — "A simple regex in the right spot beats GPT-4 in the wrong spot." The value is in how components flow together, not what each can do alone.
- Key forecast: "In five years, the question won't be 'can you code?' It'll be 'can you orchestrate code?'"
- Five types of computation emerging: Deterministic (code), Probabilistic (ML), Semantic (LLMs), Quantum, Biological.

## How I'll Apply It

Before every build, ask: "Which type of computation does this problem need?" Most of it will be deterministic code or simple rules. Only use AI for the semantic layer — understanding, generating, interpreting. Keep a 60/30/10 ratio as a rough budget.

## Cross-Reference

This is the capstone concept the whole course builds toward. It synthesizes the abstraction layers (2.2), OpenClaw orchestration (2.5), and the automation ladder (2.4). The "boring beats brilliant" principle connects to "one client first" — solve the real problem, not the shiny one.
