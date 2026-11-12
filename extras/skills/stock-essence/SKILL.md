---
name: stock-essence
description: Extract the key facts, trends, risks, and implications from a company revenue report and related news coverage. Use when asked to read earnings calls, financial statements, or market commentary and assess what matters for the company’s performance and outlook.
---

# Stock Essence

Analyze a company’s revenue report and related news with a focus on the evidence. Summarize what changed, what matters most, and what remains uncertain without turning speculation into fact.

## Process

1. Identify the company, reporting period, and the specific revenue report or earnings materials being reviewed.
2. Extract the core numbers: revenue, growth rate, segment performance, margins, guidance, and notable one-time items or foreign-exchange effects.
3. Read the company’s reported drivers of change and compare them to related news, product updates, market conditions, or competitive signals.
4. Separate the facts in the report from interpretation, including commentary about demand, pricing, customer mix, execution, or industry conditions.
5. Assess the key implications: what is improving, what is weakening, and what risks or uncertainties matter most for investors.
6. Summarize only what the available evidence supports. If a claim depends on missing data or assumptions, say so explicitly.

## Response

Use a concise structure appropriate to the request:

- **Stock essence:** the core takeaway in one or two sentences.
- **Revenue performance:** the headline revenue trend, segment results, and the main drivers or headwinds.
- **Key signals from news and context:** important developments, product announcements, competitive pressure, macro factors, or operational issues reported in the news.
- **Implications:** how the results and news likely affect revenue quality, growth outlook, margins, execution, and investor sentiment.
- **Risks and uncertainties:** the main open questions, assumptions, or missing information that could change the interpretation.

Do not present unsupported conclusions as fact. Distinguish reported results, management commentary, and outside news from your own analysis.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
