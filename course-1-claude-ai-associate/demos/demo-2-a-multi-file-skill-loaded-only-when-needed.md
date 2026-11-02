# Demo 2: A Multi-File Skill, Loaded Only When Needed

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Demo:** 2 of 6
**Time:** about 12 minutes

> Part of **[Claude.ai Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Design a Skill so the main file stays small and detail files load only when a situation calls for them. Time: about 12 minutes.

**Files:** [`demo-files/demo2/pinecrest-meeting-recap/`](../demo-files/demo2/pinecrest-meeting-recap) (with `SKILL.md` and three files in `references/`), [`demo-files/demo2/test-notes.md`](../demo-files/demo2/test-notes.md)

**Context:** The main file holds the rules and points to three reference files. Two of them are conditional. The escalation file carries a reference code (ESC-7 or ESC-9) that can only appear if Claude read that file, which makes loading visible.

**Steps:**

1. Open `SKILL.md` and read out the two "read the matching file only if" lines. Open the `references` folder.
2. Install the folder as a Skill and turn off other test Skills.
3. Run Notes A from `test-notes.md` in a new chat. Check the recap has no reference code and no compliance line.
4. Run Notes B in a new chat. Look for the Member Complaints Desk and the code ESC-7.
5. Run Notes C in a new chat. Look for the compliance line with rule CF-3, and no ESC code.
6. Ask the room: what would break if all three reference files were pasted into the main `SKILL.md`?

**Expected result:** Notes A gives a plain recap. Notes B includes extension 4417 and ESC-7. Notes C includes the line "Compliance review: statement about returns or guarantees (rule CF-3)." Each reference file appears only when its situation does.

> **Instructor note:** Loading other files only as needed is verified. The body should stay under 500 lines, and this one is far smaller. Whether Claude reads the right file on every run is the model's call, so one miss is possible. Rerun the failing case once and discuss it as a design lesson about clearer wording in `SKILL.md`. The zip upload steps are UNVERIFIED, as in Demo 1.

> **Why this matters:** A Skill that carries every rule in one file pays for all of it on every run and becomes hard to review. Splitting by situation keeps each run focused and each file owned and reviewable.

---

**Previous:** [Demo 1: A Skill That Never Triggers](demo-1-a-skill-that-never-triggers.md) · **Next:** [Demo 3: Read Tools and Write Tools: Design a Connector](demo-3-read-tools-and-write-tools-design-a-connector.md)


*Demo 2 of 6*
