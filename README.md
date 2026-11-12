<div align="center">
  <img src="assets/essence-extract-logo.svg" alt="" width="80" height="80">

  # Essence-Extract

  **Evidence-first workflows for Claude Code.**

  Turn incident logs, codebases, decisions, and product evidence into clear HTML reports with inline SVG, optional Three.js visuals, and embedded structured data.
</div>

## Why use it

- **Predictable output:** every skill returns HTML with the same embedded data contract.
- **Auditable claims:** repository findings cite exact paths and line numbers; other sources cite sections, timestamps, or page locations.
- **Less setup:** choose a persona bundle or a few individual skills instead of copying folders by hand.
- **Useful follow-through:** request an ADR or postmortem draft and the relevant skill can create the artifact in your repo.

## Install

### Claude Code plugin

Add the marketplace once, then install the complete skill suite:

```text
/plugin marketplace add TeddyPika/Essence-Extract
/plugin install essence-extract@essence-extract
```

Or use Claude Code's CLI:

```bash
claude plugin marketplace add TeddyPika/Essence-Extract
claude plugin install essence-extract@essence-extract
```

### Interactive installer

With Node.js 18+, run this from the project where you want the selected skills:

```bash
npx --yes --package=github:TeddyPika/Essence-Extract essence-extract
```

Choose a persona bundle (`core`, `sre`, `product`, or `extras`), `all`, or a comma-separated list such as `code-essence, incident-essence`. Existing skills are never replaced without confirmation.

For local development, run the installer directly:

```bash
node scripts/install.mjs
```

## Persona bundles

| Bundle | Skills | Best for |
| --- | --- | --- |
| **Core engineering** (4) | `code-essence`, `architecture-essence`, `decision-essence`, `validation-essence` | Code conventions, system maps, ADRs, and evidence-backed validation |
| **SRE & incidents** (3) | `incident-essence`, `root-cause-essence`, `security-essence` | Impact summaries, causal analysis, and security posture |
| **Product & strategy** (4) | `user-need-essence`, `metrics-essence`, `risk-essence`, `roi-essence` | User evidence, KPIs, trade-offs, and returns |
| **Specialist extras** (8) | `vanilla-essence`, `research-essence`, `policy-essence`, `safe-ai-essence`, `rubric-essence`, `web-design-essence`, `game-design-essence`, `stock-essence` | Research, governance, design, and financial analysis |

`master-essence` routes to the best-fit skill and is available individually or in the full install. `stock-essence` and `game-design-essence` live under [`extras/skills/`](extras/skills/).

## Use

Ask Claude Code to invoke a skill with the relevant repository or source material:

```text
Use code-essence on this repository. Cite each convention with file paths and line numbers.
Use incident-essence on samples/incident-raw.log.
Use decision-essence to compare these options and save the approved decision as an ADR.
```

To draft files, explicitly ask the skill to create them. `decision-essence` checks `docs/adr/` and creates the next `NNNN-title.md`; `incident-essence` drafts under `docs/postmortems/`. Neither writes an artifact unless requested.

## Output contract

By default, every skill returns a complete HTML5 report with semantic sections for summary, verified facts, unverified assumptions, residual risks, recommended actions, and open questions. Each page embeds a JSON object in `<script type="application/json" id="essence-data">`; this object follows the strict schema, so it remains machine-readable without making bare JSON the user-facing report.

| Key | Purpose |
| --- | --- |
| `skill`, `summary` | Selected skill and concise result |
| `verified_facts` | Supported findings with category and source/location/quote evidence |
| `unverified_assumptions` | Plausible but unconfirmed statements and why they remain unverified |
| `residual_risks` | Evidence-backed remaining risks, with severity (`low`, `medium`, `high`, `unknown`) |
| `recommended_actions` | Next steps with status and owner (or `null`) |
| `open_questions` | Material questions the evidence cannot answer |

Use inline SVG for relevant timelines or relationships. Three.js is available for interactive visualizations with a static SVG fallback; it should enhance the report, never carry required facts. Escape source text in HTML and JSON. Empty arrays mean no supported items; the skills must not fill gaps with invented facts. Ask for another format explicitly when needed.

## License

MIT. See [LICENSE](LICENSE).
