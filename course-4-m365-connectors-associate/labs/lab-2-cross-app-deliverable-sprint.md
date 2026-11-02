# Lab 2: Cross-App Deliverable Sprint

**Course:** Microsoft 365 Connectors Associate
**Duration:** 40 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Microsoft 365 Connectors Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Lab 1 completed — you need your **corrected** `forecast-model-working.xlsx`
- [ ] Microsoft Word and PowerPoint with Claude available
- [ ] `demo-files\email-thread-forecast-review.txt`
- [ ] `demo-files\draft-board-memo.docx` (optional reference)
- [ ] The Outlook add-in is optional. It is a public beta — use the pasted text if you do not have it

> **Note:** no step in this lab sends email. The Outlook add-in drafts and summarizes only.

---

## Overview

Dana asked for a one-page memo and a short deck for the finance committee. The thread has the asks. **Your corrected workbook has the numbers.**

The point is carrying one deliverable through three apps in one conversation, without re-explaining it. If the context does not carry, record that it happened.

---

## Part 1: Summarize the Thread

### Step 1: Open the Thread

If you have the Outlook add-in and the thread is in your mailbox, open it there. Otherwise paste the text into the Claude pane in Word.

> **Troubleshooting:** if the attachment does not open from Outlook, save the workbook from the folder instead.

### Step 2: Summarize Who Owes What

Ask Claude to summarize the thread: who owes what, the decisions needed, and the open questions.

**Expected result:** a summary naming people, decisions and questions.

### Step 3: Check the Summary Against the Thread

Correct anything missing.

**Acceptance criteria:** the summary was verified before anything was built on it.

> **Key Insight:** everything downstream inherits this summary. Verifying it here is cheaper than finding the gap in the deck.

---

## Part 2: Answer the Questions from the Model

### Step 4: Answer Priya and Marcus from the Workbook

Open your corrected workbook. In the **same conversation**, ask Claude to answer the questions of Priya and Marcus from the model.

**Acceptance criteria:** both questions answered from the corrected figures.

> **Common Pitfall:** if the figures look low, you opened the original workbook. Use the corrected copy.

### Step 5: Confirm You Were Not Asked to Repeat the Thread

**Acceptance criteria:** you have recorded whether the conversation carried the thread context across apps.

> **Troubleshooting:** if Claude does not remember the thread in the next app, paste a two-line summary and carry on. Note that it happened and what it cost.

---

## Part 3: Draft the Memo

### Step 6: Draft the One-Page Memo

Open a new Word document. Ask Claude to draft the one-page memo for the finance committee: what changed and what needs a decision.

**Acceptance criteria:** under one page, naming both decisions.

### Step 7: Check Three Figures Against the Workbook

**Acceptance criteria:** three figures verified by hand.

---

## Part 4: Build the Deck

### Step 8: Turn the Memo into Three Slides

Open a new PowerPoint deck.

**Acceptance criteria:** exactly three slides.

> **Common Pitfall:** if the deck has more than three slides or invents numbers, ask again for three slides and for sources.

### Step 9: Check Each Slide Figure Against the Memo

**Acceptance criteria:** every slide figure matches the memo.

### Step 10: Ask for Every Number and Its Source

**Acceptance criteria:** a list of every number in the deck with where it came from.

---

## Part 5: Save

### Step 11: Save the Memo and the Deck

---

## Part 6: Checkpoint

### Step 12: Verify Your Progress

- [ ] The thread summary was checked against the thread before anything was built on it
- [ ] Anything the summary missed was corrected
- [ ] Priya and Marcus both answered from the **corrected** workbook
- [ ] Whether context carried across apps is recorded
- [ ] One deliverable moved through at least three apps
- [ ] The memo is under one page
- [ ] The memo states the corrected revenue, 13,122,800 for FY2027
- [ ] The memo names both decisions: approve the forecast, confirm the tax rate
- [ ] Three memo figures verified by hand against the workbook
- [ ] The deck has exactly three slides
- [ ] Every slide figure matches the memo
- [ ] Every number in the deck has a stated source
- [ ] No figure in either deliverable is invented
- [ ] Memo and deck saved

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Context does not carry | Claude does not remember the thread in the next app | Paste a two-line summary and carry on. Note that it happened |
| Attachment will not open | Outlook cannot open the workbook | Save the workbook from the folder instead |
| Old figures in the memo | Revenue is lower than expected | You used the original workbook. Use the corrected copy from Lab 1 |
| No Outlook add-in | The add-in is unavailable | It is a public beta and optional. Use the pasted text |
| Deck overruns or invents | More than three slides, or numbers with no source | Ask again for three slides and for sources |

---

## What You Built

In 40 minutes, you:

- Carried one deliverable from a thread to a memo to a deck in a single conversation
- Verified the thread summary before building on it, which is the step everything downstream depends on
- Caught the difference between the original and corrected workbook, which would have put a wrong revenue figure in front of a committee
- Traced every number in the final deck back to a source
- Recorded whether the cross-app context actually held, rather than assuming it

---

## What's Next

Lab 3, the PowerPoint Plays Capstone, builds a repeatable deck pattern rather than a one-off deliverable.

---

## Facilitator Notes

A good result is a memo under one page and a deck of three slides, each with figures that match the corrected workbook (revenue 13,122,800 for FY2027).

Look for students who verified the summary before building on it, and for a deck that states a decision.

The claim that the four add-ins share conversation state is documented, but how it behaves on this build, and how Outlook handles attachments, needs rehearsal. If the conversation does not carry across apps, accept the pasted summary and ask the student what it cost.

The Outlook add-in drafts and summarizes; no step sends email.

---

*Lab 2 Complete*
