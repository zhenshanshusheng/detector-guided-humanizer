# Contributing

This repo improves through experiments, not opinions. Every methodology claim must be backed by a measured result.

## Adding an Experiment

1. Run the experiment following PLAYBOOK.md (or document deviations).
2. Append to EXPERIMENTS.md with: date, detector, text stats, full result table, conclusion.
3. If the finding changes a rule: update CHECKLIST.md and/or METHOD.md.
4. Add a CHANGELOG.md entry.

## Reporting a New AI Tell

Format:
- **Trigger:** exact, locatable pattern (regex-able, not vibes)
- **Evidence:** before/after scores on the same text
- **Fix:** the minimal edit that removes it

Tells without measured evidence go in EXPERIMENTS.md "observations", not CHECKLIST.md.

## Reporting a Failure

Failed approaches are as valuable as successful ones. Document: what you tried, the scores, and your best hypothesis for why it failed. Our DON'T list exists because of documented failures.

## Ground Rules

- No credentials, API keys, or private data in commits. Ever.
- Facts over style: this repo is about measurement, not taste.
- Keep it reproducible: include enough detail that another AI assistant can replicate the experiment from PLAYBOOK.md alone.
