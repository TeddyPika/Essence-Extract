---
name: decision-essence
description: Summarize the decision being made, the options considered, and the reasoning behind the chosen path. Use when asked to understand trade-offs, rationale, or decision quality in architecture or planning documents.
---

# Decision Essence

Summarize the reasoning behind a decision using only the evidence available in the source material. Focus on the decision context, the options considered, the trade-offs, and the factors that drove the chosen path.

## Process

1. Identify the decision, its context, and the stakeholders or constraints that shaped it.
2. Extract the options or approaches under consideration, including any rejected alternatives.
3. Capture the criteria used to evaluate the options, such as cost, speed, risk, complexity, maintainability, or compliance.
4. Separate the decision itself from the explanation or post-hoc rationale. Note where the source states a trade-off, a constraint, or a consequence.
5. Summarize the final choice and the evidence or reasoning supporting it while keeping uncertainty visible.

## Response

Use a concise structure appropriate to the request:

- **Decision essence:** the key decision in one or two sentences.
- **Context and constraints:** the problem, goals, and pressures shaping the choice.
- **Options considered:** the main alternatives or paths evaluated.
- **Reasoning and trade-offs:** the criteria, preferences, and compromises that informed the decision.
- **Outcome and gaps:** the chosen path, remaining uncertainty, and any unaddressed concerns.

Do not treat assumptions as facts, and clearly distinguish evidence-based reasoning from speculation.

## Optional ADR artifact

If the user explicitly asks to save or draft an ADR in the repository, inspect `docs/adr/` with `Glob` and `Read`, select the next unused zero-padded number, and use `Write` to create `docs/adr/NNNN-title.md`. Never overwrite an existing ADR or create a file without the user's request. Include context, the decision, options, evidence-based rationale, consequences, and unresolved questions. Report the created path in a `recommended_actions` item with status `completed`.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
