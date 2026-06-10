# Folder-as-Workspace System

**Source:** Skool: The Foundation / Module 3 / 3.1 The Full Walkthrough

## Core Idea

Instead of building AI agents (which get obsolete when models update), build a folder system with markdown files that route your AI to the right context. The folder structure IS the architecture — AGENTS.md as the map, context files as rooms, skills as plug-ins.

## Why It Matters

- Agents lock you into a specific AI provider's ecosystem. Folders and markdown files are universal — any AI tool can read them. When the next model drops, your folder structure still works.
- The three layers: (1) AGENTS.md at the root tells the AI what the project is and how to navigate it, (2) CONTEXT.md files in each subfolder tell the AI what's in that room, (3) skills/plugins are reusable instruction sets loaded on demand.
- This replaces: vector databases, RAG pipelines, multi-agent orchestrators, and most custom tooling. A flat file system that both you and the AI can read and write.
- Jake's key insight: folders are the new database, markdown is the new API. Files are persistent, debuggable, version-controllable, and model-agnostic.

## How I'll Apply It

This Framework folder IS my implementation of this system. I'll continue refining it — making sure every subfolder has a CONTEXT.md, keeping the AGENTS.md sharp, and adding skills as reusable prompt modules.

## Cross-Reference

This is the practical implementation of everything in Foundation & Mindset. The abstraction layers video explains WHY files work better than agents. The template pattern explains WHY markdown is the right format. The deconstruction video explains how to iterate on the system.

Skool lesson adds: the three-layer system (map, rooms, tools) is built on separation of concerns — a 1972 software engineering principle. Naming conventions replace databases: no SQL, no vector DB, just `api-auth-guide_draft.md`, `demo_v2.md`, `2026-03-launch-week.md`. The routing table is the AI's navigation — for task X, read these files, skip those.
