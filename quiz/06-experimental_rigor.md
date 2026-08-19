# Aspect 6 — Experimental Rigor

**Dimension:** Are the experiments well-designed, fairly compared, and
analyzed deeply enough to support the claims (ablations, error bars,
sensitivity, negative results)?

**Source basis:** `../rules/04-troubling-trends-lipton-steinhardt.md` §2
(Sources of gains), §6.1; `../rules/05-pineau-reproducibility-checklist.md` §E;
`../rules/01-neurips-paper-checklist.md` §6–8;
`../rules/06-ai-review-prompt.md` §1,5.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Items are **N/A** for papers
with no experiments.

## Items

### E01. Is there a systematic ablation study isolating each component's contribution?
- **Pass if:** Yes
- **Rationale:** Missing ablations obscure the source of empirical gains
  (troubling trend #2).
- **Source:** `05` §18; `04` §2

### E02. Is a sensitivity analysis included for key hyperparameters?
- **Pass if:** Yes
- **Rationale:** Sensitivity analysis shows robustness to hyperparameter choice.
- **Source:** `05` §19

### E03. Are negative results (settings where the method underperforms) reported?
- **Pass if:** Yes
- **Rationale:** Hiding negative results misrepresents the method's scope and
  invertibility.
- **Source:** `05` §20; `04` §6.2

### E04. Are baselines recent state-of-the-art (not strawmen)?
- **Pass if:** Yes
- **Rationale:** Strawman baselines inflate apparent gains.
- **Source:** `06` §5; `03` §Quality

### E05. Are baselines tuned with the same compute/hyperparameter-search budget as the proposed method?
- **Pass if:** Yes
- **Rationale:** Unequal budgets are the most common unfair-comparison failure.
- **Source:** `06` §5; `05` §16

### E06. Are baseline hyperparameters reported?
- **Pass if:** Yes
- **Rationale:** Unreported baseline hyperparameters block replication of the
  comparison.
- **Source:** `05` §16; `06` §5

### E07. Are baselines evaluated under the same data splits and evaluation protocol?
- **Pass if:** Yes
- **Rationale:** Mismatched protocols make comparisons meaningless.
- **Source:** `06` §5; `05` §15

### E08. Are error bars / std dev / confidence intervals reported for experiments supporting main claims?
- **Pass if:** Yes
- **Rationale:** "No error bars" is a top reviewer concern.
- **Source:** `01` §7; `05` §12; `06` §1

### E09. Is the number of runs per result reported?
- **Pass if:** Yes
- **Rationale:** Run counts ground the variance estimates.
- **Source:** `05` §10; `06` §1

### E10. Are random seeds reported (or stated as unfixed)?
- **Pass if:** Yes
- **Rationale:** Seeds enable exact replication.
- **Source:** `05` §11; `06` §1

### E11. Are multiple seeds used to estimate variance (not a single run)?
- **Pass if:** Yes
- **Rationale:** A single run cannot estimate variance; multiple seeds are
  required.
- **Source:** `01` §7; `05`

### E12. Is the method for computing error bars stated?
- **Pass if:** Yes
- **Rationale:** The method (bootstrap, closed-form, etc.) affects
  interpretation.
- **Source:** `01` §7

### E13. Is standard deviation distinguished from standard error of the mean?
- **Pass if:** Yes
- **Rationale:** std vs stderr differ by √n; conflating them misleads.
- **Source:** `01` §7

### E14. Are significance tests reported where comparative claims are made?
- **Pass if:** Yes
- **Rationale:** Significance tests guard against claiming wins within noise.
- **Source:** `05` §12

### E15. Are the factors of variability captured (split, init, random draws)?
- **Pass if:** Yes
- **Rationale:** Without knowing what varies, error bars are uninterpretable.
- **Source:** `01` §7

### E16. Do ablations disentangle bundled changes (one variable at a time)?
- **Pass if:** Yes
- **Rationale:** Bundled changes obscure which component is responsible.
- **Source:** `04` §2

### E17. Is the source of empirical gains identified and correctly attributed?
- **Pass if:** Yes
- **Rationale:** Misattributing gains (e.g. to architecture when tuning is
  responsible) is a canonical trend.
- **Source:** `04` §2; `06` §1

### E18. Are qualitative error analyses or robustness checks included?
- **Pass if:** Yes
- **Rationale:** Error analysis and robustness checks yield insight beyond
  numbers.
- **Source:** `04` §2 (positive examples)

### E19. Is performance reported across multiple datasets/settings (not a single benchmark)?
- **Pass if:** Yes
- **Rationale:** Single-benchmark evaluation limits generalizability claims.
- **Source:** `03` §Significance concerns

### E20. Is the evaluation protocol standard and consistently applied across methods?
- **Pass if:** Yes
- **Rationale:** Inconsistent protocols invalidate comparisons.
- **Source:** `06` §5

### E21. Are training details (data splits, hyperparameters, selection) fully specified?
- **Pass if:** Yes
- **Rationale:** Missing training details block reproduction.
- **Source:** `01` §6

### E22. Are compute resources per run and total disclosed?
- **Pass if:** Yes
- **Rationale:** Compute disclosure is required to judge feasibility.
- **Source:** `01` §8; `05` §13

### E23. Are hyperparameters selected via a documented procedure (not hand-picked)?
- **Pass if:** Yes
- **Rationale:** Hand-picked hyperparameters on the test set are a rigor
  failure.
- **Source:** `01` §6; `05` §9

### E24. Is the experimental scope sufficient to support the breadth of claims?
- **Pass if:** Yes
- **Rationale:** Broad claims on narrow evaluation is a rigor/significance
  mismatch.
- **Source:** `03` §Significance concerns

### E25. Are results presented to answer "what worked and why", not just "how well"?
- **Pass if:** Yes
- **Rationale:** Insight, not just headline numbers, is the hallmark of strong
  empirical work.
- **Source:** `04` §6.1
