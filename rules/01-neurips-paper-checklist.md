# NeurIPS Paper Checklist

**Source:** <https://neurips.cc/public/guides/PaperChecklist>
**Fetched:** Aug 19, 2026

The NeurIPS Paper Checklist encourages best practices for responsible machine
learning research, addressing **reproducibility, transparency, research ethics,
and societal impact**. It is included in the official NeurIPS LaTeX style file
and **must not be removed — papers without the checklist will be desk-rejected.**

The checklist follows the references (and optional supplemental material) in the
submission PDF and **does NOT count towards the page limit.**

## How to Answer Each Question

- Answer **yes**, **no**, or **n/a**.
- **n/a** means the question is *Not Applicable* or the relevant information is
  *Not Available*.
- Optionally add a 1–2 sentence justification and/or a reference to the paper
  section(s) that support the answer.
- Checklist answers are visible to reviewers, area chairs, senior area chairs,
  and ethics reviewers, and are published with the final paper.
- **Answering "no" or "n/a" is NOT grounds for rejection** provided a proper
  justification is given (e.g., "error bars not reported because the experiment
  is too computationally expensive"). Reviewers are instructed not to penalize
  honest disclosures.

---

## The 16 Checklist Questions

### 1. Claims
> Do the main claims made in the abstract and introduction accurately reflect
> the paper's contributions and scope?

- Claims should match theoretical and experimental results in terms of how much
  the results can be expected to generalize.
- Contributions should be clearly stated in the abstract and introduction, along
  with important assumptions and limitations.
- Aspirational goals are acceptable as motivation, provided it is clear they are
  not attained by the paper.

### 2. Limitations
> Did you discuss the limitations of the work?

A separate "Limitations" section is encouraged. Authors should:

- Point out strong assumptions and how robust results are to violations
  (independence assumptions, noiseless settings, model well-specification,
  asymptotic approximations, etc.).
- Reflect on how assumptions might be violated in practice and the implications.
- Reflect on the scope of claims (e.g., tested on only a few datasets / runs).
- Articulate implicit empirical assumptions.
- Reflect on factors influencing performance (e.g., a face-recognition model
  failing under low resolution; a speech-to-text system failing on jargon).

> Reviewers are explicitly instructed **not** to penalize honesty about
> limitations. A worse outcome is reviewers discovering unacknowledged
> limitations.

- **Answer "n/a"** → the paper has no limitation.
- **Answer "no"** → the paper has limitations, but they are not discussed.

### 3. Theory, Assumptions and Proofs
> If you are including theoretical results, did you state the full set of
> assumptions of all theoretical results, and did you include complete proofs?

- State the full set of **assumptions** in every theorem.
- Include complete **proofs** (in main paper or supplemental material). If in
  the supplement, provide a short proof sketch in the main paper.
- Any informal proof in the core paper must be complemented by formal proofs in
  the appendix/supplement.
- Theorems and Lemmas relied upon must be properly referenced.

### 4. Experimental Result Reproducibility
> If the contribution is a dataset or model, what steps did you take to make
> your results reproducible or verifiable?

NeurIPS does not require releasing code, but does require *some reasonable
avenue for reproducibility*, depending on the contribution:

- **New algorithm** → make clear how to reproduce it.
- **New architecture** → describe the architecture fully.
- **New model (e.g., LLM)** → provide either a way to access the model or a way
  to reproduce it (open-source dataset or construction instructions).
- **Closed-source model** → access may be limited (e.g., registered users) but
  some path to verification must exist.

### 5. Open Access to Data and Code
> If you ran experiments, did you include the code, data, and instructions
> needed to reproduce the main experimental results?

- Instructions must contain the exact command and environment needed to run.
- Covers new method **and** baselines; capture as many minor experiments as
  possible. If only a subset is reproducible, state which.
- "No, because the code is proprietary" is an acceptable answer.
- Anonymize code/data at submission time.
- Papers cannot be rejected solely for missing code **unless** code is central
  to the contribution (e.g., a new open-source benchmark).

### 6. Experimental Setting/Details
> If you ran experiments, did you specify all the training details (e.g., data
> splits, hyperparameters, how they were chosen)?

- Important details belong in the main paper; full details can go with code, in
  an appendix, or as supplemental material.
- Information about how hyperparameters were selected must appear in the paper
  or supplementary materials.
- **Answer "n/a"** → the paper has no experiments.

### 7. Experiment Statistical Significance
> Does the paper report error bars suitably and correctly defined or other
> appropriate information about the statistical significance of the experiments?

- "Yes" requires error bars, confidence intervals, or significance tests — at
  least for experiments supporting the main claims.
- Clearly state the **factors of variability** captured (train/test split,
  initialization, random draws, overall run conditions).
- Explain the **method** for computing error bars (closed-form, library, bootstrap).
- State assumptions (e.g., normally distributed errors).
- Clarify whether the bar is **standard deviation** or **standard error of the
  mean**.
- 1-sigma error bars are OK if stated; 2-sigma preferred if Normality is
  unverified.
- For asymmetric distributions, avoid symmetric error bars that yield
  out-of-range values (e.g., negative error rates).

### 8. Experiments Compute Resources
> For each experiment, does the paper provide sufficient information on the
> compute resources (type of compute workers, memory, time of execution) needed
> to reproduce the experiments?

- Indicate compute type (CPU/GPU, internal cluster, cloud provider) including
  relevant memory and storage.
- Provide the compute required per individual run **and** estimate total
  compute.
- Disclose whether the full research project required more compute than the
  reported experiments (e.g., preliminary or failed runs).

### 9. Code of Ethics
> Have you read the NeurIPS Code of Ethics and ensured that your research
> conforms to it?

- Explain any deviations, preserving anonymity (e.g., jurisdiction-specific
  legal considerations).

### 10. Broader Impacts
> If appropriate for the scope and focus of your paper, did you discuss
> potential negative societal impacts of your work?

Examples of negative societal impacts:

- Malicious or unintended uses (disinformation, fake profiles, surveillance).
- Fairness considerations (technologies that unfairly impact specific groups).
- Privacy considerations.
- Security considerations.

Authors should consider:

- Harms when technology is **used as intended and functioning correctly**.
- Harms when technology is **used as intended but gives incorrect results**.
- Harms from **(intentional or unintentional) misuse**.

Foundational research not tied to a specific application generally need not
discuss impacts — but a *direct path* to a negative application should be
flagged (e.g., generative-model improvements enabling Deepfakes).

Mitigation strategies are encouraged: gated release, defenses alongside attacks,
misuse monitoring, efficiency/accessibility improvements.

### 11. Safeguards
> Do you have safeguards in place for responsible release of models with a high
> risk for misuse (e.g., pretrained language models)?

- High-risk / dual-use released models should include safeguards for controlled
  use (usage guidelines, access restrictions).
- Datasets scraped from the Internet may pose safety risks — describe how
  unsafe content was filtered.
- Effective safeguards are challenging; a best-faith effort is encouraged.

### 12. Licenses
> If you are using existing assets (code, data, models), did you cite the
> creators and respect the license and terms of use?

- Cite the original paper producing the code package or dataset.
- State the **version** of the asset you are using.
- Include a URL where possible.
- State the license name (e.g., CC-BY 4.0) for each asset.
- For scraped data, state the source's copyright and terms of service.
- For released assets, include license, copyright, and terms of use in the
  package.
- For repackaged datasets, state both the original license and the derived one.
- Check [paperswithcode.com/datasets](https://paperswithcode.com/datasets) and
  its [licensing guide](https://paperswithcode.com/datasets/license).
- If licensing info is unavailable online, contact the asset's creators.

### 13. New Assets
> If you are releasing new assets, did you document them and provide these
> details alongside the assets?

- Communicate dataset/code/model details via **structured templates**:
  training, license, limitations, etc.
- Discuss whether and how consent was obtained from people whose data is used.
- Anonymize assets at submission (anonymized URL or zip).
- **Answer "n/a"** → no new assets are released.

### 14. Crowdsourcing and Research with Human Subjects
> If you used crowdsourcing or conducted research with human subjects, did you
> include the full text of instructions given to participants and screenshots,
> if applicable, as well as details about compensation (if any)?

- Full instructions and screenshots may go in supplemental material; if human
  subjects are the main contribution, include detail in the main paper.
- Per the NeurIPS Code of Ethics, workers involved in data collection, curation,
  or other labor **must be paid at least the minimum wage** in your country.

### 15. IRB Approvals
> Did you describe any potential participant risks and obtain Institutional
> Review Board (IRB) approvals (or an equivalent approval/review based on the
> requirements of your institution), if applicable?

- IRB approval (or equivalent) may be required for any human-subjects research,
  varying by country/institution.
- If obtained, clearly state this in the paper.
- For initial submissions, **do not include information that breaks anonymity**
  (e.g., the reviewing institution).

### 16. Declaration of LLM Usage
> Does the paper describe the usage of LLMs if it is an important, original, or
> non-standard component of the core methods in this research?

- Declaration is **not required** if LLMs are used only for writing, editing, or
  formatting and do not impact core methodology, scientific rigorousness, or
  originality.
- **Answer "n/a"** → core method development does not involve LLMs as an
  important, original, or non-standard component.

---

## Quick Reference: Answer Semantics

| Question type | `yes` | `no` | `n/a` |
|---|---|---|---|
| Most questions | Done / included | Not done / not included | Not applicable |
| Limitations (#2) | Discussed | Has limitations but not discussed | Paper has no limitation |
| Experiments (#6, #7, #8) | Reported properly | Not reported | Paper has no experiments |
| New assets (#13) | Documented | Not documented | No new assets released |
| LLM usage (#16) | Described | Not described (but required) | LLMs not part of core method |
