# Lab 2: Cross-App Deliverable Sprint

> Part of **[Microsoft 365 Connectors Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
