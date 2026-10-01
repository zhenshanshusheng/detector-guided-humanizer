# Playbook: Step-by-Step SOP for AI Assistants

Follow this exactly. It is designed to be executed by any capable AI assistant with API access to the target AI text detector.

## Prerequisites

- [ ] API access to the target detector (endpoint, auth, request format documented)
- [ ] The `scripts/` in this repo (or equivalents)
- [ ] The original text, split into paragraphs
- [ ] Token budget: ~100K tokens per 8,000-char article (adjust for your detector's pricing)

## Phase 0: Baseline

1. Score the **full original text** against the detector. Record: overall Human/AI/Suspected %, per-segment labels + confidence.
2. This is your control. Every later measurement compares against it.

## Phase 1: Heat Map

1. Split the text into paragraphs (~200–400 chars each).
2. Score each paragraph **individually** (`scripts/heatmap.py`).
3. Build a table: paragraph ID → Human/AI/Suspected + confidence.
4. **Triage:**
   - Paragraphs scoring Human → leave alone.
   - Paragraphs scoring AI → Phase 2 targets.
   - Paragraphs scoring Suspected → note, revisit in Phase 3 if needed.

**Expected:** Most paragraphs will already pass. Focus energy on the failures.

## Phase 2: Candidate Selection

For each AI-flagged paragraph:

1. Generate **3–4 paraphrase candidates** using `prompts/paraphrase-diverse.md`.
   - Vary lexical choice AND sentence structure AND information order.
   - Keep all facts identical. Keep length within ±20%.
   - Apply CHECKLIST.md rules (no new AI tells).
2. Score **every candidate** against the detector.
3. Select the candidate with the **lowest AI score** (prefer Human > Suspected > low-confidence AI).
4. If all candidates still score AI with high confidence: generate 3–4 more candidates seeded from the best one, with explicit instruction to differ structurally. Repeat once.
5. Replace the paragraph with the winner.

**Quality gate:** Read the winner aloud. If it sounds worse than the original for a human reader, try once more. Never sacrifice readability for the score.

## Phase 3: Window Iteration

1. Assemble the full text from all paragraphs (winners + untouched).
2. Score the **full text**. Record per-window labels.
3. For each AI-flagged window:
   a. Extract the window text.
   b. Rewrite it (2–3 candidates), applying CHECKLIST.md + lessons from Phase 2 winners.
   c. Score candidates standalone; pick the best.
   d. Splice the winner back into the full text **at exact character positions** (replace last-to-first to avoid offset drift).
4. **Scan for splice artifacts** (`scripts/verify.py`): duplicated sentences, missing spaces after periods, double spaces. Fix before scoring.
5. Re-score the full text.
6. **Repeat** until AI = 0% across all windows, or two consecutive iterations show no improvement.

**Known gotcha:** Changing text length reshuffles the detector's chunk windows. A previously-clean window may flip to AI after you fix another. This is normal — iterate on the new AI windows.

## Phase 4: Final Verification

1. Score the final full text one more time. Confirm AI = 0%.
2. Run `scripts/verify.py`: no duplicates, no missing spaces, no broken HTML (if applicable).
3. **Fact audit:** Spot-check 5–10 factual claims against the original. All must match.
4. **Read-through:** Read the full text as a human. It should read naturally — if any passage feels "optimized for a robot," revise it manually.

## Phase 5: Record

1. Append the experiment to EXPERIMENTS.md: original score, final score, number of iterations, what worked, what didn't.
2. If you discovered a new AI tell or a new failure mode, add it to CHECKLIST.md.
3. Update CHANGELOG.md.

## Stop Conditions

- AI = 0% on full text → **done, deploy.**
- Two full iterations with no AI% reduction → **stop, report the plateau.**
- Any iteration degrades human readability → **revert to previous best, stop.**

## Token Budget Guide (Zhuque API)

| Operation | Approx. cost |
|---|---|
| Paragraph heat map (27 paras) | ~16K tokens |
| Candidate scoring (12 candidates) | ~7K tokens |
| Full-text check (~8K chars) | ~14K tokens |
| **Typical article, 3 iterations** | **~80–100K tokens** |
