# Demo 5: Map the Reach: Add-in Versus Connector

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Demo:** 5 of 6
**Time:** about 15 minutes

> Part of **[Microsoft 365 Connectors Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

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

**Previous:** [Demo 4: One Conversation, Four Apps](demo-4-one-conversation-four-apps.md) · **Next:** [Demo 6: One Finance Play, End to End](demo-6-one-finance-play-end-to-end.md)


*Demo 5 of 6*
