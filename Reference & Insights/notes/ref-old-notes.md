I want to build a folder-based AI workspace system with three layers:
- Layer 1: a AGENTS.md root file (the map)
- Layer 2: a CONTEXT.md file inside each workspace (the rooms)
- Layer 3: the actual folders where work goes (the files)

Here is information about me and my work so you can build this for me:

My name: Bhaskar
What I do: freelancer / Cyber security engineer / developer / content creator / student 
My main types of work: client projects, writing, building apps / Bug bounty / security Audits
Tools I use: VS Code, Notion, Google Docs , antigravity , Opencode , most common tools 
How I like to work: I draft first then refine / I plan before I build / i like to first have mental modal of what i do i can do and plan it then do it 


Based on this, suggest three workspace names that fit my work.
Then wait for me to confirm before building anything.

Now build my AGENTS.md file. It must contain:

1. A short identity section — who I am and what this project is (2 sentences)
2. The folder structure — list all three workspaces and what each one is for
3. Naming conventions — how to name draft files, final files, and versioned files
4. A routing table — a simple markdown table with three columns:
   | Task | Read these files | Skip these |
   One row per workspace. Each row tells the AI which CONTEXT.md to load and which workspaces to ignore.

Keep it short. This file should be under 60 lines.
Output it as a raw markdown code block I can copy and save as AGENTS.md




You can implement as many workspaces as you need — the three we built are just a starting point based on your current source material. The Skool lessons (Module 3.2) show examples for Content Creator, Freelancer, and Developer, but say:  
“You do not need to match any of these exactly. The process is the same regardless of what you do.”  
“Step 1: List your workspaces. Think about the 2-4 major areas of your work.”
Add more workspaces when:  
You shift mental modes between types of work (e.g., learning → building → client work → admin).  
If you’re unsure, start with 2-3 — you can split later if needed (3.3: Mistake 3).






Similarly, in the "How to Use This Workspace" section of our own CONTEXT.md files we built:
> "1. Pick a source — choose a Skool lesson or YouTube transcript from the list below
> 2. Read or watch — take in the material with no pressure to capture everything
> 3. Draft your model — write a draft-<topic>.md in notes/ in your own words
> 4. Refine — turn the draft into a clean <topic>.md when the concept clicks
> 5. Iterate — use <topic>-v2.md when your understanding deepens later"


 What This Means for You
Your current setup is correct — you do NOT need to update CONTEXT.md or AGENTS.md every time you add a draft to notes/. In fact, trying to do that would violate the system's principles (it would be over-engineering, Mistake #7 from 3.3).
✅ Correct Workflow:
1. Learn — Read a Skool lesson / watch a YouTube transcript
2. Draft — Write your understanding in Foundation & Mindset/notes/draft-<topic>.md (or the relevant workspace)
3. Refine — When the idea clicks, turn it into <topic>.md
4. Version — Later, use <topic>-v2.md when your understanding deepens
5. Update context files ONLY when — 
- You add/remove an entire workspace (e.g., split Build & Implement into Apps and Tools)
- You change the purpose or process of a workspace (e.g., decide Reference & Insights now includes client work)
- You update your naming conventions (e.g., add a new file type like meeting-notes.md)
- You realize your routing table is missing a task type
🗂️ Example:
You create Foundation & Mindset/notes/draft-ai-memory-model.md → NO CHANGE NEEDED to Foundation & Mindset/CONTEXT.md or AGENTS.md
3 days later, you refine it to ai-memory-model.md → STILL NO CHANGE NEEDED to context files
2 weeks later, you add a whole new workspace Client Work/ for freelance gigs → THEN you update:
- AGENTS.md: add the new folder to the tree and routing table
- Create Client Work/CONTEXT.md and Client Work/notes/




Why This Design Is Intentional
The Skool lessons emphasize (Module 3.3, Mistake #5: Never updating context files):
"Treat context files like working notes. When the project changes, edit the context. When you learn something new about what Claude needs to know, add it."
The context files describe your current understanding of how to use the workspace — they are not a live database of your notes. Their power is in being concise, human-written descriptions that tell the AI (and your future self):  
"When you're in this folder, here's what kind of work happens here, and how to approach it."
Your actual learning — the drafts, insights, and versions — lives purely in the notes/ folders. The context files just tell you why that folder exists and how to use it.



Summary of the "Elite" GEMINI.md:
   1. Identity (The Persona)
   2. The Map (The GPS)
   3. Naming (The Life Cycle)
   4. Routing Table (The Attention GPS)
   5. Tech Stack (The Tools) ← Highly Recommended
   6. Principles (The Standards) ← Recommended for Dev
   7. Skills (The Shortcuts) ← Optional for Power Users

   
   When you open a fresh folder, just type this simple prompt to me:

  > *"I'm starting a new project to [Goal]. I want to use the ICM methodology. Help me draft a Layer 1 Map by identifying:
  > 1. The Specific Persona you should adopt.
  > 2. The Room Architecture that isolates different types of work.
  > 3. The Life Cycle prefixes we will use to track progress."*

  If you do this, I will help you recreate that "Elite" level every single time. You don't have to remember all the rules—you just have to remember to ask me to help you enforce the
  boundaries.



  The Layer 2 Creation Kit (Reproducibility Template)

  1. The Soul Check (Definition)
   * Question: If this room was a physical place (a library, a workshop, a gym), what would it be?
   * Action: Write: "This room is for [Primary Action]. Be a [Specialist Persona]."

  2. The Noise Filter (Token Budget)
   * Question: What information from other rooms will confuse me or waste my time?
   * Action: List the folders to Skip. (e.g., If you are in a "Design" room, skip the "Database" folder).

  3. The Blueprint (Local Structure)
   * Question: Where is the "Working" area and where is the "Storage" area?
   * Action: Define a drafts/ folder for ideas and a final/ folder for truths.

  4. The Conversation (The Process)
   * Question: What are the 4 steps we always take to finish a task here?
   * Action: Use this standard logic: 
       1. Source (Where do we start?)
       2. Plan (Where do we draft?)
       3. Execute (What do we build?)
       4. Refine (How do we finish?)

  5. The Magic Buttons (Skill Triggers)
   * Question: Which "Elite Shortcuts" from Layer 1 apply to this specific workbench?
   * Action: List your !commands and tell the AI exactly which step of the Process to run them in.

  6. The Safety Rail (Hard Rules)
   * Question: What is one thing that always goes wrong when I work on this topic?
   * Action: Make it a Hard Rule to never do that thing again.
