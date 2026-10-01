# Research Background

## How AI Text Detectors Work

Two technical families (after guillaumemeyer/watermarks-remover):

### Family A: Statistical / Zero-Shot
Score text by **perplexity** (how surprising each token is to a reference language model) and **burstiness** (variance in sentence-level perplexity/length). Human writing is high-perplexity and high-variance; instruction-tuned LLM output is low-perplexity and metronomic.

- **GPTZero (original):** perplexity + burstiness
- **DetectGPT** (Mitchell et al., 2023): checks if text sits at a local maximum of model log-probability via perturbations
- **Binoculars** (Hans et al., 2024): ratio of two LLMs' cross-perplexity — robust, zero-shot

### Family B: Trained Neural Classifiers
Transformers fine-tuned on large human/AI paired corpora. Learn **post-training artifacts** (RLHF style fingerprints) rather than "AI-ness" per se.

- **Pangram, Originality.ai, Copyleaks, Turnitin, GPTZero (current)**
- **Tencent Zhuque** (`@makers/zhuque-text`) — the detector this methodology was validated against
- Hardened with **hard-negative mining**: paraphraser/"humanizer" outputs included as AI-class training data

**Key implication:** Against Family B, perplexity tricks and synonym swaps are weak. The classifier has seen your tricks in training.

## Key Academic Papers

| Paper | Finding |
|---|---|
| Krishna et al. (2023), "Paraphrasing Evades Detectors" (DIPPER) | Paraphrasing drops DetectGPT accuracy 70.3% → 4.6%. Canonical evasion paper. |
| Hu et al. (2023), RADAR | GAN-style co-training of paraphraser + detector. Detection as minimax arms race. |
| Cheng et al. (2025), "Adversarial Paraphrasing" | **Detector-in-the-loop** humanization: 87.88% avg detection reduction. Undirected paraphrasing *increases* detection 8–15% on modern classifiers. |
| David & Gervais (2025), AuthorMist | RL-trained paraphraser using detector APIs as reward: 78.6–96.2% attack success. |
| Zha et al. (2025), PADBen | Iterative paraphrasing (3–5 rounds) defeats detectors but causes semantic drift after 5 rounds. |

## The lieflat-less-ai-tone Study

[lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) — corpus linguistics study (629 articles, 2.8M Chinese characters, 5 LLMs vs human authors). 11 statistically validated AI-tone features:

| # | Feature | Ratio (AI/Human) |
|---|---|---|
| 1 | Antithesis ("not A but B" / 不是A而是B) | 3.4× |
| 2 | Dense enumeration with 、 | 1.8× |
| 3 | Adjacent-sentence structural isomorphism | 2.0× |
| 4 | Em-dash overuse | 3.0× |
| 5 | Colon abuse (prompts + empty list intros) | 3.8× / 9.4× |
| 6 | Ordinal numbers as headings | 3.1× |
| 7 | Idealized personification metaphors | 7.3× |
| 8 | Generalizations covering existing data | 0.35× (reverse) |
| 9 | Opener clichés ("说白了") | 3.2× |
| 10 | Translationese (5 structures) | 2.6–5.3× |
| 11 | Paragraph-initial zero-anaphora comments | **4.4×** |

Notable **debunked** folk wisdoms: humans use 2.4× MORE metaphors, 17× MORE questions, and equal sentence-length variance vs AI. "Add human touches" advice is empirically backwards.

Our CHECKLIST.md adapts the applicable features to English.

## Why This Matters

The academic consensus: **detection is unreliable and beatable**; the credible counter is ensembles + retrieval logging (impractical for most deployments). This repo operationalizes the research into a repeatable process.
