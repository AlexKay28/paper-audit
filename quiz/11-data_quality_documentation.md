# Aspect 11 — Data Quality & Documentation

**Dimension:** Are datasets described, documented, and released responsibly,
with provenance, preprocessing, consent, and known biases addressed?

**Source basis:** `../rules/05-pineau-reproducibility-checklist.md` §5–7, §B;
`../rules/01-neurips-paper-checklist.md` §5, §12–14;
`../rules/06-ai-review-prompt.md` §6, §7;
`../rules/04-troubling-trends-lipton-steinhardt.md` §4.1.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Many items are **N/A** for papers
that use no data.

## Items

### D01. Is each dataset described (size, modalities, source, year)?
- **Pass if:** Yes
- **Rationale:** Dataset provenance is required to interpret and reuse
  results.
- **Source:** `05` §5

### D02. Are train/validation/test split sizes reported?
- **Pass if:** Yes
- **Rationale:** Split sizes affect comparability and variance.
- **Source:** `05` §5

### D03. Are label statistics reported (class balance; mean/std for regression)?
- **Pass if:** Yes
- **Rationale:** Label statistics let reviewers detect imbalance and
  miscalibration.
- **Source:** `05` §5

### D04. Are all data pre-processing steps described (normalization, tokenization, augmentation, filtering)?
- **Pass if:** Yes
- **Rationale:** Undisclosed preprocessing is a major reproducibility gap.
- **Source:** `05` §6

### D05. Is the data release path stated (released, or construction instructions)?
- **Pass if:** Yes
- **Rationale:** Data must be accessible or reconstructable.
- **Source:** `01` §4,5; `05` §4

### D06. For new datasets, is a datasheet / data card included?
- **Pass if:** Yes
- **Rationale:** Datasheets (Gebru et al.) are the standard for dataset
  documentation.
- **Source:** `05` §7

### D07. For new datasets, is the motivation/composition documented?
- **Pass if:** Yes
- **Rationale:** Motivation and composition ground the dataset's intended use.
- **Source:** `05` §7

### D08. For new datasets, is the collection process documented?
- **Pass if:** Yes
- **Rationale:** Collection process transparency is a datasheet requirement.
- **Source:** `05` §7

### D09. For new datasets, are intended uses stated?
- **Pass if:** Yes
- **Rationale:** Intended-use documentation prevents misuse.
- **Source:** `05` §7

### D10. For new datasets, is the license and terms of use stated?
- **Pass if:** Yes
- **Rationale:** License disclosure is required for responsible release.
- **Source:** `05` §7; `01` §12

### D11. For new datasets, was consent obtained from people whose data is used?
- **Pass if:** Yes
- **Rationale:** Consent procedures are required for human-derived data.
- **Source:** `01` §13; `05` §7

### D12. For new datasets, are known biases / limitations documented?
- **Pass if:** Yes
- **Rationale:** Documenting known biases is required for responsible release.
- **Source:** `05` §7; `04` §4.1

### D13. For web-scraped datasets, is unsafe-content filtering described?
- **Pass if:** Yes
- **Rationale:** Scraped data poses safety risks that must be addressed.
- **Source:** `01` §11

### D14. Are dataset versions stated for reused datasets?
- **Pass if:** Yes
- **Rationale:** Version pinning aids reproducibility and license tracking.
- **Source:** `01` §12

### D15. Are dataset licenses cited and respected?
- **Pass if:** Yes
- **Rationale:** License compliance is mandatory for reused assets.
- **Source:** `01` §12

### D16. For repackaged datasets, are both original and derived licenses stated?
- **Pass if:** Yes
- **Rationale:** Repackaging must preserve and state the original license.
- **Source:** `01` §12

### D17. Are datasets anonymized at submission time?
- **Pass if:** Yes
- **Rationale:** Anonymization is required during double-blind review.
- **Source:** `01` §5; `02`

### D18. Is the dataset's representativeness / coverage discussed?
- **Pass if:** Yes
- **Rationale:** Coverage limitations affect generalization claims.
- **Source:** `04` §1 (coverage concept); `05` §7

### D19. Are dataset biases that could affect conclusions discussed?
- **Pass if:** Yes
- **Rationale:** Unexamined dataset bias invalidates downstream claims.
- **Source:** `04` §4.1; `05` §7

### D20. Is the relationship between train/test distribution discussed (distribution shift)?
- **Pass if:** Yes
- **Rationale:** Train/test distribution mismatch affects generalization
  interpretation.
- **Source:** `04` §4.2 (covariate shift)

### D21. For human-subjects data, are IRB approvals and compensation described?
- **Pass if:** Yes
- **Rationale:** IRB and fair compensation are required for human-subjects
  research.
- **Source:** `01` §14–15

### D22. For crowdsourced data, are instructions and screenshots provided?
- **Pass if:** Yes
- **Rationale:** Instruction transparency is required for crowdsourced data.
- **Source:** `01` §14

### D23. Is data maintenance / hosting described for new datasets?
- **Pass if:** Yes
- **Rationale:** Maintenance plans prevent dataset rot.
- **Source:** `05` §7

### D24. Is data quality control (validation, cleaning) described?
- **Pass if:** Yes
- **Rationale:** Undocumented cleaning hides potential biases.
- **Source:** `05` §6

### D25. Are data ethics concerns (privacy, re-identification) addressed where relevant?
- **Pass if:** Yes
- **Rationale:** Privacy and re-identification are dataset ethics issues.
- **Source:** `02` (Ethics Statement); `01` §10
