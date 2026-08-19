# Aspect 10 — Related Work & Positioning

**Dimension:** Is the related-work coverage adequate, recent, and honest, with
the paper clearly positioned against the closest prior work?

**Source basis:** `../rules/03-ml-reviewer-guidelines.md` §Originality, Novelty
concerns; `../rules/04-troubling-trends-lipton-steinhardt.md` §2, §6.2;
`../rules/01-neurips-paper-checklist.md` §12 (Licenses / attribution);
`../rules/06-ai-review-prompt.md` §8.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### RW01. Is there a dedicated Related Work section?
- **Pass if:** Yes
- **Rationale:** A clearly delineated section lets reviewers find positioning
  fast.
- **Source:** `03` §Originality; `06` §8

### RW02. Is the related-work coverage adequate (not superficial)?
- **Pass if:** Yes
- **Rationale:** Thin related work suggests uncalibrated novelty.
- **Source:** `03` §Novelty concerns

### RW03. Is the closest prior work explicitly compared (not just generic citations)?
- **Pass if:** Yes
- **Rationale:** "Similar to [paper X]" concerns require direct comparison to
  X.
- **Source:** `03` §Novelty concerns

### RW04. Is the paper positioned against the single most similar prior work?
- **Pass if:** Yes
- **Rationale:** Positioning against the closest work is the key novelty
  question.
- **Source:** `03` §Originality; `04`

### RW05. Are recent (last ~2 years) works cited?
- **Pass if:** Yes
- **Rationale:** Ignoring recent work suggests the novelty claim is
  uncalibrated.
- **Source:** `03` §Novelty concerns

### RW06. Are concurrent works acknowledged?
- **Pass if:** Yes
- **Rationale:** Unacknowledged concurrent work can look like appropriation.
- **Source:** `03` §Originality

### RW07. Are seminal / foundational works cited (not only recent)?
- **Pass if:** Yes
- **Rationale:** Citing only recent work can obscure the lineage of ideas.
- **Source:** `04` §2 (Melis et al. revisiting old baselines)

### RW08. Is the delta over prior work explicitly stated (what is new)?
- **Pass if:** Yes
- **Rationale:** Surfacing the delta lets reviewers assess the true
  contribution.
- **Source:** `03` §Originality; `04`

### RW09. Is the delta over prior work demonstrated, not merely asserted?
- **Pass if:** Yes
- **Rationale:** Asserted deltas without evidence are unconvincing.
- **Source:** `03` §Novelty concerns

### RW10. Are baselines traced to their original sources (cited, not anonymous)?
- **Pass if:** Yes
- **Rationale:** Baselines presented without citation obscure provenance.
- **Source:** `01` §12; `05` §17

### RW11. Are reused assets (code/data/models) cited with version and license?
- **Pass if:** Yes
- **Rationale:** License and version citation is required for reused assets.
- **Source:** `01` §12

### RW12. Is the prior work described accurately (not strawmanned)?
- **Pass if:** Yes
- **Rationale:** Misrepresenting prior work to look better is a serious
  defect.
- **Source:** `04` §6.2 (critical writing); `03` §Originality

### RW13. Is credit attributed honestly (no appropriation of ideas without citation)?
- **Pass if:** Yes
- **Rationale:** Uncited reuse of others' ideas is a research-integrity
  violation.
- **Source:** `01` §9,12; `04`

### RW14. Is the paper placed in the context of broader research themes?
- **Pass if:** Yes
- **Rationale:** Broader positioning increases significance and readability.
- **Source:** `03` §Significance ("connect to broader themes")

### RW15. Does the paper discuss the lineage / evolution of the approach?
- **Pass if:** Yes
- **Rationale:** Lineage helps readers understand what is reused vs new.
- **Source:** `03` §Originality; `04`

### RW16. Are competing approaches fairly represented (not cherry-picked)?
- **Pass if:** Yes
- **Rationale:** Cherry-picking competitors misrepresents the field.
- **Source:** `04` §2, §6.2

### RW17. Does the paper avoid citing the reviewer's own work disproportionately?
- **Pass if:** Yes
- **Rationale:** Reviewers are told not to reject for missing self-citations,
  but disproportionate self-citation signals insularity.
- **Source:** `03` §NeurIPS ("What Reviewers Should Avoid")

### RW18. Are open problems / unsolved questions correctly identified?
- **Pass if:** Yes
- **Rationale:** Mislabeling solved problems as open (or vice versa) misleads.
- **Source:** `04` §6.1 ("clear about which problems are open vs solved")

### RW19. Does the paper cite the original sources of reused techniques (e.g. baselines from prior work)?
- **Pass if:** Yes
- **Rationale:** Citing a technique's second-hand user instead of its creator
  misattributes credit.
- **Source:** `01` §12; `05` §17

### RW20. Is the related work organized thematically (not a chronological list)?
- **Pass if:** Yes
- **Rationale:** Thematic organization aids readability and positioning.
- **Source:** `03` §Clarity

### RW21. Does the paper explain how it improves on each closely related work?
- **Pass if:** Yes
- **Rationale:** Listing related work without contrast leaves the delta
  implicit.
- **Source:** `03` §Novelty concerns; `04`

### RW22. Are arXiv preprints cited appropriately (with version caution)?
- **Pass if:** Yes
- **Rationale:** arXiv self-citations must not break anonymity; versions can
  drift.
- **Source:** `02` (arXiv self-citations FAQ)

### RW23. Does the paper acknowledge prior negative results it builds on?
- **Pass if:** Yes
- **Rationale:** Building on negative results without acknowledgment hides
  intellectual debt.
- **Source:** `04` §6.2

### RW24. Is the positioning consistent with the actual contribution (no overclaiming novelty)?
- **Pass if:** Yes
- **Rationale:** Overclaiming novelty beyond what the related-work comparison
  supports is a defect.
- **Source:** `01` §1; `03` §Originality
