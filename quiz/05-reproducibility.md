# Aspect 5 — Reproducibility

**Dimension:** Can the reported results be verified, replicated, and extended
by others from the information provided?

**Source basis:** `../rules/05-pineau-reproducibility-checklist.md` (Pineau et
al.); `../rules/01-neurips-paper-checklist.md` §4–8;
`../rules/02-iclr-author-guide.md` (Reproducibility Statement);
`../rules/06-ai-review-prompt.md` §6.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Many items are **N/A** for pure
theory papers — exclude them from the denominator.

## Items

### P01. Is there a clear description of the algorithm(s) (pseudocode, equations, or diagrams)?
- **Pass if:** Yes
- **Rationale:** A clear algorithm description is the foundation of
  reproducibility.
- **Source:** `05` §1

### P02. Is computational complexity analyzed for non-standard algorithms?
- **Pass if:** Yes
- **Rationale:** Complexity analysis lets others judge feasibility before
  re-running.
- **Source:** `05` §2

### P03. Are non-trivial hardware/software dependencies described?
- **Pass if:** Yes
- **Rationale:** Hidden dependencies (specific GPUs, libraries) block
  replication.
- **Source:** `05` §3

### P04. Is source code released (or an anonymized URL provided at submission)?
- **Pass if:** Yes
- **Rationale:** Code release is the strongest reproducibility signal; an
  anonymized URL suffices at submission.
- **Source:** `05` §4; `02` (Source Code Submission)

### P05. Is data released, or a path to reproduce it provided (open dataset or construction instructions)?
- **Pass if:** Yes
- **Rationale:** Data must be accessible or reconstructable.
- **Source:** `01` §4,5; `05` §4

### P06. For closed-source models, is some verification path provided (e.g. registered access)?
- **Pass if:** Yes
- **Rationale:** Closed-source models still require a path to verification.
- **Source:** `01` §4

### P07. Is each dataset described (size, modalities, source, year)?
- **Pass if:** Yes
- **Rationale:** Dataset provenance is required to interpret and reuse results.
- **Source:** `05` §5

### P08. Are train/validation/test split sizes reported?
- **Pass if:** Yes
- **Rationale:** Split sizes affect comparability and variance.
- **Source:** `05` §5

### P09. Are label statistics reported (class balance; mean/std for regression)?
- **Pass if:** Yes
- **Rationale:** Label statistics let reviewers detect imbalance and
  miscalibration.
- **Source:** `05` §5

### P10. Are all data pre-processing steps described (normalization, tokenization, augmentation, filtering)?
- **Pass if:** Yes
- **Rationale:** Undisclosed preprocessing is a major reproducibility gap.
- **Source:** `05` §6

### P11. For new datasets, is a datasheet / data card included?
- **Pass if:** Yes
- **Rationale:** Datasheets (Gebru et al.) are the standard for dataset
  documentation.
- **Source:** `05` §7

### P12. For new datasets, are license, consent, and known biases documented?
- **Pass if:** Yes
- **Rationale:** Licensing and bias disclosure are required for responsible
  dataset release.
- **Source:** `05` §7

### P13. Is the full set of hyperparameters reported per algorithm per dataset?
- **Pass if:** Yes
- **Rationale:** Reporting only final values hides the search space.
- **Source:** `05` §8; `01` §6

### P14. Are architecture details (layers, hidden sizes, activations) reported?
- **Pass if:** Yes
- **Rationale:** Architecture must be fully specified to rebuild the model.
- **Source:** `05` §8

### P15. Are training horizon and early-stopping criteria reported?
- **Pass if:** Yes
- **Rationale:** Training length and stopping rules affect final results.
- **Source:** `05` §8

### P16. Is the hyperparameter search described (range, method, # trials, selection criterion)?
- **Pass if:** Yes
- **Rationale:** Search procedure documentation is essential; final values
  alone are insufficient.
- **Source:** `05` §9; `01` §6

### P17. Is the number of runs per reported result stated?
- **Pass if:** Yes
- **Rationale:** Run counts are needed to interpret variance estimates.
- **Source:** `05` §10

### P18. Are random seeds reported (or explicitly stated as unfixed)?
- **Pass if:** Yes
- **Rationale:** Seeds enable exact replication; "unfixed" is an acceptable
  honest answer.
- **Source:** `05` §11; `06` §6

### P19. Are mean and std/error (or confidence intervals) reported per result?
- **Pass if:** Yes
- **Rationale:** Point estimates without spread are not reproducible in spirit.
- **Source:** `05` §12

### P20. Are compute resources disclosed (GPU type, count, runtime per run, total)?
- **Pass if:** Yes
- **Rationale:** Compute disclosure lets others judge feasibility and carbon
  cost.
- **Source:** `05` §13; `01` §8

### P21. Are software versions (framework, CUDA) reported?
- **Pass if:** Yes
- **Rationale:** Version drift breaks replication; versions must be pinned.
- **Source:** `05` §14

### P22. Are baselines reproduced under the same conditions as the proposed method?
- **Pass if:** Yes
- **Rationale:** Taking baseline numbers from prior work without
  re-verification is unfair.
- **Source:** `05` §15

### P23. Are baseline hyperparameters reported and baselines tuned fairly (same budget)?
- **Pass if:** Yes
- **Rationale:** Unequal tuning budgets systematically bias comparisons.
- **Source:** `05` §16

### P24. Is original authors' code/data used for baselines where available, with deviations noted?
- **Pass if:** Yes
- **Rationale:** Using reference implementations reduces implementation
  mismatch.
- **Source:** `05` §17

### P25. Is there a paragraph-long Reproducibility Statement referencing the relevant sections/appendices?
- **Pass if:** Yes
- **Rationale:** ICLR explicitly encourages a reproducibility statement
  pointing to details.
- **Source:** `05` §21; `02` (Reproducibility Statement)

### P26. Are exact commands and environment needed to run provided?
- **Pass if:** Yes
- **Rationale:** Reproduction instructions must contain the exact command and
  environment.
- **Source:** `01` §5

### P27. Is it stated which subset of experiments is reproducible if not all are?
- **Pass if:** Yes
- **Rationale:** Partial reproducibility must be honestly scoped.
- **Source:** `01` §5
