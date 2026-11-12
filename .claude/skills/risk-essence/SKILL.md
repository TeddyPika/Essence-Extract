---
name: risk-essence
description: Extract the main risks, trade-offs, and failure modes from a proposal, incident report, or design document. Use when asked to assess risk exposure, uncertainty, or likely failure paths.
---

# Risk Essence

Summarize the risk position of a project, system, or proposal using only the available evidence. Focus on the key risks, trade-offs, uncertainty, and likely failure modes without inventing consequences that the source does not support.

## Process

1. Identify the subject being evaluated, its scope, and the time horizon or context relevant to the risk discussion.
2. Extract stated risks, assumptions, constraints, and uncertainties. Separate risks that are explicit from those that are merely implied.
3. Distinguish the kinds of risk discussed, such as technical, operational, security, compliance, delivery, or business risk.
4. Note how the source describes mitigation, fallback plans, or the consequences of failure. If trade-offs are discussed, capture them clearly.
5. Summarize residual risk and missing information. If evidence is limited, say so and identify what additional facts would change the conclusion.

## Response

Use a concise structure appropriate to the request:

- **Risk essence:** the main risk message in one or two sentences.
- **Key risks and failure modes:** the principal risks, adverse outcomes, and failure scenarios described.
- **Trade-offs and constraints:** the main choices, dependencies, and compromises that shape the risk profile.
- **Mitigations and safeguards:** any controls, contingencies, or monitoring mentioned.
- **Residual risk and gaps:** unanswered questions, assumptions, or missing evidence that matter.

Ground each point in the source material and preserve uncertainty rather than resolving it silently.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
