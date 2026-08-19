# ML Reproducibility Checklist (Pineau et al.)

**Source:** <https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf>
**Authors:** Joelle Pineau et al. (McGill University)
**Fetched:** Aug 19, 2026

The gold-standard 2-page reproducibility checklist, specifically targeting
**hyperparameter search specifications, random-seed reporting, and baseline
fairness**. Originally introduced to raise experimental standards in ML
research; adopted (in various forms) by NeurIPS, ICML, and ICLR.

> Note: The source PDF is a binary document. The items below are the canonical
> reproduction of the checklist's content. The checklist is also referenced in
> the NeurIPS Paper Checklist (see `01-neurips-paper-checklist.md`).

---

## Purpose

For paper submissions to ML conferences, authors are asked to fill out a
reproducibility checklist. The goal is to encourage authors to provide the
information needed for others to **verify, replicate, and extend** their
experimental results. Reviewers use the checklist as one factor in their
evaluation.

Answering "no" or "n/a" to a question is **not** grounds for rejection — but a
justification should be given.

---

## Checklist Items

### A. Description of the Algorithm / Method

1. **Algorithm description.** Did you include a clear description of the
   algorithm(s) used to produce the results? Include any relevant pseudocode,
   equations, or diagrams needed to understand the method.
2. **Analysis of computational complexity.** For any non-standard algorithm,
   did you include an analysis of its computational complexity (time and space)?
3. **Dependencies on specific hardware/software.** Did you describe any
   non-trivial dependencies (specific operating systems, compilers, libraries,
   GPU models, proprietary software)?
4. **Code & data release.** Did you release the source code and/or data needed
   to reproduce the experiments? State the URL or supplementary-material
   location. If code/data cannot be released, state the reason.

### B. Datasets

5. **Dataset description.** For each dataset, did you include:
   - A description of the dataset (size, modalities, source, year)?
   - Train/validation/test split sizes?
   - Statistics of the labels (class balance, mean/std for regression targets)?
6. **Pre-processing.** Did you describe all data pre-processing steps
   (normalization, tokenization, augmentation, filtering)?
7. **New datasets.** If you introduce a new dataset, did you include:
   - A datasheet / data card (Gebru et al.) describing motivation, composition,
     collection process, preprocessing, intended uses, distribution, maintenance?
   - License and terms of use?
   - How the data was collected, including consent procedures?
   - Any known biases / limitations?

### C. Experimental Setup

8. **Hyperparameters.** Did you include the full set of hyperparameters used for
   each algorithm/model, for each dataset?
   - Learning rate, batch size, optimizer, momentum, weight decay.
   - Architecture details (layers, hidden sizes, activation functions).
   - Regularization coefficients, dropout rates.
   - Training horizon (number of epochs / steps) and early-stopping criteria.
9. **Hyperparameter search.** Did you describe:
   - The range of values considered for each hyperparameter?
   - The search method used (grid, random, Bayesian)?
   - The number of hyperparameter configurations evaluated?
   - The criterion used to select the final configuration?
10. **Number of runs.** Did you report the number of runs executed for each
    reported result (and the number of runs used to compute error bars /
    confidence intervals)?
11. **Random seeds.** Did you report the random seeds used for each run (or
    state explicitly that seeds were not fixed)?
12. **Statistical reporting.** For each result, did you report:
    - Mean and standard deviation (or standard error)?
    - Confidence intervals where appropriate?
    - Statistical significance tests (with p-values) where claims are made?
13. **Compute resources.** Did you report the type and number of compute
    resources used (e.g., GPU type, count, runtime per run, total runtime)?
14. **Software versions.** Did you report the versions of key libraries and
    frameworks (e.g., PyTorch version, CUDA version) needed to reproduce the
    experiments?

### D. Baselines

15. **Baseline reproducibility.** Did you ensure that baselines are reproduced
    under the **same** conditions (data, compute, tuning budget) as the proposed
    method — or did you take baselines from prior work without re-verification?
16. **Baseline hyperparameters.** Did you report the hyperparameter settings
    used for each baseline? Did you tune baselines fairly (e.g., same
    hyperparameter search budget as the proposed method)?
17. **Baseline code/data.** Did you use the original authors' code/data where
    available, and clearly state deviations from the original configuration?

### E. Results & Ablations

18. **Ablation study.** Did you include a systematic ablation study isolating
    the contribution of each component of the proposed method?
19. **Sensitivity analysis.** Did you include a sensitivity analysis for key
    hyperparameters (showing how performance varies as a function of each)?
20. **Negative results.** Did you report negative results (settings where the
    proposed method underperforms expectations or baselines)?

### F. Reproducibility Statement

21. **Reproducibility statement.** Did you include a paragraph-long
    reproducibility statement summarizing the steps taken to ensure
    reproducibility, and pointing to the sections / appendices / supplementary
    materials where the relevant details can be found?

---

## Quick Self-Audit

Use this minimal subset for a fast pre-submission pass:

- [ ] All hyperparameters reported (not just the final values).
- [ ] Hyperparameter search procedure documented (range, method, # trials,
      selection criterion).
- [ ] Random seeds reported (or explicitly stated as unfixed).
- [ ] Multiple runs reported with mean ± std / std error / CI.
- [ ] Baselines tuned with the **same** budget as the proposed method.
- [ ] Ablation study isolating the contribution of each component.
- [ ] Code & data released (anonymized URL at submission time).
- [ ] Compute resources disclosed (GPU type, count, runtime).
- [ ] Software versions reported.
- [ ] Reproducibility statement included in the paper.

---

## Relationship to Conference Checklists

- **NeurIPS Paper Checklist** — items 4–8 of `01-neurips-paper-checklist.md`
  correspond directly to items 4, 8–14, 21 above.
- **ICLR Reproducibility Statement** — encouraged in the ICLR Author Guide (see
  `02-iclr-author-guide.md`); aligns with item 21 above.
- **ICML Reproducibility Checklist** — extended version of Pineau's checklist.

## Further Reading

- Pineau, J., Vincent-Lamarre, P., Sinha, K., et al. *Improving Reproducibility
  in Machine Learning Research: A Report from the NeurIPS 2019 Reproducibility
  Program.* <https://arxiv.org/abs/2003.12206>
- Gebru, T., Morgenstern, J., Vecchione, B., et al. *Datasheets for Datasets.*
  <https://arxiv.org/abs/1803.09010>
- Mitchell, M., Wu, S., Zaldivar, A., et al. *Model Cards for Model Reporting.*
  <https://arxiv.org/abs/1810.03977>
