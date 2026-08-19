# Aspect 13 — Claims Calibration

**Dimension:** Are claims honestly calibrated — matching evidence, scoped to
what was tested, and free of overclaiming — with limitations genuinely
discussed?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §1,2;
`../rules/03-ml-reviewer-guidelines.md` §ACL (Limitations), §Significance
concerns; `../rules/04-troubling-trends-lipton-steinhardt.md` §1, §4.1, §6.1;
`../rules/06-ai-review-prompt.md` §1.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### CC01. Do the main claims in abstract/intro accurately reflect contributions and scope?
- **Pass if:** Yes
- **Rationale:** Overstated claims relative to evidence is the canonical
  calibration failure.
- **Source:** `01` §1; `06` §1

### CC02. Are aspirational goals clearly distinguished from attained results?
- **Pass if:** Yes
- **Rationale:** Aspirational framing is fine as motivation but must not be
  presented as achieved.
- **Source:** `01` §1

### CC03. Are contributions clearly stated in the abstract and introduction?
- **Pass if:** Yes
- **Rationale:** Surfacing contributions up front lets reviewers credit and
  calibrate them.
- **Source:** `01` §1

### CC04. Are important assumptions and limitations stated alongside contributions?
- **Pass if:** Yes
- **Rationale:** Contributions and their caveats belong together.
- **Source:** `01` §1

### CC05. Is there a dedicated Limitations section?
- **Pass if:** Yes
- **Rationale:** A separate Limitations section is encouraged (and required at
  ACL).
- **Source:** `01` §2; `03` §ACL

### CC06. Are strong assumptions and robustness-to-violations discussed?
- **Pass if:** Yes
- **Rationale:** Reviewers want to know how results degrade if assumptions
  break.
- **Source:** `01` §2

### CC07. Is the scope of claims reflected (e.g. tested on only a few datasets/runs)?
- **Pass if:** Yes
- **Rationale:** Overclaiming scope is a calibration defect.
- **Source:** `01` §2

### CC08. Are implicit empirical assumptions articulated?
- **Pass if:** Yes
- **Rationale:** Hidden empirical assumptions can invalidate conclusions.
- **Source:** `01` §2

### CC09. Are factors influencing performance discussed?
- **Pass if:** Yes
- **Rationale:** Discussing performance factors (e.g. resolution, jargon) is
  expected.
- **Source:** `01` §2

### CC10. Do the stated limitations undermine the core claims?
- **Pass if:** No
- **Rationale:** If acknowledged limitations invalidate the claims, the claims
  are too strong.
- **Source:** `03` §ACL

### CC11. Is the Limitations section honest and comprehensive (not a token gesture)?
- **Pass if:** Yes
- **Rationale:** Token limitations sections are flagged by reviewers.
- **Source:** `03` §ACL

### CC12. Are potential negative impacts addressed in limitations/ethics?
- **Pass if:** Yes
- **Rationale:** Negative impacts belong in limitations or a dedicated section.
- **Source:** `03` §ACL

### CC13. Are "human-level" / "state-of-the-art" claims restricted to a specific task/dataset?
- **Pass if:** Yes
- **Rationale:** Unqualified "human-level" claims portray false capabilities.
- **Source:** `04` §4.1

### CC14. Are generalization claims restricted to the tested distribution?
- **Pass if:** Yes
- **Rationale:** Conflating train→test with population→population overstates
  capability.
- **Source:** `04` §4.3

### CC15. Are "first to" assertions verified (not unverified novelty claims)?
- **Pass if:** Yes
- **Rationale:** "First to X" claims without verification are misleading.
- **Source:** `04` §4

### CC16. Is the breadth of claims matched by the breadth of evaluation?
- **Pass if:** Yes
- **Rationale:** Broad claims on narrow evaluation is a calibration/soundness
  mismatch.
- **Source:** `03` §Significance concerns

### CC17. Are headline numbers contextualized (insight into "what/why", not just "how well")?
- **Pass if:** Yes
- **Rationale:** Raw numbers without insight are low scientific value.
- **Source:** `04` §6.1

### CC18. Are negative results (settings where the method underperforms) reported, not hidden?
- **Pass if:** Yes
- **Rationale:** Hiding negative results misrepresents the method's scope.
- **Source:** `05` §20; `04` §6.2

### CC19. Are speculative explanations clearly labeled as speculation (not explanation)?
- **Pass if:** Yes
- **Rationale:** Disguising speculation as explanation is troubling trend #1.
- **Source:** `04` §1

### CC20. Do speculative discussions reside in a quarantined section?
- **Pass if:** Yes
- **Rationale:** Quarantining speculation prevents it being cited as fact.
- **Source:** `04` §1 (Dropout positive example)

### CC21. Is the paper clear about which problems are open vs solved?
- **Pass if:** Yes
- **Rationale:** Mislabeling solved problems as open misleads follow-up work.
- **Source:** `04` §6.1

### CC22. Are claims of improvement accompanied by significance evidence?
- **Pass if:** Yes
- **Rationale:** Claiming wins within noise is a calibration failure.
- **Source:** `05` §12; `01` §7

### CC23. Does the paper avoid overstating significance relative to evidence?
- **Pass if:** Yes
- **Rationale:** Overstated significance is a calibration defect.
- **Source:** `01` §1

### CC24. Are limitations on impact (compute, data, scale requirements) disclosed?
- **Pass if:** Yes
- **Rationale:** Hidden adoption costs inflate perceived significance.
- **Source:** `01` §2

### CC25. Does the paper avoid complacency (strong results excusing weak arguments)?
- **Pass if:** Yes
- **Rationale:** "Strong results excuse weak arguments" is a flagged
  complacency trend.
- **Source:** `04` §5.1

### CC26. Are performance claims tied to specific metrics, datasets, and settings?
- **Pass if:** Yes
- **Rationale:** Untethered performance claims are uncalibrated.
- **Source:** `01` §1; `03` §Significance

### CC27. Does the paper acknowledge where results might not generalize?
- **Pass if:** Yes
- **Rationale:** Silence on generalization limits is an overclaim risk.
- **Source:** `04` §4.3; `01` §2
