# Microsoft 365 Connectors Associate: Labs

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Contents:** Three timed hands-on labs and a take-home lab. The numbers match the slide deck.

---

## About this guide

Labs 1 to 3 are student-run in your own Excel, Word, PowerPoint and Outlook with the Claude add-ins. Lab 4 is take-home and configures the Microsoft 365 connector.

Keep the two products separate. The add-ins work inside the app you are driving. The connector is a chat-side integration, and its optional write tools are what can send email or change calendar events, and only when enabled and approved by an administrator. The add-ins are not shown sending email in these labs.

The files are in `demo-files`. Work on copies. Every person, company and figure is fictional. Claude can word things differently each time, so judge results against each Checkpoint. Add-in menu labels can differ by build; the steps say "open the Claude pane".

---

## Lab 1: Excel Financial Model Workshop

**Learning objective:** Trace, debug and adjust a messy multi-tab model with Claude for Excel, then add a sourced figure. Time: 45 minutes.

**Files:** `demo-files\harbor-peak-forecast-model.xlsx`, `demo-files\industry-benchmarks.csv`

**Context:** Harbor Peak's FY2027 board pack goes out Friday. The model has errors. Dana needs it checked and one peer comparison with a source.

**Steps:**

1. Save a copy of the workbook as `forecast-model-working.xlsx` and enable editing.
2. Open the Claude pane.
3. Ask Claude to explain how the five tabs connect.
4. Ask Claude to check every total and subtotal and list anything that does not add up. Do not accept the list yet.
5. Check Revenue row 9 yourself. Confirm the cause.
6. Ask Claude to fix it and list the cells changed.
7. Ask Claude to find any number typed inside a formula on the Costs tab.
8. Ask Claude to replace it with the Assumptions reference. Check the cell.
9. Ask Claude to compare the tax rate on the Summary tab with the Assumptions tab.
10. Decide which tax rate to present. Write your choice and reason in a cell note.
11. Ask Claude to make the model use that rate from one place only.
12. Add a tab named Benchmarks and import `industry-benchmarks.csv`.
13. Ask Claude to compare the FY2027 EBIT margin with the peer median and cite the cells.
14. Add a Summary row that holds the peer median, its source note and its as-of date.
15. Write three sentences in a cell: what was wrong, what you changed, what you decided.

**Checkpoint:** FY2026 total revenue is 12,380,000 and FY2027 is 13,122,800. Marketing grows at the Assumptions inflation rate. Summary after-tax profit equals P&L net income for the rate you chose. A sourced peer figure sits in the workbook with its date.

**Common problems:**

- The workbook shows zeros or empty cells: select Enable Editing and recalculate.
- Claude changes more than you asked: say "list the cells you will change first" and stop it before it writes.
- Claude says the model looks fine: ask it to trace the Revenue total from the service lines.
- Claude changes the 6 percent growth rate because of the 4 percent in the thread: the plan stays at 6 percent.
- No financial data connector appears: use the CSV. That is expected.

**Facilitator note:** Three errors are planted: a SUM range that stops at row 7 (Revenue B9:D9), a typed 12 percent inside the Marketing formula (Costs C7), and a typed 21 percent tax rate on the Summary tab against 24 percent in Assumptions. A good result has all three found, each checked by the student by eye, the cell changes listed, and a stated tax decision. After the fixes at 24 percent, FY2027 EBIT is 2,561,960 and net income is 1,947,090; the full table is in `demo-files\ANSWER-KEY.md`. Watch for students who accept Claude's totals without opening a formula. The financial data connector names in the outline are UNVERIFIED; the lab does not depend on a connector.

---

## Lab 2: Cross-App Deliverable Sprint

**Learning objective:** Carry one deliverable from a thread to a memo to a deck in one conversation without re-explaining it. Time: 40 minutes.

**Files:** `demo-files\email-thread-forecast-review.txt`, your corrected `forecast-model-working.xlsx`, `demo-files\draft-board-memo.docx` (optional reference)

**Context:** Dana asked for a one-page memo and a short deck for the finance committee. The thread has the asks. Your corrected workbook has the numbers.

**Steps:**

1. Open the thread text. If you have the Outlook add-in and the thread is in your mailbox, open it there. Otherwise paste the text into the Claude pane in Word.
2. Ask Claude to summarize the thread: who owes what, the decisions needed, the open questions.
3. Check the summary against the thread. Correct anything missing.
4. Open your corrected workbook. In the same conversation, ask Claude to answer Priya's and Marcus's questions from the model.
5. Check that Claude did not ask you to repeat the thread.
6. Open a new Word document. Ask Claude to draft the one-page memo for the finance committee: what changed and what needs a decision.
7. Review the memo for figures. Check three against the workbook.
8. Open a new PowerPoint deck. Ask Claude to turn the memo into three slides.
9. Check each slide figure against the memo.
10. Ask Claude to list every number in the deck and where it came from.
11. Save the memo and the deck.

**Checkpoint:** One deliverable has moved through at least three apps. The memo and deck state the corrected revenue, name the two decisions (approve the forecast, confirm the tax rate), and every figure traces to the workbook.

**Common problems:**

- Claude does not remember the thread in the next app: paste a two-line summary and carry on. Note that it happened.
- The attachment does not open from Outlook: save the workbook from the folder instead.
- The memo uses the old, low revenue figure: you used the original workbook. Use the corrected copy.
- No Outlook add-in: it is a public beta and optional. Use the pasted text.
- The deck has more than three slides or invents numbers: ask for three slides and for sources.

**Facilitator note:** A good result is a memo under one page and a deck of three slides, each with figures that match the corrected workbook (revenue 13,122,800 for FY2027). Look for students who verified the summary before building on it, and for a deck that states a decision. The claim that the four add-ins share conversation state is documented, but how it behaves on this build, and how Outlook handles attachments, needs rehearsal. If the conversation does not carry across apps, accept the pasted summary and ask the student what it cost. The Outlook add-in drafts and summarizes; no step sends email.

---

## Lab 3: PowerPoint Plays Capstone

**Learning objective:** Produce a finished, shareable asset from a finance play using Claude for PowerPoint, with Word for supporting copy. Time: 60 minutes.

**Files:** `demo-files\plays\` (choose one play: `play1` to `play4`, each a .csv and a brief .md)

**Context:** Each play is a dataset and a brief. You will present your asset to the room at the end.

**Steps:**

1. Read the brief for the play you choose. Write its goal and audience in one line.
2. Open the dataset in Excel. Ask Claude to compute what the brief asks for.
3. Check two computed figures by hand.
4. Open Word. Ask Claude to draft the supporting copy: a headline and three short lines.
5. Edit the copy. Keep the tone the brief names.
6. Open a blank PowerPoint deck with the class template.
7. Ask Claude to build the slide or slides from the brief, the results and your copy.
8. Check every figure on the slide against Excel.
9. Ask Claude to improve readability for the back of the room.
10. Ask Claude to check the slide against the brief's rules and list any it breaks.
11. Fix any rule that breaks.
12. Add the speaker notes: three bullets for your presentation.
13. Present the asset in three minutes.

**Checkpoint:** A finished asset that follows its brief, with figures that match the dataset, no real person's likeness, and suitable to share outside the room. Each student presents it.

**Common problems:**

- The chart does not render: build it in Excel and paste it into the slide.
- Claude invents a cause for a trend: label it a hypothesis or remove it.
- Claude adds a stock photo of a person: replace it with a text label or a plain shape.
- The slide is crowded: ask for one idea and one chart.
- Play 3 does not match the workbook: that is intended. Say so on the slide.

**Facilitator note:** What good looks like by play: Play 1 leads with Fund Administration (about 27 percent decline, 41 to 30 bps). Play 2 states top 3 clients hold 26.9 percent and top 5 hold 35.5 percent. Play 3 notices that the bridge ends at 12,712,800 against 13,122,800 in the workbook, a 410,000 fee compression step the model does not include. Play 4 gives total outstanding of 549,000 and flags two clients over 30 days late. Reward a student who found and stated a discrepancy over one with the prettiest slide. Chart creation in PowerPoint needs rehearsal on the class build.

---

## Lab 4: Connector Briefing Automation (take-home)

**Learning objective:** Configure the Microsoft 365 connector's write tools to draft a daily briefing, and set the approvals deliberately. No timed slot.

**Files:** none. Use a sandbox tenant or a test mailbox only.

**Context:** The connector reads Outlook, the calendar and Teams, and its optional write tools can draft email and manage calendar events. A briefing needs only reading and drafting. You will turn on as little as possible and test it on safe data.

> **Safety rules.** Use a sandbox tenant or a test mailbox that holds no real client or personal data. Do not test on a work or personal mailbox. If you are not a tenant administrator, do not attempt admin consent; ask the administrator, and stop at the step that needs them. Never paste credentials or tokens into a chat.

**Steps:**

1. Confirm that your test account is on a Microsoft Entra business tenant. Personal Microsoft accounts do not work.
2. Confirm that you can reach the connector settings in Claude. If you are not an Owner, ask the person who is.
3. Ask the Owner to enable the connector. Ask a Global Administrator to give the one-time consent.
4. Write down who approved, and when.
5. Open the list of the connector's tools. Write each as read or write.
6. Turn on only the read tools: mail search, calendar and Teams.
7. Run a read-only test: "Summarize the last 24 hours of my test mailbox and list tomorrow's calendar."
8. Check the summary against the mailbox.
9. Ask your administrator whether draft and calendar write tools may be enabled. Wait for the answer.
10. If approved, turn on draft email only. Leave send and calendar changes off.
11. For each write tool you enabled, set the approval so that you confirm each action. Use the control the tool shows. Do not assume it.
12. Write a briefing prompt: sections for urgent mail, today's meetings and open Teams questions. Ask Claude to create a draft addressed to your own test mailbox.
13. Run it. Confirm that a draft exists and nothing was sent.
14. Try one request that should be refused: "Send it now." Record what happened.
15. Write a one-page rollout note: tools on, tools off, approver, who reviews drafts weekly.

**Checkpoint:** A briefing prompt that creates a draft in a test mailbox, with write tools limited to drafting, per-action approval on, and a rollout note naming the approver.

**Common problems:**

- The connector is not visible: it is not enabled, or consent is missing.
- A write tool is blocked: a tenant that consented before write tools launched must re-approve. Writes are blocked by default for it.
- Nothing is found: the test mailbox is empty. Add test messages.
- The briefing runs only when you ask: that is expected. Scheduling it is optional.
- Claude drafts to the wrong person: check the recipient before approving.

**Facilitator note:** A good result keeps write tools to the minimum, can say which were turned on and why, and has a review step. The two-step consent (an owner enables, then an Entra Global Administrator approves) and the re-approval rule are documented. The setting names and how per-action approvals are presented are not confirmed and need rehearsal. Whether the add-in can send email is a documented conflict (a secondary source says the add-in does not request Mail.Send), so do not teach it. Sending belongs to the connector's write tools only. Which connector applies is also an open item: government documentation describes a locally run connector and the commercial support page an Anthropic-hosted one. Running the briefing on a schedule is not covered by the verified facts. Offer it only if the student's plan supports scheduled tasks, and rehearse it.
