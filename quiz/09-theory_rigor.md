# Aspect 9 — Theory Rigor

**Dimension:** Are theoretical results stated with full assumptions, proven
correctly and completely, and used to genuinely support the claims (not as
mathiness)?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §3;
`../rules/04-troubling-trends-lipton-steinhardt.md` §3 (Mathiness);
`../rules/06-ai-review-prompt.md` §2 (Math & Notation);
`../rules/03-ml-reviewer-guidelines.md` §Quality.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Items are **N/A** for papers
with no theoretical results.

## Items

### T01. Are theoretical results included in the paper?
- **Pass if:** Yes
- **Rationale:** Establishes that the theory items are applicable; a "No" makes
  the rest N/A.
- **Source:** `01` §3

### T02. Is the full set of assumptions stated for every theorem?
- **Pass if:** Yes
- **Rationale:** Hidden assumptions make theorems unverifiable.
- **Source:** `01` §3; `06` §1

### T03. Are proofs complete (in main paper or appendix)?
- **Pass if:** Yes
- **Rationale:** Complete proofs are required for theoretical results.
- **Source:** `01` §3

### T04. If proofs are in the appendix, is a short proof sketch given in the main paper?
- **Pass if:** Yes
- **Rationale:** Sketches aid readability while the appendix carries the full
  proof.
- **Source:** `01` §3; `06` §2

### T05. Are informal proofs in the core paper complemented by formal proofs in the appendix?
- **Pass if:** Yes
- **Rationale:** Informal arguments must be backed by formal treatment.
- **Source:** `01` §3

### T06. Are all theorems and lemmas relied upon properly referenced?
- **Pass if:** Yes
- **Rationale:** Unattributed lemmas hide the proof's foundation.
- **Source:** `01` §3

### T07. Are proofs correct (no known errors)?
- **Pass if:** Yes
- **Rationale:** Incorrect proofs (e.g. the original Adam convergence proof)
  undermine the contribution.
- **Source:** `04` §3 (Adam example); `01` §3

### T08. Do the theorems' conclusions actually support the main claims?
- **Pass if:** Yes
- **Rationale:** A theorem whose conclusion does not back the claims is
  mathiness, not rigor.
- **Source:** `04` §3; `06` §1

### T09. Are theorems necessary, or are some spurious (inserted only to convey depth)?
- **Pass if:** Yes
- **Rationale:** "More equations tend to convince reviewers of depth" —
  spurious theorems are a flagged trend.
- **Source:** `04` §3; `06` §2

### T10. Are formal and informal claims clearly distinguished (no slippage)?
- **Pass if:** Yes
- **Rationale:** Blurring formal/informal conceals weaknesses in both.
- **Source:** `04` §3; `06` §2

### T11. Are claims that look formal but aren't (e.g. paraphrased results from other fields) clearly labeled?
- **Pass if:** Yes
- **Rationale:** Appearing formal without being formal misleads readers.
- **Source:** `04` §3

### T12. Is broad theory (e.g. no-free-lunch) invoked only where formally applicable?
- **Pass if:** Yes
- **Rationale:** Invoking NFL to justify heuristics without guarantees is a
  flagged misuse.
- **Source:** `04` §3

### T13. Is the theoretical setting (e.g. convex case) aligned with the empirical setting (e.g. non-convex)?
- **Pass if:** Yes
- **Rationale:** A convex theorem cited for non-convex experiments is a
  mismatch (Adam example).
- **Source:** `04` §3

### T14. Are assumptions realistic (not so strong as to be vacuous)?
- **Pass if:** Yes
- **Rationale:** Overly strong assumptions make theorems irrelevant to
  practice.
- **Source:** `01` §2 (limitations); `03` §Quality

### T15. Is the theoretical contribution genuinely new (not a re-derivation)?
- **Pass if:** Yes
- **Rationale:** Re-deriving known theory as novelty is mathiness-adjacent.
- **Source:** `04` §3

### T16. Is every symbol/variable in theorems and proofs defined?
- **Pass if:** Yes
- **Rationale:** Undefined variables make proofs impossible to verify.
- **Source:** `06` §2; `01` §3

### T17. Is notation consistent across the theory and the rest of the paper?
- **Pass if:** Yes
- **Rationale:** Inconsistent notation between theory and experiments signals
  carelessness.
- **Source:** `06` §2

### T18. Are theorem conditions checked/held in the experimental setup?
- **Pass if:** Yes
- **Rationale:** Theory that is never connected to the experiments is
  decorative.
- **Source:** `01` §3; `03` §Quality

### T19. Is the proof approach (e.g. novel technique) identified and motivated?
- **Pass if:** Yes
- **Rationale:** A bare proof without context undervalues the theoretical
  contribution.
- **Source:** `06` §2

### T20. Are converse results or tightness of bounds discussed where relevant?
- **Pass if:** Yes
- **Rationale:** Tightness/converse results show the theorem is not loose.
- **Source:** `03` §Quality

### T21. Does the paper avoid using math to obscure weak empirical claims?
- **Pass if:** Yes
- **Rationale:** Using equations to bolster weak prose is the core mathiness
  failure mode.
- **Source:** `04` §3

### T22. Could a reader rely on the explanation to make predictions or get a system to work?
- **Pass if:** Yes
- **Rationale:** The "writing test" — theorems included to please reviewers
  fail this.
- **Source:** `04` §6.1 (writing test)

### T23. Are the theoretical results clearly tied to the paper's contributions (not orphan theorems)?
- **Pass if:** Yes
- **Rationale:** Orphan theorems (stated but unused) suggest padding.
- **Source:** `04` §3; `06` §1

### T24. Are asymptotic / approximate results clearly labeled with the regime?
- **Pass if:** Yes
- **Rationale:** Asymptotic results mislabeled as exact mislead.
- **Source:** `01` §2 (limitations)
