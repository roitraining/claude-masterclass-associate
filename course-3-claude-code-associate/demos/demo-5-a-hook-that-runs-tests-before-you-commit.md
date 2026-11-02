# Demo 5: A Hook That Runs Tests Before You Commit

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 5 of 9
**Time:** about 10 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Require passing tests before a commit, with a hook as the gate. Time: about 10 minutes.

**Files:** [`$FILES/hooks/run_tests_before_commit.py`](../demo-files/hooks/run_tests_before_commit.py) (already copied in Demo 4) and [`$FILES/shipdesk/tests/`](../demo-files/shipdesk/tests).

**Context:** The same exit code 2 mechanism, used as a quality gate. The script runs only when the Bash command contains `git commit`.

**Steps:**

1. Confirm the hook is in `.claude/settings.json` from Demo 4. It is the second command under the `Bash` matcher.
2. In `~/work/shipdesk`, break a test on purpose by changing `17.65` to `18.65` in `tests/test_pricing.py`.
3. In `claude`, ask: "Commit the current changes with the message 'wip'."
4. Read the block message and the test failure it carries.
5. Ask Claude to fix the test, then commit again.
6. Run `git log --oneline` to show the commit landed only after the tests passed.

**Expected result:** The first commit is blocked with "Commit blocked: tests are failing" and the pytest tail. Claude fixes the cause and the second commit succeeds.

> **Instructor note:** Same unverified details as Demo 4: the stdin JSON, and that the hook runs in the project directory. The script uses `.venv/bin/python` when present, so activate the environment or keep it at that path. This gate protects commits made through Claude's Bash tool, and not commits a person makes in their own terminal. Say so.

> **Why this matters:** A test requirement that depends on a person remembering is a hope. A hook makes it a rule.

---

**Previous:** [Demo 4: A Hook That Blocks a Dangerous Command](demo-4-a-hook-that-blocks-a-dangerous-command.md) · **Next:** [Demo 6: Review an Agent-Produced Pull Request](demo-6-review-an-agent-produced-pull-request.md)


*Demo 5 of 9*
