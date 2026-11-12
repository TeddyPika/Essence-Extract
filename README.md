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

## License

This project is licensed under the [MIT License](LICENSE).
