# Demo 4: Dispatch: Check and Steer From a Phone

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 4 of 7
**Time:** about 15 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Describe Dispatch, where it can and cannot be used today, and what a phone instruction can trigger on a desktop. Time: about 15 minutes.

**Files:** [`demo-files/dispatch`](../demo-files/dispatch): `dispatch-sandbox` and `phone-instructions.md`.

**Context:** Dispatch is one conversation across a phone and a desktop. The desktop does the work with local files, connectors, and plugins. **Dispatch is a limited beta on some Pro and Max plans. It is not available to new users.** Expect that most students cannot use it. The instructor demonstrates on an account that has it, and students who can access Dispatch may follow along. Everyone else follows the fallback path.

**Steps (instructor demonstration):**

1. State the access limits above. Ask who has Dispatch. Note the count.
2. On the instructor desktop, share only the `dispatch-sandbox` folder. Keep the computer awake and Claude Desktop open.
3. From the phone, send instruction 1 from `phone-instructions.md`. Read the result on the phone.
4. Send instruction 2. Then instruction 3, which edits a file. Open the file on the desktop to confirm.
5. Before sending instruction 4, ask the room: what will the desktop do? Send it and record what you were asked before the delete.
6. Close the demo: a phone instruction acted on files on a desktop. Ask who else could type that instruction if the phone was lost.

**Fallback path (no Dispatch):**

1. Start a cloud task from the desktop with `q3-exceptions-summary.csv` attached and ask for a two-sentence summary.
2. Check the task from the Claude mobile app or from claude.ai in a browser.
3. Ask: what could this phone check NOT do that Dispatch could? Answer: it cannot reach local files, connectors, or plugins on the desktop, and it cannot start work there.

**Expected result:** Instructions 1 and 2 are read only. Instruction 3 changes the file. Instruction 4 asks for approval or confirmation before the delete, and the file is only removed if approved. In the fallback, the cloud task completes and its result is visible from the phone.

> **Instructor note:** Everything about what Dispatch reaches comes from Anthropic's help article. The setup path is Dispatch on the left side panel, then Get started, then the file access and keep-awake toggles, then Finish setup. The exact approval behavior for a phone-sent delete is **unconfirmed**. Treat it as an observation, not a promise. Computer use is not available on Linux. Rehearse on the real account the day before.

> **Why this matters:** Remote steering extends your desktop's reach to anything that can send it an instruction. Treat the phone as a credential.

---

**Previous:** [Demo 3: Schedule a Briefing, Then Read a Run](demo-3-schedule-a-briefing-then-read-a-run.md) · **Next:** [Demo 5: Break It on Purpose: Unattended Failure](demo-5-break-it-on-purpose-unattended-failure.md)


*Demo 4 of 7*
