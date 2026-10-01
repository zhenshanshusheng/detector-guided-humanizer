# Changelog

All notable changes to this methodology are documented here. Format: `YYYY-MM-DD — description`.

## [2.0.0] — 2026-10-02

Checklist expanded from 8 to 16 rules by merging [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 (MIT, via Wikipedia "Signs of AI writing"). New rules marked [H]: one-line closers, deep-sounding sayings, arguing-with-no-one, repeated openings, overused AI words, inflated significance, -ing riders, sales language, borrowed authority, verbose verbs. V1 rules (detector-validated) kept as the core; [H] rules adopted as pattern catalog. Rules reorganized into Staging / Rhythm / Inflation sections.

## [1.0.0] — 2026-10-02

Initial release. Validated against Tencent Zhuque `@makers/zhuque-text` on a full-length English product review article (~8,300 chars): AI 100% → AI 0% / Suspected 65% / Human 35%.

Includes:
- 3-phase detector-guided methodology (METHOD.md)
- V1 surgical checklist with 8 rules + tested DON'T list (CHECKLIST.md)
- Step-by-step SOP for AI assistants (PLAYBOOK.md)
- Research background: detector families, 5 key papers, lieflat study summary (RESEARCH.md)
- Full experimental log: 11 controlled variants + iterative full-article optimization (EXPERIMENTS.md)
- Prompt templates (prompts/) and scoring/selection scripts (scripts/)

## How Updates Work

1. **New experiment** → append to EXPERIMENTS.md, update CHANGELOG.md with date + finding.
2. **New AI tell discovered** → add to CHECKLIST.md rules, note in CHANGELOG.md.
3. **New failure mode** → document in EXPERIMENTS.md "Key Observations", note in CHANGELOG.md.
4. **Methodology change** → update METHOD.md + PLAYBOOK.md together, bump minor version, note in CHANGELOG.md.

Rule: no methodology claim without an experiment entry backing it. Folk wisdom stays out.
