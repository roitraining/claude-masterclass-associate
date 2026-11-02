# Microsoft 365 Connectors Associate: Demos

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Contents:** 6 instructor-led demos. Each takes 15 minutes or less and has a learning objective. The numbers match the Today's Demos slide.

---

## About this guide

Each demo has the same layout: a learning objective, a time, a Files line when the demo uses files, a short context paragraph, steps, an Expected result, an Instructor note, and a Why this matters note.

Two products are in play, and they stay separate in every demo:

- **The Office add-ins** (Excel, Word, PowerPoint, Outlook) run in a sidebar inside the app you are driving.
- **The Microsoft 365 connector** is a chat-side integration that searches Outlook, Teams, SharePoint and OneDrive. Its optional write tools are what can send email or change calendar events, and only when enabled and approved by an administrator.

Anything that touches a Microsoft 365 tenant, the connector, or a financial data source is run by the instructor on the ROI sandbox tenant only. Students watch and use the sample files. Never use a production mailbox, a production drive, or real client data.

The files are in `demo-files`:

- `harbor-peak-forecast-model.xlsx`: a messy five-tab workbook (Assumptions, Revenue, Costs, P&L, Summary).
- `industry-benchmarks.csv`: fictional peer medians.
- `email-thread-forecast-review.txt`: a five-message thread that references the workbook.
- `draft-board-memo.docx`: a draft memo.
- `plays\`: four finance plays, each a dataset and a brief.
- `ANSWER-KEY.md`: facilitator only.

Every person, company and figure is fictional. Claude can produce different wording each time, so check results against the Expected result and not exact text. The add-in menus and button names can change between builds, so these steps say "open the Claude pane" and do not depend on exact labels. Rehearse each demo on the class build.

> **Work on a copy.** Save a copy of each file before a demo. Claude for Excel writes to cells.

---

## Prerequisites

- [ ] **Instructor:** an ROI sandbox Microsoft 365 tenant (Microsoft Entra) with a business plan, a mailbox, a OneDrive, a SharePoint site and a Teams channel containing only fictional content. Personal Microsoft accounts do not work with the connector.
- [ ] **Instructor:** the Excel, Word and PowerPoint add-ins installed from Microsoft AppSource. The Outlook add-in is optional.
- [ ] **Instructor:** the connector enabled by an Owner and consented by an Entra Global Administrator on the sandbox tenant, read tools on. Write tools off unless Demo 5 says otherwise.
- [ ] The `demo-files` folder on the instructor machine.

---

## Demo 1: Trace and Debug a Broken Formula

**Learning objective:** Use Claude for Excel to trace a number across tabs and find a formula that is silently wrong. Time: about 12 minutes.

**Files:** `demo-files\harbor-peak-forecast-model.xlsx`

**Context:** Total revenue looks low against its service lines, and nobody has traced it. Do not look at the formulas first. Let Claude find the cause.

**Steps:**

1. Open a copy of the workbook in Excel and enable editing.
2. Open the Claude pane.
3. Ask: "Map how the five tabs connect. Which tabs feed the P&L?"
4. Ask: "Total revenue on the Revenue tab looks low compared with the lines above it. Trace it and tell me why."
5. Read the explanation. Select `Revenue!B9` and check the range yourself.
6. Ask Claude to fix the totals for all three years and to list every cell it changed.
7. Ask: "Which cells on the P&L and Summary tabs change because of this?"

**Expected result:** Claude explains that the Revenue totals sum rows 4 to 7 and leave out row 8, Reporting Subscriptions. FY2026 total moves from 11,400,000 to 12,380,000. The fix flows to the P&L and Summary. Claude lists the cells it changed.

> **Instructor note:** The workbook contains two further planted errors. Do not reveal them here. They are the work of Lab 1. The Excel add-in reading and writing cells, formulas and formatting is documented. The exact menu wording and how it presents its change list need rehearsal on the class build.

> **Why this matters:** A total that is a little low reads as plausible. Claude's trace is only useful if you check the formula it points to.

---

## Demo 2: Pull a Data Source Into Excel

**Learning objective:** Bring an external figure into a model with its source and date attached. Time: about 12 minutes.

**Files:** `demo-files\industry-benchmarks.csv`

**Context:** The board will ask how the forecast compares with peers. This demo sources a peer median instead of pasting a number from memory. The default path uses the sample CSV so it works on every plan and tenant.

**Steps:**

1. In the corrected workbook, add a tab named Benchmarks.
2. Import `industry-benchmarks.csv` into that tab.
3. Ask Claude: "Compare our FY2027 EBIT margin with the peer median in the Benchmarks tab. Show the figure, its source and its as-of date."
4. Check the answer against the cells it cites.
5. Ask Claude to add a row to the Summary tab with the peer median, the source note and the as-of date.
6. Optional, only if the sandbox plan has a financial data connector in Excel: repeat step 3 against the connector and compare the figure with the CSV.

**Expected result:** Claude reports a peer median EBIT margin of 18 percent, the FY2027 model margin of about **19.3 percent**, and the source note and the 2026-06-30 date. The Summary tab has a sourced row.

> **On that 19.3 percent.** Demo 1 fixed only the Revenue SUM range, so at this point FY2027 EBIT is 2,527,960 on revenue of 13,122,800, which is 19.26 percent. The figure rises to **19.5 percent** (EBIT 2,561,960) only after the hardcoded 12 percent marketing cell in `Costs!C7` is also fixed, and that error is held back for Lab 1. Recomputed from the workbook on October 22, 2026. If you say 19.5 here, the screen will disagree with you.

> **Instructor note:** UNVERIFIED. The financial data connector names in the outline (S&P Global, LSEG, Moody's, FactSet) come from another course outline and are not confirmed. Do not promise them. Say that the demo works with the CSV and that a connector, if present, follows the same pattern. If you run step 6, rehearse it first and treat the result as unconfirmed.

> **Why this matters:** A figure without a source and a date cannot be defended in front of a board.

---

## Demo 3: Redline a Draft With Judgment

**Learning objective:** Use Claude for Word to change tone and enforce consistency with tracked changes, then decide which changes to keep. Time: about 12 minutes.

**Files:** `demo-files\draft-board-memo.docx`

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

## Demo 4: One Conversation, Four Apps

**Learning objective:** Carry one piece of work through Outlook, Excel, Word and PowerPoint without re-explaining it. Time: about 15 minutes.

**Files:** `demo-files\email-thread-forecast-review.txt`, `harbor-peak-forecast-model.xlsx`

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

## Demo 5: Map the Reach: Add-in Versus Connector

**Learning objective:** Separate what the add-ins can see from what the connector can search, and read from write on each surface. Time: about 15 minutes.

**Context:** Instructor only, on the ROI sandbox tenant. Students fill in the table as you go.

**Steps:**

1. Draw a table with rows Excel, Word, PowerPoint, Outlook, Mailbox, Teams, SharePoint, OneDrive. Add columns Reach, Read, Write.
2. In Excel, show that the add-in works on the workbook you have open. Fill the first row.
3. Open a Claude chat in the browser, signed in to the sandbox. Ask: "Search my sandbox mailbox for the forecast review thread and summarize it." This is the connector, not an add-in.
4. Ask a Teams question and a SharePoint question against the sandbox content only.
5. Open the connector's settings. Show whether the write tools are on or off and who controls them.
6. Say the rule: the connector's write tools are optional and need administrator approval. A tenant that consented before write tools launched must re-approve.
7. Ask the class: "Client files sit in a shared drive and a Teams channel. Which surface can Claude reach, and who should decide?" Complete the table.

**Expected result:** The completed table shows the add-ins working inside the app and files in use, and the connector searching mailboxes, Teams, SharePoint and OneDrive from chat. Writes are separated per surface. The class names an owner for the data-handling decision.

> **Instructor note:** The documented facts are the connector surfaces (Outlook, SharePoint, OneDrive, Teams), the Entra tenant requirement, owner enable then Global Administrator consent, optional write tools, and re-approval. "Add-ins are limited to files the student has open" comes from the outline and is not confirmed. State it as the working assumption. Open conflict: government documentation describes a locally run connector and the commercial support page describes an Anthropic-hosted one. Confirm which applies before class. Whether cross-app coordination works through Bedrock, Google Cloud or Microsoft Foundry is UNVERIFIED; the add-ins are documented for third-party platforms with Outlook limited. The settings screens need rehearsal.

> **Why this matters:** The risk is in the surface that can write, so name it before you switch it on.

---

## Demo 6: One Finance Play, End to End

**Learning objective:** Go from a dataset and a brief to a finished, shareable slide with Claude for PowerPoint. Time: about 15 minutes.

**Files:** `demo-files\plays\play1-fee-pressure.csv`, `demo-files\plays\play1-fee-pressure-brief.md`

**Context:** The play is a fee pressure radar. You demonstrate Play 1 only. Students choose from the other plays in Lab 3.

**Steps:**

1. Open the brief and the dataset. Read the goal, audience and rules aloud.
2. In Excel, open the CSV and ask Claude: "Calculate the percent decline in average fee from 2023 to 2026 for each segment, largest first."
3. Open a blank PowerPoint deck with the class template and open the Claude pane.
4. Ask: "Build one slide from this brief and these results. Headline states the finding. One chart. A callout for the steepest decline."
5. Check each number on the slide against step 2.
6. Ask Claude to shorten the headline and make the chart readable at the back of the room.
7. Add a text placeholder where a person might appear. Do not add a real photo.

**Expected result:** One slide with a headline stating that Fund Administration fees fell about 27 percent (41 to 30 bps), a chart, and a callout. Every figure matches the Excel result.

> **Instructor note:** PowerPoint generating and editing slides from templates is documented. Chart creation on a slide needs rehearsal; if the chart does not render, build it in Excel and paste it in. Never say a result is correct without the Excel check in step 5.

> **Why this matters:** A slide that others will forward carries your name. Check it before you share it.
