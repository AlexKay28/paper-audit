# Aspect 21 — Scientific Storytelling (Narrative Structure)

**Dimension:** Does the paper carry the reader through one coherent
problem-solving arc — context, challenge, action, resolution — with complexity
scaffolded so the argument can actually be reconstructed?

**Source basis:** `../rules/07-scientific-storytelling.md` §1–7 (OCAR, ABT,
information laddering, curiosity gaps, prose mechanics);
`../rules/04-troubling-trends-lipton-steinhardt.md` §1 (Speculation), §3–4
(Mathiness, Misuse of Language); `../rules/03-ml-reviewer-guidelines.md`
§Clarity; `../rules/06-ai-review-prompt.md` §2,4.

## How to answer

Answer each item **Yes** / **No** / **N/A**. **Pass if** states which answer
counts as a pass. See `README.md` for scoring.

This aspect judges *structure and communication*, not correctness — a sound
paper can score badly here, and that is the signal it is meant to give. A few
items are **N/A** when the device in question is absent by design (e.g. ST13 if
the paper uses no analogies, ST14 if there is no method to exemplify).

Note the overlap with `01-readability.md`: readability asks whether individual
sentences, symbols, and figures are legible; this aspect asks whether the paper
as a whole is a single argument with a beginning, a tension, and an end.

## Items

### ST01. Does the opening establish the context a reader needs before the specific problem is named?
- **Pass if:** Yes
- **Rationale:** The Opening of OCAR builds the world the challenge lives in;
  without it the gap has nothing to be a gap in.
- **Source:** `07` §2

### ST02. Does the introduction state an explicit challenge or knowledge gap, rather than only listing prior work?
- **Pass if:** Yes
- **Rationale:** A related-work recital is not a Challenge; the reader must be
  told what is missing and why it matters.
- **Source:** `07` §2, §3; `03` §Clarity

### ST03. Can the paper's central question be stated in a single sentence?
- **Pass if:** Yes
- **Rationale:** If the question cannot be compressed to one sentence, the paper
  is likely answering several, and the arc has no single spine.
- **Source:** `07` §2, §3

### ST04. Does the Discussion/Conclusion resolve the challenge raised in the opening (rather than landing on a different takeaway)?
- **Pass if:** Yes
- **Rationale:** OCAR closure: a Resolution that answers a question the paper
  never posed leaves the stated gap open.
- **Source:** `07` §2

### ST05. Is the abstract a complete arc (context → gap → approach → finding → meaning)?
- **Pass if:** Yes
- **Rationale:** The abstract is the whole arc in miniature and is the only part
  most readers will finish.
- **Source:** `07` §2; `02` (abstracts are used in reviewer bidding)

### ST06. Does the title state a finding or claim rather than only naming a topic?
- **Pass if:** Yes
- **Rationale:** "X improves Y under Z" carries the arc; "On X and Y" defers all
  of it to the reader.
- **Source:** `07` §2

### ST07. Can the core argument be written as a single ABT (And / But / Therefore) sentence?
- **Pass if:** Yes
- **Rationale:** The ABT test exposes whether a cause-and-effect arc exists at
  all, or only a topic and some results.
- **Source:** `07` §3

### ST08. Does the introduction read as an "and-then" list of facts with no cause-and-effect linkage?
- **Pass if:** No
- **Rationale:** "And-then" writing is the narrative-free data dump the ABT
  framework exists to replace.
- **Source:** `07` §3

### ST09. Does each major section transition make clear why the next step follows from the previous one?
- **Pass if:** Yes
- **Rationale:** Sections joined only by sequence force the reader to supply the
  logic themselves.
- **Source:** `07` §2, §3; `03` §Clarity

### ST10. Is there a stated tension — an anomaly, contradiction, or failure of existing methods — motivating the work?
- **Pass if:** Yes
- **Rationale:** The "But" is the engine; without opposition there is no
  narrative movement, only description.
- **Source:** `07` §3, §7

### ST11. Does the paper keep a single central conflict rather than several competing ones?
- **Pass if:** Yes
- **Rationale:** Multiple competing "Buts" fragment the arc and leave the reader
  unsure which question the paper actually answers.
- **Source:** `07` §3

### ST12. Is each core technical concept introduced with an intuition or analogy before its formal definition?
- **Pass if:** Yes
- **Rationale:** Rung one of the information ladder; formalism without a prior
  anchor produces cognitive overload.
- **Source:** `07` §4

### ST13. Where analogies are used, is it stated where they break down?
- **Pass if:** Yes
- **Rationale:** An analogy with no stated limits becomes a false model the
  reader carries through the rest of the paper. **N/A** if no analogies are used.
- **Source:** `07` §4

### ST14. Is there a concrete running example or toy case grounding the abstract machinery?
- **Pass if:** Yes
- **Rationale:** Concreteness is what lets a reader test their understanding of
  the abstraction as they go.
- **Source:** `07` §4, §6

### ST15. Is there a one-paragraph plain version of the method before the full technical treatment?
- **Pass if:** Yes
- **Rationale:** The simplified conceptual baseline (rung two) lets a reader
  hold the shape of the method before the details arrive.
- **Source:** `07` §4

### ST16. Is terminology density on the opening page low enough for a reader outside the immediate subarea to follow?
- **Pass if:** Yes
- **Rationale:** Every undefined term in the opening is borrowed against the
  reader's attention before any of it has been earned.
- **Source:** `07` §4, §1; `06` §2

### ST17. Does the opening create a specific gap the reader wants closed (a paradox, surprise, or failed expectation)?
- **Pass if:** Yes
- **Rationale:** Deprivation-type curiosity — a contradiction in what the reader
  thought they understood — is the strongest engine for reading on.
- **Source:** `07` §5

### ST18. Is the counterintuitive or surprising element of the results made explicit rather than buried in a table?
- **Pass if:** Yes
- **Rationale:** A surprise the reader has to derive for themselves is a
  surprise most readers will miss.
- **Source:** `07` §5; `06` §4

### ST19. Are results framed against the reader's likely prior expectation?
- **Pass if:** Yes
- **Rationale:** A number is only legible as a finding relative to what one
  would have predicted without the paper.
- **Source:** `07` §5

### ST20. Does the paper open a hook or promise that the results never pay off?
- **Pass if:** No
- **Rationale:** An unpaid curiosity gap is a rhetorical debt, and reads to a
  reviewer as overclaiming.
- **Source:** `07` §5; `04` §1

### ST21. Is the most important information placed in the stress position (end of sentence, paragraph, section)?
- **Pass if:** Yes
- **Rationale:** Readers retain what sits at the end of a unit; burying the key
  item mid-paragraph wastes the emphasis the position provides.
- **Source:** `07` §2, §6

### ST22. Does each paragraph make a single point, stated in its first or last sentence?
- **Pass if:** Yes
- **Rationale:** One paragraph, one point is what makes a paper skimmable
  without loss of argument.
- **Source:** `07` §2, §6

### ST23. Is the prose predominantly active voice, with the actor named where agency matters?
- **Pass if:** Yes
- **Rationale:** Passive constructions hide who did what to which data — an
  ambiguity that matters for methods and claims alike.
- **Source:** `07` §6, §1

### ST24. Is jargon used only where it buys precision, rather than as a marker of rigor?
- **Pass if:** Yes
- **Rationale:** Terminology deployed for authority rather than exactness is the
  language-misuse failure mode.
- **Source:** `07` §6; `04` §3–4

### ST25. Does the paper use narrative framing to imply significance beyond what the evidence supports?
- **Pass if:** No
- **Rationale:** Narrative technique is subordinate to precision; dramatic
  framing must not do work the results cannot.
- **Source:** `07` §1, §6; `04` §1, §6.1

### ST26. Does the figure sequence tell the story on its own — could a reader follow the argument from the figures alone?
- **Pass if:** Yes
- **Rationale:** Reviewers skim figures first; a figure sequence that carries
  the arc is a second, faster path through the paper.
- **Source:** `07` §2; `06` §4

### ST27. After reading only the abstract and introduction, could a reader outside the subarea state the paper's contribution?
- **Pass if:** Yes
- **Rationale:** The end-to-end test of the arc: context, challenge, and claimed
  resolution all delivered before the technical body begins.
- **Source:** `07` §1, §2
