# Paper Review Guidelines & Checklists

A curated reference set of official conference checklists, reviewer instructions,
and foundational AI/ML paper-evaluation guides. Use these as prompt context for
LLM-assisted paper review, or as a pre-submission self-audit.

## Contents

| # | File | Source | Focus |
|---|------|--------|-------|
| 1 | [`01-neurips-paper-checklist.md`](01-neurips-paper-checklist.md) | [NeurIPS Paper Checklist Guidelines](https://neurips.cc/public/guides/PaperChecklist) | 16-question mandatory checklist: reproducibility, transparency, ethics, societal impact |
| 2 | [`02-iclr-author-guide.md`](02-iclr-author-guide.md) | [ICLR 2025 Author Guide](https://iclr.cc/Conferences/2025/AuthorGuide) | Double-blind review, code submission, ethics & reproducibility statements |
| 3 | [`03-ml-reviewer-guidelines.md`](03-ml-reviewer-guidelines.md) | [ML Reviewer Guidelines (PNemo04/My_skills)](https://github.com/PNemo04/My_skills/blob/main/skills/research-writing/ml-paper-writing/references/reviewer-guidelines.md) | Cross-conference scoring rubrics (NeurIPS/ICML/ICLR/ACL) + rebuttal best practices |
| 4 | [`04-troubling-trends-lipton-steinhardt.md`](04-troubling-trends-lipton-steinhardt.md) | [Lipton & Steinhardt, arXiv:1807.03341](https://arxiv.org/abs/1807.03341) | 4 rejection traps: mathiness, speculation, bad ablations, language misuse |
| 5 | [`05-pineau-reproducibility-checklist.md`](05-pineau-reproducibility-checklist.md) | [Pineau et al. Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf) | Gold-standard 2-page checklist: hyperparameters, seeds, baseline fairness |
| 6 | [`06-ai-review-prompt.md`](06-ai-review-prompt.md) | Synthesized from sources above | Ready-to-paste prompt for LLM-based paper review |

## How to Use

1. **Pre-submission self-audit** — Work through `01` and `05` against your draft.
2. **Anticipate reviewer concerns** — Read `03` and `04`; pre-empt common critiques.
3. **LLM-assisted review** — Paste your paper plus the prompt in `06`.
4. **Conference-specific compliance** — Refer to `02` (ICLR) and the ICLR section of `03`.

## Source Notes

- All conference content was fetched from the official sites listed above on
  Aug 19, 2026. Always cross-check the current year's CFP before submission,
  because guidelines are revised annually.
- The Pineau checklist PDF is rendered from the binary content of the original
  PDF; the structured items here are the canonical reproduction.
