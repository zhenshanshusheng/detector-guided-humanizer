# V1 Surgical Checklist: De-telling Rules

Concrete, locatable rules for removing AI-tone. Adapted from [lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) (validated on 2.8M-char Chinese corpus) and our own English experiments.

**Apply in order. Each rule fires only on its exact trigger. If unsure, leave the sentence alone.**

---

## The Rules

### 1. Em-dash reveals
**Trigger:** `—` followed by a punchline, summary, or dramatic pause.
**Fix:** Split into two sentences, or use a comma/period.
- ❌ `Don't jog on a handrail-free pad — that's how people fall off.`
- ✅ `Do not jog on a handrail-free pad. People fall off that way.`

### 2. "X, but Y" flips / "not X but Y"
**Trigger:** Contrast structure where the second half overturns the first (`isn't just X — it's Y`, `not intensity; it's consistency`, `X rather than Y`).
**Fix:** State directly without the overturn.
- ❌ `Capacity isn't just about your body weight — it's about how hard the motor works.`
- ✅ `Capacity is about more than your body weight. It is about how hard the motor works.`
- ❌ `The magic isn't intensity; it's consistency.`
- ✅ `Showing up every day beats going hard.`

### 3. Tripartite parallelism
**Trigger:** Three parallel items in a list, especially in prose (not spec tables).
**Fix:** Break into separate sentences, or reduce to two items.
- ❌ `top speed, weight capacity, noise, and folded size`
- ✅ Split across sentences or restructure.

### 4. Prompt colons
**Trigger:** Colon after a label or setup phrase (`Quirks:`, `The compromises:`, `Short answer:`, `What matters is X:`).
**Fix:** Turn the label into a sentence, or merge.
- ❌ `Quirks: speed adjusts in 0.5 mph increments only...`
- ✅ `A few quirks. Speed adjusts in 0.5 mph increments only...`
- ❌ `Short answer: yes, within reason.`
- ✅ `Yes, within reason.`

### 5. "Here's the thing" openers
**Trigger:** `Here's the thing`, `The thing about X is`, `Let's be honest`, `Truth is`.
**Fix:** Delete. Start with the content.
- These are LLM-typical openers. Removing them helped; adding them hurt (tested).

### 6. Intensifiers
**Trigger:** `actually`, `genuinely`, `really`, `dramatically` used as pure emphasis.
**Fix:** Delete. If the emphasis carries meaning, find a concrete replacement.
- ❌ `the seven walking pads actually worth buying`
- ✅ `the seven walking pads worth buying`

### 7. Invented label fragments
**Trigger:** Sentence fragments used as paragraph labels (`The compromises.`, `Short answer:`, `On the downside,`).
**Fix:** Integrate into a full sentence. (Note: we introduced some of these ourselves during editing — the detector caught them.)
- ❌ `The compromises. The 15" belt is narrow.`
- ✅ `The 15-inch belt is narrow, fine for walking but tight for jogging.`

### 8. Formulaic transitions
**Trigger:** `As a rule of thumb,`, `Still,` (sentence-initial), `For X,`, `On Y:`.
**Fix:** Delete or replace with plain connective tissue.

---

## The DON'T List (tested, failed)

These "humanizing" tricks did NOT reduce AI scores in controlled tests, or made them worse:

| Trick | Result |
|---|---|
| Add rhetorical questions | No change (AI 100% → AI 100%) |
| Add metaphors | No change |
| Add first-person voice ("I") | No change |
| Add contractions (don't, you'll) | **Worse** (LLMs overuse these too) |
| Casual slang ("lol", "btw") | "Human" at 0.09 confidence — unreliable, wrong register |
| "Here's the thing" / "The thing is" | **Worse** (classic LLM opener) |
| "Not because X, but because Y" | **Worse** (antithesis is rule #2) |
| Sentence fragments for punch | Mixed — works in FAQ, hurts in prose |

**Why:** Modern classifiers are trained on "humanized" LLM output as AI-class data. Imitating human style with an LLM just produces a different flavor of AI-class text.

---

## Fact Preservation (non-negotiable)

Every edit must preserve:
- Numbers, prices, specs, dates
- Product/model names
- Claims and their hedging ("claims", "reportedly", "roughly")
- The article's structure (headings, order, lists)

**Test:** After editing, every factual claim in the new text must be traceable to the old text. If you can't point to the source, revert.
