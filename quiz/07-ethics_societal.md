# Aspect 7 — Ethics & Societal Impact

**Dimension:** Does the paper conform to the Code of Ethics, disclose societal
impacts, handle dual-use and human-subjects concerns, and respect asset
licenses?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §9–16;
`../rules/02-iclr-author-guide.md` (Ethics Statement);
`../rules/06-ai-review-prompt.md` §7;
`../rules/04-troubling-trends-lipton-steinhardt.md` §4.1, §5.3.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Many items are **N/A** (e.g. no
human subjects, no released assets) — exclude them from the denominator.

## Items

### X01. Is conformity to the conference Code of Ethics acknowledged?
- **Pass if:** Yes
- **Rationale:** Acknowledging the Code of Ethics is a submission requirement.
- **Source:** `01` §9; `02` (Code of Ethics)

### X02. Are potential negative societal impacts discussed where appropriate?
- **Pass if:** Yes
- **Rationale:** Broader-impact discussion is required where applicable.
- **Source:** `01` §10; `06` §7

### X03. Are harms from intended, correct use considered?
- **Pass if:** Yes
- **Rationale:** Harms under normal operation are a core impact dimension.
- **Source:** `01` §10

### X04. Are harms from intended use with incorrect results considered?
- **Pass if:** Yes
- **Rationale:** Faulty outputs can cause distinct harms.
- **Source:** `01` §10

### X05. Are harms from (intentional or unintentional) misuse considered?
- **Pass if:** Yes
- **Rationale:** Misuse potential must be assessed.
- **Source:** `01` §10

### X06. For foundational research with a direct path to a harmful application, is it flagged?
- **Pass if:** Yes
- **Rationale:** Even foundational work must flag a direct path to harm.
- **Source:** `01` §10

### X07. Are mitigation strategies proposed (gated release, defenses, monitoring)?
- **Pass if:** Yes
- **Rationale:** Mitigations are encouraged where risks exist.
- **Source:** `01` §10

### X08. For high-risk dual-use released models, are safeguards described?
- **Pass if:** Yes
- **Rationale:** Dual-use models need safeguards for controlled use.
- **Source:** `01` §11; `06` §7

### X09. For web-scraped datasets, is unsafe-content filtering described?
- **Pass if:** Yes
- **Rationale:** Scraped data poses safety risks that must be addressed.
- **Source:** `01` §11

### X10. Are licenses of all used assets (code, data, models) cited and respected?
- **Pass if:** Yes
- **Rationale:** License compliance is mandatory.
- **Source:** `01` §12; `06` §7

### X11. Are asset versions stated?
- **Pass if:** Yes
- **Rationale:** Version pinning aids reproducibility and license tracking.
- **Source:** `01` §12

### X12. For released new assets, are license, copyright, and terms of use included?
- **Pass if:** Yes
- **Rationale:** Released assets must carry their licensing terms.
- **Source:** `01` §13

### X13. Are new assets documented via structured templates (training, license, limitations)?
- **Pass if:** Yes
- **Rationale:** Structured templates communicate asset details responsibly.
- **Source:** `01` §13

### X14. For crowdsourcing/human subjects, are full instructions and screenshots provided?
- **Pass if:** Yes
- **Rationale:** Instruction transparency is required for human-subjects work.
- **Source:** `01` §14

### X15. Is compensation for human workers (≥ minimum wage) described?
- **Pass if:** Yes
- **Rationale:** Per the Code of Ethics, workers must be paid at least minimum
  wage.
- **Source:** `01` §14

### X16. Is IRB approval (or equivalent) obtained and stated where applicable?
- **Pass if:** Yes
- **Rationale:** IRB approval may be required for human-subjects research.
- **Source:** `01` §15; `06` §7

### X17. Is LLM usage in the core methodology declared (if non-standard/important)?
- **Pass if:** Yes
- **Rationale:** Non-standard LLM use in core methods must be declared; writing
  assistance need not be.
- **Source:** `01` §16; `06` §7

### X18. Is an ethics statement included where ethics concerns exist?
- **Pass if:** Yes
- **Rationale:** ICLR asks for an ethics statement when concerns exist.
- **Source:** `02` (Ethics Statement)

### X19. Are bias / fairness implications addressed where relevant?
- **Pass if:** Yes
- **Rationale:** Bias and fairness are core ethics concerns for deployed ML.
- **Source:** `02`; `04` §4.1 (fairness terminology)

### X20. Are privacy and security implications addressed where relevant?
- **Pass if:** Yes
- **Rationale:** Privacy and security are listed ethics-statement topics.
- **Source:** `02`; `01` §10

### X21. Is consent (for data from people) described?
- **Pass if:** Yes
- **Rationale:** Consent procedures are required for human-derived data.
- **Source:** `01` §13; `05` §7

### X22. Are dual-use concerns addressed for models with misuse potential?
- **Pass if:** Yes
- **Rationale:** Dual-use release requires explicit safeguards discussion.
- **Source:** `01` §11; `02`

### X23. Does the paper avoid anthropomorphic overclaims that could mislead the public about capabilities?
- **Pass if:** Yes
- **Rationale:** Press and investors amplify anthropomorphic claims, causing
  real harm.
- **Source:** `04` §4.1, §5.3
