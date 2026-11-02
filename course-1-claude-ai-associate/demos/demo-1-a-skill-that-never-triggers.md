# Demo 1: A Skill That Never Triggers

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Demo:** 1 of 6
**Time:** about 12 minutes

> Part of **[Claude.ai Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Show that the description decides whether a Skill loads, by fixing a Skill that never fires. Time: about 12 minutes.

**Files:** [`demo-files/demo1/vague-skill/SKILL.md`](../demo-files/demo1/vague-skill/SKILL.md), [`demo-files/demo1/fixed-skill/SKILL.md`](../demo-files/demo1/fixed-skill/SKILL.md), [`demo-files/demo1/trigger-inputs.md`](../demo-files/demo1/trigger-inputs.md)

**Context:** The two Skills have identical bodies. Only the description differs. The vague one says "Helps with meetings and member stuff." Claude sees only the name and description until it decides a Skill is relevant, so the description is the whole trigger.

**Steps:**

1. Install `vague-skill` as a Skill in your account and turn it on. Turn all other test Skills off.
2. Paste input T1 from `trigger-inputs.md` into a new chat. Watch for the **Loaded skill** chip above the answer, then note whether the answer uses the heading "Pinecrest Recap". If Claude asks a clarifying question first, choose **Skip** and let it answer.
3. Run T2 and T3 in new chats. Record triggered or not for each.
4. Run N1 to N3 in new chats. Record each.
5. Replace the Skill with `fixed-skill`. Say aloud what the new description adds: what it does, when to use it, and when not to.
6. Rerun all six inputs. Record the results in a small table on the board.

**Expected result:** With the vague description, one or more of T1 to T3 usually fails to produce the recap format and shows no Loaded skill chip. With the fixed description, T1 to T3 show the chip and produce "Pinecrest Recap", and N1 to N3 produce ordinary answers. Triggering can vary, so show your own table and not a promised score.

> **Run on a Max account, October 22, 2026, Opus 5.5.** T1 with the vague Skill produced an ordinary email plus an internal call note, no chip and no Pinecrest heading. The same input with only the fixed Skill produced the chip and a correct recap, including "Not set" for the missing due dates and "Lending (person not named)" rather than an invented owner. The demo behaves as written.

> **Instructor note:** The Skill folder layout, the YAML description, and progressive loading are verified. **There is an interface signal, confirmed in the product on October 22, 2026:** a **Loaded skill** chip appears above the answer, and a "Used in this session - Skills: <name>" card appears at the end. Point at those rather than inferring from the output format; it is the strongest moment in this demo. **Adding a Skill:** Settings, then Customize, then Skills, then **+ Add**, which offers "Upload skill", "Create a skill" and "Create with Claude". Creating one in the form is faster in class than zipping a folder, and custom Skills work on Free as well as paid. Size limits are still UNVERIFIED. **Expect interruptions:** on the untriggered run Claude may ask one or two clarifying questions before answering; choose Skip. A vague Skill may still trigger sometimes. If it does on every input, shorten the description further.

> **Why this matters:** A Skill that does not trigger is invisible and gets blamed on the model. Writing the description to say what, when, and when not is the cheapest reliability fix there is.

---

**Next:** [Demo 2: A Multi-File Skill, Loaded Only When Needed](demo-2-a-multi-file-skill-loaded-only-when-needed.md)


*Demo 1 of 6*
