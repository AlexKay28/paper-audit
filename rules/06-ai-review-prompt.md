# Ready-to-Use AI Review Prompt

**Source:** Synthesized from the NeurIPS Paper Checklist, ICLR Author Guide,
ML Reviewer Guidelines, and Lipton & Steinhardt's *Troubling Trends* paper.

## Usage

Paste the text of your paper (or LaTeX source) along with the prompt below into
an LLM. Replace `[PASTE YOUR PAPER TEXT OR LATEX SOURCE HERE]` with your
manuscript.

For best results, also include the relevant reference document(s) from this
folder (e.g., `01-neurips-paper-checklist.md`) as additional context.

---

## Prompt

```text
You are a Senior Area Chair for a top machine learning conference (NeurIPS/ICLR).
Evaluate my paper draft using the official NeurIPS Paper Checklist and ICLR
Soundness criteria.

Focus your evaluation on:
1. Technical Soundness: Are claims overstated? Do ablations isolate the exact
   source of gains?
2. Math & Notation: Is every variable explicitly defined? Is the notation
   consistent?
3. Visuals & Captions: Are figures and tables self-contained?
4. Baselines: Are comparisons against recent state-of-the-art baselines fair
   and equivalent in compute/tuning?

Provide a score for Soundness (1-4), Presentation (1-4), and Contribution
(1-4), followed by actionable "Strengths" and "Weaknesses" bullet points.

Here is my draft:
[PASTE YOUR PAPER TEXT OR LATEX SOURCE HERE]
```

---

## Extended Prompt (Recommended for Thorough Review)

The minimal prompt above asks for high-level scores. For a more thorough audit,
use the extended prompt below, which expands the four focus areas and adds the
Lipton–Steinhardt "Troubling Trends" lens plus the Pineau reproducibility
checklist.

```text
You are a Senior Area Chair for a top machine learning conference (NeurIPS/ICLR).
Evaluate my paper draft using (a) the official NeurIPS Paper Checklist,
(b) the ICLR Soundness/Presentation/Contribution rubric, and
(c) the four "troubling trends" pitfalls identified by Lipton & Steinhardt
(arXiv:1807.03341).

=== EVALUATION DIMENSIONS ===

1. TECHNICAL SOUNDNESS (ICLR Soundness 1-4)
   - Are claims overstated relative to what the theory/experiments support?
   - Are proofs correct and complete? Are assumptions explicitly stated?
   - Do ablation studies isolate the EXACT source of empirical gains, or are
     multiple changes bundled without disentanglement?
   - Are error bars / std dev / confidence intervals reported with methodology?
   - Are random seeds reported (or stated as unfixed)?
   - Is the number of runs specified for each result?

2. MATH & NOTATION (Troubling Trend #3: Mathiness)
   - Is every variable explicitly defined at first use?
   - Is notation consistent throughout the paper?
   - Are theorems necessary, or are they "spurious" (inserted to convey depth
     without supporting the main claims)?
   - Are formal and informal claims clearly distinguished, or is there slippage
     between them?
   - Are informal proof sketches in the main paper complemented by formal proofs
     in the appendix?

3. LANGUAGE (Troubling Trend #4: Misuse of Language)
   - Are technical terms used with their precise technical meaning?
   - Are any terms overloaded (e.g., "deconvolution", "generative model",
     "covariate shift")?
   - Are anthropomorphic / suggestive terms ("curiosity", "fear", "thought
     vectors", "human-level") properly qualified?
   - Are "suitcase words" (e.g., "interpretability", "generalization") unpacked?
   - Is speculation clearly labeled as such, or is it presented as explanation?
     (Troubling Trend #1)

4. VISUALS & CAPTIONS (ICLR Presentation 1-4)
   - Are figures and tables self-contained (interpretable from the caption
     alone)?
   - Are axes labeled with units? Are legends complete?
   - Is the paper well organized and easy to follow?
   - Is the writing clear to a non-expert in this specific subfield?

5. BASELINES (Troubling Trend #2: Failure to Identify Sources of Gains)
   - Are comparisons against RECENT state-of-the-art baselines (not strawmen)?
   - Are baselines tuned with the SAME compute/hyperparameter-search budget as
     the proposed method?
   - Are baseline hyperparameters reported, and baseline code/data used where
     available?
   - Are baselines reproduced under the same data splits and evaluation protocol?

6. REPRODUCIBILITY (Pineau Checklist)
   - Are all hyperparameters reported (not just the final values)?
   - Is the hyperparameter search procedure documented (range, method, number
     of trials, selection criterion)?
   - Are code and data released (anonymized URL at submission time)?
   - Are compute resources disclosed (GPU type, count, runtime)?
   - Are software versions reported?
   - Is there a paragraph-long Reproducibility Statement?

7. ETHICS & SOCIETAL IMPACT (NeurIPS Checklist items 9-11, 14-15)
   - Are broader impacts / potential negative societal impacts discussed where
     appropriate?
   - Are safeguards described for high-risk dual-use models?
   - Are licenses of all assets cited and respected?
   - If human subjects / crowdsourcing were used, are IRB approval and
     compensation (≥ minimum wage) described?
   - Is LLM usage in the core methodology declared (if non-standard)?

8. CONTRIBUTION (ICLR Contribution 1-4)
   - Is the contribution non-trivial and clearly articulated?
   - Does it provide new insights (not necessarily a new method)?
   - Will others build upon this work?
   - Is the problem important?

=== OUTPUT FORMAT ===

Provide:

A. SCORES (with 1-sentence justification each)
   - Soundness:       1-4
   - Presentation:    1-4
   - Contribution:    1-4
   - Overall:         1-10 (ICLR scale)
   - Confidence:      1-5

B. STRENGTHS (3-5 specific bullets, each citing a paper section)

C. WEAKNESSES (3-5 specific bullets, each citing a paper section and proposing
   a concrete fix)

D. NEURIPS CHECKLIST FLAG (for each of the 16 checklist items, indicate yes /
   no / n/a and a 1-sentence note; focus on items where the paper is at risk)

E. TROUBLING-TRENDS AUDIT (explicitly call out any of the four trends the paper
   falls into, with quoted text from the manuscript)

F. TOP-3 ACTIONABLE CHANGES (ranked by expected impact on acceptance odds)

Here is my draft:
[PASTE YOUR PAPER TEXT OR LATEX SOURCE HERE]
```

---

## Tips for Best Results

1. **Include the LaTeX source** rather than a rendered PDF extract — it lets the
   model see structure (sections, theorems, captions, labels) more reliably.
2. **Provide the reference docs as context.** Paste the contents of
   `01-neurips-paper-checklist.md` and `03-ml-reviewer-guidelines.md` alongside
   your paper so the model scores against the exact rubric rather than a
   remembered approximation.
3. **Ask for section citations.** The extended prompt requests that strengths and
   weaknesses cite specific paper sections — this grounds the critique and
   reduces hallucination.
4. **Iterate.** After addressing the model's feedback, re-run the prompt on the
   revised draft to verify the fixes hold.
5. **Cross-check with a human reviewer.** LLM reviews can miss subtle technical
   errors or invent issues; treat the output as a high-signal first pass, not a
   final verdict.
