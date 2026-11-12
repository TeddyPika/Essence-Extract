---
name: user-need-essence
description: Transform interviews, tickets, or feedback into the underlying user problems and requirements. Use when asked to understand user needs, pain points, or product requirements.
---

# User Need Essence

Extract the underlying user problems, needs, and requirements from the material provided. Focus on the pain points, motivations, constraints, and recurring signals in the evidence, without adding assumptions about users that the source does not support.

## Process

1. Identify the user group, context, and source of feedback or requirements being analyzed.
2. Extract recurring pain points, goals, friction, unmet needs, and stated constraints.
3. Separate direct user statements from inferred needs, and distinguish preferences from requirements.
4. Group similar themes into clear user problems and note any evidence of urgency, frequency, or severity.
5. Summarize the requirements implied by the material and any gaps where user evidence is incomplete.

## Response

Use a concise format appropriate to the request:

- **User need essence:** the central user problem or need in one or two sentences.
- **Observed user problems:** the main pain points, frustrations, or unmet needs described.
- **Needs and requirements:** the concrete requirements, goals, or behaviors implied by the user evidence.
- **Context and constraints:** the conditions, constraints, or environments that matter.
- **Uncertainty and gaps:** areas where the evidence is weak, ambiguous, or missing.

Keep the summary evidence-based and avoid turning anecdotes into universal claims.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
