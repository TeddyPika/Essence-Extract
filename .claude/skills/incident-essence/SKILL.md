---
name: incident-essence
description: Summarize an incident's impact, timeline, contributing factors, response, and follow-up actions using the available evidence.
---

# Incident Essence

Create a clear, blameless account of an incident from reports, timelines, logs, and follow-up materials. Distinguish confirmed facts from hypotheses, and avoid reducing complex failures to a single unsupported cause.

## Process

1. Identify the incident, affected systems or people, and the available time range.
2. Reconstruct the timeline from detection through mitigation and recovery. Flag gaps or conflicting timestamps.
3. Summarize the observed impact, duration, and scope. Separate confirmed impact from estimates.
4. Extract the trigger, contributing conditions, and failed or missing safeguards only where supported by evidence.
5. Review the response and follow-up actions. Distinguish completed remediation from planned work and note unresolved risks.

## Response

Provide a concise incident summary with:

- **Impact:** what was affected, for how long, and with what confidence.
- **Timeline:** key detection, response, mitigation, and recovery events.
- **Contributing factors:** confirmed causes or conditions, separated from open hypotheses.
- **Response and recovery:** what was done and what restored service or reduced impact.
- **Follow-up:** corrective actions, ownership or status when available, and remaining gaps.

Use blameless language focused on systems and conditions. Do not invent root causes, impact estimates, or action status.

## Optional postmortem artifact

If the user explicitly asks to draft or save a postmortem file, use `Glob` and `Read` to check `docs/postmortems/`, then use `Write` to create `docs/postmortems/YYYY-MM-DD-slug.md` with the incident's known date. If the date is not in the evidence, use `undated-slug.md`; never invent a date or overwrite a file. Include impact, timeline, contributing factors, response, follow-up, and evidence. Report the created path in a `recommended_actions` item with status `completed`.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
