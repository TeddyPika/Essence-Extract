---
name: root-cause-essence
description: Analyze evidence to identify a failure's underlying and contributing causes, distinguish them from symptoms and triggers, and surface unresolved hypotheses.
---

# Root Cause Essence

Trace how and why a failure occurred using the available evidence. Treat root cause as a supported explanation of underlying conditions, not as a label for the visible symptom or the last event in a sequence.

## Process

1. Define the failure or outcome being explained, its scope, and the evidence available.
2. Build a causal sequence from relevant events and conditions. Separate the observed symptom, immediate trigger, contributing factors, and underlying causes.
3. Test each proposed cause against the evidence. Look for alternative explanations, missing links, contradictions, and conditions that allowed the failure to occur or persist.
4. Distinguish confirmed findings from hypotheses. If the evidence does not establish a root cause, say so and identify what evidence would help.
5. Consider corrective actions that address causal conditions, not just symptoms. Do not prescribe actions beyond what the evidence or user request supports.

## Response

Present a concise analysis with:

- **Failure or outcome:** what needs explaining.
- **Causal chain:** the supported sequence of events and conditions.
- **Root and contributing causes:** what is established, and how it differs from the trigger or symptom.
- **Evidence and uncertainty:** support for each cause, competing explanations, and gaps.
- **Prevention focus:** the causal conditions a corrective action would need to address.

Avoid blame, unsupported certainty, and single-cause conclusions when the evidence points to interacting factors.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
