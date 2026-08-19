# Aspect 16 — Transferability

**Dimension:** Can the work be adapted, extended, or applied beyond its
original setting? Is generality and extensibility by others demonstrated or
argued?

**Source basis:** `../rules/03-ml-reviewer-guidelines.md` §Significance,
§Significance concerns;
`../rules/04-troubling-trends-lipton-steinhardt.md` §6.1, §4.3;
`../rules/05-pineau-reproducibility-checklist.md`;
`../rules/01-neurips-paper-checklist.md` §4,5;
`../rules/06-ai-review-prompt.md` §8.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### TR01. Will others be able to build upon this work?
- **Pass if:** Yes
- **Rationale:** Follow-up potential is a primary significance signal.
- **Source:** `03` §Significance; `06` §8

### TR02. Is the work reproducible enough for others to extend it?
- **Pass if:** Yes
- **Rationale:** Irreproducible work cannot be extended, capping
  transferability.
- **Source:** `05`; `02`

### TR03. Is the method described generally (not overfit to one setting)?
- **Pass if:** Yes
- **Rationale:** Method overfit to one setting limits transfer.
- **Source:** `03` §Significance concerns

### TR04. Is performance reported across multiple datasets/settings?
- **Pass if:** Yes
- **Rationale:** Multi-setting evaluation is the evidence base for
  transferability.
- **Source:** `03` §Significance concerns

### TR05. Is the method's applicability to other domains discussed?
- **Pass if:** Yes
- **Rationale:** Discussing other domains demonstrates generality.
- **Source:** `03` §Significance ("applications")

### TR06. Is the method's generalization to out-of-distribution settings tested?
- **Pass if:** Yes
- **Rationale:** OOD generalization is the strongest transferability evidence.
- **Source:** `04` §4.3; `03` §Significance concerns

### TR07. Are the assumptions required for transfer stated?
- **Pass if:** Yes
- **Rationale:** Transfer depends on assumptions holding in new settings.
- **Source:** `01` §2,3; `04` §6.1

### TR08. Are the conditions under which the method might fail discussed?
- **Pass if:** Yes
- **Rationale:** "Under what circumstances won't it work?" is a core question.
- **Source:** `04` §8 (Cohen & Howe)

### TR09. Is the method's robustness to hyperparameters tested (sensitivity analysis)?
- **Pass if:** Yes
- **Rationale:** Hyperparameter robustness predicts transfer (tuning-free
  transfer).
- **Source:** `05` §19; `04` §6.1

### TR10. Is the method's robustness to dataset choice tested?
- **Pass if:** Yes
- **Rationale:** Robustness to dataset choice is a key transferability signal.
- **Source:** `04` §6.1; `03` §Significance concerns

### TR11. Is the method's complexity low enough for others to reimplement?
- **Pass if:** Yes
- **Rationale:** High implementation complexity raises the barrier to
  extension.
- **Source:** `05` §1; `03` §Clarity

### TR12. Are code and data released to enable extension?
- **Pass if:** Yes
- **Rationale:** Code/data release is the strongest enabler of transfer.
- **Source:** `01` §4,5; `05` §4

### TR13. Are baselines released such that others can build on them too?
- **Pass if:** Yes
- **Rationale:** Reproducible baselines enable comparative extension.
- **Source:** `05` §15–17

### TR14. Is the method's scope of applicability honestly bounded?
- **Pass if:** Yes
- **Rationale:** Unbounded transferability claims are overclaims.
- **Source:** `01` §2; `04` §4.3

### TR15. Are negative results (where the method fails to transfer) reported?
- **Pass if:** Yes
- **Rationale:** Failed transfer attempts are as informative as successful
  ones.
- **Source:** `05` §20; `04` §6.2

### TR16. Is the method connected to broader research themes (enabling cross-pollination)?
- **Pass if:** Yes
- **Rationale:** Broader connections increase the chance of transfer.
- **Source:** `03` §Significance ("connect to broader themes")

### TR17. Is the contribution framed as a building block others can compose?
- **Pass if:** Yes
- **Rationale:** Composable contributions invite follow-up work.
- **Source:** `03` §Significance; `06` §8

### TR18. Does the paper articulate what specifically is new vs reused (so others can extend the new part)?
- **Pass if:** Yes
- **Rationale:** Separating new from reused lets extenders target the right
  component.
- **Source:** `03` §Originality

### TR19. Is the method's compute requirement low enough for others to iterate?
- **Pass if:** Yes
- **Rationale:** High compute requirements cap who can extend the work.
- **Source:** `03` §Significance; `05` §13

### TR20. Are the components of the method modular (swappable for extension)?
- **Pass if:** Yes
- **Rationale:** Modularity lowers the barrier to extension.
- **Source:** `05` §1; `03` §Quality

### TR21. Is the method's transferability demonstrated rather than merely asserted?
- **Pass if:** Yes
- **Rationale:** Asserted transferability without evidence is an overclaim.
- **Source:** `01` §1; `03` §Significance

### TR22. Is the method's applicability to real-world deployment discussed?
- **Pass if:** Yes
- **Rationale:** Real-world deployment discussion grounds transferability.
- **Source:** `03` §Significance

### TR23. Is the method's performance under distribution shift characterized?
- **Pass if:** Yes
- **Rationale:** Distribution-shift performance predicts real-world transfer.
- **Source:** `04` §4.2, §4.3

### TR24. Does the paper identify open problems for follow-up work?
- **Pass if:** Yes
- **Rationale:** Flagging open problems invites directed extension.
- **Source:** `04` §6.1

### TR25. Are the method's dependencies (data, compute, libraries) realistic for others to obtain?
- **Pass if:** Yes
- **Rationale:** Unrealistic dependencies block transfer regardless of
  method quality.
- **Source:** `05` §3,4; `01` §5
