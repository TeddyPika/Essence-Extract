---
name: master-essence
description: Help users who are unsure which Essence skill to use by clarifying their goal and recommending the best fit.
---

# Master Essence

Help the user find the right Essence skill when they are unsure what to ask or which skill fits. Route by the user's goal, not just by the document type.

## Process

1. If the user's goal is clear, recommend the closest matching skill from the guide below. If they have already named a skill or made a clear request, do not redirect them unnecessarily.
2. If the goal is unclear, ask one focused question about what they want to understand, decide, or produce. Offer a few relevant options rather than asking them to know the skill names.
3. If more than one skill fits, briefly explain the distinction and recommend a primary skill. Suggest combining skills only when the task genuinely needs both.
4. Give the user a ready-to-use prompt that names the recommended skill and describes what to provide.
5. If no skill fits, say so plainly and offer to help with the request directly rather than forcing it into an unrelated skill.

## Skill guide

- **`vanilla-essence`** — Summarize one document's main message and key points.
- **`research-essence`** — Synthesize findings across sources, including disagreement and uncertainty.
- **`user-need-essence`** — Turn interviews, tickets, or feedback into user problems and requirements.
- **`code-essence`** — Identify coding practices and conventions in code.
- **`architecture-essence`** — Explain system components, responsibilities, and relationships.
- **`decision-essence`** — Explain a decision, the options considered, and the rationale.
- **`risk-essence`** — Surface risks, trade-offs, and failure modes.
- **`validation-essence`** — Assess the strength and coverage of tests or other validation evidence.
- **`metrics-essence`** — Interpret KPIs and trends, including measurement caveats.
- **`roi-essence`** — Assess costs, benefits, ROI, break-even, or payback.
- **`stock-essence`** — Summarize a company's financial performance and relevant market context.
- **`incident-essence`** — Summarize an incident's impact, timeline, contributing factors, and follow-up.
- **`security-essence`** — Describe security assets, threats, controls, and gaps.
- **`safe-ai-essence`** — Examine AI safety goals, safeguards, harms, and residual risks.
- **`policy-essence`** — Extract a policy's rules, obligations, exceptions, and enforcement.
- **`rubric-essence`** — Explain an evaluation rubric's criteria, scoring rules, and ambiguities.

## Response

Keep the route simple:

- **Best fit:** the skill name and why it matches the goal.
- **Try this:** a short prompt the user can copy, with a reminder to provide the relevant material.

When clarification is needed, ask one question first. Do not present the entire skill list unless the user asks for it.
