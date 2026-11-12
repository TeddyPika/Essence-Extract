---
name: validation-essence
description: Assess whether a project, system, or document is supported by convincing validation evidence, including tests, checks, and acceptance criteria.
---

# Validation Essence

Evaluate the evidence that a system, change, or claim has actually been validated. Focus on what is being checked, how strong the evidence is, and what remains uncertain.

## Process

1. Identify the validation target and the criteria it is expected to satisfy. If those criteria are unclear, ask which behavior, requirement, or output is meant to be validated.
2. Review the relevant tests, validation scripts, CI checks, manual verification notes, and any code paths they exercise. Distinguish direct evidence from assumptions or generic guidance.
3. Check whether the validation covers the real risk areas: correctness, edge cases, failure modes, performance, security, reliability, or user-facing behavior when relevant.
4. Separate observed evidence from gaps. Note whether validation is broad but shallow, narrow but precise, or missing entirely.
5. Keep conclusions grounded in the available artifacts. Do not claim something is validated unless the evidence supports it.

## Response

Provide a concise assessment with:

- **Validation target:** what is being checked.
- **Evidence:** the tests, scripts, or checks reviewed.
- **Coverage:** what the evidence covers and what it does not.
- **Assessment:** whether the validation is convincing, partial, or insufficient.
- **Next step:** the most important missing check, if any.

When evidence is incomplete, say so explicitly and explain what additional validation would materially improve confidence.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
