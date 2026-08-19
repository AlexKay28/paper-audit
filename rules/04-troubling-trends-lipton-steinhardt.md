# Troubling Trends in Machine Learning Scholarship

**Authors:** Zachary C. Lipton, Jacob Steinhardt
**Source:** <https://arxiv.org/abs/1807.03341> (arXiv:1807.03341, v2, Jul 26 2018)
**Presented at:** ICML 2018 The Debates
**Fetched:** Aug 19, 2026

## Abstract

Collectively, ML researchers create and disseminate knowledge about data-driven
algorithms. Papers are most valuable when they act in service of the reader —
creating foundational knowledge and communicating as clearly as possible.

Recent progress in ML comes **despite frequent departures from these ideals**.
The paper focuses on four trending patterns in ML scholarship:

1. **Failure to distinguish between explanation and speculation.**
2. **Failure to identify the sources of empirical gains** (e.g., emphasizing
   unnecessary architectural modifications when gains actually stem from
   hyperparameter tuning).
3. **Mathiness** — the use of mathematics that obfuscates or impresses rather
   than clarifies (e.g., confusing technical and non-technical concepts).
4. **Misuse of language** — choosing terms of art with colloquial connotations
   or overloading established technical terms.

Possible causes: rapid community expansion, thinness of the reviewer pool, and
misaligned incentives between scholarship and short-term measures of success
(bibliometrics, attention, entrepreneurial opportunity).

---

## 1. Troubling Trend #1 — Explanation vs. Speculation

Research into new areas often involves exploration predicated on intuitions not
yet coalesced into crisp formal representations. **Speculation** has a role for
imparting intuitions, but papers often offer speculation in the guise of
**explanations**, which are then interpreted as authoritative due to the
trappings of a scientific paper.

### Canonical Example: "Internal Covariate Shift"

The batch-normalization paper formed an intuitive theory around *internal
covariate shift*. Key terms are not crisp enough to conclusively assume a truth
value (e.g., by which divergence measure is the change quantified?). The paper
never clarifies. Later work suggests this explanation may be off the mark.

Nevertheless, the speculative explanation has been repeated as fact — e.g., one
paper states: *"It is well-known that a deep neural network is very hard to
optimize due to the internal-covariate-shift problem."*

### Self-Criticism

The authors note they have been equally guilty:

- JS: *"the high dimensionality and abundance of irrelevant features…give the
  attacker more room to construct attacks"* — without any experiments measuring
  the effect of dimensionality on attackability.
- JS: introduced the intuitive notion of *coverage* without defining it and used
  it as a form of explanation.

### Positive Examples

- **Dropout paper** (Srivastava et al.): speculates at length on connections
  between dropout and sexual reproduction, but a designated **"Motivation"
  section clearly quarantines** this discussion.
- **Practical guidelines for training neural networks** (Bengio): carefully
  conveys uncertainty — *"they should be challenged…very often have not been
  formally validated."*

---

## 2. Troubling Trend #2 — Failure to Identify the Sources of Empirical Gains

The peer review process places a premium on **technical novelty**. Many papers
emphasize complex models and fancy mathematics. But empirical advances often
come through:

- Clever problem formulations.
- Scientific experiments.
- Optimization heuristics.
- Data preprocessing techniques.
- Extensive hyperparameter tuning.
- Applying existing methods to new tasks.

When several techniques together achieve a result, it serves the reader to
elucidate **which techniques are necessary** to realize the gains.

### The Problem

Too frequently, authors propose many tweaks **absent proper ablation studies**,
obscuring the source of empirical gains. Sometimes just one change is
responsible. This can give the false impression that the authors did more work
(by proposing several improvements), when in fact they did not do enough (by
not performing proper ablations). Moreover, it misleads readers to believe all
proposed changes are necessary.

### Canonical Example: LSTMs Beat by Hyperparameter Tuning

Melis et al. 2018 demonstrated that a series of published improvements,
originally attributed to complex innovations in network architectures, were
actually due to **better hyperparameter tuning**. On equal footing, vanilla
LSTMs (hardly modified since 1997) topped the leaderboard.

Similar evaluation issues have been observed for deep reinforcement learning and
GANs.

### Positive Examples

- Many papers perform good ablation analyses.
- Retrospective attempts to isolate the source of gains can lead to new
  discoveries.
- Understanding can also come from **robustness checks** (e.g., discovering
  language models handle inflectional morphology poorly) and **qualitative
  error analysis**.
- Probing neural-network behavior led to identifying susceptibility to
  adversarial perturbations.
- Careful study of challenge datasets often reveals limitations and yields
  stronger baselines (e.g., 73% of CNN/DailyMail questions answerable from a
  single sentence).

---

## 3. Troubling Trend #3 — Mathiness

> *More equations, even when difficult to decipher, tend to convince reviewers
> of a paper's technical depth.* — experienced post-doc feedback to one author.

Mathematics imparts precision and clarity when used correctly. But not all ideas
are amenable to precise mathematical description; natural language is equally
indispensable, especially for intuitive or empirical claims.

When mathematical and natural-language statements are mixed without a clear
accounting of their relationship, **both the prose and the theory can suffer**:
problems in the theory can be concealed by vague definitions, while weak
arguments in the prose can be bolstered by the appearance of technical depth.

> **Mathiness** (following economist Paul Romer): *"Like mathematical theory,
> mathiness uses a mixture of words and symbols, but instead of making tight
> links, it leaves ample room for slippage between statements in natural
> language versus formal language."*

### Manifestations

1. **Abusing mathematics to convey technical depth** — *spurious theorems*
   inserted to lend authoritativeness to empirical results, even when the
   theorem's conclusions do not actually support the main claims.
   - **Adam optimizer paper**: offers a convergence theorem in the convex case
     (perhaps unnecessary in an applied paper focusing on non-convex
     optimization). The proof was later shown to be incorrect.
2. **Claims that are neither clearly formal nor clearly informal** — e.g.,
   citing a statistical-physics paper on Gaussian random fields and stating
   that in high dimensions "all local minima…are likely to have an error very
   close to that of the global minimum." Appears formal, but absent a specific
   theorem it is hard to verify or determine its precise content.
3. **Invoking theory in overly broad ways** — e.g., the *no free lunch theorem*
   invoked to justify using heuristic methods without guarantees, even though
   the theorem does not formally preclude guaranteed learning procedures.

### Positive Example

A counterfactual-reasoning tutorial covers a large amount of mathematical ground
in a down-to-earth manner, with numerous clear connections to applied empirical
problems. Written in clear service to the reader, it has helped spur work in the
burgeoning counterfactual-reasoning community.

---

## 4. Troubling Trend #4 — Misuse of Language

Three common avenues:

### 4.1 Suggestive Definitions

A new technical term is coined that has a **suggestive colloquial meaning**,
sneaking in connotations without arguing for them.

- **Anthropomorphic characterizations** of tasks (*reading comprehension*,
  *music composition*) and techniques (*curiosity*, *fear*).
- Model-component names suggestive of human cognition: *"thought vectors"*,
  *"consciousness prior"*.

When a suggestive term is assigned technical meaning, each subsequent paper has
no choice but to confuse its readers — either by embracing the term or by
replacing it.

**"Human-level" performance** claims can portray a false sense of capabilities:

- *"Dermatologist-level classification of skin cancer"* conceals that
  classifiers and dermatologists perform fundamentally different tasks. Real
  dermatologists encounter a wide variety of circumstances; the classifier only
  achieves low error on i.i.d. test data.
- Better-qualified: claims of human-level performance restricted to the ImageNet
  *classification task* (rather than object recognition more broadly).
- Even one careful paper was insufficient to put the public discourse back on
  track.

**Fairness literature** often overloads terminology borrowed from complex legal
doctrine (*disparate impact*) to name simple equations expressing statistical
parity. The result: a literature where *"fairness," "opportunity,"* and
*"discrimination"* denote simple statistics of predictive models, confusing
researchers and misinforming policymakers.

### 4.2 Overloading Technical Terminology

Taking a term with precise technical meaning and using it imprecisely or
contradictorily.

- **Deconvolution** formally describes reversing a convolution; now used in deep
  learning to refer to transpose convolutions / upconvolutions. New papers
  referring to "deconvolution" might (i) invoke the original meaning, (ii)
  describe upconvolution, or (iii) attempt to resolve the confusion.
- **Generative models** traditionally model p(x) or p(x,y); discriminative
  models address p(y|x). In recent work, *"generative model"* imprecisely
  refers to any model producing realistic-looking structured data. This obscures
  shortcomings — e.g., the inability of GANs/VAEs to perform conditional
  inference. Some discriminative models are now referred to as generative on
  account of producing structured outputs.
- **Covariate shift** refers to a specific type of shift where p(x) might change
  but the labeling function p(y|x) does not. The batch-normalization paper
  describes covariate shift as a change in the distribution of model inputs —
  and due to its influence, Google Scholar lists batch normalization as the
  first reference on searches for "covariate shift."

Consequence: **redefining an unsolved task to refer to something easier** can
conceal lack of progress. *Language understanding* and *reading comprehension*,
once grand challenges of AI, now refer to making accurate predictions on
specific datasets.

### 4.3 Suitcase Words

Coined by Minsky in *The Emotion Machine* (2007): suitcase words pack together
a variety of meanings that may not share "a single cause or origin."

- ***Interpretability*** holds no universally agreed-upon meaning and often
  references disjoint methods and desiderata. Papers that appear to be in
  dialogue may have different concepts in mind.
- ***Generalization*** has a specific technical meaning (train → test) and a
  more colloquial meaning closer to *transfer* (population → population) or
  *external validity* (experimental setting → real world). Conflating these
  leads to overestimating current systems' capabilities.
- Suggestive definitions and overloaded terminology contribute to new suitcase
  words. In fairness literature, terms like ***bias*** become suitcase words
  that must be subsequently unpacked.

Suitcase words can serve a useful purpose in common speech and as aspirational
terms (e.g., *artificial intelligence* as a department name). But using them in
technical arguments leads to confusion — e.g., writing an equation involving
*intelligence* and *optimization power*, implicitly assuming suitcase words can
be quantified with a one-dimensional scalar.

---

## 5. Speculation on Causes

### 5.1 Complacency in the Face of Progress

The apparent rapid progress has at times engendered an attitude that **strong
results excuse weak arguments**. Authors with strong results may feel licensed
to insert unsupported stories, omit ablation experiments, adopt exaggerated
terminology, or take less care to avoid mathiness.

The single-round nature of reviewing may cause reviewers to feel they have no
choice but to accept papers with strong quantitative findings — even if flawed,
there is no guarantee the flaws will be fixed in the next cycle.

### 5.2 Growing Pains

Since ~2012, the ML community has expanded rapidly. Side effects:

- Newer researchers may be more susceptible to these patterns (e.g., unaware of
  previous terminology).
- Rapid growth **thins the reviewer pool** — increasing the papers-to-reviewers
  ratio and decreasing the fraction of experienced reviewers.
- Less-experienced reviewers may demand architectural novelty, be fooled by
  spurious theorems, and let pass subtle issues like misuse of language.
- Experienced but over-burdened reviewers may revert to a "check-list" mentality,
  rewarding formulaic papers at the expense of intellectually ambitious work.

### 5.3 Misaligned Incentives

Reviewers are not alone in providing poor incentives. As ML garners media
attention and startups proliferate:

- **The press** provides incentives for some of these trends — anthropomorphic
  descriptions provide fodder for popular coverage (*"simulated brain"*,
  *"mimicking human levels of understanding"*).
- **Investors** fund startups sometimes on the basis of a single paper, often
  attracted to research that has received media coverage. Financial incentives
  attach to media attention.

---

## 6. Suggestions

### 6.1 For Authors

Ask **"what worked?"** and **"why?"**, rather than just **"how well?"** Raw
headline numbers provide limited value for scientific progress absent insight
into what drives them. Insight does not necessarily mean theory. Three practices
common in the strongest empirical papers:

- **Error analysis**
- **Ablation studies**
- **Robustness checks** (to hyperparameters, ideally to dataset choice)

Sound empirical inquiry can yield new insights even without a new algorithm —
e.g., demonstrating that SGD-trained networks can fit randomly-assigned labels
(questioning learning-theoretic notions of complexity), or exploring loss
surfaces of deep networks.

**Writing test:** *Would I rely on this explanation for making predictions or
for getting a system to work?* This is a good test of whether a theorem is being
included to please reviewers or to convey actual insight.

Being clear about which problems are open vs. solved encourages follow-up work
and guards against researchers neglecting questions presumed (falsely) to be
resolved.

### 6.2 For Publishers and Reviewers

Reviewers can set better incentives by asking: **"Might I have accepted this
paper if the authors had done a worse job?"** A paper describing a simple idea
that improves performance, with two negative results, should be judged more
favorably than a paper combining three ideas (without ablations) yielding the
same improvement.

- Emphasize **authoritative retrospective surveys** that strip out exaggerated
  claims, change anthropomorphic names to sober alternatives, standardize
  notation.
- **Critical writing** ought to have a voice at ML conferences — neither
  algorithms nor experiments are sufficient for addressing the validity of the
  problems or the methods of inquiry themselves.

---

## 7. Countervailing Considerations

- **Stochastic gradient descent converges faster than gradient descent** — a
  faster, noisier process may yield faster research progress. The ImageNet
  breakthrough paper proposed multiple techniques without ablations, several of
  which were later determined unnecessary; at the time, the results were so
  significant and experiments so expensive that waiting was perhaps not worth
  the cost.
- **High standards might impede publication of original ideas**, which are more
  likely to be unusual and speculative. In economics, high standards result in a
  publishing process that can take years.
- **Specialization**: researchers generating new ideas need not be the same ones
  who carefully distill knowledge.

The authors present these as **strong heuristics rather than unbreakable rules**.
If an idea cannot be shared without violating these heuristics, prefer the idea
be shared and the heuristics set aside.

---

## 8. Historical Antecedents

These issues are not unique to ML or this moment; they recur cyclically.

- **John R. Platt (1964)** — *strong inference*: adherence to specific empirical
  standards was responsible for rapid progress in molecular biology and
  high-energy physics relative to other sciences.
- **Drew McDermott (1976)** — criticized the AI community for abandoning
  self-discipline, warning prophetically: *"if we can't criticize ourselves,
  someone else will save us the trouble."* Discussed suggestive definitions and
  failure to separate speculation from technical claims.
- **Paul Cohen and Adele Howe (1988)** — addressed an AI community that "rarely
  publish[ed] performance evaluations." Suggested analyzing *"why does it
  work?", "under what circumstances won't it work?",* and *"have the design
  decisions been justified?"*
- **Armstrong et al. (2009)** — noted information-retrieval research's tendency
  to compare against the same weak baselines, producing a long series of
  improvements that did not accumulate to meaningful gains.
- **Psychology reproducibility crisis (2015)** — a landmark study suggested a
  significant portion of findings may not be reproducible.
- **N-rays** — enthusiasm paired with undisciplined scholarship led an entire
  community down a blind alley before being debunked.

---

## 9. Concluding Remarks

The community self-corrects precisely through recurring debate about what
constitutes reasonable standards for scholarship. As ML is applied in critical
domains (health, law, autonomous driving), a calibrated awareness of abilities
and limits will enable responsible deployment.

> Flawed scholarship threatens to mislead the public and stymie future research
> by compromising ML's intellectual foundations.
