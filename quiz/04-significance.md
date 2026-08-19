# Aspect 4 — Significance (Impact & Importance)

**Dimension:** Are the results impactful? Does the work address an important
problem with real-world or research-community impact?

**Source basis:** `../rules/03-ml-reviewer-guidelines.md` §Significance;
`../rules/01-neurips-paper-checklist.md` §10;
`../rules/06-ai-review-prompt.md` §8; `../rules/04-troubling-trends-lipton-steinhardt.md` §6.1.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### S01. Is the problem's importance clearly articulated?
- **Pass if:** Yes
- **Rationale:** Without a stated motivation for importance, impact is
  unassessable.
- **Source:** `03` §Significance

### S02. Are the results impactful for the research community?
- **Pass if:** Yes
- **Rationale:** Community impact is a core significance criterion.
- **Source:** `03` §Significance

### S03. Will others build upon this work?
- **Pass if:** Yes
- **Rationale:** Follow-up potential is a primary significance signal.
- **Source:** `03` §Significance; `06` §8

### S04. Is there potential for real-world impact?
- **Pass if:** Yes
- **Rationale:** Real-world impact raises significance, where applicable.
- **Source:** `03` §Significance

### S05. Is the work connected to broader research themes?
- **Pass if:** Yes
- **Rationale:** Connecting to broader themes demonstrates reach beyond a narrow
  result.
- **Source:** `03` §Significance ("How to demonstrate")

### S06. Are potential applications discussed?
- **Pass if:** Yes
- **Rationale:** Concrete applications make significance tangible.
- **Source:** `03` §Significance

### S07. Is the evaluation on multiple benchmarks/settings (not narrow)?
- **Pass if:** Yes
- **Rationale:** Narrow evaluation limits the breadth of significance claims.
- **Source:** `03` §Significance concerns

### S08. Is a restricted setting explicitly acknowledged where applicable?
- **Pass if:** Yes
- **Rationale:** Claiming broad impact from a restricted setting without
  acknowledgment is overclaiming.
- **Source:** `03` §Significance concerns

### S09. Is the restricted setting still argued to be valuable?
- **Pass if:** Yes
- **Rationale:** A narrow scope is acceptable if its value is justified.
- **Source:** `03` §Significance concerns

### S10. Is there a meaningful comparison to existing approaches (not just raw numbers)?
- **Pass if:** Yes
- **Rationale:** Raw headline numbers without comparative insight carry little
  scientific value.
- **Source:** `03` §Significance; `04` §6.1

### S11. Are broader impacts / potential negative societal impacts discussed where appropriate?
- **Pass if:** Yes
- **Rationale:** Broader-impact discussion is part of responsible, significant
  work.
- **Source:** `01` §10; `06` §7

### S12. Is the work of interest beyond a single narrow sub-subfield?
- **Pass if:** Yes
- **Rationale:** Cross-subfield interest increases significance.
- **Source:** `03` §Significance

### S13. Does the paper address an important problem (not a toy problem dressed up)?
- **Pass if:** Yes
- **Rationale:** Inflating a toy problem's importance is a significance failure.
- **Source:** `03` §Significance

### S14. Are claimed benefits backed by evidence sufficient to motivate adoption?
- **Pass if:** Yes
- **Rationale:** Significance claims must be evidence-backed, not aspirational.
- **Source:** `03` §Significance; `04` §6.1

### S15. Is the contribution likely to be cited / extended (follow-up potential)?
- **Pass if:** Yes
- **Rationale:** Citation/extension is the long-run measure of significance.
- **Source:** `03` §Significance; `06` §8

### S16. Are limitations on impact (compute, data, scale requirements) disclosed?
- **Pass if:** Yes
- **Rationale:** Hidden adoption costs inflate perceived significance.
- **Source:** `01` §2

### S17. Are results robust enough to support the significance claims (multi-seed, multi-dataset)?
- **Pass if:** Yes
- **Rationale:** Single-run, single-dataset results cannot support broad impact.
- **Source:** `03` §Significance; `05`

### S18. For foundational research, is a direct path to a harmful application flagged?
- **Pass if:** Yes
- **Rationale:** Even foundational work must flag a direct path to harm (e.g.
  Deepfakes).
- **Source:** `01` §10

### S19. Are mitigations for identified risks proposed where applicable?
- **Pass if:** Yes
- **Rationale:** Mitigations (gated release, defenses) increase responsible
  significance.
- **Source:** `01` §10

### S20. Does the paper avoid overstating significance relative to evidence?
- **Pass if:** Yes
- **Rationale:** Overstated significance is a soundness/significance defect.
- **Source:** `01` §1

### S21. Is the work reproducible enough for others to build on it?
- **Pass if:** Yes
- **Rationale:** Irreproducible work cannot be extended, capping its
  significance.
- **Source:** `05`; `02` (Reproducibility Statement)

### S22. Does the paper discuss who benefits and who might be harmed?
- **Pass if:** Yes
- **Rationale:** Distributional impact is part of a complete significance
  assessment.
- **Source:** `01` §10
