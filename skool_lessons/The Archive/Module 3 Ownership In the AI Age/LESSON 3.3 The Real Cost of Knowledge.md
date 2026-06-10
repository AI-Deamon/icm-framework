# What You'll Get From This

# What You'll Get From This

A thought experiment that reframes how you think about AI energy costs, why local AI changes the math, and what "energy per insight" means for how we deploy intelligence.

[VIDEO coming soon]

# 📝 The Lesson

I have a thought experiment for my data friends out there.

***Option 1: A solar-powered laptop with all of Wikipedia saved on it.***

***Option 2: The same laptop, but with a local AI model instead.***

It's an apocalypse. Global Internet is gone.

> Which do you pick?
>
> ![](https://substackcdn.com/image/fetch/$s_!Eg6c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff426886a-b262-4226-a626-3fab50917e22_1024x1024.png "null")

Most of you probably picked Wikipedia. It seems obvious, right? AI is this massive energy hog, while Wikipedia is just... text. Static. Efficient. **The safe choice when every watt counts.**

But here's the thing: **you're wrong.**

*Not completely wrong,* but wrong *in the way that matters.* And understanding why reveals something fascinating about how we've been thinking about **AI's energy cost all wrong.**

Let me walk you through the numbers. Because once you see them, you'll understand why the real energy problem with AI isn't what it uses - **it's where it lives.**

## **The Laptop That Could Save Your Life**

First, let's establish our apocalypse setup.

You've got a modern, efficient laptop - think MacBook Air with M-series silicon. These machines are engineering marvels, sipping just 3-5W at idle, maybe 15W during normal use.¹

Your lifeline is a portable **100W solar panel** that, assuming 5 peak sun hours daily, generates about **500 watt-hours per day.²**

With Wikipedia loaded locally, you're accessing static files from an SSD.

No computation, no networking, just reading.

Your laptop draws its baseline **15W,** giving you over 33 hours of use from your daily solar budget.³ More hours than there are in a day. Unlimited access to humanity's accumulated knowledge.

> **Seems unbeatable, right?**

Now let's look at the AI option. Running a local language model on that same efficient laptop adds about 38W to your power draw.⁴ Total consumption jumps to 53W. **Your daily budget now gives you just 9.4 hours of AI time**.

***If a complex query takes 30 seconds of processing, that's about 1,128 queries per day.***

The Wikipedia folks are feeling pretty *smug* right now. But they're missing something crucial.

![](https://substackcdn.com/image/fetch/$s_!bLYb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72ca37a2-7d01-4df4-bea4-db88ef210f2f_1536x1024.png "null")

## **The Hidden Efficiency of Intelligence**

Here's what changes everything: those 1,128 AI queries aren't equivalent to 1,128 Wikipedia searches. **They're not even in the same universe.**

When you ask Wikipedia "how to purify water," you get an article. When you ask AI the same question, you get a customized response based on what materials you just told it you have available.

Wikipedia tells you what water purification is. **AI helps you build a filter from coffee filters and sand.**

> But the real shift comes when we zoom out from our apocalypse scenario and look at the actual energy numbers of our current, connected world.

In 2021, Wikipedia's entire global server infrastructure consumed **3.143 GWh** of electricity to serve **265 billion page views.⁵**

Do the math: that's 0.0000118 kWh per page view. *Incredibly efficient.*

A single ChatGPT query? About 0.0003 kWh.⁶ **That's 25 times more energy than a Wikipedia page view.**

Case closed, right? *AI is the energy villain?*

#### **Not so fast.**

Because here's what nobody talks about:

**Wikipedia can only give you what already exists.** Every new article, every edit, every update requires human energy - the most expensive kind. AI generates new, synthesized information on demand. It's not 25 times more expensive than Wikipedia.

It's doing something **Wikipedia literally cannot do.**

## **The Real Energy Monsters**

But if you really want to understand AI's energy problem, forget about individual queries. Let's talk about *where AI actually lives.*

**Data centers** - those massive buildings full of servers that power the cloud - consume between **240 and 340 TWh globally per year.⁷**

That's **1-2% of all global electricity,** **comparable to the entire aviation industry.**⁸ In the US alone, data center consumption is projected to surge from **4.4%** of national electricity in 2023 to as high as **12% by 2028.⁹**

**Here's the kicker:** up to 40% of that energy isn't even used for computing.

**It's used for cooling.¹⁰** Every watt of electricity that goes into a server becomes heat that must be *removed.* The average data center has a Power Usage Effectiveness (PUE) **of 1.58 to 2.0,** meaning *for every watt* powering computers, *another watt* goes to overhead.¹¹

> This is where AI's reputation as an energy monster comes from.

Training GPT-3 required **1,287 MWh** - enough to power **120 American homes** for a year.¹² It also consumed **700,000 liters of fresh water just for cooling.**¹³

Google's Gemini Ultra training reportedly cost **$191 million,** much of that in energy costs.¹⁴

**But training is a one-time cost**.

*The real energy drain?* **Inference** - actually using the model.

**This accounts for 60-90% of an AI model's lifetime energy consumption.¹⁵** And when that inference happens in massive, *inefficient data centers*, **the waste compounds.**

## **The Local Revolution**

**Which brings us back to our apocalypse laptop** and why *the equation changes so dramatically.*

**Running AI locally eliminates two massive energy drains:** network transmission and centralized cooling.

* No data traveling thousands of miles to a data center and back.
* No 40% overhead for industrial cooling systems.
* Just your laptop's tiny fan (if it even has one) handling its own heat.

Suddenly, that **38W** for local AI inference *looks different.* **You're not adding 38W** to a system already burning hundreds of watts on infrastructure. **You're adding 38W, period.**

But here's where it gets really interesting. Remember how a single AI query **uses 5 to 1,000 times more energy than a Google search**, depending on who you ask?¹⁶

That massive range exists because **people are measuring different things.**

Include the data center overhead, networking, and cooling? **AI looks terrible.** Measure just the computation itself? *The gap shrinks dramatically.*

## **The Synthesis Engine**

Let me put this in perspective with a real example. I asked a local AI model running on my laptop:

> "I have coffee filters, sand, gravel, and plastic bottles. How do I build a water filter?"

The response synthesized information from multiple domains - **chemistry, engineering, survival techniques** - *into step-by-step instructions* **specific** to my **materials.**

To get the same result from Wikipedia, **I'd need to read articles on water purification, filtration media, DIY construction**, *and then* figure out how to combine that knowledge myself.

![](https://substackcdn.com/image/fetch/$s_!5qZ3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b92e110-790e-4241-a43c-47b1a573d850_1536x1024.png "null")

**Time spent:** *30 seconds* of AI processing **versus** potentially **hours** of **human research** and synthesis.

**Energy used:** 0.0003 kWh for AI versus... what? How do we even calculate the energy cost of human cognitive labor and the running of the laptop for however long it takes us to synthesis it?

**This is the paradigm shift everyone's missing.** We're comparing AI to traditional computing *like it's just a more expensive calculator.* But AI isn't doing arithmetic faster.

It's doing something fundamentally different: **automated synthesis.**

## **Numbers at a Glance**

So let’s review what I just gave you:

**Traditional Information Retrieval:**

* Google Search: ~0.0003 kWh per query
* Wikipedia page view: ~0.0000118 kWh server-side

**Cloud AI:**

* GPT-3 query: 0.0003 kWh
* GPT-4 query: 0.0005 kWh
* AI image generation: Equivalent to charging a smartphone

**Local AI:**

* Text generation on efficient laptop: 38W additional power draw
* ~0.0004 kWh per image on a PC with GPU

**But remember:** these aren't apples-to-apples comparisons.

That Wikipedia page view gets you one static page. That AI query might synthesize information from thousands of sources **into exactly what you need.**

## **The Future Is Distributed**

The real insight from our apocalypse thought experiment isn't about choosing between Wikipedia and AI. It's about recognizing that the massive energy cost of AI **isn't inherent to the technology** - **it's a function of how we've chosen to deploy it.**

***Centralized in massive data centers? AI is an energy disaster. Distributed across billions of efficient devices? It becomes something else entirely.***

> The irony is delicious.

We've spent decades moving computing **to the cloud for efficiency.**

But AI might be the technology that brings it all back home. *Not because local* is always more efficient - those hyperscale data centers with their 1.1 PUE and renewable energy contracts often are more efficient.²⁴ But because the overhead of centralization might finally outweigh its benefits.

## **So Which Laptop Do You Choose?**

If you asked me *four years ago,* I would have said Wikipedia, no question.

Unlimited access to static knowledge versus limited access to dynamic intelligence? Easy choice.

But I've changed my mind. Not because the energy math changed - but because I've realized I was asking the wrong question.

**It's not about energy per query.** *It's about energy per insight.*

Energy per problem solved.

In an apocalypse, I don't need (or want) to browse Wikipedia for **33 hours a day.** I need to solve immediate, specific problems with the materials at hand. *I need synthesis,* not just retrieval. I need intelligence, not just information.

Give me the AI. I'll ration **those 9.4 hours** like they're gold. Because in a world where every decision might be life or death, having a tireless advisor that can synthesize humanity's knowledge into specific solutions **is worth more than all the encyclopedia articles ever written.**

The real lesson? We've been so focused on traditional information pipelines that we've missed the revolution happening at the edges. Every efficiency gain, every smaller model, every local deployment chips away at the assumption that intelligence **must be centralized to be efficient.**

The apocalypse laptop *isn't just a thought experiment.*

It's a glimpse of computing's future: distributed, efficient, and intelligent. The question isn't whether AI uses too much energy. It's whether we're deploying it in the right places.

Your move, data friends. **Which laptop are you really choosing?**

---

*The calculations and energy comparisons in this article are drawn from comprehensive analysis of data center consumption, AI training costs, and device efficiency studies. For the full technical breakdown and additional citations, see the references below.*

# **Why This Is in This Course**

The earlier lessons in this course focus on mindset, methodology, and the value of human expertise. This lesson is about infrastructure. It matters because the decisions being made right now about how AI is deployed, centralized versus distributed, cloud versus local, will determine who has access to these tools and at what cost.

The computational orchestration framework from this course (60% traditional code, 30% rule-based logic, 10% AI) is partly an answer to the energy question. If you know which layer a problem belongs on, you do not waste compute on tasks that do not need it. You run AI on the 10% that requires synthesis and handle the rest with cheaper, more efficient methods. That is good engineering. It is also good energy policy.

Understanding how AI actually consumes energy, and where the waste really lives, makes you a better decision-maker about when and how to use it.