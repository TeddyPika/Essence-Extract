---
name: code-essence
description: Extract evidence-based coding practices and conventions from a codebase or code scripts. Use when asked what patterns a project follows, how its code is structured, or what practices can be learned from example code.
---

# Code Essence

Identify reusable coding practices from the code the user provides or the relevant parts of their repository. Ground conclusions in evidence; do not present generic advice as if the project uses it.

## Process

1. Determine whether the request concerns a standalone script, a particular area, or the whole codebase. If the target is unclear and would materially change the findings, ask which files or area to examine.
2. Read the relevant code before drawing conclusions. For a repository-level request, inspect project guidance and a representative set of related source files; consult tests and configuration when they help explain a pattern.
3. Look for practices that are repeated or deliberately enforced, such as naming, control flow, error handling, API boundaries, testing, and formatting. Treat an isolated choice as an example, not a project-wide convention.
4. Separate observed conventions from suggested improvements. Explain where evidence is limited or examples disagree; do not assume that a pattern is best merely because it appears in the code.
5. Keep findings actionable and scoped to the user's request. Do not edit code unless asked.

## Response

Summarize the most useful practices as concise bullets. For each, state:

- **Practice:** what the code does.
- **Evidence:** the relevant file and symbol or line, with a brief description of the example.
- **Applicability:** where the practice fits and any caveat.

When useful, distinguish **Observed convention** from **Possible improvement**. Prioritize a small number of well-supported findings over a long list of generic principles. If the available code is too limited to support a conclusion, say so and request or identify the additional files that would help.

## Claude Code tools and citations

For repository analysis, use Claude Code's `Glob` and `Grep` to locate relevant files and repeated patterns, then `Read` the exact code and tests. Use `Bash` only for relevant, non-destructive checks. Cite every repository-grounded fact with an exact path and line number or range (for example, `src/auth/middleware.ts:42-48`). A convention must be supported by more than one example or explicitly labeled as a single instance. Never infer unseen code.

## Output contract

By default, return a complete, self-contained HTML5 report, not bare JSON or Markdown. Use semantic HTML sections headed Summary, Verified Facts, Unverified Assumptions, Residual Risks, Recommended Actions, and Open Questions; render cited evidence visibly and escape source text as text. Use inline SVG for relevant timelines or relationships. When an interactive 3D view is useful, use Three.js with a static SVG fallback; essential facts must remain available if it fails. Embed exactly one JSON object conforming to `schemas/essence-output.schema.json` in `<script type="application/json" id="essence-data">`; the inline field contract remains self-contained when an individual skill is installed without that file. Never interpolate untrusted source content as HTML or executable JavaScript; safely escape its text and JSON. The embedded JSON object must include exactly these top-level keys: `skill`, `summary`, `verified_facts`, `unverified_assumptions`, `residual_risks`, `recommended_actions`, and `open_questions`. Use an empty array when a section has no supported entries. Each verified fact has `category`, `statement`, and at least one `evidence` item; each evidence item has `source`, `location`, and `quote`. Use exact file-and-line citations for repository claims and source sections, timestamps, or page references for other material. Assumptions require `statement` and `why_unverified`; risks require `statement`, `severity` (`low`, `medium`, `high`, or `unknown`), and cited `evidence`; actions require `action`, `status` (`proposed`, `in_progress`, `completed`, or `unknown`), and `owner` (a name or `null`). Do not infer missing facts. This contract overrides any prose-oriented response examples above. Follow another format only when the user explicitly requests one.
