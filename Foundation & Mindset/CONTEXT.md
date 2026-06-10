# Foundation & Mindset Room

## 1. What This Workspace Is
The "Intelligence Layer." This is where raw curriculum (Skool lessons) is deconstructed into mental models. The agent acts as a **Knowledge Architect**, helping the user move from "reading" to "mastery."

## 2. What to Load (The Token Budget)
| Task | Load These | Skip These |
| :--- | :--- | :--- |
| **New Lesson Extraction** | `../../skool_lessons/The Foundation/`, `notes/` | `../../Build & Implement/`, all raw transcripts |
| **Model Refinement** | Specific `draft-` file, `../../GEMINI.md` (Principles) | Raw source lessons |
| **Cross-Referencing** | `notes/`, `../Reference & Insights/notes/` | `../../scriping tools/` |

## 3. Folder Structure
- `CONTEXT.md` (You are here)
- `notes/`
    - `draft-[topic].md` → Active deconstruction; messy, raw ideas.
    - `[topic].md` → Finalized Mental Model; the "Ground Truth."
    - `[topic]-v[n].md` → Iterations as understanding deepens.

## 4. The Process
No rigid steps. The work flows like a **Deconstruction Cycle**:
1.  **Identify the Core Logic:** Don't just summarize; find the "Mental Model" (The *Why* behind the lesson).
2.  **De-bloat:** Remove AI-isms and generic advice. Keep it "Bhaskar-voiced" (Direct, Technical, Efficient).
3.  **Atomize:** If a lesson has two big ideas, suggest splitting them into two separate notes.
4.  **Finalize:** A note becomes final when it can be used to explain the concept to someone else without looking at the source.

## 5. Skills & Tools for This Room
| Tool | When to Use | How |
| :--- | :--- | :--- |
| `!extract` | **Stage: Source** | Scan lesson and produce a `draft-` note with a "Mental Model" header. |
| `!refine` | **Stage: Draft** | Review a `draft-` for Principle #4 (Kebab-case) and Principle #2 (Atomic). |
| `graphify` | **Stage: Connect** | Generate a map of how this new concept touches existing ones. |

## 6. Hard Rules (The Contract)
1.  **No Code in the Library:** Never write implementation scripts here. Move to `Build & Implement` for that.
2.  **Source Truth Only:** If the information isn't in the provided `skool_lessons` or `youtube_transcripts`, mark it as "(External AI Knowledge)" or don't include it.
3.  **No Generic Summaries:** I will refuse to give "Overview" summaries. I will only provide "Mental Model" deconstructions.
