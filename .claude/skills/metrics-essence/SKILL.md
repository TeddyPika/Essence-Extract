---
name: metrics-essence
description: Explain what metrics and KPIs show, how they change, and what their definitions and limitations allow you to conclude.
---

# Metrics Essence

Interpret metrics in context. Summarize the signal they provide without confusing correlation with causation or treating a number as meaningful without its definition and comparison basis.

## Process

1. Identify the question the metrics are meant to answer and the population, time period, and unit of analysis.
2. Check metric definitions, sources, baselines, targets, and relevant breakdowns. Note missing or inconsistent definitions.
3. Describe meaningful levels, trends, differences, and outliers. Compare like with like and distinguish absolute from relative changes.
4. Consider measurement limitations, sample size, uncertainty, data quality, and possible confounding factors when the evidence allows.
5. Separate observations from explanations. Do not infer causes, success, or failure from a metric alone.

## Response

Provide a concise interpretation with:

- **Question and measures:** what is being measured and why.
- **Key signals:** the most important levels, trends, and comparisons.
- **Caveats:** definitions, data limitations, or uncertainty affecting interpretation.
- **Implications:** what the evidence supports, and what it does not establish.
- **Next check:** the most useful additional breakdown or measurement, if needed.

If the metric definitions or data are insufficient, state what is missing rather than guessing.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
