# Aspect 12 — Visuals & Design

**Dimension:** Are figures and tables well-designed, self-contained, and
correctly integrated, with clear axes, legends, and captions?

**Source basis:** `../rules/06-ai-review-prompt.md` §4 (Visuals & Captions);
`../rules/03-ml-reviewer-guidelines.md` §Clarity concerns;
`../rules/01-neurips-paper-checklist.md` (general presentation).

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Items are **N/A** for papers
with no figures/tables.

## Items

### V01. Are figures and tables self-contained (interpretable from the caption alone)?
- **Pass if:** Yes
- **Rationale:** Reviewers skim captions; a figure that needs the main text
  fails its job.
- **Source:** `06` §4; `03` §Clarity concerns

### V02. Are all axes labeled, with units where applicable?
- **Pass if:** Yes
- **Rationale:** Axis labels and units are the minimum for a plot to be
  interpretable.
- **Source:** `06` §4

### V03. Are legends complete and unambiguous?
- **Pass if:** Yes
- **Rationale:** Missing or cryptic legends make multi-series plots unreadable.
- **Source:** `06` §4

### V04. Are captions readable without referring back to the main text?
- **Pass if:** Yes
- **Rationale:** Captions are skimmed in isolation; they must stand alone.
- **Source:** `06` §4

### V05. Are figure/table numbers referenced correctly in the text?
- **Pass if:** Yes
- **Rationale:** Broken references interrupt reading and signal a rushed
  submission.
- **Source:** `06` §4; `03` §Clarity

### V06. Are figures rendered at a readable size and resolution?
- **Pass if:** Yes
- **Rationale:** Tiny or low-resolution figures are unusable to reviewers.
- **Source:** `06` §4

### V07. Is color choice accessible (colorblind-friendly, not relying on red/green alone)?
- **Pass if:** Yes
- **Rationale:** Inaccessible color choices exclude readers; an accessibility
  baseline.
- **Source:** `06` §4 (general presentation)

### V08. Are tables formatted for readability (alignment, no overflow)?
- **Pass if:** Yes
- **Rationale:** Overflowing or misaligned tables impede parsing.
- **Source:** `06` §4

### V09. Do plots use appropriate scales (linear/log, with justification)?
- **Pass if:** Yes
- **Rationale:** Misleading scales distort apparent differences.
- **Source:** `06` §4

### V10. Are bar charts avoided for continuous distributions (per Tufte-style guidance)?
- **Pass if:** Yes
- **Rationale:** Bar charts hide distribution shape; discouraged for continuous
  data.
- **Source:** `06` §4

### V11. Are error bars / distributions shown, not just point estimates?
- **Pass if:** Yes
- **Rationale:** Point-only plots hide variance and overstate differences.
- **Source:** `01` §7; `06` §4

### V12. Are figure captions informative (describe what is shown and the key takeaway)?
- **Pass if:** Yes
- **Rationale:** A caption that only restates the title adds no value.
- **Source:** `06` §4

### V13. Are diagrams (architecture, pipeline) clearly labeled?
- **Pass if:** Yes
- **Rationale:** Unlabeled components make architecture figures useless.
- **Source:** `06` §4

### V14. Are equations numbered and referenced where used?
- **Pass if:** Yes
- **Rationale:** Unnumbered equations that are referenced later break flow.
- **Source:** `06` §2

### V15. Are figures placed near their first reference (not stranded)?
- **Pass if:** Yes
- **Rationale:** Stranded figures force flipping and break reading flow.
- **Source:** `06` §4

### V16. Is the visual density appropriate (not cluttered, not sparse)?
- **Pass if:** Yes
- **Rationale:** Clutter obscures the message; sparsity wastes space.
- **Source:** `06` §4

### V17. Are fonts in figures large enough to read?
- **Pass if:** Yes
- **Rationale:** Tiny figure fonts are a common, easily-fixed defect.
- **Source:** `06` §4

### V18. Do tables include units in headers where applicable?
- **Pass if:** Yes
- **Rationale:** Missing units make table values ambiguous.
- **Source:** `06` §4

### V19. Are significant differences / best results clearly marked in tables?
- **Pass if:** Yes
- **Rationale:** Marking best results aids quick scanning; unmarked tables bury
  the message.
- **Source:** `06` §4

### V20. Are figures consistent in style (fonts, colors, line weights)?
- **Pass if:** Yes
- **Rationale:** Inconsistent styling looks unprofessional and hinders
  comparison.
- **Source:** `06` §4

### V21. Does the paper avoid redundant figures (same info in multiple plots)?
- **Pass if:** Yes
- **Rationale:** Redundant figures waste space and reader attention.
- **Source:** `06` §4

### V22. Are figures used to convey information that text alone cannot?
- **Pass if:** Yes
- **Rationale:** Figures that merely repeat text add no value.
- **Source:** `06` §4

### V23. Are tables used where comparison of exact values matters?
- **Pass if:** Yes
- **Rationale:** Tables suit exact comparison; plots suit trends.
- **Source:** `06` §4

### V24. Are subfigures clearly labeled (a), (b), ... and referenced?
- **Pass if:** Yes
- **Rationale:** Unlabeled subfigures confuse references.
- **Source:** `06` §4
