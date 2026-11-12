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
