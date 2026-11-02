# Demo 3: Redline a Draft With Judgment

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Demo:** 3 of 6
**Time:** about 12 minutes

> Part of **[Microsoft 365 Connectors Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Use Claude for Word to change tone and enforce consistency with tracked changes, then decide which changes to keep. Time: about 12 minutes.

**Files:** [`demo-files\draft-board-memo.docx`](../demo-files/draft-board-memo.docx)

**Context:** The memo is for a finance committee and reads like a chat message. It also has figures that may not match the workbook.

**Steps:**

1. Open the memo in Word and open the Claude pane.
2. Ask: "Review this memo for a finance committee. List the tone problems, the inconsistent terms and anything unsupported. Do not edit yet."
3. Ask: "Now edit with tracked changes. Use a formal, plain tone. Use one term for clients and one for each quarter."
4. Read the tracked changes. Reject one change you disagree with.
5. Add a Word comment on the tax paragraph and ask Claude to resolve it from the comment.
6. Ask: "Which figures in this memo should I check against the workbook?"

**Expected result:** Claude lists casual wording, mixed terms (customers and clients, Q3 and third quarter), passive phrasing, a missing decision request, and two tax rates (21 and 24 percent). The edits appear as tracked changes. Claude flags the "strong activity" claim as unsupported and does not confirm it.

> **Instructor note:** Tracked changes, redlining and comment-driven editing in Word are documented. How Claude reads a Word comment as an instruction needs rehearsal. Do not let Claude settle the tax rate. That is a decision for a person (Lab 1).

> **Why this matters:** A tracked change is a proposal. The judgment about what a committee should read stays with you.

---

**Previous:** [Demo 2: Pull a Data Source Into Excel](demo-2-pull-a-data-source-into-excel.md) · **Next:** [Demo 4: One Conversation, Four Apps](demo-4-one-conversation-four-apps.md)


*Demo 3 of 6*
