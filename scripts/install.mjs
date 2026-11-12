#!/usr/bin/env node
import { cpSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createInterface } from "node:readline/promises";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const bundles = {
  core: [
    "code-essence",
    "architecture-essence",
    "decision-essence",
    "validation-essence",
  ],
  sre: ["incident-essence", "root-cause-essence", "security-essence"],
  product: [
    "user-need-essence",
    "metrics-essence",
    "risk-essence",
    "roi-essence",
  ],
  extras: [
    "vanilla-essence",
    "research-essence",
    "policy-essence",
    "safe-ai-essence",
    "rubric-essence",
    "web-design-essence",
    "game-design-essence",
    "stock-essence",
  ],
};

const extraSkills = new Set(["game-design-essence", "stock-essence"]);
const sources = new Map([
  ...Object.values(bundles)
    .flat()
    .map((name) => [
      name,
      join(root, extraSkills.has(name) ? "extras" : ".claude", "skills", name),
    ]),
  ["master-essence", join(root, ".claude", "skills", "master-essence")],
]);
const allSkills = [...sources.keys()];

function parseSelection(answer) {
  const selected = new Set();
  for (const token of answer
    .split(",")
    .map((item) => item.trim().toLowerCase())
    .filter(Boolean)) {
    if (token === "all") {
      allSkills.forEach((skill) => selected.add(skill));
    } else if (bundles[token]) {
      bundles[token].forEach((skill) => selected.add(skill));
    } else if (sources.has(token)) {
      selected.add(token);
    } else {
      throw new Error(
        `Unknown selection "${token}". Choose core, sre, product, extras, all, or a listed skill name.`,
      );
    }
  }
  if (selected.size === 0) {
    throw new Error("Select at least one bundle or skill.");
  }
  return [...selected];
}

async function main() {
  if (!process.stdin.isTTY || !process.stdout.isTTY) {
    throw new Error("Run this installer in an interactive terminal.");
  }
  const prompt = createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  try {
    console.log("Essence-Extract skill installer\n");
    console.log("Bundles: core (4), sre (3), product (4), extras (8), all (20)");
    console.log("Or enter individual skill names, separated by commas.");
    console.log("Skills: " + allSkills.join(", ") + "\n");
    const answer = await prompt.question("Install which bundle(s) or skill(s)? ");
    const selected = parseSelection(answer);
    const destination = join(process.cwd(), ".claude", "skills");
    const existing = selected.filter((name) =>
      existsSync(join(destination, name)),
    );
    let replaceExisting = false;
    if (existing.length > 0) {
      console.log(`Already installed: ${existing.join(", ")}`);
      replaceExisting =
        (await prompt.question("Replace these skills? [y/N] "))
          .trim()
          .toLowerCase() === "y";
    }

    mkdirSync(destination, { recursive: true });
    const installed = [];
    const skipped = [];
    for (const name of selected) {
      if (existing.includes(name) && !replaceExisting) {
        skipped.push(name);
        continue;
      }
      cpSync(sources.get(name), join(destination, name), {
        recursive: true,
        force: true,
      });
      installed.push(name);
    }

    console.log(
      `Installed ${installed.length} skill(s) to ${destination}.`,
    );
    if (skipped.length > 0) {
      console.log(`Skipped existing skills: ${skipped.join(", ")}`);
    }
  } finally {
    prompt.close();
  }
}

main().catch((error) => {
  console.error(`Installation failed: ${error.message}`);
  process.exitCode = 1;
});
