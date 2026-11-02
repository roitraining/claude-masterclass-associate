# Demo 5: Score a Skill Against a Test Set

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Demo:** 5 of 6
**Time:** about 15 minutes

> Part of **[Claude.ai Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Run a Skill against questions with known answers, score the result, and decide what to check every time versus sample. Time: about 15 minutes.

**Files:** [`demo-files/demo5/fee-qa-skill/`](../demo-files/demo5/fee-qa-skill) (a Skill with a 2026 fee schedule and a retired 2025 one), `test-set.csv`, `sample-run-results.csv`, `scoring-sheet.csv`

**Context:** The test set has ten questions with known answers. Each can fail in one of four ways: arithmetic, omission, stale source, citation mismatch. To save time, a sample run is provided with errors already in it.

**Steps:**

1. Open `test-set.csv`. Read three questions and their known answers.
2. Install the `fee-qa-skill` folder and run questions 1 to 3 live in new chats. Compare each to the known answer.
3. Open `sample-run-results.csv`. Score each of the ten rows 1 or 0 against `test-set.csv` and write the error category for each miss.
4. Compute the pass rate.
5. Ask the room: which error categories do we check on every run, and which can we sample?
6. Decide one fix to the Skill for the worst error, for example "show the arithmetic," and say how you would retest.

**Expected result:** Score 6 of 10, a 60 percent pass rate. The four misses are question 1 ($10, stale source), question 3 ($155, arithmetic), question 4 ($108, omission of the 3-fee daily cap), and question 9 (cites 2.2 and not 2.3, citation mismatch). Suggested policy: check every dollar figure every time, since arithmetic and stale-source errors are cheap to catch and costly to miss, and sample citation wording and phrasing.

> **Instructor note:** The live runs depend on Skill triggering and may differ from the sample run. If a live answer is correct, say so, then move to the sample file. The scoring method is the point. The retired 2025 file inside the Skill is a deliberate trap, and whether Claude uses it depends on the model, so a stale answer is possible but not guaranteed.

> **Why this matters:** A Skill without a test set is a guess you repeat. Ten questions and a pass rate turn "it seems fine" into evidence, and the error taxonomy tells you where to put the human check.

---

**Previous:** [Demo 4: Research With Conflicting Sources](demo-4-research-with-conflicting-sources.md) · **Next:** [Demo 6: Build an AI-Powered Artifact](demo-6-build-an-ai-powered-artifact.md)


*Demo 5 of 6*
