# Paper Evaluation Quiz

A binary-question rubric for evaluating an ML/AI research paper across several
aspects. Each aspect lives in its own file; each file contains 20–50 yes/no
items. Answering the items yields a per-aspect score and an overall paper score.

All items are grounded in the reference documents under `../rules/`. Each item
cites the rule file(s) and section it derives from.

## Aspects

| # | File | Aspect | Primary source basis |
|---|------|--------|----------------------|
| 1 | [`01-readability.md`](01-readability.md) | Readability (Clarity / Writing) | `03` §Clarity, `04` §3–4, `06` §2,4 |
| 2 | [`02-accuracy.md`](02-accuracy.md) | Accuracy (Technical Soundness) | `01` §1,3,7, `03` §Quality, `04` §2–3, `06` §1 |
| 3 | [`03-novelty.md`](03-novelty.md) | Novelty (Originality) | `03` §Originality, `04`, `06` §8 |
| 4 | [`04-significance.md`](04-significance.md) | Significance (Impact) | `03` §Significance, `01` §10, `06` §8 |
| 5 | [`05-reproducibility.md`](05-reproducibility.md) | Reproducibility | `05` (Pineau), `01` §4–8, `02`, `06` §6 |
| 6 | [`06-experimental_rigor.md`](06-experimental_rigor.md) | Experimental Rigor | `04` §2, `05` §E, `01` §6–8, `06` §1,5 |
| 7 | [`07-ethics_societal.md`](07-ethics_societal.md) | Ethics & Societal Impact | `01` §9–16, `02`, `06` §7, `04` §4 |
| 8 | [`08-completeness.md`](08-completeness.md) | Completeness (Self-containedness) | `01` §1–3, `03`, `02`, `06` |

## How to answer

For each item, answer exactly one of:

- **Yes** — the criterion is satisfied.
- **No** — the criterion is not satisfied.
- **N/A** — not applicable to this paper (e.g. the paper has no experiments, no
  human subjects, no theoretical results).

Each item has a **Pass if** line stating which answer counts as a pass. Most
items pass on **Yes**; a few (where the criterion is the absence of a problem)
pass on **No**.

> Answering **No** or **N/A** is not, by itself, grounds to reject a paper —
> NeurIPS/Pineau guidance explicitly says honest disclosure should not be
> penalized. The score is a signal, not a verdict. See `../rules/01-*.md` and
> `../rules/05-*.md`.

## Scoring

### Per aspect

Exclude **N/A** items from both numerator and denominator:

```
aspect_score = (# passes) / (# items answered Yes or No) × 100
```

If an aspect has no applicable items at all (e.g. a theory paper with none of
the experimental items applicable), mark that aspect **N/A** and exclude it from
the overall score.

### Overall

Equal weights across applicable aspects:

```
overall_score = average of aspect_scores (over non-N/A aspects)
```

### Thresholds (suggested, tunable)

| Score | Band | Interpretation |
|-------|------|----------------|
| ≥ 85 | Strong | Aspect is in good shape |
| 70–84 | Acceptable | Minor revisions |
| 50–69 | Borderline | Substantial revisions needed |
| < 50 | Weak | Likely a reject reason on this aspect |

A paper is considered **good on an aspect** at `aspect_score ≥ 80`, and
**good overall** at `overall_score ≥ 80` with no individual aspect below 60
(no single fatal flaw).

## Workflow

1. Read the paper end-to-end (main + appendix + supplementary).
2. For each aspect file, go item by item; record Yes / No / N/A with a short
   note pointing to the paper section that justifies the answer.
3. Compute `aspect_score` for each aspect and the `overall_score`.
4. For any aspect below 70, read the failed items' rationales and sources; turn
   them into a revision checklist.
5. Re-run after revisions to verify the score moved.

## Notes

- The item sets intentionally overlap across aspects (e.g. error bars appear in
  both `accuracy` and `experimental_rigor`). This is deliberate: each aspect is
  independently scorable, and overlap reflects how reviewers actually weigh the
  same evidence from multiple angles.
- Source citations like `03 §Clarity` refer to file `03-ml-reviewer-guidelines.md`
  in `../rules/`, section "Clarity".
