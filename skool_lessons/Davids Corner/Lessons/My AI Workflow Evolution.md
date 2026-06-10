# My AI Workflow Evolution - Davids Corner

## **What you'll get from this**

This piece presents an advanced interpretation of Jake Van Clief's Interpretable Context Methodology. It layers on Harness Engineering — a set of practical extensions for building more reliable, self-improving agent systems.

The goal is not to build the most elaborate setup. The goal is to create a workflow that stays simple, transparent, and actually supports the work only you can do.

## **The hook**

Many of us start with simple one-shot prompting when we first bring AI into our work. It feels fast at the beginning, but limitations show up quickly. Costs add up fast with repeated use, and there's no lasting progress.

I've always leaned toward open-source tools, especially while volunteering for a nonprofit. Every dollar and every token matters, so I needed setups that were sustainable, transparent, and under my control.

---

## **Introduction**

If you are new to this approach, start with the core of Jake's Method first. Learn the fundamentals before adding layers on top. The basics deliver the biggest gains and keep things grounded.

If you already have markdown files running Jake's Method that exceed 150 lines, go back and optimize them. Long files often hide unnecessary complexity. Tighten the structure, sharpen the context scoping, and remove anything that no longer serves a clear purpose. Cleaner files make the whole system run better.

---

## **The Evolution**

Now that that's out of the way....

In the early days I treated AI like a quick consultant. I would write one detailed prompt, get an answer, and move on. ChatGPT and Gemini worked as entry points, but they offered no real continuity or memory. Costs added up fast with repeated use, and there was no lasting progress.

That pushed me to prioritize cost efficiency and open-source options from the start. I looked for generous free tiers and nonprofit-friendly credits:

* Cloudflare offered strong free limits for workers, AI, and storage.
* Alibaba Cloud provided large token awards and credits that made experimentation possible without burning budget.
* Various self-hosted and open models kept everything transparent and controllable.

This approach helped me avoid locking into any single company's pricing or roadmap.

Participating in devpost hackathons introduced me to more structured ways of working with AI. One tool that stood out was Kiro, an AI IDE built around spec-driven development. Instead of vague prompts, you define clear specifications first, and the system helps turn them into reliable code.

That experience shifted me toward spec-first workflows. I explored the BMAD Method — a structured, persona-based framework using YAML and specialized agents for analysis, planning, and implementation. These methods reduced inconsistency and the constant need to re-explain context.

All of this eventually led me to Jake's method. It felt like a natural step forward: from one-shot prompting to spec-driven work to more structured agentic workflows.

I first added Open Brain for basic persistent memory. It was a helpful step at the time, but I soon saw the limits of simple vector databases and pure RAG setups.

Simple vector retrieval struggles with three core issues. It lacks true relational understanding between concepts. Context tends to fragment or get buried as the knowledge base grows. And it offers no built-in layer for reasoning, critique, or self-improvement — it only retrieves, it does not evolve.

These gaps became clear when handling complex, multi-month tasks for the nonprofit.

I experimented with ClaudeBot and then implemented ZeroClaw, a lightweight Rust-based open-source harness. It delivered good speed and a minimal footprint, but it still fell short on deeper integrations and agentic capabilities I needed.

The real leap came with Cognee, an open-source knowledge engine that goes beyond basic RAG. It builds structured knowledge graphs with rich relationships and persistent memory. I paired it with Hermes' Agent from Nous Research — a self-improving, persistent agent.

This combination now gives me:

* Long-term memory through knowledge graphs instead of flat vectors
* Automatic discovery of relationships across projects
* The ability for the agent to reflect, critique, and generate new skills over time
* Full open-source control that fits tight volunteer budgets

## **Summary**

Each stage solved a specific friction. One-shot prompting was quick but shallow. Open-source free tiers kept things sustainable. Spec-driven methods added reliability. Simple vector memory offered basic persistence but lacked depth. Hermes + Cognee finally delivered relational memory, autonomous reasoning, and real self-improvement.

## **Reflection**

The evolution was never about chasing the newest closed-source tool. It was a practical search for open, controllable workflows that could scale with real nonprofit work.

I now have a setup that feels like a genuine thinking partner rather than a one-off responder. The repetitive context management and basic synthesis get handed off, so I can focus on judgment, strategy, and the human parts of the work that matter most.

---

## **The takeaway**

Stop renting your memory. The evolution was never about chasing the newest closed-source tool — it was a practical search for open, controllable workflows that actually support the work only you can do.

## **Read this if**

You're walking a similar path — prioritizing open-source, cost awareness, and moving past basic RAG toward structured agent memory.

## **Resources**

* Jake's Interpretable Context Methodology (ICM)
* Harness Engineering
* Cloudflare Workers/AI
* Alibaba Cloud credits
* Kiro AI IDE
* BMAD Method
* Open Brain
* ClaudeBot
* ZeroClaw
* Cognee
* Hermes' Agent (Nous Research)

## **Next up**

If this resonated, dig into how Cognee builds knowledge graphs with rich relationships, or explore Hermes Agent for self-improving persistent agents — and see how the stack delivers relational memory that actually evolves.

---

**Disclaimer:** This is garage tinkering — not production gospel. My path from one-shot prompting to Hermes + Cognee worked for my nonprofit volunteer work, but your mileage may vary. The stack evolves fast, duct-tape what works, and keep grinding toward workflows that serve you.

#aiworkflow #oneshotprompting #agenticworkflows #opensource #hermes #cognee #knowledgegraphs #rag #specdriven #persistentmemory