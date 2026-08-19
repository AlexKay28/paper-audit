# Aspect 20 — ACL Compliance

**Dimension:** Does the paper satisfy ACL-specific requirements — the
mandatory Limitations section, linguistic soundness, resource documentation,
multilingual consideration, and ethics review?

**Source basis:** `../rules/03-ml-reviewer-guidelines.md` §ACL;
`../rules/01-neurips-paper-checklist.md` §13,14 (shared ethics);
`../rules/02-iclr-author-guide.md` (shared ethics topics).

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Several items are **N/A** for
non-NLP papers or papers with no linguistic/resource angle.

## Items

### AL01. Is there a dedicated Limitations section (ACL-required)?
- **Pass if:** Yes
- **Rationale:** ACL specifically requires a Limitations section.
- **Source:** `03` §ACL (Limitations Section)

### AL02. Are limitations honest and comprehensive (not token)?
- **Pass if:** Yes
- **Rationale:** ACL reviewers check whether limitations are honest and
  comprehensive.
- **Source:** `03` §ACL (Limitations Section)

### AL03. Do the stated limitations undermine the core claims?
- **Pass if:** No
- **Rationale:** If limitations invalidate the claims, the claims are too
  strong.
- **Source:** `03` §ACL (Limitations Section)

### AL04. Are potential negative impacts addressed?
- **Pass if:** Yes
- **Rationale:** ACL reviewers check whether negative impacts are addressed.
- **Source:** `03` §ACL (Limitations Section)

### AL05. Are linguistic claims accurate (linguistic soundness)?
- **Pass if:** Yes
- **Rationale:** ACL adds NLP-specific evaluation: linguistic soundness.
- **Source:** `03` §ACL (ACL-Specific Criteria)

### AL06. Are datasets/models properly documented (resource documentation)?
- **Pass if:** Yes
- **Rationale:** ACL adds resource documentation as a criterion.
- **Source:** `03` §ACL (ACL-Specific Criteria)

### AL07. Is multilingual consideration addressed (if applicable)?
- **Pass if:** Yes
- **Rationale:** ACL asks whether language diversity is addressed where
  applicable.
- **Source:** `03` §ACL (ACL-Specific Criteria)

### AL08. Are dual-use concerns addressed (ACL ethics review)?
- **Pass if:** Yes
- **Rationale:** ACL has a dedicated ethics review for dual-use concerns.
- **Source:** `03` §ACL (Ethics Review)

### AL09. Are data privacy issues addressed (ACL ethics review)?
- **Pass if:** Yes
- **Rationale:** Privacy is an ACL ethics-review topic.
- **Source:** `03` §ACL (Ethics Review)

### AL10. Are bias and fairness implications addressed (ACL ethics review)?
- **Pass if:** Yes
- **Rationale:** Bias/fairness is an ACL ethics-review topic.
- **Source:** `03` §ACL (Ethics Review)

### AL11. Does the review/paper re-express the position fairly (Dennett's rule 1)?
- **Pass if:** Yes
- **Rationale:** ACL follows Dennett's rules; fair re-expression is rule 1.
- **Source:** `03` §ACL (Following Daniel Dennett's Rules)

### AL12. Does the paper list agreements (acknowledge what works) (Dennett's rule 2)?
- **Pass if:** Yes
- **Rationale:** Listing agreements is Dennett's rule 2.
- **Source:** `03` §ACL (Following Daniel Dennett's Rules)

### AL13. Does the paper credit what was learned (Dennett's rule 3)?
- **Pass if:** Yes
- **Rationale:** Crediting the contribution is Dennett's rule 3.
- **Source:** `03` §ACL (Following Daniel Dennett's Rules)

### AL14. Does the paper critique only after establishing understanding (Dennett's rule 4)?
- **Pass if:** Yes
- **Rationale:** Critique follows understanding (Dennett's rule 4).
- **Source:** `03` §ACL (Following Daniel Dennett's Rules)

### AL15. Is there a Summary (1 paragraph) of what the paper does + main contribution?
- **Pass if:** Yes
- **Rationale:** ACL review-structure best practice opens with a Summary.
- **Source:** `03` §ACL (Review Structure Best Practices)

### AL16. Are Strengths listed as 3–5 specific bullets with rationale?
- **Pass if:** Yes
- **Rationale:** ACL review structure expects specific Strengths.
- **Source:** `03` §ACL (Review Structure Best Practices)

### AL17. Are Weaknesses listed as 3–5 specific bullets with proposed fixes?
- **Pass if:** Yes
- **Rationale:** ACL review structure expects specific Weaknesses with fixes.
- **Source:** `03` §ACL (Review Structure Best Practices)

### AL18. Are Questions (2–4 clarifications) anticipated?
- **Pass if:** Yes
- **Rationale:** ACL review structure includes Questions.
- **Source:** `03` §ACL (Review Structure Best Practices)

### AL19. Are minor issues (typos, formatting) cleaned up?
- **Pass if:** Yes
- **Rationale:** ACL review structure includes a Minor Issues field.
- **Source:** `03` §ACL (Review Structure Best Practices)

### AL20. Is there a clear overall assessment / recommendation?
- **Pass if:** Yes
- **Rationale:** ACL review structure closes with an overall assessment.
- **Source:** `03` §ACL (Review Structure Best Practices)

### AL21. For NLP resources, is a datasheet / data card provided?
- **Pass if:** Yes
- **Rationale:** ACL's resource-documentation criterion aligns with datasheets.
- **Source:** `03` §ACL; `05` §7

### AL22. Are linguistic terms used with their precise technical meaning?
- **Pass if:** Yes
- **Rationale:** Linguistic soundness requires precise terminology.
- **Source:** `03` §ACL; `04` §4.2

### AL23. Is language diversity / cross-lingual applicability discussed where relevant?
- **Pass if:** Yes
- **Rationale:** Multilingual consideration is ACL-specific.
- **Source:** `03` §ACL (ACL-Specific Criteria)

### AL24. Are annotator agreement / quality metrics reported for linguistic resources?
- **Pass if:** Yes
- **Rationale:** Annotator agreement is standard for NLP resources.
- **Source:** `03` §ACL; `05` §5

### AL25. Is the paper scoped to a language/dataset without overclaiming universality?
- **Pass if:** Yes
- **Rationale:** Overclaiming linguistic universality from a single language
  is a calibration failure.
- **Source:** `03` §ACL; `04` §4.2
