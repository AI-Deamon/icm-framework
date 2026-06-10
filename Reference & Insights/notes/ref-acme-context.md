# Acme Reference: CONTEXT.md Example

This file serves as a reference for the "Elite" Layer 2 (Room Context) standard used by the Acme DevRel team.

## Original Source Content:

```markdown
# Writing Room

## What This Workspace Is
Where ideas become polished drafts. Someone brings a topic. The agent helps research, outline, write, and refine it in the right voice. Output goes to final/ and can feed into the production pipeline.

## What to Load
| Task | Load These | Skip These |
| :--- | :--- | :--- |
| Write a blog post | docs/voice.md, docs/style-guide.md | docs/audience.md (unless targeting specific) |
| Write a tutorial | docs/voice.md, docs/audience.md, docs/style-guide.md | - |
| Edit/review a draft | docs/voice.md, the draft itself | docs/audience.md, docs/style-guide.md |
| Research only | Nothing from docs/ | Use Web Search MCP |

## Folder Structure
writing-room/
├── CONTEXT.md
├── docs/
│   ├── voice.md (Personality constraints)
│   ├── style-guide.md (Formatting/structure)
│   └── audience.md (Who reads this)
├── drafts/ (Work in progress)
└── final/ (Ready for production)

## The Process
1. **Understand the topic** - what's the idea and why does it matter?
2. **Find the angle** - what's the specific take, not the generic explainer?
3. **Write in brand voice** - at the right depth for the audience.
4. **Catch problems** - voice drift, AI-isms, structural issues.

## Skills & Tools for This Workspace
| Skill / Tool | When to Use | How |
| :--- | :--- | :--- |
| /humanizer | Before any draft moves to final/ | Catches AI-isms. Non-negotiable. |
| /doc-coauthoring | Long-form pieces only (2000+ words) | Activates structured co-writing. |
| Web Search MCP | Research phase | Current data/competitor analysis. |

## Hard Rules
1. **Specs are contracts, not blueprints.**
2. **Output must be tested.**
3. **Don't build without a spec.**
```
