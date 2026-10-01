# Detector-Guided Humanizer

A practical methodology for reducing AI-tone in AI-assisted writing, validated through controlled experiments against a commercial AI text detector (Tencent Zhuque, `@makers/zhuque-text`).

**Core finding:** Don't guess what "sounds human." Use the detector itself as the judge. Generate diverse candidates, let the detector pick the winner, iterate on what remains.

## Results

On a full-length English product review article (~8,300 characters):

| Stage | Human | AI | Suspected |
|---|---|---|---|
| Original | 0% | **100%** | 0% |
| After this method | 35% | **0%** | 65% |

Zero of 8 text segments still classified as AI.

## The Method (3 phases)

1. **Heat map** — Score each paragraph individually. Most will already pass; focus effort on the few that don't.
2. **Candidate selection** — For each failing paragraph, generate 3–4 diverse paraphrases. Score them all. Keep the winner.
3. **Window iteration** — Score the full text. Attack remaining AI-flagged windows the same way. Repeat until AI hits 0%.

See [METHOD.md](METHOD.md) for the full methodology, [PLAYBOOK.md](PLAYBOOK.md) for the step-by-step SOP any AI assistant can follow.

## Key Principles

- **Subtraction > addition.** Removing AI tells works. Adding "human" features (questions, metaphors, first-person) does not — and can backfire.
- **The detector rewards flatness, not flair.** Every rhetorical flourish is a potential AI signal.
- **Undirected paraphrasing can make it worse.** Modern classifiers are trained on paraphraser output as AI-class data.

## Repo Map

| File | What |
|---|---|
| [METHOD.md](METHOD.md) | Core methodology and why it works |
| [CHECKLIST.md](CHECKLIST.md) | V1 surgical de-telling checklist (concrete rules) |
| [PLAYBOOK.md](PLAYBOOK.md) | Step-by-step SOP for AI assistants |
| [RESEARCH.md](RESEARCH.md) | How detectors work + key academic papers |
| [EXPERIMENTS.md](EXPERIMENTS.md) | Full experimental log with all data |
| [prompts/](prompts/) | Prompt templates for candidate generation |
| [scripts/](scripts/) | Scoring and selection scripts |
| [CHANGELOG.md](CHANGELOG.md) | Versioned methodology updates |

## Updating This Repo

This is a living methodology. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new experiments, and [CHANGELOG.md](CHANGELOG.md) for the update history.

## License

MIT
