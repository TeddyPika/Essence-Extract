---
name: architecture-essence
description: Extract the main system components, responsibilities, and relationships from code or a design document. Use when asked to understand architecture, boundaries, and system structure.
---

# Architecture Essence

Summarize the architecture of a system or subsystem using the source material provided. Focus on the components, responsibilities, boundaries, and relationships that matter most to understanding how the system works.

## Process

1. Identify the system or subsystem being described and the relevant scope, including major components or services.
2. Extract the key responsibilities, boundaries, and interactions among components.
3. Note architectural patterns, interfaces, data flows, and dependencies that shape how the system operates.
4. Separate the stated architecture from assumptions or inferred design choices. Distinguish documented decisions from probable interpretation.
5. Summarize the overall structure and any important constraints, trade-offs, or risks implied by the architecture.

## Response

Use a concise, structured summary:

- **Architecture essence:** the main structural idea in one or two sentences.
- **Main components and responsibilities:** the important parts of the system and what each does.
- **Interactions and boundaries:** how components communicate, where trust boundaries exist, and what interfaces matter.
- **Patterns and trade-offs:** any architectural patterns, constraints, or design trade-offs evident in the material.
- **Open questions and gaps:** missing detail, ambiguity, or areas where the source is incomplete.

Cite the relevant files, modules, or design sections when available and keep the summary grounded in evidence.

## Claude Code tools and citations

When analyzing a repository, inspect it with Claude Code's `Glob`, `Grep`, and `Read` tools before drawing conclusions. Use `Bash` only for relevant, non-destructive checks. Cite every repository-grounded fact with the exact path and line number or range (for example, `src/auth/middleware.ts:42-48`). Do not cite a file or line you have not read.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Use exact file-and-line citations for repository claims and source sections, timestamps, or page references for other material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
