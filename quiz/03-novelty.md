# Aspect 3 — Novelty (Originality)

**Dimension:** Does the paper provide new insights? Is the contribution
non-trivial and clearly distinguished from prior work?

**Source basis:** `../rules/03-ml-reviewer-guidelines.md` §Originality;
`../rules/04-troubling-trends-lipton-steinhardt.md` §2, §6.1;
`../rules/06-ai-review-prompt.md` §8; `../rules/01-neurips-paper-checklist.md`
§1,4.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### N01. Does the paper provide new insights (not necessarily a new method)?
- **Pass if:** Yes
- **Rationale:** Originality can come from novel insights about existing
  methods, not only new methods.
- **Source:** `03` §Originality (NeurIPS insight); `06` §8

### N02. Is the contribution non-trivial (not a straightforward extension)?
- **Pass if:** Yes
- **Rationale:** Trivial/incremental contributions are a standard reject reason.
- **Source:** `03` §Originality

### N03. Is what is new clearly articulated relative to prior work?
- **Pass if:** Yes
- **Rationale:** "Incremental contribution" concerns arise when the delta is
  unclear.
- **Source:** `03` §Originality, Novelty concerns; `04`

### N04. Is the closest prior work explicitly compared (not just generic Related Work)?
- **Pass if:** Yes
- **Rationale:** "Similar to [paper X]" concerns require explicit comparison to
  X.
- **Source:** `03` §Novelty concerns

### N05. If the contribution is evaluating existing approaches, does it yield novel insights?
- **Pass if:** Yes
- **Rationale:** Evaluation papers can be highly original if they reveal
  non-obvious findings.
- **Source:** `03` §Originality (NeurIPS insight)

### N06. Is the problem framing genuinely novel (or is it a known problem with a known solution re-applied)?
- **Pass if:** Yes
- **Rationale:** Re-applying existing methods to new tasks is fine, but the
  novelty must be honestly located.
- **Source:** `04` §2

### N07. If gains come from hyperparameter tuning rather than the proposed method, is that honestly characterized?
- **Pass if:** Yes
- **Rationale:** Misattributing tuning gains to architectural novelty is a
  canonical troubling trend (Melis et al.).
- **Source:** `04` §2

### N08. Is the contribution distinguished from incremental architectural tweaks?
- **Pass if:** Yes
- **Rationale:** Emphasizing complex models when gains stem from elsewhere
  misleads.
- **Source:** `04` §2

### N09. Are proposed changes shown to be necessary (via ablation), not merely sufficient?
- **Pass if:** Yes
- **Rationale:** Without ablations, all proposed changes appear necessary when
  some may be redundant.
- **Source:** `04` §2

### N10. Is the novelty claim grounded in a clear delta over the closest prior work?
- **Pass if:** Yes
- **Rationale:** Novelty must be positioned relative to a concrete baseline,
  not in a vacuum.
- **Source:** `03` §Originality; `04`

### N11. Does the paper avoid presenting known results as novel?
- **Pass if:** Yes
- **Rationale:** Presenting well-known results as new is a strong-reject signal
  (NeurIPS score 1).
- **Source:** `03` §Scoring (Strong Reject)

### N12. Is the methodological contribution (algorithm/architecture/model) clearly described as new vs reused?
- **Pass if:** Yes
- **Rationale:** Blurring new and reused components inflates apparent novelty.
- **Source:** `01` §4

### N13. Is the theoretical contribution (if any) genuinely new (not a re-derivation)?
- **Pass if:** Yes
- **Rationale:** Re-deriving known theory as novelty is mathiness-adjacent.
- **Source:** `04` §3

### N14. Is the empirical contribution (if any) more than a leaderboard climb (includes analysis)?
- **Pass if:** Yes
- **Rationale:** Pure leaderboard gains without insight are low novelty.
- **Source:** `04` §6.1

### N15. Does the paper cite and position itself against recent (last ~2 years) prior work?
- **Pass if:** Yes
- **Rationale:** Ignoring recent prior work suggests the novelty claim is
  uncalibrated.
- **Source:** `03` §Novelty concerns

### N16. Are concurrent works acknowledged?
- **Pass if:** Yes
- **Rationale:** Unacknowledged concurrent work can look like appropriation.
- **Source:** `03` §Originality

### N17. Is the contribution clearly stated in the abstract and introduction?
- **Pass if:** Yes
- **Rationale:** Novelty that is not surfaced up front is hard for reviewers to
  credit.
- **Source:** `01` §1

### N18. Is the originality honest (no appropriation of prior ideas without citation)?
- **Pass if:** Yes
- **Rationale:** Uncited reuse of others' ideas is an ethics/research-integrity
  violation.
- **Source:** `01` §9,12; `04`

### N19. If applying existing methods to new tasks, is the novelty located in the scientific finding?
- **Pass if:** Yes
- **Rationale:** Application alone is weak novelty; the finding must be the
  contribution.
- **Source:** `04` §2

### N20. Does the paper articulate what specifically is new vs what is reused?
- **Pass if:** Yes
- **Rationale:** Separating new from reused lets reviewers assess the true
  contribution.
- **Source:** `03` §Originality

### N21. Is the claimed novelty proportional to the demonstrated evidence (no overclaiming)?
- **Pass if:** Yes
- **Rationale:** Overclaiming novelty beyond evidence is a soundness defect.
- **Source:** `01` §1

### N22. Does the work open new research directions (will others build on it)?
- **Pass if:** Yes
- **Rationale:** Follow-up potential is a marker of originality and
  significance.
- **Source:** `03` §Originality; `06` §8

### N23. Are novelty claims free of unverified "first to" assertions?
- **Pass if:** Yes
- **Rationale:** "First to X" claims without verification are misleading.
- **Source:** `04` §4

### N24. If the contribution is a negative result or analysis, is its originality as a finding clear?
- **Pass if:** Yes
- **Rationale:** Negative/analytical results can be original if framed as a
  finding, not a failure.
- **Source:** `04` §6.1
