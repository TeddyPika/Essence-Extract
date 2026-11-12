---
name: game-design-essence
description: Extract the core player fantasy, gameplay loop, systems, progression, pacing, and design intent from game design documents or game pitches.
---

# Game Design Essence

Turn a game concept, pitch, or design document into a concise, evidence-based summary of how the game is supposed to feel, flow, and reward players.

## Process

1. Read the source material before summarizing. If the document is incomplete or draft-like, say so and work only from the evidence available.
2. Identify the game’s premise, target audience, and player fantasy. Note whether the design emphasizes competition, exploration, creativity, social play, progression, or narrative immersion.
3. Extract the game’s primary gameplay loop: what players do, how they do it, what they earn or unlock, and how the loop repeats.
4. Capture the major systems that shape play, including progression, rewards, difficulty, combat or challenge, economy, social features, and content cadence when they are described.
5. Look for intent around pacing, onboarding, retention, and meaningful choices. Distinguish clearly stated design goals from assumptions or unresolved questions.
6. If no format is requested, use the default response structure below. Keep the result grounded in the source material and avoid inventing mechanics, audience fit, or business promises not supported by the text.

## Default response

**Game summary:** One or two sentences describing the game’s premise, the player fantasy, and the core objective.

**Core design:**
- Player fantasy and target audience
- Primary gameplay loop
- Key systems and progression structure
- Difficulty, pacing, and retention hooks
- Notable trade-offs, risks, or open questions

For very short materials, provide the summary and the most relevant design points only. If the document is ambiguous, state the ambiguity plainly rather than presenting a guess as fact.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Cite source sections, timestamps, or exact file-and-line locations for repository material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
