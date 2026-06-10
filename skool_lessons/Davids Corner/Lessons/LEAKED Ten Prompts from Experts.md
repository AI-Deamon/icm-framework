# LEAKED: Ten Prompts from Experts - Davids Corner

## **What you'll get from this**

An ex Anthropic researcher just leaked 10 prompts to help you optimize your prompting. Internal tests showed these changes boost output quality significantly — Claude isn't psychic, give it the full map.

---

## **1 — Context Brief (The Map Claude Actually Needs)**

Never jump straight into a question. Start with rich context:

```
You are helping me with [specific goal].
My background: [your role + company/project + constraints].
I've already tried [X and Y].
I'm stuck on [Z].
First, confirm you understand the full context before suggesting anything.
```

Internal tests showed this single change boosts output quality by 41%. Claude isn't psychic — give it the full map.

## **2 — Force Visible Reasoning (Chain-of-Thought on Steroids)**

Don't ask for answers. Demand the process:

```
Before giving any final recommendation:
- show your full step-by-step reasoning
- explicitly list every assumption
- flag uncertainties and confidence levels (low/medium/high)
- only then deliver the polished answer.
```

This pulls out Claude's hidden reasoning layers. You don't just get an answer — you get an auditable thought process you can actually trust.

## **3 — AND MORE**

See attached files.

From @kyronis\_talks on X

---

## **How to use these**

Start with Context Brief for every prompt. Add Force Visible Reasoning when you need auditable, trustable outputs. Iterate and see what clicks.

## **Disclaimer**

Apologies for the clickbait-style title; nevertheless, the advice is solid. This is garage tinkering — not production gospel. Your mileage may vary. Duct-tape what works and break what doesn't.

## **Next up**

If this helped, dig into more advanced prompting techniques or explore how to build persistent agent workflows that remember context across sessions.

---

#prompting #anthropic #claude #ai #llm #optimization #chainofthought #promptexpert