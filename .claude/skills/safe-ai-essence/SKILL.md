---
name: safe-ai-essence
description: Extract the safety goals, risk controls, and governance boundaries for AI systems from policies, model cards, workflows, and design documentation. Use when asked about AI harms, safety, guardrails, compliance, or residual risk.
---

# Safe AI Essence

Summarize the safety and governance posture of an AI system from the material provided. Focus on the actual safeguards, intended use, risk areas, and remaining gaps; do not present speculative harms as if they were documented facts.

## Process

1. Identify the AI system, model, workflow, or policy being assessed and the context in which it is used.
2. Extract the stated safety goals, risk categories, intended boundaries, and prohibited or discouraged uses.
3. Separate implemented controls from assumptions or future plans. Look for guardrails such as human review, content filtering, data minimization, evaluation, logging, red-teaming, and escalation paths.
4. Check whether the material describes monitoring, testing, incident response, or model update processes. Note the evidence for each claim and whether it is operational or merely aspirational.
5. Summarize residual risk and missing evidence. If the source does not support a conclusion, say so and identify what additional information would help.

## Response

Use a concise structure suitable to the request:

- **AI safety essence:** the core safety message in one or two sentences.
- **System scope and intended use:** what the model or workflow is meant to do and where it is not meant to be used.
- **Risks and harms:** the key categories of risk or harm described by the source material.
- **Controls and mitigations:** the concrete safeguards, evaluation methods, and governance practices in place.
- **Residual risk and gaps:** uncertainties, missing controls, or open questions that could affect safety.

Ground each point in the available source material and preserve uncertainty rather than filling gaps with assumptions.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
