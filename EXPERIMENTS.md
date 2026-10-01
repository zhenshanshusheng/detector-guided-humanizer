# Experiment Log

All experiments run 2026-10-02 against Tencent Zhuque `@makers/zhuque-text` API (model updated 2026-07-21). Target: English product review article (~8,300 chars).

## Round 0: Baseline vs Skill Rewrite

| Variant | Human | AI | Conf |
|---|---|---|---|
| Original intro (1,457 ch) | 0% | 100% | 0.9999 |
| Skill-based rewrite (1,590 ch) | 0% | 100% | 0.9999 |

**Conclusion:** Narrative restructuring without tell-removal does nothing.

## Round 1: Four Hypotheses (1,263–1,553 ch each)

| Variant | Hypothesis | Human | AI | Conf |
|---|---|---|---|---|
| V1 surgical | Remove surface tells only | 0% | 0% | Sus 100% (0.982) ✓ |
| V2 human-voice | Add questions, I-voice, metaphor | 0% | 100% | 0.9999 ✗ |
| V3 forum-slang | Casual register shift | 100% | 0% | 0.0904 (unreliable) |
| V4 kitchen-sink | Everything combined | 0% | 100% | 0.9999 ✗ |

**Conclusion:** Subtraction works; addition doesn't.

## Round 2: Refinements of V1

| Variant | Change vs V1 | Human | AI | Conf |
|---|---|---|---|---|
| V5 | + contractions, 1 question | 0% | 100% | 0.9999 ✗ |
| V6 | + colloquial diction ("Here's the thing") | 0% | 100% | 0.9983 ✗ |
| V7 | + non-template opening ("Not because X, but because Y") | 0% | 100% | 0.9998 ✗ |
| V8 | Further flattening | 0% | 0% | Sus 100% (0.9472) |

**Conclusion:** Each "improvement" reintroduced a tell. Contractions, "Here's the thing", antithesis are LLM-typical.

## Round 3: Full Article

| Stage | Human | AI | Sus | Notes |
|---|---|---|---|---|
| Original full (8,155 ch) | 0% | 100% | 0% | 8/8 windows AI |
| Surgical pass (25 paras) | 0% | 100% | 0% | Per-window conf slightly down |
| + heat-map targeting (3 paras) | 0% | 49.4% | 50.6% | 4/8 windows AI |
| + window iteration r1 | 38.1% | 21.9% | 40.0% | 2/8 AI |
| + window iteration r2 | 12.9% | 28.2% | 58.9% | Chunk-boundary shuffle |
| + duplicate fix | 12.4% | 14.7% | 72.9% | Removed splice-duplicated sentence |
| + window iteration r3 | 12.4% | 8.4% | 79.1% | 1/8 AI |
| **Final** | **35.0%** | **0.0%** | **65.0%** | **0/8 windows AI** ✓ |

## Paragraph Heat Map (after surgical pass)

27 paragraphs scored individually: **24 Human, 3 AI** (p07, p18, p20).

Failing paragraphs and fixes:
- **p07** (staccato complaint list) → 4 candidates → winner: reordered, varied rhythm → Human
- **p18** ("the honest answer" template) → 4 candidates → all Human → picked lowest-conf
- **p20** ("The magic of X is Y, not Z" antithesis) → 4 candidates → 3 Human → picked lowest-conf

## Key Observations

1. **Chunk-boundary shuffle:** The detector segments text into ~1050-char positional windows. Changing text length reshuffles windows, which can flip previously-clean segments. Mitigation: iterate, replace last-to-first.
2. **Splice artifacts are AI signals:** A duplicated sentence from window splicing single-handedly flipped a clean window back to AI. Always run `scripts/verify.py`.
3. **Standalone ≠ in-context:** Paragraphs scoring Human alone can score AI inside longer windows and vice versa. The full-text check is the ground truth.
4. **Diminishing returns are real:** AI 100%→50% took 1 iteration; 50%→0% took 4. Stop at AI=0% or two flat iterations.

## Token Cost

~95K tokens total for the full article (Zhuque bills ~1.7 tokens/char).
