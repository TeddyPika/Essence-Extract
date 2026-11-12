# Essence-Extract

A curated collection of Claude Code skills for extracting key meaning from documents, code, and strategic artifacts.

## Overview

Essence-Extract gives Claude a structured way to turn raw information into concise, evidence-based summaries. Each skill is designed to focus on a specific kind of extraction task without inventing conclusions or drifting into unsupported assumptions.

## Installation

Choose the skill(s) you want and copy them into your project's `.claude/skills/` directory:

```bash
mkdir -p .claude/skills
cp -R /path/to/Essence-Extract/.claude/skills/<skill-name> .claude/skills/
```

Alternatively, open this repository directly as your Claude Code project and use the skills from there.

## Usage

After installing a skill, invoke it in Claude Code with the skill name and provide the relevant document, codebase, or project context.

Example:

```text
Use the vanilla-essence skill on this document.
```

```text
Use the code-essence skill on this repository and explain the main coding patterns.
```

## Available Skills

| Skill | Purpose |
| --- | --- |
| `vanilla-essence` | Summarize a document into a brief main takeaway and supporting key points. |
| `code-essence` | Extract coding patterns, conventions, and practices from code or a codebase. |
| `roi-essence` | Identify ROI, payback, and break-even logic based on the available evidence. |
| `safe-ai-essence` | Extract safety goals, risk areas, guardrails, and residual concerns from AI system descriptions and policies. |
| `security-essence` | Summarize security posture, assets, threats, controls, and gaps from technical or policy materials. |
| `risk-essence` | Surface key risks, trade-offs, and failure modes from proposals, reports, and design docs. |
| `decision-essence` | Capture the decision being made, options considered, and reasoning behind the chosen path. |
| `policy-essence` | Reduce policies or compliance documents to rules, obligations, exceptions, and enforcement points. |
| `architecture-essence` | Extract system components, responsibilities, and relationships from code or design documents. |
| `user-need-essence` | Turn interviews, tickets, and feedback into the underlying user problems and requirements. |
| `stock-essence` | Extract financial trends, business drivers, and market context from earnings reports and related commentary. |
| `validation-essence` | Assess whether a project, change, or claim is supported by meaningful tests, checks, and validation evidence. |
| `research-essence` | Synthesize the main findings, evidence, and uncertainty from research materials and source documents. |
| `metrics-essence` | Interpret KPI levels and trends while accounting for metric definitions, context, and limitations. |
| `incident-essence` | Summarize incident impact, timeline, contributing factors, response, and follow-up actions. |
| `rubric-essence` | Clarify evaluation criteria, scoring levels, rules, and ambiguities in a rubric. |
| `master-essence` | Help users who are unsure which Essence skill to use by clarifying their goal and recommending a fit. |

## Choosing Between Related Skills

Some skills cover adjacent topics. Use the one that matches the main question:

- **`master-essence`:** Use this as a starting point if you are unsure which skill fits. It asks about your goal and recommends a skill and prompt.
- **`vanilla-essence` or `research-essence`:** Use `vanilla-essence` to summarize one document. Use `research-essence` to synthesize findings across sources, including disagreements and uncertainty. For interviews or feedback, use `user-need-essence` to identify user problems and requirements.
- **`code-essence` or `architecture-essence`:** Use `code-essence` to identify coding practices and conventions. Use `architecture-essence` to explain system components, responsibilities, and interactions.
- **`decision-essence`, `risk-essence`, or `architecture-essence`:** Use `decision-essence` to explain a choice and its rationale, `risk-essence` to assess uncertainties and failure modes, and `architecture-essence` to describe system structure.
- **`risk-essence`, `security-essence`, or `safe-ai-essence`:** Use `risk-essence` for broad project or proposal risks, `security-essence` for system assets, threats, and security controls, and `safe-ai-essence` for AI-specific harms, safeguards, intended use, and governance.
- **`policy-essence` or `safe-ai-essence`:** Use `policy-essence` for general rules, obligations, and exceptions. Use `safe-ai-essence` for safety practices and remaining risks in AI systems; use both when assessing an AI system against a policy.
- **`roi-essence` or `stock-essence`:** Use `roi-essence` for an investment or project's costs, benefits, and returns. Use `stock-essence` for a company's revenue performance and related business or market context.
- **`validation-essence` or `security-essence`:** Use `validation-essence` to assess whether tests or checks provide convincing evidence. Use `security-essence` to assess the security posture itself.
- **`metrics-essence` or `stock-essence`:** Use `metrics-essence` to interpret a set of measures or KPIs. Use `stock-essence` for company revenue performance and related business or market context.

## License

This project is licensed under the [MIT License](LICENSE).
