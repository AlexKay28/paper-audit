# Aspect 8 — Completeness (Self-containedness)

**Dimension:** Is the paper self-contained, with stated contributions,
limitations, related work, and all supporting material present and locatable?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §1–3,5;
`../rules/03-ml-reviewer-guidelines.md` §Clarity, ACL (Limitations);
`../rules/02-iclr-author-guide.md` (Supplementary);
`../rules/06-ai-review-prompt.md` §1,4.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### C01. Are contributions clearly stated in the abstract and introduction?
- **Pass if:** Yes
- **Rationale:** Surfacing contributions up front lets reviewers credit them.
- **Source:** `01` §1

### C02. Are important assumptions and limitations stated alongside contributions?
- **Pass if:** Yes
- **Rationale:** Contributions and their caveats belong together.
- **Source:** `01` §1

### C03. Is there a dedicated Limitations section?
- **Pass if:** Yes
- **Rationale:** A separate Limitations section is encouraged (and required at
  ACL).
- **Source:** `01` §2; `03` §ACL

### C04. Are strong assumptions and robustness-to-violations discussed?
- **Pass if:** Yes
- **Rationale:** Reviewers want to know how results degrade if assumptions
  break.
- **Source:** `01` §2

### C05. Is the scope of claims reflected (e.g. tested on only a few datasets/runs)?
- **Pass if:** Yes
- **Rationale:** Overclaiming scope is a completeness/soundness defect.
- **Source:** `01` §2

### C06. Are implicit empirical assumptions articulated?
- **Pass if:** Yes
- **Rationale:** Hidden empirical assumptions can invalidate conclusions.
- **Source:** `01` §2

### C07. Are factors influencing performance discussed?
- **Pass if:** Yes
- **Rationale:** Discussing performance factors (e.g. resolution, jargon) is
  expected.
- **Source:** `01` §2

### C08. Is the related work coverage adequate (recent and comprehensive)?
- **Pass if:** Yes
- **Rationale:** Inadequate related work suggests uncalibrated novelty.
- **Source:** `03`; `04`

### C09. Is the closest prior work explicitly compared?
- **Pass if:** Yes
- **Rationale:** The closest work must be directly addressed.
- **Source:** `03` §Novelty concerns

### C10. Is the paper self-contained (core content understandable without external docs)?
- **Pass if:** Yes
- **Rationale:** Self-containedness is an explicit reviewer criterion.
- **Source:** `03` §Clarity

### C11. Are all theorems' assumptions stated?
- **Pass if:** Yes
- **Rationale:** Unstated assumptions make theorems unverifiable.
- **Source:** `01` §3

### C12. Are proofs complete or sketched in main + full in appendix?
- **Pass if:** Yes
- **Rationale:** Theoretical results require complete proofs somewhere.
- **Source:** `01` §3

### C13. Is reproducibility detail provided (appendix acceptable)?
- **Pass if:** Yes
- **Rationale:** Reproducibility detail may live in an appendix but must exist.
- **Source:** `03` §Clarity; `01` §4–8

### C14. Is notation consistent and defined?
- **Pass if:** Yes
- **Rationale:** Inconsistent/undefined notation is a completeness defect.
- **Source:** `03` §Clarity

### C15. Is the Limitations section honest and comprehensive?
- **Pass if:** Yes
- **Rationale:** Token limitations sections are flagged by reviewers.
- **Source:** `03` §ACL

### C16. Do the stated limitations undermine the core claims?
- **Pass if:** No
- **Rationale:** If limitations invalidate claims, the claims are too strong.
- **Source:** `03` §ACL

### C17. Are potential negative impacts addressed in limitations/ethics?
- **Pass if:** Yes
- **Rationale:** Negative impacts belong in limitations or a dedicated section.
- **Source:** `03` §ACL

### C18. Is there a summary/conclusion recapping contributions?
- **Pass if:** Yes
- **Rationale:** A conclusion consolidates the contribution for the reader.
- **Source:** `06` §1 (general structure)

### C19. Are all referenced figures/tables present and correctly numbered?
- **Pass if:** Yes
- **Rationale:** Missing/misnumbered figures signal a rushed submission.
- **Source:** `06` §4

### C20. Are all citations resolvable (no broken or placeholder references)?
- **Pass if:** Yes
- **Rationale:** Broken citations impede verification of related-work claims.
- **Source:** `06` §1

### C21. Is supplementary material (code/data/appendix) properly referenced from the main text?
- **Pass if:** Yes
- **Rationale:** Reviewers must be able to locate supplementary content.
- **Source:** `02` (Supplementary); `01` §5

### C22. Are appendices organized so reviewers can locate overflow detail?
- **Pass if:** Yes
- **Rationale:** Appendices may sit in the main PDF or a supplementary file,
  but must be navigable.
- **Source:** `02` (Supplementary)

### C23. Does the paper disclose if fewer than all experiments are reproducible?
- **Pass if:** Yes
- **Rationale:** Partial reproducibility must be honestly scoped.
- **Source:** `01` §5
