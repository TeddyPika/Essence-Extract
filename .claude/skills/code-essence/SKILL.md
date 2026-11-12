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
