---
name: web-design-essence
description: Analyze a web page, screen, or design brief to extract visual hierarchy, layout patterns, user flows, and design intent. Use when assessing landing pages, product interfaces, or website UX decisions.
---

# Web Design Essence

Assess a webpage or interface by extracting its purpose, visual structure, interaction pattern, and overall user experience from the provided material.

## Process

1. Identify the page or screen, target audience, and the user goal it is trying to support.
2. Extract the visual hierarchy: headline, supporting content, calls to action, navigation, and the order in which attention is meant to flow.
3. Analyze layout and composition: spacing, alignment, contrast, section grouping, consistency, and any responsive or mobile-specific considerations evident in the material.
4. Evaluate interaction design: primary user flow, clickable elements, state changes, feedback, and points of friction.
5. Separate evidence from inference: distinguish clear design intent from assumptions about brand, audience, or conversion goals.
6. Summarize the design's strengths, trade-offs, constraints, and any unanswered questions that should be validated with users or stakeholders.

## Response

Use a concise, structured summary:

- **Web design essence:** the central design idea in one or two sentences.
- **Core purpose and audience:** what the page is trying to achieve and for whom.
- **Visual hierarchy:** the strongest elements, the intended order of attention, and how the design guides the eye.
- **Layout and interaction patterns:** page structure, navigation, calls to action, and how sections connect into a user flow.
- **Usability and trade-offs:** strengths, friction points, accessibility or responsiveness considerations, and constraints implied by the design.
- **Open questions:** missing detail, assumptions, or areas that need validation before implementation or refinement.

Ground the assessment in the supplied design material and avoid inventing user needs, business goals, or product claims that are not stated.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
