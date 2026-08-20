#!/usr/bin/env python3
"""Paper evaluation scorer.

Parses the aspect files in `quiz/`, reads an answer sheet, and computes
per-aspect and overall scores per the methodology in `quiz/README.md`.

Usage
-----
Generate a blank answer sheet (lists every item as a comment you fill in):

    python score.py --gen-template > answers.txt

Score a filled-in answer sheet:

    python score.py --answers answers.txt
    python score.py --answers answers.txt --json     # machine-readable
    python score.py --answers answers.txt --quiz-dir quiz

Answer-sheet format
-------------------
One item per line:  <ID>: <Yes|No|N/A>
Blank lines and lines starting with '#' are ignored. Unanswered (missing)
items are reported as warnings and counted as non-passes (failures) in the
denominator, so they pull the score down — answer every item or mark N/A.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

ANSWERS = {"yes", "no", "n/a", "na"}  # accepted spellings (case-insensitive)
BANDS = [(85, "Strong"), (70, "Acceptable"), (50, "Borderline"), (0, "Weak")]
GOOD_ASPECT = 80
GOOD_OVERALL = 80
NO_FATAL_FLAW = 60  # no single aspect below this for "good overall"


@dataclass
class Item:
    aspect: str          # e.g. "readability"
    id: str              # e.g. "R01"
    question: str
    pass_if_yes: bool    # True => pass on Yes; False => pass on No
    answer: Optional[str] = None  # "yes" | "no" | "n/a" | None (missing)


@dataclass
class AspectResult:
    name: str
    title: str
    items: List[Item] = field(default_factory=list)

    @property
    def answered(self) -> List[Item]:
        # items with an explicit Yes/No answer (excludes N/A and missing)
        return [i for i in self.items if i.answer in ("yes", "no")]

    @property
    def scored(self) -> List[Item]:
        # denominator: everything not marked N/A. Missing items are included
        # here (and never pass), so unanswered items pull the score down.
        return [i for i in self.items if i.answer != "n/a"]

    @property
    def passes(self) -> int:
        return sum(1 for i in self.answered if _passed(i))

    @property
    def score(self) -> Optional[float]:
        n = len(self.scored)
        if n == 0:
            return None  # entire aspect is N/A
        return 100.0 * self.passes / n

    @property
    def all_na(self) -> bool:
        return bool(self.items) and all(i.answer == "n/a" for i in self.items)

    @property
    def missing(self) -> List[Item]:
        return [i for i in self.items if i.answer is None]


def _passed(item: Item) -> bool:
    if item.answer not in ("yes", "no"):
        return False
    if item.pass_if_yes:
        return item.answer == "yes"
    return item.answer == "no"


def _band(score: Optional[float]) -> str:
    if score is None:
        return "N/A"
    for threshold, label in BANDS:
        if score >= threshold:
            return label
    return "Weak"


# ---------------------------------------------------------------------------
# Parsing the quiz files
# ---------------------------------------------------------------------------

HEADER_RE = re.compile(r"^###\s+([A-Z]+\d+)\.\s*(.*)$")
PASS_RE = re.compile(r"^\-\s*\*\*Pass if:\*\*\s*(Yes|No)", re.IGNORECASE)


def parse_aspect_file(path: Path) -> AspectResult:
    name = path.stem.split("-", 1)[1]  # "01-readability.md" -> "readability"
    title = _title_from_file(path)
    res = AspectResult(name=name, title=title)
    lines = path.read_text(encoding="utf-8").splitlines()
    current: Optional[Item] = None
    for line in lines:
        m = HEADER_RE.match(line)
        if m:
            if current:
                res.items.append(current)
            current = Item(aspect=name, id=m.group(1), question=m.group(2).strip(),
                           pass_if_yes=True)
            continue
        if current:
            pm = PASS_RE.match(line)
            if pm:
                current.pass_if_yes = pm.group(1).lower() == "yes"
    if current:
        res.items.append(current)
    return res


def _title_from_file(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def load_quiz(quiz_dir: Path) -> List[AspectResult]:
    files = sorted(quiz_dir.glob("[0-9][0-9]-*.md"))
    if not files:
        sys.exit(f"No aspect files found in {quiz_dir}")
    return [parse_aspect_file(f) for f in files]


# ---------------------------------------------------------------------------
# Answer sheet
# ---------------------------------------------------------------------------

def gen_template(aspects: List[AspectResult]) -> str:
    out = ["# Paper Evaluation Answer Sheet",
           "# Format:  <ID>: <Yes|No|N/A>     (lines starting with '#' are ignored)",
           "# Unanswered items count as failures — answer every item or mark N/A.",
           ""]
    for a in aspects:
        out.append(f"# === {a.name} ===")
        for it in a.items:
            flag = "Yes" if it.pass_if_yes else "No"
            out.append(f"{it.id}:\t# pass if {flag} — {it.question}")
        out.append("")
    return "\n".join(out)


LINE_RE = re.compile(r"^([A-Z]+\d+)\s*:\s*(\S+)")


def load_answers(path: Path) -> Dict[str, str]:
    answers: Dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        m = LINE_RE.match(line)
        if not m:
            sys.exit(f"Unparseable answer line: {raw!r}")
        item_id, val = m.group(1), m.group(2).strip().lower().rstrip(".")
        if val not in ANSWERS:
            sys.exit(f"Invalid answer for {item_id}: {val!r} (use Yes / No / N/A)")
        answers[item_id] = "n/a" if val == "na" else val
    return answers


def apply_answers(aspects: List[AspectResult], answers: Dict[str, str]) -> None:
    seen = set()
    for a in aspects:
        for it in a.items:
            seen.add(it.id)
            it.answer = answers.get(it.id)
    extra = set(answers) - seen
    for item_id in sorted(extra):
        print(f"warning: answer for unknown item {item_id} ignored", file=sys.stderr)
    for a in aspects:
        for it in a.missing:
            print(f"warning: {it.id} ({a.name}) unanswered — counted as failure",
                  file=sys.stderr)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report_text(aspects: List[AspectResult]) -> str:
    # Widen the name column to fit the longest aspect name so long names
    # (e.g. "data_quality_documentation") don't shift the rest of the row.
    width = max([22] + [len(a.name) + 2 for a in aspects])
    rule = width + 45  # width of a full row under the format strings below
    lines = []
    lines.append("=" * rule)
    lines.append("PAPER EVALUATION SCORES")
    lines.append("=" * rule)
    lines.append(f"{'Aspect':<{width}}{'Score':>8}  {'Band':<12}{'Pass':>6}/"
                 f"{'Scor':>4}  {'N/A':>4}  {'Miss':>4}")
    lines.append("-" * rule)
    scored = []
    for a in aspects:
        na = sum(1 for i in a.items if i.answer == "n/a")
        miss = len(a.missing)
        scor = len(a.scored)
        score = a.score
        if score is None:
            lines.append(f"{a.name:<{width}}{'N/A':>8}  {'—':<12}{a.passes:>6}/{scor:>4}  "
                         f"{na:>4}  {miss:>4}")
        else:
            scored.append(score)
            lines.append(f"{a.name:<{width}}{score:>7.1f}%  {_band(score):<12}"
                         f"{a.passes:>6}/{scor:>4}  {na:>4}  {miss:>4}")
    lines.append("-" * rule)
    if scored:
        overall = sum(scored) / len(scored)
        worst = min(scored)
        good_overall = overall >= GOOD_OVERALL and worst >= NO_FATAL_FLAW
        lines.append(f"{'OVERALL':<{width}}{overall:>7.1f}%  {_band(overall):<12}"
                     f"   good overall: {'YES' if good_overall else 'no'}")
        lines.append(f"{'worst aspect':<{width}}{worst:>7.1f}%   "
                     f"(no aspect < {NO_FATAL_FLAW}: "
                     f"{'YES' if worst >= NO_FATAL_FLAW else 'no'})")
    else:
        lines.append("OVERALL: no applicable aspects (all N/A)")
    lines.append("=" * rule)

    # Per-aspect failure detail (revision checklist)
    for a in aspects:
        failed = [i for i in a.answered if not _passed(i)]
        if not failed:
            continue
        lines.append("")
        lines.append(f"=== {a.name} — failed items ({len(failed)}) ===")
        for it in failed:
            flag = "Yes" if it.pass_if_yes else "No"
            lines.append(f"  {it.id} [pass if {flag}, answered {it.answer}] "
                         f"{it.question}")
    return "\n".join(lines) + "\n"


def report_json(aspects: List[AspectResult]) -> str:
    scored = [a.score for a in aspects if a.score is not None]
    overall = sum(scored) / len(scored) if scored else None
    worst = min(scored) if scored else None
    payload = {
        "aspects": [
            {
                "name": a.name,
                "title": a.title,
                "score": a.score,
                "band": _band(a.score),
                "scored": len(a.scored),
                "answered": len(a.answered),
                "passes": a.passes,
                "na": sum(1 for i in a.items if i.answer == "n/a"),
                "missing": len(a.missing),
                "failed": [
                    {"id": i.id, "question": i.question,
                     "pass_if": "Yes" if i.pass_if_yes else "No",
                     "answer": i.answer}
                    for i in a.answered if not _passed(i)
                ],
            }
            for a in aspects
        ],
        "overall": overall,
        "overall_band": _band(overall) if overall is not None else None,
        "worst_aspect": worst,
        "good_overall": (overall is not None and overall >= GOOD_OVERALL
                         and (worst is None or worst >= NO_FATAL_FLAW)),
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--quiz-dir", default="quiz", type=Path,
                   help="directory with aspect .md files (default: quiz)")
    p.add_argument("--answers", type=Path, help="answer sheet to score")
    p.add_argument("--json", action="store_true", help="emit JSON instead of text")
    p.add_argument("--gen-template", action="store_true",
                   help="print a blank answer sheet to stdout and exit")
    args = p.parse_args(argv)

    aspects = load_quiz(args.quiz_dir)

    if args.gen_template:
        sys.stdout.write(gen_template(aspects))
        return 0

    if not args.answers:
        p.error("--answers is required (or use --gen-template)")
    if not args.answers.exists():
        p.error(f"answers file not found: {args.answers}")

    answers = load_answers(args.answers)
    apply_answers(aspects, answers)

    out = report_json(aspects) if args.json else report_text(aspects)
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
