# Surgical Checklist: De-telling Rules (v2.0)

Concrete, locatable rules for removing AI-tone. V1 rules validated by our own detector experiments (2026-10-02). V2 additions adopted from [blader/humanizer](https://github.com/blader/humanizer) (based on Wikipedia's "Signs of AI writing") — marked [H].

**Apply in order. Each rule fires only on its exact trigger. If unsure, leave the sentence alone.**

---

## A. Staging instead of stating (strongest — act on one sighting)

### 1. "X, but Y" flips / "not X but Y" [V1 validated]
**Trigger:** Contrast where the second half overturns the first (`isn't just X — it's Y`, `not intensity; it's consistency`, `X rather than Y`, split across sentences: "This does not mean X. It means Y.")
**Fix:** State directly. Keep a contrast only when the negative half corrects a belief the reader actually holds.
- ❌ `Capacity isn't just about your body weight — it's about how hard the motor works.`
- ✅ `Capacity is about more than your body weight. It is about how hard the motor works.`

### 2. One-line closers and dramatic fragments [H]
**Trigger:** One-sentence paragraph restating the previous paragraph (`That is the real win.`, `That distinction matters.`, `Read that again.`); row of fragments (`No aesthetic prior. No nostalgia.`); a sentence after an example naming what it showed (`This shows the importance of...`).
**Fix:** Cut closers that repeat. Merge fragment rows into a sentence with a specific claim.
- ❌ `Caching cuts repeat work.\n\nThat is the real win.`
- ✅ `Caching cuts repeat work.`

### 3. Deep-sounding sayings [H]
**Trigger:** `the real question is`, `at its core`, `what really matters`, `fundamentally`, `the heart of the matter`, `X is the Y of Z`, `X becomes a trap`.
**Fix:** Replace with the specific claim.
- ❌ `At its core, what really matters is organizational readiness.`
- ✅ `That mostly depends on whether the organization is ready to change its habits.`

### 4. "Here's the thing" openers [V1 validated]
**Trigger:** `Here's the thing`, `The thing about X is`, `Let's be honest`, `Truth is`, `Let's dive in`, `Here's what you need to know`.
**Fix:** Delete. Start with the content.

### 5. Arguing with no one [H]
**Trigger:** `This isn't about`, `I'm not saying`, `To be clear`, `Don't get me wrong`, `Some might say... but`, `You might think... but`.
**Fix:** Remove the defense; state the claim. Keep only objections the text actually answers.
- ❌ `This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter.`
- ✅ Cut to the actual point.

---

## B. Rhythm by rule

### 6. Em-dash reveals [V1 validated]
**Trigger:** `—` followed by a punchline, summary, or dramatic pause. Dashes used as universal connector.
**Fix:** Split into two sentences, or use comma/period/parentheses.
- ❌ `Don't jog on a handrail-free pad — that's how people fall off.`
- ✅ `Do not jog on a handrail-free pad. People fall off that way.`

### 7. Tripartite parallelism [V1 validated]
**Trigger:** Three parallel items in prose, three parallel examples, three short facts + a lesson.
**Fix:** Merge examples, develop the strongest one, or vary structure. Keep three real items when the meaning needs three.
- ❌ `top speed, weight capacity, noise, and folded size`
- ✅ Split across sentences or restructure.

### 8. Prompt colons and label fragments [V1 validated]
**Trigger:** Colon after a label (`Quirks:`, `Short answer:`); fragments as paragraph labels (`The compromises.`); bold labels on every list item.
**Fix:** Turn labels into sentences. Turn labeled lists into prose when labels carry no information.
- ❌ `Short answer: yes, within reason.`
- ✅ `Yes, within reason.`

### 9. Repeated sentence openings [H]
**Trigger:** Several sentences in a row starting with the same subject.
**Fix:** Merge sentences, change the subject, or begin with the action.

---

## C. Inflation and borrowed authority

### 10. Overused AI words [H]
**Trigger:** `delve`, `crucial`, `pivotal`, `robust` (figurative), `landscape` (abstract), `tapestry`, `testament`, `showcase`, `underscore` (verb), `intricate`, `vibrant`, `meticulous`, `bolstered`, `garner`, `deep dive`, `enduring`.
**Fix:** Replace with plain equivalents. These words are tells wherever they appear, especially in groups.
- ❌ `An enduring testament to Italian influence, showcasing how pasta integrated into the culinary landscape.`
- ✅ `Pasta dishes, introduced during Italian colonization, remain common.`

### 11. Inflated significance [H]
**Trigger:** `stands as a testament`, `pivotal moment`, `plays a key role`, `shaping the`, `underscores its importance`, `reflects a broader`, `setting the stage for`, `the future looks bright`, `exciting times ahead`.
**Fix:** Keep the fact, drop the significance. End on the last concrete fact.
- ❌ `Established in 1989, marking a pivotal moment in the evolution of regional statistics.`
- ✅ `Established in 1989, part of a wider decentralization.`

### 12. Shallow -ing riders [H]
**Trigger:** `highlighting`, `underscoring`, `showcasing`, `ensuring`, `reflecting`, `symbolizing`, `fostering` bolted onto a simple fact to sound deeper.
**Fix:** Keep the fact; cut the rider unless the source supports it.

### 13. Sales language [H]
**Trigger:** `nestled`, `breathtaking`, `renowned`, `must-visit`, `stunning`, `rich` (figurative), `groundbreaking` (figurative), `in the heart of`.
**Fix:** State what the thing is.
- ❌ `Nestled in the breathtaking Gonder region, a vibrant town with rich heritage.`
- ✅ `A town in the Gonder region of Ethiopia.`

### 14. Borrowed authority [H]
**Trigger:** `experts argue`, `observers have cited`, `industry reports`, `some critics`, prestige outlet lists, follower counts as credibility.
**Fix:** Name the real source and what it said, or cut the claim.

### 15. Verbose verbs [H]
**Trigger:** `serves as`, `stands as`, `functions as`, `boasts`, `features`, `offers` where `is`, `are`, `has` would do.
**Fix:** Use the simple verb.
- ❌ `The gallery features four spaces and boasts 3,000 square feet.`
- ✅ `The gallery has four rooms totaling 3,000 square feet.`

### 16. Intensifiers [V1 validated]
**Trigger:** `actually`, `genuinely`, `really`, `dramatically` as pure emphasis.
**Fix:** Delete.

---

## The DON'T List (tested, failed)

| Trick | Result |
|---|---|
| Add rhetorical questions | No change (AI 100% → AI 100%) |
| Add metaphors | No change |
| Add first-person voice ("I") | No change |
| Add contractions (don't, you'll) | **Worse** (LLMs overuse these too) |
| Casual slang ("lol", "btw") | "Human" at 0.09 confidence — unreliable |
| "Here's the thing" / "The thing is" | **Worse** (classic LLM opener) |
| "Not because X, but because Y" | **Worse** (antithesis is rule #1) |
| Sentence fragments for punch | Mixed — works in FAQ, hurts in prose |

**Why:** Modern classifiers are trained on "humanized" LLM output as AI-class data. Imitating human style with an LLM just produces a different flavor of AI-class text.

---

## Fact Preservation (non-negotiable)

Every edit must preserve: numbers, prices, specs, dates, product/model names, claims and their hedging, article structure.

**Test:** Every factual claim in the new text must be traceable to the old text. If you can't point to the source, revert.

## Sources
- V1 rules: our detector experiments (EXPERIMENTS.md), lieflat-less-ai-tone corpus study
- [H] rules: [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 (MIT), via Wikipedia "Signs of AI writing"
