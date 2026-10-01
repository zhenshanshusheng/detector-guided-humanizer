# Prompts

## Diverse Paraphrase (`paraphrase-diverse.md`)

Use for Phase 2 candidate generation. Generate 3–4 candidates per call by varying the strategy each time.

---

Paraphrase the following paragraph. Requirements:

1. **Preserve all facts exactly:** numbers, prices, specs, dates, product/model names, claims and their hedging (e.g. "claims", "reportedly", "roughly"). Do not add any new facts.
2. **Keep similar length** (±20% of original character count).
3. **Maximize difference** from the original in: word choice, sentence structure, and information order. Reorder sentences where natural. Change active/passive voice. Split long sentences or merge short ones.
4. **Do NOT add:** rhetorical questions, metaphors, first-person anecdotes, slang, contractions (in formal prose), "Here's the thing" style openers, em-dashes (—), "not X but Y" contrasts, or three-item parallel lists.
5. **Do NOT use:** prompt colons (e.g. "Quirks:", "Short answer:"), label fragments, or formulaic transitions ("As a rule of thumb,", "Still,").

Output ONLY the paraphrased paragraph, no explanations.

Original paragraph:
```
{PARAGRAPH}
```

---

## Surgical Edit (`paraphrase-surgical.md`)

Use for the initial V1-style pass. Minimal edits only.

---

Edit the following paragraph to remove AI-typical writing tells. Change as little as possible:

1. Replace em-dash reveals (— + punchline) with periods.
2. Split "X, but Y" / "not X but Y" contrasts into direct statements.
3. Break three-item parallel lists into separate sentences.
4. Replace prompt colons ("Label:") with full sentences.
5. Remove intensifiers used as pure emphasis (actually, genuinely, really).
6. Keep every fact, number, name, and the paragraph's meaning identical.

Output ONLY the edited paragraph.

Original paragraph:
```
{PARAGRAPH}
```
