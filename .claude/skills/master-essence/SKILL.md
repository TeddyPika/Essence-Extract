---
name: master-essence
description: Automatically route an Essence task to the best-fit skill and carry it out, asking for clarification only when needed.
---

# Master Essence

Automatically handle the user's request with the best-fit Essence skill. Route by the goal, not just the document type. Do not stop at recommending a skill or make the user invoke it again.

Perform routing and the selected skill's work directly. Do not invoke agents, delegate to subagents, or use agent tools.

## Process

1. Identify what the user wants to understand, decide, or produce, along with the relevant material they supplied.
2. Select the most specific matching skill from the guide below. If the user explicitly names an Essence skill, use that skill unless it clearly conflicts with their request.
3. If the selected skill's `SKILL.md` is available in the workspace, read it and follow its process and response guidance. If it is not available, use the guide below to complete the task directly; do not ask the user to invoke another skill.
4. If the goal or necessary scope is ambiguous enough to change the result, ask one focused clarifying question. Otherwise proceed with a reasonable, clearly stated scope.
5. If multiple skills are genuinely needed, apply the primary skill first and use only the relevant supporting skill guidance.
6. If no skill fits, help with the request directly instead of forcing an unrelated route.

## Skill guide

- **`vanilla-essence`** — Summarize one document's main message and key points.
- **`research-essence`** — Synthesize findings across sources, including disagreement and uncertainty.
- **`user-need-essence`** — Turn interviews, tickets, or feedback into user problems and requirements.
- **`code-essence`** — Identify coding practices and conventions in code.
- **`architecture-essence`** — Explain system components, responsibilities, and relationships.
- **`web-design-essence`** — Analyze page hierarchy, layout, interaction flow, and interface intent for digital products and websites.
- **`game-design-essence`** — Extract player fantasy, gameplay loop, progression, systems, and design intent from game docs.
- **`decision-essence`** — Explain a decision, the options considered, and the rationale.
- **`risk-essence`** — Surface risks, trade-offs, and failure modes.
- **`validation-essence`** — Assess the strength and coverage of tests or other validation evidence.
- **`metrics-essence`** — Interpret KPIs and trends, including measurement caveats.
- **`roi-essence`** — Assess costs, benefits, ROI, break-even, or payback.
- **`stock-essence`** — Summarize a company's financial performance and relevant market context.
- **`incident-essence`** — Summarize an incident's impact, timeline, contributing factors, and follow-up.
- **`root-cause-essence`** — Analyze the evidence for underlying and contributing causes of a failure.
- **`security-essence`** — Describe security assets, threats, controls, and gaps.
- **`safe-ai-essence`** — Examine AI safety goals, safeguards, harms, and residual risks.
- **`policy-essence`** — Extract a policy's rules, obligations, exceptions, and enforcement.
- **`rubric-essence`** — Explain an evaluation rubric's criteria, scoring rules, and ambiguities.

## Response

Complete the task using the selected skill's workflow. Briefly name the route only when useful, then provide the requested analysis or output. Do not give the user a copyable prompt instead of doing the work. When clarification is needed, ask one focused question and wait.

When the user supplies a repository or asks for code-grounded analysis, use Claude Code's `Glob`, `Grep`, and `Read` tools to inspect the relevant source; use `Bash` only for non-destructive, relevant checks. Route repo conventions to `code-essence` and system structure to `architecture-essence`. Do not claim a route was evaluated by running a model unless it was.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. Set `skill` to the selected skill name; the embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite exact repository paths and lines for codebase claims, and cite sections, timestamps, or page locations for other sources. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
