# Aspect 1 — Readability (Clarity / Writing & Organization)

**Dimension:** Clarity — is the paper clearly written, well organized, and
self-contained?

**Source basis:** `../rules/03-ml-reviewer-guidelines.md` §Clarity;
`../rules/04-troubling-trends-lipton-steinhardt.md` §3 (Mathiness), §4 (Misuse
of Language); `../rules/06-ai-review-prompt.md` §2 (Math & Notation), §4
(Visuals & Captions); `../rules/01-neurips-paper-checklist.md` §1,3.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

## Items

### R01. Are all key terms defined at first use?
- **Pass if:** Yes
- **Rationale:** Undefined terms force the reader to guess meaning; first-use
  definition is the baseline of clarity.
- **Source:** `03` §Clarity; `06` §2

### R02. Is mathematical notation consistent throughout the paper?
- **Pass if:** Yes
- **Rationale:** Inconsistent notation (same symbol for different objects, etc.)
  is a top reviewer clarity complaint.
- **Source:** `03` §Clarity; `06` §2

### R03. Is there a notation table or symbol glossary (or could one be built trivially)?
- **Pass if:** Yes
- **Rationale:** A glossary lets readers resolve symbols without searching;
  standard in strong papers with heavy notation.
- **Source:** `06` §2; `03` §Clarity ("create notation table")

### R04. Is every variable in every equation explicitly defined?
- **Pass if:** Yes
- **Rationale:** Undefined variables are a common and fatal clarity defect.
- **Source:** `06` §2; `01` §3

### R05. Are figures and tables self-contained (interpretable from the caption alone)?
- **Pass if:** Yes
- **Rationale:** Reviewers skim captions; a figure that needs the main text to
  parse fails its job.
- **Source:** `06` §4; `03` §Clarity concerns

### R06. Are all axes labeled, with units where applicable?
- **Pass if:** Yes
- **Rationale:** Axis labels and units are the minimum for a plot to be
  interpretable.
- **Source:** `06` §4

### R07. Are legends complete and unambiguous?
- **Pass if:** Yes
- **Rationale:** Missing or cryptic legends make multi-series plots unreadable.
- **Source:** `06` §4

### R08. Is the paper well organized with clear section signposting?
- **Pass if:** Yes
- **Rationale:** Organization and signposting let readers navigate efficiently;
  a frequent "hard to follow" cause.
- **Source:** `03` §Clarity concerns; `06` §4

### R09. Is the writing clear to a non-expert in this specific subfield?
- **Pass if:** Yes
- **Rationale:** Conference reviewers may be adjacent-field experts; clarity
  beyond the narrow subfield widens impact.
- **Source:** `06` §4; `03` §Clarity

### R10. Is the paper self-contained (core content understandable without external docs)?
- **Pass if:** Yes
- **Rationale:** Self-containedness is an explicit reviewer criterion; reliance
  on undisclosed external material fails it.
- **Source:** `03` §Clarity

### R11. Are technical terms used with their precise technical meaning?
- **Pass if:** Yes
- **Rationale:** Imprecise use of terms of art (e.g. "deconvolution",
  "generative model", "covariate shift") is a flagged troubling trend.
- **Source:** `04` §4.2; `06` §3

### R12. Are overloaded terms (e.g. "deconvolution", "generative model", "covariate shift") clarified or avoided?
- **Pass if:** Yes
- **Rationale:** Overloaded terminology causes persistent community confusion.
- **Source:** `04` §4.2

### R13. Are anthropomorphic / suggestive terms ("curiosity", "fear", "thought vectors", "human-level") properly qualified or avoided?
- **Pass if:** Yes
- **Rationale:** Suggestive definitions sneak in unearned connotations and can
  mislead readers and the public.
- **Source:** `04` §4.1; `06` §3

### R14. Are "suitcase words" ("interpretability", "generalization", "bias") unpacked with a concrete definition?
- **Pass if:** Yes
- **Rationale:** Suitcase words pack disjoint meanings; papers using them
  without definition talk past each other.
- **Source:** `04` §4.3; `06` §3

### R15. Are theorems necessary rather than spurious (inserted only to convey depth)?
- **Pass if:** Yes
- **Rationale:** "Mathiness" — using equations to impress rather than clarify —
  is an explicit rejection trap.
- **Source:** `04` §3; `06` §2

### R16. Are formal and informal claims clearly distinguished (no slippage between math and prose)?
- **Pass if:** Yes
- **Rationale:** Blurring formal/informal claims conceals weaknesses in both.
- **Source:** `04` §3; `06` §2

### R17. Are informal proof sketches in the main paper complemented by formal proofs in the appendix?
- **Pass if:** Yes
- **Rationale:** Sketches are welcome for readability but must be backed by
  complete proofs.
- **Source:** `01` §3; `06` §2

### R18. Is speculation clearly labeled as such, rather than presented as explanation?
- **Pass if:** Yes
- **Rationale:** Disguising speculation as explanation is the first troubling
  trend (e.g. "internal covariate shift").
- **Source:** `04` §1; `06` §3

### R19. Do speculative/intuitive discussions reside in a clearly quarantined section (e.g. "Motivation")?
- **Pass if:** Yes
- **Rationale:** Quarantining speculation (as the Dropout paper does) prevents it
  being cited as fact.
- **Source:** `04` §1 (Dropout positive example)

### R20. Is the abstract informative and accurate (not a placeholder)?
- **Pass if:** Yes
- **Rationale:** Placeholder/duplicate abstracts are removed at submission; the
  abstract drives reviewer bidding.
- **Source:** `02` §Submission Timeline; `01` §1

### R21. Are cross-references (sections, figures, tables, equations) consistent and correct?
- **Pass if:** Yes
- **Rationale:** Broken references interrupt reading and signal a rushed
  submission.
- **Source:** `06` §4; `03` §Clarity

### R22. Are "human-level" / "state-of-the-art" claims restricted to a specific task or dataset?
- **Pass if:** Yes
- **Rationale:** Unqualified "human-level" claims portray false capabilities.
- **Source:** `04` §4.1

### R23. Are captions readable without referring back to the main text?
- **Pass if:** Yes
- **Rationale:** Captions are skimmed in isolation; they must stand alone.
- **Source:** `06` §4

### R24. Is each claim traceable to supporting evidence (a theorem, experiment, or citation)?
- **Pass if:** Yes
- **Rationale:** Unsupported claims are an explicit technical-soundness and
  clarity defect.
- **Source:** `01` §1; `06` §2

### R25. Is the grammar/typo level acceptable (no pervasive errors impeding understanding)?
- **Pass if:** Yes
- **Rationale:** Pervasive errors erode credibility and slow reading.
- **Source:** `03` §Clarity

### R26. Are length/page limits respected, with appendices used for overflow detail?
- **Pass if:** Yes
- **Rationale:** Over-limit submissions risk desk rejection; overflow belongs in
  appendices.
- **Source:** `02` §Camera-Ready / FAQ

### R27. Are abbreviations and acronyms expanded at first use?
- **Pass if:** Yes
- **Rationale:** Unexpanded acronyms are a trivial but common clarity defect.
- **Source:** `03` §Clarity

### R28. Are there signs of copy-editing / a non-author read (or equivalent proxy)?
- **Pass if:** Yes
- **Rationale:** "Have non-authors read before submission" is explicit guidance;
  unedited drafts are visibly rougher.
- **Source:** `03` §Clarity ("How to ensure clarity")
