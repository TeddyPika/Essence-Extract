---
name: roi-essence
description: Extract and assess return-on-investment information from documents, project proposals, or codebase context. Use when asked about a project's costs, benefits, ROI, payback, or business value.
---

# ROI Essence

Summarize the return-on-investment case supported by the provided material. Make the costs, benefits, time horizon, assumptions, and evidence clear; never invent financial inputs or present an unsupported estimate as a fact.

## Process

1. Identify the project or investment being evaluated and read the relevant source material. For codebase requests, use relevant project documentation and implementation context; do not infer business value from code alone.
2. Extract stated costs and benefits, their units, timing, duration, and source. Separate one-time from recurring amounts and monetary from non-monetary outcomes.
3. Check that the figures use compatible currencies and time periods. Note whether costs include implementation, operation, maintenance, migration, or other relevant items when the source addresses them.
4. Calculate ROI only when the necessary inputs and time horizon are clear. Use `ROI = (total benefits - total costs) / total costs × 100%`. State the values and period used. If costs are zero, missing, or incompatible, do not report a numeric ROI; explain what is needed.
5. Calculate break-even only when the relevant cost and benefit structure is clear:
   - For a product or service with fixed costs and per-unit values, use `break-even units = fixed costs / (unit selling price - unit variable cost)`. The denominator is the contribution margin per unit; if it is zero or negative, there is no finite break-even volume under those assumptions.
   - For a project or investment, identify when cumulative benefits equal cumulative costs. Use dated cash flows when available; otherwise state that the result is a simple, undiscounted break-even and identify the period.
   - State which break-even definition applies, show the inputs and units, and do not imply precision beyond the source data.
6. Keep break-even, payback period, net benefit, and ROI distinct. Report payback only when timing and cash flow information support it.
7. Separate source claims from your calculations and any assumptions. If requested to estimate, label each added assumption and show how it affects the result. Ask for clarification when a missing choice would materially change the answer.

## Response

Use a concise structure appropriate to the request:

- **ROI essence:** the main value proposition in one or two sentences.
- **Benefits and costs:** the key figures, units, timing, and evidence.
- **ROI / break-even / payback:** the supported calculations requested, or why a metric cannot be calculated from the available information.
- **Assumptions and gaps:** uncertainties or missing inputs that could change the conclusion.

Cite relevant files, sections, or code symbols when available. Preserve uncertainty and conflicting figures rather than silently resolving them. Do not frame the result as financial advice.
