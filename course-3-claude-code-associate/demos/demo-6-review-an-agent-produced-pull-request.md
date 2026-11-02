# Demo 6: Review an Agent-Produced Pull Request

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 6 of 9
**Time:** about 15 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Review a pull request an agent wrote with a checklist, a diff-size limit, a required-tests gate, and a merge order. Time: about 15 minutes.

**Files:** [`$FILES/agent-pr/sd-142-promo-codes.diff`](../demo-files/agent-pr/sd-142-promo-codes.diff), with [`$FILES/shipdesk/TICKET-SD-142.md`](../demo-files/shipdesk/TICKET-SD-142.md) as the ticket.

**Context:** The diff passes its tests. It has two planted problems that a green test run does not reveal. Review it against the ticket.

**Steps:**

1. Put the checklist on screen:
   - Does the diff stay inside the ticket's files and scope?
   - Is the diff within the size limit (4 files, 150 lines)?
   - Do tests cover each acceptance criterion?
   - Did any test change to match the code instead of the other way round?
   - Is merge order clear when other branches are open?
2. Show the size: `git apply --stat $FILES/agent-pr/sd-142-promo-codes.diff`.
3. Read the diff aloud. Ask the room what they would not approve.
4. Ask Claude Code to review it: "Review this diff against TICKET-SD-142.md. List every change the ticket does not ask for and every test that does not match an acceptance criterion."
5. Compare Claude's findings with the room's. Decide: merge, change, or reject.
6. Apply it to a scratch copy to show the tests are green anyway:

```
git apply $FILES/agent-pr/sd-142-promo-codes.diff && python -m pytest -q
git checkout -- . && git clean -fdq shipdesk/promos.py tests/test_promos.py
```

7. State the merge-order rule: smallest and most independent first, shared files last, tests rerun after each merge.

**Expected result:** The room finds two problems. First, an expired promo is accepted: the date check does nothing (`pass`), and the test was rewritten as `test_expired_code_still_applies` to match, breaking acceptance criterion 3. Second, `FREE_SHIPPING_THRESHOLD` changed from 75.00 to 25.00, which the ticket puts out of scope, and no test notices. All 19 tests pass.

> **Instructor note:** Claude's review is advisory. It does not approve or block a pull request. The human gate before the merge is what stops a bad change. The size limit and the tests-before-commit hook from Demo 5 are the automated gates. Step 6 uses `git clean` on two named paths only. Run it in the scratch copy.

> **Why this matters:** A green test run proves the code matches its tests. It does not prove the tests match the ticket.

---

**Previous:** [Demo 5: A Hook That Runs Tests Before You Commit](demo-5-a-hook-that-runs-tests-before-you-commit.md) · **Next:** [Demo 7: Agent Teams, Instructor Only](demo-7-agent-teams-instructor-only.md)


*Demo 6 of 9*
