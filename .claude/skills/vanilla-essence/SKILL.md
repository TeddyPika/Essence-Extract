---
name: vanilla-essence
description: Summarize the main message, ideas, and takeaways of a document. Use when asked for a summary or overview of a document.
---

# Vanilla Essence

Write a clear, concise summary of a provided document without adding unsupported interpretation.

## Process

1. Read the entire document before summarizing. If the document is incomplete or too long to access in full, say so and work only from the available text.
2. Identify its central purpose or message, the main ideas or events that support it, and the intended audience or outcome when evident.
3. Focus on the main ideas and events. Leave out repetition and minor details unless they are important to the document's meaning.
4. Preserve the document's tone and important distinctions. Do not invent context, claims, motivations, or conclusions.
5. Match the requested format and length. If none is specified, use the concise default below.

## Default response

**Summary:** One or two sentences stating the document's main message or purpose.

**Key points:**
- Three to five concise points capturing the ideas, events, or reasoning needed to understand the summary.

For a very short document, return only the summary. If the user asks for a particular audience, style, or format, adapt the wording while preserving the original meaning. If the document is ambiguous, briefly identify the ambiguity rather than presenting a guess as fact.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
