# What You'll Get From This

# What You'll Get From This

The discipline that emerged from everything in this course. Not how to use AI. How to know when to use AI, when to use traditional code, and when to keep a human in the loop. This is what the early videos were building toward.

# 📝 Why This Lesson Is Here

In Module 2, I described a coding pyramid: machine code at the base, Python in the middle, LLMs at the top. Each layer lets a novice do what used to require an expert. I also introduced the THINK acronym for working with AI, a simple workflow for academic writing.

Both of those were early versions of the same idea. They were pointing at something I did not have a name for yet.

Now it has a name: computational orchestration.

This is the discipline of knowing which type of computation to apply to which problem. Traditional code for the deterministic parts. Language models for the semantic parts. Humans for the judgment calls. And most importantly, knowing when to use which.

The article below lays out where this idea came from, why it matters, and the 60/30/10 pattern that keeps showing up in every successful AI implementation I have built or observed. 60% traditional database queries. 30% basic rule-based logic. 10% actual AI calls, only where semantic understanding matters. The 10% makes the whole thing feel intelligent. The 90% makes it actually work.

If you came to this course through the old videos in Module 2, this is where the early thinking landed. If you started here, go back and watch those videos after reading this. You will see the seeds of everything in this article planted years earlier.

═══════════════════════════════════════

---

# I've been watching something weird happen in tech, and nobody's really talking about it.

Not the AI hype - god knows we have enough of that.

I mean the thing underneath. The pattern that keeps showing up when senior engineers actually build something that works.

They're not "using AI" the way LinkedIn influencers think. Sure there is prompt engineering or now the new buzz word is “context engineering” for vibe coders.

But honestly the real developers, they're doing something else entirely. Something that doesn't have a name yet.

Well, it does now. I'm calling it **Computational Orchestration.**

![](https://substackcdn.com/image/fetch/$s_!5If7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfba125e-a939-4b95-bef8-4b6ad4eb7f59_585x390.png "null")

## **Here's What I Keep Seeing**

Walk into any company that's actually shipping AI features (not just talking about them), and you'll find the same thing:

> Some grizzled engineer who's given up trying to explain what they actually do.

"*I'm the AI person,*" they'll say, dead-eyed, because it's easier than explaining that they spend **80% of their time preventing AI from being used where it shouldn't be.**

These people aren't prompt engineers. They're not "AI specialists." They're doing something harder - they're **orchestrating** different types of computation to **solve** actual problems.

Traditional code for the deterministic stuff. LLMs for the semantic stuff. Humans for the judgment calls. And most importantly, **they know when to use which.**

That's not a job title. That's a discipline that's emerging whether we name it or not.

## **Why "Orchestration" Isn't Just Another Buzzword**

Look, I hate buzzwords as much as you do. Probably more. But orchestration is the only word that actually captures what's happening.

I spent two hours straight trying to figure out what to call “AI engineers” that didn’t use the word AI. It really comes down to this.

When you *orchestrate*, you're not playing every instrument. You're not even writing all the music. You're deciding **when the strings come in**, when the percussion drops out, when to let the soloist improvise.

> As a great Jazz musician once said, the silence between the notes is the hardest part of Jazz.

That's exactly what we're doing with computation now:

* This part needs deterministic code
* This part needs an LLM
* This part needs human judgment
* This part needs all three in sequence

  ![](https://substackcdn.com/image/fetch/$s_!F-Bb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd33db2a-b429-428a-83ed-60ffbc7fc686_949x951.png "null")

## **The Thing Nobody Wants to Admit**

Most "AI transformations" are failing. Not because the tech doesn't work, but because nobody's orchestrating it.

Companies are doing the equivalent of giving everyone in the **orchestra a trumpet and telling them to play as loud as possible.** Then they wonder why it sounds like *shit*.

Real orchestration looks boring from the outside. Like that client I worked with last month - they came in wanting "AI everything." What we built:

* 60% regular database queries (because they're fast and cheap)
* 30% basic if-then logic (because it's debuggable)
* 10% actual AI calls (only where semantic understanding mattered)

**The 10% made the whole thing feel magical.** The 90% made it actually work.

That's computational orchestration. Not defaulting to the shiniest tool but knowing which computation fits which problem.

## **What Makes This a Discipline, Not Just Common Sense**

Three things keep showing up in every successful implementation:

#### **1. Abstraction Without Abandonment**

We're not replacing code with prompts. We're adding a semantic layer on top, the same way Python sits on top of C. Every time I see someone claim "AI will replace programming," I know they've never actually built anything.

You still need to understand the layers below. You just work at a higher level most of the time.

> I wrote a whole article on the history of this process if you want to dive deeper: [The Next Language Layer](https://jakevanclief.substack.com/p/the-next-language-layer "https://jakevanclief.substack.com/p/the-next-language-layer")

#### **2. Judgment AND Implementation**

The hardest part of my job isn't making AI work. **It's knowing when not to use it.**

Last week, a small startup wanted me to build an AI system to schedule their meetings. I built them a Google Calendar integration instead and let Gemini handle the rest.

Took less than an hour. Works perfectly.

They think I'm a genius. (*I would love to call myself one, but I have a laundry list of dumb things I still do on a daily basis that might prove otherwise*).

That's the judgment layer - **knowing when boring beats brilliant.**

#### **3. Flow Over Features**

It doesn't matter if your LLM can write Shakespeare if it's in the wrong place in the pipeline. **A simple regex in the right spot beats GPT-4 in the wrong spot.**

The value isn't in what each component can do. It's in how they flow together.

![](https://substackcdn.com/image/fetch/$s_!cN9x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ad32c5d-2181-4678-864c-c2d0e71e02fe_586x583.png "null")

## **The Uncomfortable Truth About Where This Goes**

We've been here before. When compilers came along in the 1950s, assembly programmers lost their minds. *"Real programmers write machine code!"* They weren't wrong - **they were just about to become irrelevant.**

Same thing's happening now. In five years, the question won't be "*can you code?"* It'll be *"can you orchestrate code?"*

Because here's what's really happening: We're not getting one type of computation anymore. We're getting lots of them:

* Deterministic (traditional code)
* Probabilistic (ML models)
* Semantic (LLMs)
* Quantum (coming sooner than you think)
* Biological (yeah, that's a thing now)

> Someone needs to orchestrate all of this. Not just architect the systems but understand how different types of computation complement and constrain each other.

If you're a developer who finds yourself:

* Designing systems that mix code and AI
* Explaining why we shouldn't use AI for that particular thing
* Building the glue between human decisions and machine execution
* Spending more time on "when" than "how"

Congratulations. **You're already a computational orchestrator.** You just didn't know what to call it.

And that's the thing - this discipline is emerging whether we name it or not. I'm just tired of not having words for what we actually do.

## **The Call to Action (Or Whatever)**

I'm not trying to sell you on a certification or a course. I don't have a framework to license or a methodology to trademark.

I'm just naming something that's already happening.

Because once we name it, we can talk about it. **Once we can talk about it, we can teach it.** Once we can teach it, we can stop having the same dumb arguments about whether AI will replace programmers.

It won't. It'll just change what programming means. **Again.**

It WILL replace SOME programmers, at least as we see them.

Just like compilers did.

Just like high-level languages did.

Just like every abstraction layer before.

The code isn't dying. **It's just moving up a level.** And someone needs to orchestrate what happens at that level.

> That someone might as well be us.

Welcome to computational orchestration.

You're probably already doing it.

---

*Jake Van Clief* *Computational Orchestration Architect* ….. *Naming the thing we're all doing anyway*