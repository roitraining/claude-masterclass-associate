# Claude.ai Associate: Demos

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Contents:** 6 instructor-led demos. Each takes 15 minutes or less and has a learning objective. The numbers match the Today's Demos slide.

---

## About this guide

Each demo has the same layout: a learning objective, a time, a Files line when the demo uses files, a short Context, numbered Steps, an Expected result, an Instructor note, and a Why this matters note.

The demo files are in the `demo-files` folder next to this guide. Every person, company, and figure in them is fictional. The default scenario is financial services (Pinecrest Credit Union). Claude can produce different wording each time, so check results against the Expected result and not against exact text.

This is a 200-level class. The demos assume the Essentials baseline and do not re-teach what a Skill is or how to spot a citation.

> **Instructor-only rule.** Demo 3 and Demo 4 can touch a connector or a connected account. Run any live connector step on an ROI sandbox account only. Students do the offline or sample-data version in every case.

> **Rehearse first.** Several product behaviors below are unconfirmed. They are flagged in each Instructor note. Rehearse every demo on the class setup before delivery.

---

## Swap the scenario

The files use financial services. To swap to healthcare or government, keep the structure and replace the nouns.

| Financial services (default) | Healthcare | Government |
|------------------------------|------------|------------|
| Pinecrest Credit Union | Cedar Valley Health Network | Ridgeway County |
| Member meeting recap | Patient-access call recap | Resident meeting recap |
| Fee schedule | Patient price list | Permit and license fee schedule |
| Service requests | Patient access requests | 311 service requests |
| Complaint triage | Patient grievance triage | Resident complaint triage |
| Compliance flag rule | Privacy flag rule | Public records flag rule |

Healthcare: use no real patient data, including in examples. Government: note that a public records request may later cover what is pasted, so use sample data only. Rewrite the files, then recompute every known answer.

---

## Demo 1: A Skill That Never Triggers

**Learning objective:** Show that the description decides whether a Skill loads, by fixing a Skill that never fires. Time: about 12 minutes.

**Files:** `demo-files/demo1/vague-skill/SKILL.md`, `demo-files/demo1/fixed-skill/SKILL.md`, `demo-files/demo1/trigger-inputs.md`

**Context:** The two Skills have identical bodies. Only the description differs. The vague one says "Helps with meetings and member stuff." Claude sees only the name and description until it decides a Skill is relevant, so the description is the whole trigger.

**Steps:**

1. Install `vague-skill` as a Skill in your account and turn it on. Turn all other test Skills off.
2. Paste input T1 from `trigger-inputs.md` into a new chat. Watch for the **Loaded skill** chip above the answer, then note whether the answer uses the heading "Pinecrest Recap". If Claude asks a clarifying question first, choose **Skip** and let it answer.
3. Run T2 and T3 in new chats. Record triggered or not for each.
4. Run N1 to N3 in new chats. Record each.
5. Replace the Skill with `fixed-skill`. Say aloud what the new description adds: what it does, when to use it, and when not to.
6. Rerun all six inputs. Record the results in a small table on the board.

**Expected result:** With the vague description, one or more of T1 to T3 usually fails to produce the recap format and shows no Loaded skill chip. With the fixed description, T1 to T3 show the chip and produce "Pinecrest Recap", and N1 to N3 produce ordinary answers. Triggering can vary, so show your own table and not a promised score.

> **Run on a Max account, October 22, 2026, Opus 5.5.** T1 with the vague Skill produced an ordinary email plus an internal call note, no chip and no Pinecrest heading. The same input with only the fixed Skill produced the chip and a correct recap, including "Not set" for the missing due dates and "Lending (person not named)" rather than an invented owner. The demo behaves as written.

> **Instructor note:** The Skill folder layout, the YAML description, and progressive loading are verified. **There is an interface signal, confirmed in the product on October 22, 2026:** a **Loaded skill** chip appears above the answer, and a "Used in this session - Skills: <name>" card appears at the end. Point at those rather than inferring from the output format; it is the strongest moment in this demo. **Adding a Skill:** Settings, then Customize, then Skills, then **+ Add**, which offers "Upload skill", "Create a skill" and "Create with Claude". Creating one in the form is faster in class than zipping a folder, and custom Skills work on Free as well as paid. Size limits are still UNVERIFIED. **Expect interruptions:** on the untriggered run Claude may ask one or two clarifying questions before answering; choose Skip. A vague Skill may still trigger sometimes. If it does on every input, shorten the description further.

> **Why this matters:** A Skill that does not trigger is invisible and gets blamed on the model. Writing the description to say what, when, and when not is the cheapest reliability fix there is.

---

## Demo 2: A Multi-File Skill, Loaded Only When Needed

**Learning objective:** Design a Skill so the main file stays small and detail files load only when a situation calls for them. Time: about 12 minutes.

**Files:** `demo-files/demo2/pinecrest-meeting-recap/` (with `SKILL.md` and three files in `references/`), `demo-files/demo2/test-notes.md`

**Context:** The main file holds the rules and points to three reference files. Two of them are conditional. The escalation file carries a reference code (ESC-7 or ESC-9) that can only appear if Claude read that file, which makes loading visible.

**Steps:**

1. Open `SKILL.md` and read out the two "read the matching file only if" lines. Open the `references` folder.
2. Install the folder as a Skill and turn off other test Skills.
3. Run Notes A from `test-notes.md` in a new chat. Check the recap has no reference code and no compliance line.
4. Run Notes B in a new chat. Look for the Member Complaints Desk and the code ESC-7.
5. Run Notes C in a new chat. Look for the compliance line with rule CF-3, and no ESC code.
6. Ask the room: what would break if all three reference files were pasted into the main `SKILL.md`?

**Expected result:** Notes A gives a plain recap. Notes B includes extension 4417 and ESC-7. Notes C includes the line "Compliance review: statement about returns or guarantees (rule CF-3)." Each reference file appears only when its situation does.

> **Instructor note:** Loading other files only as needed is verified. The body should stay under 500 lines, and this one is far smaller. Whether Claude reads the right file on every run is the model's call, so one miss is possible. Rerun the failing case once and discuss it as a design lesson about clearer wording in `SKILL.md`. The zip upload steps are UNVERIFIED, as in Demo 1.

> **Why this matters:** A Skill that carries every rule in one file pays for all of it on every run and becomes hard to review. Splitting by situation keeps each run focused and each file owned and reviewable.

---

## Demo 3: Read Tools and Write Tools: Design a Connector

**Learning objective:** Decide which tools a custom connector should expose, which stay read-only, and how to name them so Claude picks the right one. Time: about 15 minutes.

**Files:** `demo-files/demo3/tool-catalog.csv`, `demo-files/demo3/connector-design-worksheet.md`

**Context:** A custom connector is a remote MCP server. Everyone who connects reaches whatever its tools reach. The ten candidate tools mix safe reads, dangerous reads, and writes. This is a design exercise on paper, run as a group.

**Steps:**

1. Open `tool-catalog.csv` on the screen and read the ten tools.
2. Fill Part 1 of the worksheet as a group, tool by tool: Expose now, Later phase, or Never.
3. Compare with the key below and discuss each difference.
4. Fill Part 2: rename `query1`, `get_data` and `doStuff`, and write a one-sentence description for each.
5. Fill Part 3 and Part 4: authentication, reach, and the order of the approval path.
6. Optional, instructor only: on an ROI sandbox Team or Enterprise account, open the admin Connectors settings and show where a custom web connector is added (server URL, optional OAuth fields). Do not enter a real server.

**Expected result:** The key below. Good names read like search_service_tickets: a verb, a noun, and a description that says when to use it. The approval path runs: request with the tool list, security review, pilot group, publish.

| Tool | Decision | Reason |
|------|----------|--------|
| get_member_summary | Expose now | Read, minimal fields |
| search_service_tickets | Expose now | Read, no identifiers beyond ticket |
| get_fee_schedule | Expose now | Read, public data |
| list_branch_hours | Expose now | Read, public data |
| get_full_member_record | Never | Returns tax ID, date of birth, account numbers |
| run_sql_query | Never | Unbounded read, bypasses every field decision |
| create_service_ticket | Later phase | Write, reversible, pilot first |
| update_member_address | Later phase | Write to a member file, needs approval flow |
| send_member_email | Never | Write, external, cannot be recalled |
| close_account | Never | Write, moves money, irreversible |

> **Instructor note:** Beta status, owner setup on Team and Enterprise, individual user connection, and the public-reachability requirement are verified. Per-tool permission controls inside Claude are UNVERIFIED. Do not promise that a student can switch off a single tool in the Claude interface. Teach the design decision as one made in the server and in the approval review. Anthropic warns that custom connectors reach services it has not verified, so say that. The optional admin screen is instructor-only and the exact labels may differ from this guide.

> **Why this matters:** A connector is a standing door into your systems. Deciding what stays closed, before anyone connects, is cheaper than discovering it afterward. Tool names and descriptions decide whether Claude picks the right tool at all.

---

## Demo 4: Research With Conflicting Sources

**Learning objective:** Triage sources by reliability, and decide what to do when two sources disagree. Time: about 15 minutes.

**Files:** `demo-files/demo4/research-prompt.md`, `source-a-industry-brief.md`, `source-b-regulator-bulletin.md`, `source-c-vendor-blog.md`, `triage-log-template.csv`

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

## Demo 5: Score a Skill Against a Test Set

**Learning objective:** Run a Skill against questions with known answers, score the result, and decide what to check every time versus sample. Time: about 15 minutes.

**Files:** `demo-files/demo5/fee-qa-skill/` (a Skill with a 2026 fee schedule and a retired 2025 one), `test-set.csv`, `sample-run-results.csv`, `scoring-sheet.csv`

**Context:** The test set has ten questions with known answers. Each can fail in one of four ways: arithmetic, omission, stale source, citation mismatch. To save time, a sample run is provided with errors already in it.

**Steps:**

1. Open `test-set.csv`. Read three questions and their known answers.
2. Install the `fee-qa-skill` folder and run questions 1 to 3 live in new chats. Compare each to the known answer.
3. Open `sample-run-results.csv`. Score each of the ten rows 1 or 0 against `test-set.csv` and write the error category for each miss.
4. Compute the pass rate.
5. Ask the room: which error categories do we check on every run, and which can we sample?
6. Decide one fix to the Skill for the worst error, for example "show the arithmetic," and say how you would retest.

**Expected result:** Score 6 of 10, a 60 percent pass rate. The four misses are question 1 ($10, stale source), question 3 ($155, arithmetic), question 4 ($108, omission of the 3-fee daily cap), and question 9 (cites 2.2 and not 2.3, citation mismatch). Suggested policy: check every dollar figure every time, since arithmetic and stale-source errors are cheap to catch and costly to miss, and sample citation wording and phrasing.

> **Instructor note:** The live runs depend on Skill triggering and may differ from the sample run. If a live answer is correct, say so, then move to the sample file. The scoring method is the point. The retired 2025 file inside the Skill is a deliberate trap, and whether Claude uses it depends on the model, so a stale answer is possible but not guaranteed.

> **Why this matters:** A Skill without a test set is a guess you repeat. Ten questions and a pass rate turn "it seems fine" into evidence, and the error taxonomy tells you where to put the human check.

---

## Demo 6: Build an AI-Powered Artifact

**Learning objective:** Build a small internal tool as an artifact that calls Claude, and say who pays for those calls. Time: about 15 minutes.

**Files:** `demo-files/demo6/build-prompt.md`, `demo-files/demo6/sample-complaints.txt`

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
