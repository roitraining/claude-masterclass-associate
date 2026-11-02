# Demo 6: Build an AI-Powered Artifact

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Demo:** 6 of 6
**Time:** about 15 minutes

> Part of **[Claude.ai Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Build a small internal tool as an artifact that calls Claude, and say who pays for those calls. Time: about 15 minutes.

**Files:** [`demo-files/demo6/build-prompt.md`](../demo-files/demo6/build-prompt.md), [`demo-files/demo6/sample-complaints.txt`](../demo-files/demo6/sample-complaints.txt)

**Context:** A normal artifact displays content. An AI-powered artifact sends its own prompts to Claude when a user presses a button, so it works as a tool. This demo builds a complaint triage tool that previews the Lab 3 capstone.

**Steps:**

1. Paste the build prompt from `build-prompt.md` into a new chat and let the artifact render.
2. Paste Complaint 1 from `sample-complaints.txt` into the tool and press Triage.
3. Check the category, urgency, summary and draft reply.
4. Run Complaints 2 to 5. For Complaint 5, read the reply for any request for a card number or PIN.
5. Send the follow-up prompt for a Copy button and a length warning.
6. Open the Share options. Discuss who would sign in, and whose usage the calls count against.

**Expected result:** Complaint 1: Fees, High. Complaint 2: Cards, High. Complaint 3: Wires, Normal. Complaint 4: Online banking, Normal. Complaint 5: Fraud, High, with a reply that never asks for a card number or PIN. Claude may phrase summaries differently each run.

> **Instructor note:** Verified: an artifact can run its own prompts through `window.claude.complete()`, and an Anthropic help article confirms AI-powered artifacts exist. Billing is UNVERIFIED against current official documentation. A June 2025 secondary write-up says a published app asks the viewer to sign in with their own account so usage bills to the viewer. Say that it is unconfirmed and do not state it as fact. Whether the feature is available on every plan or setting is also unconfirmed, so rehearse on a Pro account. If the tool fails to call Claude, show the build prompt and describe the capstone instead of debugging live.

> **Why this matters:** A small tool in front of a prompt makes a task repeatable for people who will never write the prompt. It also creates a place where usage, data, and review need an owner.

---

**Previous:** [Demo 5: Score a Skill Against a Test Set](demo-5-score-a-skill-against-a-test-set.md)


*Demo 6 of 6*
