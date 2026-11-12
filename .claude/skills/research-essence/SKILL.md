---
name: research-essence
description: Synthesize the core facts, evidence, and conclusions from research materials while distinguishing verified findings from assumptions and gaps.
---

# Research Essence

Turn research inputs into a concise, grounded synthesis of the main question, evidence, and conclusions. Prioritize what is actually supported by sources over speculation or broad interpretation.

## Process

1. Identify the research question, topic, or decision being investigated. If the objective is unclear, ask what the user is trying to learn or decide.
2. Read the relevant sources and extract the core facts, claims, evidence, and trade-offs. Separate direct evidence from commentary, inference, or weakly supported assertions.
3. Look for patterns across sources: where they agree, where they disagree, and what remains unresolved. Note whether the claim is well-supported, contested, or not yet established.
4. Distinguish findings from opinions, assumptions, and missing information. Do not treat speculation as fact.
5. Summarize the result in a way that would help a decision-maker understand the main evidence, implications, and remaining uncertainty.

## Response

Provide a compact synthesis with:

- **Research question:** what is being investigated.
- **What the evidence says:** the main verified findings.
- **Points of disagreement or uncertainty:** conflicting sources or missing evidence.
- **Implications:** what the findings suggest for a decision or next step.
- **Confidence level:** high, moderate, or low based on source quality and coverage.

When the evidence is limited or weak, say so plainly and explain what would materially improve confidence.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
