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
