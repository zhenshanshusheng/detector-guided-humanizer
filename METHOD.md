# Method: Detector-Guided Iterative Humanization

## The Problem

AI detectors flag AI-assisted content. Standard advice ("add personal anecdotes", "vary sentence length", "write like you talk") is folk wisdom — untested, and our experiments show most of it doesn't work or actively backfires.

## The Key Insight

From Cheng et al. (2025), "Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text":

> A training-free humanizer that wraps any instruction-tuned LLM with a loop **guided by the detector itself as an oracle** sets the new research ceiling for evasion — 87.88% average detection reduction. Meanwhile, **basic (undirected) paraphrasing INCREASES detection rates** on modern classifiers by 8–15%.

Translation: stop guessing. The detector is the ground truth. Generate candidates, measure, keep winners, iterate.

## Why Undirected Rewriting Fails

Modern neural classifiers (Family B detectors — Pangram, GPTZero, Originality, Zhuque) are hardened with **hard-negative mining**: paraphraser and "humanizer" tool outputs are included in training as AI-class examples. So:

- Synonym swaps → still AI (trained as AI)
- "Write more casually" → still AI (the casual-LLM distribution is also trained as AI)
- Adding questions/metaphors/first-person → still AI (surface features, not distributional shift)

What works is **removing the specific distributional signals** the classifier keys on — and the only reliable way to find them is to ask the classifier.

## The 3-Phase Process

### Phase 1: Heat Map

Score each paragraph (or ~300-char unit) individually against the detector.

**Why:** In our test, 24 of 27 paragraphs already scored Human. Without the heat map, you'd waste effort rewriting the whole article. The heat map tells you exactly where the AI signal lives.

**How:** See `scripts/heatmap.py`. Record per-paragraph Human/AI/Suspected + confidence.

**Output:** A list of failing paragraphs to target in Phase 2.

### Phase 2: Candidate Selection

For each failing paragraph:

1. Generate 3–4 paraphrase candidates with **high lexical diversity AND structural reordering** (see `prompts/paraphrase-diverse.md`).
2. Score every candidate against the detector.
3. Keep the lowest-AI-scoring candidate.
4. If all candidates still score AI, generate 3–4 more from the best one (second round).

**Critical constraints:**
- All facts, numbers, names, dates must be preserved exactly.
- Similar length (±20%).
- No new rhetorical flourishes (see CHECKLIST.md "don't" list).

**Why this works:** You're sampling the paraphrase space and using the detector as a fitness function. This is rejection sampling guided by ground truth, not vibes.

### Phase 3: Window Iteration

1. Assemble the full text from winners.
2. Score the full text (the detector will segment it into ~1000-char windows).
3. For each remaining AI-flagged window: extract it, generate 2–3 rewrite candidates, score standalone, splice in the winner.
4. Re-score the full text. **Watch for chunk-boundary shifts** — changing text length reshuffles the detector's windows, which can flip previously-clean segments. If this happens, iterate once more on the new AI windows.
5. Stop when AI = 0% across all windows, or when two consecutive iterations show no improvement.

**Watch for splice artifacts:** Window replacement can create duplicated sentences or missing spaces at boundaries. Always scan for these before scoring (see `scripts/verify.py`).

## The Subtraction Principle

Our controlled experiments (11 test variants) established:

| Approach | Result |
|---|---|
| Remove AI tells (em-dash reveals, "X but Y", parallel lists, prompt colons) | AI 100% → Suspected 100% ✓ |
| Add questions, metaphors, first-person voice | AI 100% → AI 100% ✗ |
| Add contractions ("don't", "you'll") | AI 100% → AI 100% (worse) ✗ |
| Casual forum slang | Human 100% but 0.09 confidence (unreliable) ✗ |
| "Here's the thing" style openers | AI 100% (worse — it's an LLM-typical phrase) ✗ |

**The detector doesn't reward "human-ness." It punishes "AI-ness."** Every rhetorical flourish you add is another potential AI signal. The winning move is flat, plain, unadorned prose — not colorful human imitation.

## When to Stop

- **AI = 0%** across all windows: done. This is the practical ceiling.
- **Two iterations with no improvement:** stop. Further edits risk degrading prose quality for no detector gain.
- **Suspected-dominant is a win.** A "Suspected" verdict means the detector cannot confidently call it AI. Chasing 100% Human has sharply diminishing returns.

## Limitations

- Requires API access to the target detector (or a reliable proxy).
- Each full-text check costs tokens (~1.7 tokens/char on Zhuque). Budget ~100K tokens per article.
- The detector's chunking is positional; length changes reshuffle windows (mitigated by iterating).
- Hardened classifiers (2025+) may resist even this method on some texts. Report failures honestly in EXPERIMENTS.md.
