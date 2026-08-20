# Paper Readability Evaluation

A binary-question rubric for evaluating an ML/AI research paper across 21
aspects, producing a per-aspect score and an overall score. All quiz items are
grounded in the reference documents under `rules/`.

## Layout

```
rules/      reference checklists & reviewer guidelines (source of truth)
quiz/       the evaluation rubric — one file per aspect, 20–29 items each
score.py    scorer: parses quiz files, reads an answer sheet, prints scores
```

| Aspect | File | Items |
|---|---|---|
| Readability (Clarity) | `quiz/01-readability.md` | 28 |
| Accuracy (Soundness) | `quiz/02-accuracy.md` | 29 |
| Novelty (Originality) | `quiz/03-novelty.md` | 24 |
| Significance (Impact) | `quiz/04-significance.md` | 22 |
| Reproducibility | `quiz/05-reproducibility.md` | 27 |
| Experimental Rigor | `quiz/06-experimental_rigor.md` | 25 |
| Ethics & Societal Impact | `quiz/07-ethics_societal.md` | 23 |
| Completeness | `quiz/08-completeness.md` | 23 |
| Theory Rigor | `quiz/09-theory_rigor.md` | 24 |
| Related Work & Positioning | `quiz/10-related_work_positioning.md` | 24 |
| Data Quality & Documentation | `quiz/11-data_quality_documentation.md` | 25 |
| Visuals & Design | `quiz/12-visuals_design.md` | 24 |
| Claims Calibration | `quiz/13-claims_calibration.md` | 27 |
| Resource Efficiency | `quiz/14-resource_efficiency.md` | 24 |
| Fairness & Bias | `quiz/15-fairness_bias.md` | 25 |
| Transferability | `quiz/16-transferability.md` | 25 |
| NeurIPS Compliance | `quiz/17-neurips_compliance.md` | 25 |
| ICLR Compliance | `quiz/18-iclr_compliance.md` | 25 |
| ICML Compliance | `quiz/19-icml_compliance.md` | 25 |
| ACL Compliance | `quiz/20-acl_compliance.md` | 25 |
| Scientific Storytelling | `quiz/21-scientific_storytelling.md` | 27 |

Total: **526 items** across 21 aspects (17 general + 4 conference-specific). See `quiz/README.md` for the full scoring methodology.

## Evaluation cycle

### 1. Prepare

Read the paper end-to-end: main text, appendix, and supplementary material
(code, data cards if present). Have the paper open alongside the answer sheet.

### 2. Generate a blank answer sheet

```bash
python score.py --gen-template > answers.txt
```

This lists every item from every aspect file with a `# pass if Yes/No` hint and
the question text. The quiz files are the single source of truth — the template
is regenerated from them, so the two never drift.

### 3. Answer each item

Edit `answers.txt`. For each line, replace the `# ...` comment with one of:

- `Yes` — the criterion is satisfied.
- `No` — the criterion is not satisfied.
- `N/A` — not applicable to this paper (e.g. no experiments, no human subjects,
  no theoretical results).

Format: `<ID>: <Yes|No|N/A>`. Lines starting with `#` and blank lines are
ignored. Example:

```
R01: Yes
R02: No
R03: N/A
```

Notes:

- Answer **every item**. Unanswered items count as failures (they pull the score
  down) to force completeness — if you mean "doesn't apply", mark `N/A`.
- Each item's `pass if` hint says which answer counts as a pass. Most pass on
  `Yes`; a few (e.g. "Do the stated limitations undermine the core claims?")
  pass on `No`.
- Record a short pointer to the paper section that justifies each answer — it
  makes the later revision pass much faster.

### 4. Score

```bash
python score.py --answers answers.txt            # text report
python score.py --answers answers.txt --json     # machine-readable
```

Output, per aspect: score, band, passes/scored, N/A count, missing count; plus
a per-aspect list of failed items as a revision checklist.

### 5. Interpret

Scoring (`quiz/README.md`):

- `aspect_score = passes / (non-N/A items) × 100`
- `overall_score = mean of applicable aspect scores` (N/A aspects excluded)
- "Good on an aspect" = score ≥ 80
- "Good overall" = overall ≥ 80 **and** no aspect below 60 (no single fatal flaw)

Bands: `≥85 Strong` · `70–84 Acceptable` · `50–69 Borderline` · `<50 Weak`.

Answering `No` or `N/A` is **not** an automatic reject — NeurIPS/Pineau guidance
explicitly says honest disclosure should not be penalized. The score is a signal
pointing at where to revise, not a verdict.

### 6. Revise

For any aspect below 70 (or any failed item you want to address), open that
aspect's file in `quiz/`, read the failed item's `Rationale` and `Source` line,
and fix the paper accordingly. The `Source` field cites the rule file and
section (e.g. `04 §2` = `rules/04-troubling-trends-lipton-steinhardt.md` §2) so
you can read the original guidance behind the item.

### 7. Re-run

After revisions, re-answer the affected items and re-score to confirm the score
moved. Repeat the cycle until the overall and per-aspect scores meet your
threshold.

## Requirements

Python 3.8+. No dependencies (`score.py` uses only the standard library).
