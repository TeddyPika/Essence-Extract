---
name: rubric-essence
description: Clarify a rubric's criteria, performance levels, scoring rules, and ambiguities to support consistent evaluation.
---

# Rubric Essence

Explain how a rubric is intended to guide evaluation. Preserve its criteria and scoring distinctions, and surface ambiguity without silently rewriting the standard.

## Process

1. Identify what the rubric evaluates, its intended audience, and the available scoring scale.
2. Extract each criterion, its relative weight if stated, and the observable evidence or performance levels described.
3. Explain how scores or ratings distinguish levels of performance, including any thresholds, aggregation rules, or required conditions.
4. Identify overlapping criteria, vague terms, missing anchors, and other features that could lead evaluators to inconsistent results.
5. Separate what the rubric explicitly says from interpretation. Do not apply a score to a submission unless asked and given the item to evaluate.

## Response

Summarize the rubric with:

- **Purpose and scale:** what is evaluated and how ratings are expressed.
- **Criteria:** the dimensions and weights, when specified.
- **Performance distinctions:** what separates lower and higher ratings.
- **Scoring rules:** how criteria combine or affect the final outcome.
- **Ambiguities:** areas that may lead to inconsistent interpretation.

When the rubric does not define a scoring rule or performance level, identify the gap rather than assuming one.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
