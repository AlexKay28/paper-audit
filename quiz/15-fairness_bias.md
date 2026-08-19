# Aspect 15 — Fairness & Bias

**Dimension:** Are fairness, bias, and disparate-impact concerns addressed,
with terminology used precisely and mitigations proposed where relevant?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §10,11,13;
`../rules/02-iclr-author-guide.md` (Ethics Statement);
`../rules/06-ai-review-prompt.md` §7;
`../rules/04-troubling-trends-lipton-steinhardt.md` §4.1, §4.3.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Many items are **N/A** for
papers with no deployed/human-impact angle.

## Items

### FB01. Are bias / fairness implications addressed where relevant?
- **Pass if:** Yes
- **Rationale:** Bias and fairness are core ethics concerns for deployed ML.
- **Source:** `02`; `04` §4.1

### FB02. Are groups potentially affected by the system identified?
- **Pass if:** Yes
- **Rationale:** Identifying affected groups grounds a concrete fairness
  analysis.
- **Source:** `01` §10; `02`

### FB03. Is disparate impact on subgroups measured or discussed?
- **Pass if:** Yes
- **Rationale:** Disparate impact is the core fairness question.
- **Source:** `04` §4.1; `01` §10

### FB04. Is dataset bias (historical, selection, representation) discussed?
- **Pass if:** Yes
- **Rationale:** Unexamined dataset bias invalidates downstream fairness
  claims.
- **Source:** `05` §7; `04` §4.1

### FB05. Are known biases in the data documented (for new datasets)?
- **Pass if:** Yes
- **Rationale:** Documenting known biases is required for responsible release.
- **Source:** `05` §7

### FB06. Is fairness terminology used precisely (not overloaded)?
- **Pass if:** Yes
- **Rationale:** Overloading "fairness", "opportunity", "discrimination"
  confuses readers and policymakers.
- **Source:** `04` §4.1

### FB07. Is "bias" unpacked with a concrete definition (not a suitcase word)?
- **Pass if:** Yes
- **Rationale:** "Bias" is a suitcase word; using it without definition is
  imprecise.
- **Source:** `04` §4.3

### FB08. Are fairness metrics defined and their assumptions stated?
- **Pass if:** Yes
- **Rationale:** Fairness metrics embed value judgments; assumptions must be
  explicit.
- **Source:** `04` §4.1

### FB09. Are trade-offs between fairness metrics acknowledged (e.g. impossibility results)?
- **Pass if:** Yes
- **Rationale:** Fairness metrics conflict; ignoring trade-offs oversimplifies.
- **Source:** `04` §4.1

### FB10. Are mitigations proposed for identified biases?
- **Pass if:** Yes
- **Rationale:** Mitigations are encouraged where biases exist.
- **Source:** `01` §10,11

### FB11. Are dual-use concerns addressed for models with misuse potential?
- **Pass if:** Yes
- **Rationale:** Dual-use release requires explicit safeguards discussion.
- **Source:** `01` §11; `02`

### FB12. For high-risk released models, are safeguards described?
- **Pass if:** Yes
- **Rationale:** Dual-use models need safeguards for controlled use.
- **Source:** `01` §11; `06` §7

### FB13. Are privacy and security implications addressed where relevant?
- **Pass if:** Yes
- **Rationale:** Privacy and security are listed ethics-statement topics.
- **Source:** `02`; `01` §10

### FB14. Is consent (for data from people) described?
- **Pass if:** Yes
- **Rationale:** Consent procedures are required for human-derived data.
- **Source:** `01` §13; `05` §7

### FB15. Are harms from intended, correct use considered?
- **Pass if:** Yes
- **Rationale:** Harms under normal operation are a core impact dimension.
- **Source:** `01` §10

### FB16. Are harms from intended use with incorrect results considered?
- **Pass if:** Yes
- **Rationale:** Faulty outputs can cause distinct harms, especially for
  vulnerable groups.
- **Source:** `01` §10

### FB17. Are harms from (intentional or unintentional) misuse considered?
- **Pass if:** Yes
- **Rationale:** Misuse potential must be assessed.
- **Source:** `01` §10

### FB18. Is a direct path to a harmful application flagged (even for foundational research)?
- **Pass if:** Yes
- **Rationale:** Even foundational work must flag a direct path to harm.
- **Source:** `01` §10

### FB19. Are mitigation strategies proposed (gated release, defenses, monitoring)?
- **Pass if:** Yes
- **Rationale:** Mitigations increase responsible significance where risks
  exist.
- **Source:** `01` §10

### FB20. Does the paper avoid anthropomorphic overclaims that could mislead about capabilities?
- **Pass if:** Yes
- **Rationale:** Anthropomorphic overclaims can cause real-world harm via
  misperception.
- **Source:** `04` §4.1, §5.3

### FB21. Is the demographic representativeness of data discussed where relevant?
- **Pass if:** Yes
- **Rationale:** Demographic gaps in data cause disparate impact.
- **Source:** `05` §7; `01` §10

### FB22. Are fairness evaluations conducted on relevant subgroups (where applicable)?
- **Pass if:** Yes
- **Rationale:** Subgroup evaluation is the evidence base for fairness claims.
- **Source:** `01` §10; `04` §4.1

### FB23. Is the deployment context's effect on bias discussed?
- **Pass if:** Yes
- **Rationale:** Bias depends on deployment context; abstract fairness claims
  are fragile.
- **Source:** `01` §10; `02`

### FB24. Are limitations of fairness metrics acknowledged (no single metric suffices)?
- **Pass if:** Yes
- **Rationale:** No single fairness metric is sufficient; claiming otherwise
  is a calibration failure.
- **Source:** `04` §4.1, §4.3

### FB25. Is fairness framed as a socio-technical (not purely technical) problem where relevant?
- **Pass if:** Yes
- **Rationale:** Reducing fairness to a single equation misinforms
  policymakers.
- **Source:** `04` §4.1
