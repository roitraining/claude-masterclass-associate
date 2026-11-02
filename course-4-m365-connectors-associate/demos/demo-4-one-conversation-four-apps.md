# Demo 4: One Conversation, Four Apps

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Demo:** 4 of 6
**Time:** about 15 minutes

> Part of **[Microsoft 365 Connectors Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Carry one piece of work through Outlook, Excel, Word and PowerPoint without re-explaining it. Time: about 15 minutes.

**Files:** [`demo-files\email-thread-forecast-review.txt`](../demo-files/email-thread-forecast-review.txt), `harbor-peak-forecast-model.xlsx`

**Context:** Dana needs a memo and a short deck from the workbook. The thread holds the asks and the open questions. The add-ins are documented as sharing conversation state, so the chain should continue in each app.

**Steps:**

1. Put the thread in the sandbox mailbox ahead of time, or paste the text into the Claude pane in Outlook or Word.
2. In the first app, ask: "Summarize this thread. List who owes what, the decisions needed, and the file it refers to."
3. Open the workbook in Excel. In the Claude pane, ask: "Using the thread we just discussed, check the points Priya and Marcus raised."
4. Open a new Word document. Ask: "Draft the one-page memo Dana asked for, for the finance committee, from what we found."
5. Open PowerPoint. Ask: "Turn the memo into a three-slide deck."
6. Point at each pane and note that you did not repeat the context.

**Expected result:** The thread summary names the workbook and the two decisions (approve the forecast, confirm the tax rate). The Excel pass finds the low revenue total and the two tax rates. The memo and deck use those findings.

> **Instructor note:** The add-ins "share conversation state" is the documented claim. Whether the conversation continues automatically in each app on the class build, and how Outlook handles an attached workbook, is not confirmed. Rehearse it. If a pane does not carry the conversation, paste a two-line summary and say so; do not hide it. Outlook is a public beta and may not be installed. The Outlook add-in drafts and summarizes. It is not shown sending email here. UNVERIFIED: a secondary source says the add-in does not request Mail.Send. Treat sending as the connector's job and see Demo 5.

> **Why this matters:** The saving is in not rebuilding the context for each app. It only holds if the first summary was right.

---

**Previous:** [Demo 3: Redline a Draft With Judgment](demo-3-redline-a-draft-with-judgment.md) · **Next:** [Demo 5: Map the Reach: Add-in Versus Connector](demo-5-map-the-reach-add-in-versus-connector.md)


*Demo 4 of 6*
