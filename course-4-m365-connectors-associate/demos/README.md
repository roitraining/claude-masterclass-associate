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

## The demos

- **[Demo 1: Trace and Debug a Broken Formula](demo-1-trace-and-debug-a-broken-formula.md)**
- **[Demo 2: Pull a Data Source Into Excel](demo-2-pull-a-data-source-into-excel.md)**
- **[Demo 3: Redline a Draft With Judgment](demo-3-redline-a-draft-with-judgment.md)**
- **[Demo 4: One Conversation, Four Apps](demo-4-one-conversation-four-apps.md)**
- **[Demo 5: Map the Reach: Add-in Versus Connector](demo-5-map-the-reach-add-in-versus-connector.md)**
- **[Demo 6: One Finance Play, End to End](demo-6-one-finance-play-end-to-end.md)**

---

The combined guide remains at [`../demos.md`](../demos.md) and is still the source of record. These per-demo files are split out of it for easier reading and review.

---

## Related

- **[Labs guide](../labs/README.md)** — the 4 hands-on labs for this course, one file per lab.
