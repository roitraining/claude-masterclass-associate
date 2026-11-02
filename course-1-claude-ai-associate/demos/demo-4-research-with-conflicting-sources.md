# Demo 4: Research With Conflicting Sources

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Demo:** 4 of 6
**Time:** about 15 minutes

> Part of **[Claude.ai Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Triage sources by reliability, and decide what to do when two sources disagree. Time: about 15 minutes.

**Files:** [`demo-files/demo4/research-prompt.md`](../demo-files/demo4/research-prompt.md), `source-a-industry-brief.md`, `source-b-regulator-bulletin.md`, `source-c-vendor-blog.md`, `triage-log-template.csv`

**Context:** Part one is a live Research run on the web. Part two uses three fictional sources that disagree, so the room can triage them with a known answer.

**Steps:**

1. Turn on web search. From the plus menu, choose Research. Paste the live prompt from `research-prompt.md` and start it.
2. While it runs, open the three source files and read the Method line of each.
3. When the report returns, open three inline citations. For each, check that the page supports the figure attached to it.
4. Fill `triage-log-template.csv` on the screen for sources A, B and C: date, publisher kind, method stated, reliability, keep or drop, reason.
5. In a new chat, attach the three files and paste the offline prompt. Read how Claude resolves the 0.62, 0.48, and 0.9 percent figures.
6. Ask the room: should the answer be one number or a range with an explanation?

**Expected result:** A good triage keeps B (newest, all institutions, filings, stated method), keeps A with a caveat (small survey, unweighted, not verified), and drops C (stale, no method, a sales post). A and B may not truly conflict. A is a simple average of 118 respondents and B is a balance-weighted average of all filers, so the gap is partly definitions. A good answer reports 0.48 percent weighted as the primary figure, mentions the definition difference, and does not rely on C.

> **Instructor note:** Verified: Research is on paid plans, needs web search on, starts from the plus menu, citations are inline links, it uses more of the rate limit, and fabricated references remain possible. Research results on the live question are not predictable, so do not promise a figure. Connecting a Google Workspace source is optional and depends on the account, so do it only on an ROI sandbox account, and only after rehearsal. Students do the offline files. If Research is slow, start it before the explanation and return to it.

> **Why this matters:** A report with citations is only as good as its weakest source. Triage and conflict handling are the work a person still owns.

---

**Previous:** [Demo 3: Read Tools and Write Tools: Design a Connector](demo-3-read-tools-and-write-tools-design-a-connector.md) · **Next:** [Demo 5: Score a Skill Against a Test Set](demo-5-score-a-skill-against-a-test-set.md)


*Demo 4 of 6*
