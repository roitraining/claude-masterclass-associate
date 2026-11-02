# Lab 4: Connector Briefing Automation (take-home)

> Part of **[Microsoft 365 Connectors Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
