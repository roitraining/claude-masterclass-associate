# Lab 4: Connector Briefing Automation (take-home)

**Course:** Microsoft 365 Connectors Associate
**Duration:** Untimed — no timed slot, work at your own pace
**Format:** Take-home lab. Sandbox tenant or test mailbox only

> Part of **[Microsoft 365 Connectors Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] A test account on a Microsoft Entra **business** tenant. Personal Microsoft accounts do not work
- [ ] A sandbox tenant or test mailbox holding **no** real client or personal data
- [ ] Access to the Owner who can enable the connector, and to a Global Administrator who can give consent
- [ ] Test messages in the mailbox, so a summary has something to find
- [ ] No demo files needed

> **Safety rules.** Use a sandbox tenant or a test mailbox that holds no real client or personal data. **Do not test on a work or personal mailbox.** If you are not a tenant administrator, do not attempt admin consent — ask the administrator, and stop at the step that needs them. **Never paste credentials or tokens into a chat.**

---

## Overview

The connector reads Outlook, the calendar and Teams, and its optional write tools can draft email and manage calendar events.

**A briefing needs only reading and drafting.** You turn on as little as possible and test it on safe data.

---

## Part 1: Confirm Access and Consent

### Step 1: Confirm the Tenant Type

Confirm your test account is on a Microsoft Entra business tenant.

**Acceptance criteria:** a business tenant, not a personal Microsoft account.

### Step 2: Confirm You Can Reach the Connector Settings

If you are not an Owner, ask the person who is.

### Step 3: Have the Owner Enable It and an Administrator Consent

Ask the Owner to enable the connector, and a Global Administrator to give the one-time consent.

> **Note:** if you are not an administrator, stop here and wait. Do not attempt admin consent yourself.

### Step 4: Record Who Approved, and When

**Acceptance criteria:** the approver and date written down.

---

## Part 2: Enable Read Tools Only

### Step 5: List Every Tool as Read or Write

**Acceptance criteria:** each tool classified read or write, in writing.

### Step 6: Turn On Only the Read Tools

Mail search, calendar and Teams.

**Acceptance criteria:** no write tool is on yet.

---

## Part 3: Test Read-Only

### Step 7: Run a Read-Only Test

Ask: "Summarize the last 24 hours of my test mailbox and list tomorrow's calendar."

**Expected result:** a summary and a calendar list.

> **Troubleshooting:** if nothing is found, the test mailbox is empty. Add test messages.

### Step 8: Check the Summary Against the Mailbox

**Acceptance criteria:** the summary verified against what is actually there.

---

## Part 4: Request and Enable Draft Only

### Step 9: Ask Your Administrator About Write Tools, Then Wait

Ask whether draft and calendar write tools may be enabled. **Wait for the answer.**

### Step 10: If Approved, Turn On Draft Email Only

Leave send and calendar changes **off**.

**Acceptance criteria:** draft email on; send and calendar writes off.

### Step 11: Set Per-Action Approval on Every Write Tool

Use the control the tool shows.

**Acceptance criteria:** you confirm each action before it happens.

> **Key Insight:** do not assume how the approval control is presented. Find it and set it deliberately.

---

## Part 5: Build and Run the Briefing

### Step 12: Write the Briefing Prompt

Sections for urgent mail, today's meetings and open Teams questions. Ask Claude to create a draft addressed to your own test mailbox.

**Expected result:** a prompt that produces a draft, not a sent message.

### Step 13: Run It and Confirm Nothing Was Sent

**Acceptance criteria:** a draft exists, and nothing was sent.

> **Common Pitfall:** check the recipient before approving. Claude can draft to the wrong person.

---

## Part 6: Test the Refusal

### Step 14: Try a Request That Should Be Refused

Ask: "Send it now."

**Acceptance criteria:** you have recorded what happened.

---

## Part 7: Write the Rollout Note

### Step 15: Write One Page

Cover tools on, tools off, the approver, and who reviews drafts weekly.

**Acceptance criteria:** all four, with the approver named.

---

## Part 8: Checkpoint

### Step 16: Verify Your Progress

- [ ] The test account is on an Entra business tenant
- [ ] A sandbox tenant or test mailbox was used, with no real client or personal data
- [ ] No credential or token was ever pasted into a chat
- [ ] The Owner enabled the connector and an administrator consented
- [ ] The approver and date are recorded
- [ ] Every tool is classified read or write in writing
- [ ] Only read tools were on for the first test
- [ ] A read-only summary was produced and checked against the mailbox
- [ ] Administrator approval was requested and waited for before enabling any write tool
- [ ] Draft email is the only write tool enabled
- [ ] Send and calendar changes remain off
- [ ] Per-action approval is set on every enabled write tool
- [ ] A briefing prompt creates a draft in the test mailbox
- [ ] A draft exists and nothing was sent
- [ ] The recipient was checked before approving
- [ ] A refusal test was run and the result recorded
- [ ] A one-page rollout note names tools on, tools off, the approver, and the weekly draft reviewer

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Connector not visible | It does not appear in settings | It is not enabled, or consent is missing |
| Write tool blocked | A write tool refuses to work | A tenant that consented before write tools launched must re-approve. Writes are blocked by default for it |
| Nothing found | The summary is empty | The test mailbox is empty. Add test messages |
| Runs only on demand | The briefing does not run itself | Expected. Scheduling it is optional |
| Wrong recipient | A draft is addressed to the wrong person | Check the recipient before approving |

---

## What You Built

Working at your own pace, you:

- Turned on the smallest set of tools that does the job, and classified every tool read or write before enabling anything
- Tested read-only first, and verified the summary against the real mailbox
- Waited for administrator approval instead of enabling write access because you could
- Kept send and calendar changes off, with per-action approval on the one write tool you did enable
- Tested the refusal path, and wrote a rollout note naming who approves and who reviews

---

## What's Next

This is the final lab in Microsoft 365 Connectors Associate, and in the Associate track. The habit to carry: enable the minimum, test read-only first, and name the human who reviews what the tool drafts.

---

## Facilitator Notes

A good result keeps write tools to the minimum, can say which were turned on and why, and has a review step.

The two-step consent (an owner enables, then an Entra Global Administrator approves) and the re-approval rule are documented. The setting names and how per-action approvals are presented are not confirmed and need rehearsal.

Whether the add-in can send email is a documented conflict (a secondary source says the add-in does not request Mail.Send), so do not teach it. Sending belongs to the write tools of the connector only.

Which connector applies is also an open item: government documentation describes a locally run connector and the commercial support page an Anthropic-hosted one.

Running the briefing on a schedule is not covered by the verified facts. Offer it only if the plan of the student supports scheduled tasks, and rehearse it.

---

*Lab 4 Complete*
