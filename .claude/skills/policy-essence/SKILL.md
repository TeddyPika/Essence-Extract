---
name: policy-essence
description: Reduce a long policy, process, or compliance document to the rules, obligations, and exceptions that matter. Use when asked to understand governance, responsibilities, or required controls.
---

# Policy Essence

Condense a policy or governance document into the rules, obligations, exceptions, and responsibilities that matter most. Focus on what is required, what is prohibited, what is discretionary, and what is not clearly specified.

## Process

1. Identify the policy scope, audience, and governing authority or context.
2. Extract the purpose, applicable actors, and key obligations or restrictions.
3. Capture exceptions, allowable deviations, escalation paths, and required approvals or notices.
4. Note any definitions, thresholds, reporting duties, and enforcement or compliance mechanisms that change how the policy is applied.
5. Separate clear policy language from ambiguous or missing guidance, and highlight where additional clarification would matter.

## Response

Use a concise structure suitable to the request:

- **Policy essence:** the central purpose or requirement in one or two sentences.
- **Core rules and obligations:** the main requirements, responsibilities, and restrictions.
- **Exceptions and conditions:** when exceptions apply, what approvals are needed, and what limitations exist.
- **Enforcement and reporting:** monitoring, compliance steps, escalation, or documentation requirements.
- **Gaps and ambiguity:** unclear areas, missing definitions, or unresolved questions.

Focus on the practical effect of the policy rather than repeating its wording at length.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
