# Claude Code Setup & Workflow

**Source:** Skool: The Foundation / Module 4 / 4.1-4.5 Claude Code series

## Core Idea

Claude Code is not just a REPL for coding — it's a terminal-native AI coworker that reads your entire project context. The 5-session series covers: (1) install and configure properly, (2) Claude Code in practice, (3) Claude Desktop as a thinking partner, (4) making Claude understand your project, (5) advanced workflows.

## Why It Matters

- Most people use Claude wrong: they copy-paste snippets into the web interface. Claude Code runs in your terminal inside your project — it sees your file tree, reads your code, and understands context without you having to explain it every time.
- Session 4 is the key one: making Claude understand your project means writing a AGENTS.md that describes the architecture, conventions, and goals. Without this file, Claude starts fresh every session and wastes tokens re-learning your project.
- MCP (Model Context Protocol) setup is critical — it lets Claude access tools (like file system, database, browser) directly from the terminal instead of you having to copy-paste results.

## How I'll Apply It

- Make sure AGENTS.md is always up to date before starting a new session
- Set up MCP servers for the tools I use most (filesystem, GitHub, browser)
- Use Claude Desktop (with projects) for thinking/planning, Claude Code for execution

## Cross-Reference

The AGENTS.md file is the concrete implementation of the template pattern (Foundation & Mindset). It's a Mad Libs template for the project — the AI fills in the blanks as it works.

Skool lessons add: Session 4.2 explains the Read-Think-Write-Check-Adjust iteration loop. Session 4.3 shifts from using Claude as a "vending machine" to a thinking partner. Session 4.4 teaches writing the AGENTS.md that makes Claude behave like it's been on your project for a month.
