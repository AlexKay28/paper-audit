# Aspect 2 — Accuracy (Technical Soundness)

**Dimension:** Are claims well-supported, proofs correct, experiments properly
controlled, and baselines fair?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §1,3,7;
`../rules/03-ml-reviewer-guidelines.md` §Quality;
`../rules/04-troubling-trends-lipton-steinhardt.md` §2 (Sources of gains), §3
(Mathiness); `../rules/05-pineau-reproducibility-checklist.md` §D (Baselines);
`../rules/06-ai-review-prompt.md` §1.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### A01. Do the main claims in abstract/intro accurately reflect contributions and scope (not overstated)?
- **Pass if:** Yes
- **Rationale:** Overstated claims relative to evidence is the canonical
  soundness failure.
- **Source:** `01` §1; `06` §1

### A02. Are aspirational goals clearly distinguished from attained results?
- **Pass if:** Yes
- **Rationale:** Aspirational framing is fine as motivation but must not be
  presented as achieved.
- **Source:** `01` §1

### A03. Are all assumptions of every theoretical result explicitly stated?
- **Pass if:** Yes
- **Rationale:** Hidden assumptions make theorems unverifiable.
- **Source:** `01` §3; `06` §1

### A04. Are proofs complete (in main paper or appendix, with a sketch in the main if in appendix)?
- **Pass if:** Yes
- **Rationale:** Complete proofs are required for theoretical results.
- **Source:** `01` §3; `06` §2

### A05. Are proofs correct (no known errors; relied-upon theorems/lemmas properly cited)?
- **Pass if:** Yes
- **Rationale:** Incorrect proofs (e.g. the Adam convergence proof) undermine
  the contribution.
- **Source:** `01` §3; `04` §3 (Adam example)

### A06. Is every claim supported by theoretical analysis or experimental evidence?
- **Pass if:** Yes
- **Rationale:** "Claims not supported" is a top reviewer concern.
- **Source:** `03` §Quality; `06` §1

### A07. Do theorems' conclusions actually support the main claims (not spurious)?
- **Pass if:** Yes
- **Rationale:** A theorem whose conclusion does not back the claims is
  mathiness, not rigor.
- **Source:** `04` §3; `06` §1

### A08. Is broad theory (e.g. no-free-lunch) invoked only where formally applicable?
- **Pass if:** Yes
- **Rationale:** Invoking NFL to justify heuristics without guarantees is a
  flagged misuse.
- **Source:** `04` §3

### A09. Are empirical gains attributed to the correct source (ablations isolate the cause)?
- **Pass if:** Yes
- **Rationale:** Failure to identify the source of gains is troubling trend #2.
- **Source:** `04` §2; `06` §1

### A10. Are multiple proposed changes disentangled via ablation rather than bundled?
- **Pass if:** Yes
- **Rationale:** Bundled changes obscure which component is responsible.
- **Source:** `04` §2; `06` §1

### A11. Are baselines appropriate and recent (not strawmen)?
- **Pass if:** Yes
- **Rationale:** Weak baselines inflate apparent gains.
- **Source:** `03` §Quality; `06` §5

### A12. Are baselines compared fairly (same data, compute, tuning budget)?
- **Pass if:** Yes
- **Rationale:** Unequal tuning budgets systematically favor the proposed
  method.
- **Source:** `05` §15–17; `06` §5

### A13. Is the methodology sound and reproducible from the description?
- **Pass if:** Yes
- **Rationale:** Methodological soundness is the core quality criterion.
- **Source:** `03` §Quality

### A14. Are experiments properly controlled?
- **Pass if:** Yes
- **Rationale:** Uncontrolled experiments cannot support causal claims.
- **Source:** `03` §Quality

### A15. Is the evaluation protocol standard and consistently applied across methods?
- **Pass if:** Yes
- **Rationale:** Inconsistent protocols make comparisons meaningless.
- **Source:** `06` §5

### A16. Are error bars / std dev / confidence intervals reported for results supporting main claims?
- **Pass if:** Yes
- **Rationale:** Missing error bars is a frequent rejection concern.
- **Source:** `01` §7; `05` §12; `06` §1

### A17. Is the method for computing error bars stated (closed-form, bootstrap, library)?
- **Pass if:** Yes
- **Rationale:** Method matters; identical numbers can mean different things.
- **Source:** `01` §7

### A18. Are the factors of variability captured (train/test split, init, random draws)?
- **Pass if:** Yes
- **Rationale:** Without knowing what varies, the error bar is uninterpretable.
- **Source:** `01` §7

### A19. Is it clarified whether bars are standard deviation or standard error of the mean?
- **Pass if:** Yes
- **Rationale:** std and stderr differ by √n; conflating them misleads.
- **Source:** `01` §7

### A20. Are error bars symmetric only where appropriate (no out-of-range values like negative rates)?
- **Pass if:** Yes
- **Rationale:** Symmetric bars on skewed distributions produce nonsensical
  values.
- **Source:** `01` §7

### A21. Are statistical significance tests reported where comparative claims are made?
- **Pass if:** Yes
- **Rationale:** Significance tests guard against claiming wins within noise.
- **Source:** `05` §12

### A22. Is the number of runs per reported result stated?
- **Pass if:** Yes
- **Rationale:** A single run cannot estimate variance.
- **Source:** `05` §10; `06` §1

### A23. Are random seeds reported (or explicitly stated as unfixed)?
- **Pass if:** Yes
- **Rationale:** Unreported seeds block exact replication.
- **Source:** `05` §11; `06` §1

### A24. Are negative results (settings where the method underperforms) reported, not hidden?
- **Pass if:** Yes
- **Rationale:** Hiding negative results misrepresents the method's scope.
- **Source:** `05` §20; `04` §6.2

### A25. Are generalization claims restricted to the tested distribution (no population→population conflation)?
- **Pass if:** Yes
- **Rationale:** Conflating train→test with population→population overstates
  capability.
- **Source:** `04` §4.3

### A26. Are limitations of the method honestly discussed?
- **Pass if:** Yes
- **Rationale:** Honest limitations are encouraged; reviewers should not
  penalize them.
- **Source:** `01` §2; `03` §Quality

### A27. Do the stated limitations undermine the core claims?
- **Pass if:** No
- **Rationale:** If acknowledged limitations invalidate the claims, the claims
  are too strong.
- **Source:** `03` §ACL (Limitations section)

### A28. Are headline numbers contextualized (insight into "what worked and why", not just "how well")?
- **Pass if:** Yes
- **Rationale:** Raw numbers without insight are low scientific value.
- **Source:** `04` §6.1

### A29. Is the experimental scope (datasets, settings) sufficient to support the breadth of claims?
- **Pass if:** Yes
- **Rationale:** Broad claims on narrow evaluation is a significance/soundness
  mismatch.
- **Source:** `03` §Significance concerns
