# Aspect 14 — Resource Efficiency

**Dimension:** Are compute resources disclosed, and is the method's efficiency
(compute, memory, time, energy) characterized and reasonably justified?

**Source basis:** `../rules/01-neurips-paper-checklist.md` §8;
`../rules/05-pineau-reproducibility-checklist.md` §2,3,13;
`../rules/06-ai-review-prompt.md` §6;
`../rules/03-ml-reviewer-guidelines.md` §Quality.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring. Items are **N/A** for papers
with no experiments.

## Items

### RE01. Is the type of compute disclosed (CPU/GPU, cluster, cloud provider)?
- **Pass if:** Yes
- **Rationale:** Compute type disclosure is required for reproducibility.
- **Source:** `01` §8; `05` §13

### RE02. Is the number of compute workers (e.g. GPU count) reported?
- **Pass if:** Yes
- **Rationale:** Worker count is needed to estimate feasibility and cost.
- **Source:** `01` §8; `05` §13

### RE03. Is memory/storage of the compute resources described?
- **Pass if:** Yes
- **Rationale:** Memory constraints affect which configurations are feasible.
- **Source:** `01` §8; `05` §3

### RE04. Is the compute required per individual run reported?
- **Pass if:** Yes
- **Rationale:** Per-run compute lets others estimate replication cost.
- **Source:** `01` §8

### RE05. Is the total compute for the reported experiments estimated?
- **Pass if:** Yes
- **Rationale:** Total compute disclosure is expected.
- **Source:** `01` §8

### RE06. Is it disclosed whether the full research project required more compute than reported (preliminary/failed runs)?
- **Pass if:** Yes
- **Rationale:** Hidden preliminary compute understates true cost and
  selective-reporting risk.
- **Source:** `01` §8

### RE07. Is the runtime (time of execution) per run reported?
- **Pass if:** Yes
- **Rationale:** Runtime is required to estimate replication wall-clock cost.
- **Source:** `01` §8; `05` §13

### RE08. For non-standard algorithms, is computational complexity analyzed (time and space)?
- **Pass if:** Yes
- **Rationale:** Complexity analysis lets others judge feasibility before
  re-running.
- **Source:** `05` §2

### RE09. Are non-trivial hardware/software dependencies described?
- **Pass if:** Yes
- **Rationale:** Hidden dependencies block replication.
- **Source:** `05` §3

### RE10. Are software versions (framework, CUDA) reported?
- **Pass if:** Yes
- **Rationale:** Version drift breaks replication; versions must be pinned.
- **Source:** `05` §14

### RE11. Is the method's efficiency compared to baselines (compute, memory, time)?
- **Pass if:** Yes
- **Rationale:** Efficiency relative to baselines is part of a fair comparison.
- **Source:** `05` §15–17; `03` §Quality

### RE12. Is the method's scalability characterized (how cost grows with input/model size)?
- **Pass if:** Yes
- **Rationale:** Scalability determines practical applicability.
- **Source:** `05` §2; `03` §Quality

### RE13. Is training vs inference cost distinguished where relevant?
- **Pass if:** Yes
- **Rationale:** Conflating train and inference cost misrepresents deployment
  feasibility.
- **Source:** `01` §8; `03` §Significance

### RE14. Is the energy/carbon cost discussed or estimable from the disclosed compute?
- **Pass if:** Yes
- **Rationale:** Energy disclosure is increasingly expected for large-scale
  experiments.
- **Source:** `01` §8; `05` §13

### RE15. Is the efficiency claimed justified by evidence (not asserted)?
- **Pass if:** Yes
- **Rationale:** Asserting efficiency without measurement is an overclaim.
- **Source:** `03` §Quality; `01` §1

### RE16. Are efficiency claims contextualized against accuracy (Pareto frontier)?
- **Pass if:** Yes
- **Rationale:** Efficiency claims without accuracy context can mislead.
- **Source:** `03` §Significance; `06` §5

### RE17. Is the compute accessible to ordinary researchers (not requiring exceptional resources)?
- **Pass if:** Yes
- **Rationale:** Methods requiring exceptional compute limit follow-up work.
- **Source:** `03` §Significance (reproducibility for extension)

### RE18. Are cheaper ablation variants reported (so others can sanity-check)?
- **Pass if:** Yes
- **Rationale:** Cheap variants let others verify findings without full compute.
- **Source:** `05` §18,20

### RE19. Is the method's resource footprint honestly acknowledged as a limitation where relevant?
- **Pass if:** Yes
- **Rationale:** Hiding large compute requirements inflates perceived
  accessibility.
- **Source:** `01` §2

### RE20. Are wall-clock and FLOPs/tokens both reported where appropriate?
- **Pass if:** Yes
- **Rationale:** Wall-clock is hardware-dependent; FLOPs/tokens normalize
  comparisons.
- **Source:** `05` §13

### RE21. Is the training horizon (epochs/steps) reported?
- **Pass if:** Yes
- **Rationale:** Training length affects compute and final results.
- **Source:** `05` §8

### RE22. Is early-stopping criteria reported (so compute isn't wasted in replication)?
- **Pass if:** Yes
- **Rationale:** Early-stopping rules affect both compute and results.
- **Source:** `05` §8

### RE23. Are distributed-training details (if used) described?
- **Pass if:** Yes
- **Rationale:** Distributed setup affects reproducibility and cost.
- **Source:** `05` §3

### RE24. Is the method's memory footprint characterized (peak memory)?
- **Pass if:** Yes
- **Rationale:** Peak memory determines feasibility on available hardware.
- **Source:** `05` §2,3
