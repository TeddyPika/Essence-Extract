---
name: security-essence
description: Extract the security posture, key assets, trust boundaries, and likely threats from code, architecture docs, or security reviews. Use when asked about risk, controls, vulnerabilities, or defensive design.
---

# Security Essence

Summarize the security position of a system or codebase using only what the available material supports. Focus on the security goals, threat model, protections, and residual risk without inventing vulnerabilities or controls that are not evidenced.

## Process

1. Identify the system, data flows, and trust boundaries being analyzed. If the target is unclear, ask which components, services, or documents should be reviewed.
2. Extract the relevant assets, sensitive data, user roles, entry points, and external dependencies. Note whether the source describes authentication, authorization, secrets handling, transport security, or data protection.
3. Look for common security patterns: least privilege, segmentation, validation, secure defaults, logging and detection, incident response, and dependency hygiene.
4. Separate observed controls from assumptions or design intent. If the code or documents show a control, explain the evidence; if they do not, say so and avoid assuming it exists.
5. Summarize key threats, defensive controls, and remaining gaps. Prioritize the issues most likely to matter in the stated environment and clearly mark uncertainty.

## Response

Use a brief structure appropriate to the request:

- **Security essence:** the main security posture in one or two sentences.
- **Assets and trust boundaries:** the important data, components, and system boundaries.
- **Threats and risks:** the main risks or attack paths that the material discusses.
- **Controls in place:** the concrete security practices, standards, or mitigations observed.
- **Gaps and priorities:** the key missing protections, assumptions, or follow-up actions.

Where possible, cite the exact file, module, policy, or architecture section supporting each point. Distinguish facts from inference and preserve uncertainty.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
