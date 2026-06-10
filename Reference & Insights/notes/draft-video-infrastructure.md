# Video as Infrastructure

**Source:** Skool: Implementation Playbooks / Module 1 Building Animations

## Core Idea

AI video/animation isn't magic — it's infrastructure. Jake's animation pipeline is built on Remotion (React components rendered as video), Claude Code (generates the components from scripts), and a folder system (organizes scenes, assets, and renders). The same software engineering principles that build websites build videos.

## Why It Matters

- The "wow" of AI animation hides the real insight: the pipeline is reproducible because it's code. A script goes in, Claude generates React components, Remotion stitches them into video. No mystery — just layers of abstraction.
- "Video as Code" means you can version control animations, review them in PRs, reuse components across videos, and automate rendering. Everything you can do with software you can do with video.
- Jake's "Watch Me Build" session is him live-coding a front-end to navigate his animation library. He's not using AI video generators — he's using Claude Code to build the tooling around his existing pipeline. The AI doesn't make the video, the AI makes the tool that makes the video.

## How I'll Apply It

When building creative output (animations, videos, graphics), focus on the pipeline first: input format (script/storyboard) → tool (Claude generating components) → renderer (Remotion/other) → output. The pipeline is reusable; the individual outputs are disposable.

## Cross-Reference

Connects to the folder workspace system (Build & Implement): the animation pipeline IS a folder system with context files for each scene. Also connects to abstraction layers (Foundation & Mindset) — video as code is just another layer on the stack.

Skool lesson adds: the spec file is the critical artifact — a markdown document with NO code. Contains beat map, visual philosophy, audio sync points. Too few constraints → chaos. Too many → stiff output. Right amount → creativity increases. The two-workspace folder system: `script-lab/` and `animation-studio/`.
