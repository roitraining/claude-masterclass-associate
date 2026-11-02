# Claude.ai Associate: Labs

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Contents:** Three timed hands-on labs and a take-home lab. Labs are student-run. Each has a learning objective, a time, a Files line, Context, Steps, a Checkpoint, Common problems, and a Facilitator note.

---

## About this guide

The files are in the `demo-files` folder next to this guide, in `lab1`, `lab2`, `lab3`, and `lab4`. Every person, company, and figure is fictional. The default scenario is financial services (Pinecrest Credit Union). Claude can produce different wording each time, so check results against the known answers and not against exact text.

Each student needs a paid Claude account (Pro or higher). Students use sample data only. No lab asks for a password, key or token, and no student connects a live connector unless IT has pre-approved it. The offline version is the default.

## Swap the scenario

To swap to healthcare or government, keep every file's structure and replace the nouns: Pinecrest Credit Union becomes Cedar Valley Health Network or Ridgeway County; the fee schedule becomes a patient price list or a permit fee schedule; service requests become patient access requests or 311 requests. Use no real patient or resident data. Rewrite the files and recompute every known answer and the Lab 2 and Lab 3 keys.

---

## Lab 1: Build and Test a Skill

**Learning objective:** Build a Skill for a recurring task, test whether it triggers on the right inputs and stays quiet on the wrong ones, and revise it. Time: 45 minutes.

**Files:** `demo-files/lab1/default-task-brief.md`, `SKILL-template.md`, `service-requests-week-42.csv`, `trigger-test-inputs.md`, `trigger-test-log.csv`

**Context:** Choose a real recurring task from your own work. If you do not have one, use the default task in `default-task-brief.md`. The description is the trigger, so most of your effort goes there. Do not start from a blank page: use the template.

**Steps:**

1. Pick your task and write its output layout in three to six numbered parts.
2. Copy `SKILL-template.md` into a folder named for your Skill.
3. Write the description: what the Skill does, when to use it, and when not to.
4. Fill in the layout and the rules, including what to write when information is missing.
5. Install the Skill in your account and turn off your other Skills.
6. Open `trigger-test-inputs.md`, or write five inputs of your own: three that should trigger the Skill in different wording, and two that should not.
7. Run each input in its own new chat. Record triggered or not, and whether the output is correct, in `trigger-test-log.csv`.
8. Compare outputs with the known answers in the inputs file, or with answers you worked out yourself.
9. Revise the description or the body to fix each miss. Change one thing at a time.
10. Rerun only the inputs that failed, then rerun all five once.

**Checkpoint:** Each student leaves with a Skill that passes its own five trigger tests, a completed test log, and a note of what changed between the first and last run.

**Common problems:**

- The Skill never triggers: the description is too general. Name the task and the words a user would say.
- The Skill triggers on the negative inputs: add a "do not use for" sentence.
- The output ignores the layout: shorten the body, number the parts, and state the order.
- A count in the output is wrong: add "use only the data supplied, never estimate a count."
- Skill upload fails: check that the folder has a `SKILL.md` at its top and ask the instructor for the upload steps rehearsed in class.
- Results change between runs: rerun twice and decide by the majority.

**Facilitator note:** A good result for the default task is a description that names the weekly service request brief, and a log where inputs 1 to 3 trigger and 4 to 5 do not. On the default data, correct output shows 12 requests with 8 open; Fees 4, Cards 2, Wires 2, Online banking 2, Fraud 1, Other 1; open High-priority SR-4101, SR-4105 and SR-4106; open 3 days or more SR-4101, SR-4104 and SR-4105. Students with their own tasks will not have an answer key, so make them state the expected output before they run it. Skill upload steps and size limits are unconfirmed and need rehearsal on the class setup, so have a working path ready before the lab starts. Triggering is not fully deterministic, so a single miss is not a fail. Look for the reasoning in the log and not for a perfect score.

---

## Lab 2: Scoring a Portfolio of Skill Candidates

**Learning objective:** Score eight candidate tasks, rank them, decide Skill or one-off prompt for each, and write a business case for the top pick. Time: 40 minutes.

**Files:** `demo-files/lab2/scoring-guide.md`, `scoring-sheet.csv`, `candidate-backlog.csv`

**Context:** Use eight tasks from your own backlog. If you cannot list eight, use `candidate-backlog.csv`, which has default scores to compare against. Score honestly. A task that sounds exciting but runs twice a year is not a Skill.

**Steps:**

1. Read `scoring-guide.md`. Note which three criteria count against a task.
2. List eight candidate tasks from your own work in `scoring-sheet.csv`.
3. Score each task from 1 to 5 on all six criteria, without computing the total yet.
4. Compute each score using the formula in the guide.
5. Apply the decision rule to each task: Hold, Skill, or One-off prompt.
6. Rank the eight tasks by score and break ties as the guide says.
7. Compare with a partner. Pick the one score you disagree on most and settle it.
8. Write the one-sentence business case for your top pick.
9. Name the one task you would never build until a data owner approves, and why.

**Checkpoint:** Each student leaves with a ranked shortlist of eight tasks, a Skill-or-prompt decision for each, and a one-sentence business case for the top pick.

**Common problems:**

- Everything scores a 4 or 5 on impact: force at least two tasks to a 2 or lower.
- Students flip the three inverted criteria: the guide already flips them in the formula, so score each criterion as described.
- A task has no clear owner of its data: score sensitivity high and decide with the rule.
- A very sensitive task ranks high: the Hold rule overrides score.
- The business case has no numbers: write a minutes estimate, even a rough one.

**Facilitator note:** For the default backlog, a good result is: C8 (29, Skill), C1 (28, Skill), C4 (27, Skill), C2 (26, Skill), C5 (22, One-off prompt, ahead of C6 on impact), C6 (22, One-off prompt), C3 (20, Hold, because sensitivity is 5), C7 (19, One-off prompt). The top pick is C8, answering staff questions about the fee schedule. The weights are a teaching device and can be argued, so reward a clear defense of a changed score and not a match to the key. Students scoring their own backlog will have different answers. Check that the rule was applied as written and that the business case has numbers.

---

## Lab 3: Connector + Artifact Capstone

**Learning objective:** Combine a connector design, a Skill, and an AI-powered artifact into one deliverable, and measure it against a test set. Time: 60 minutes.

**Files:** `demo-files/lab3/connector-spec-template.md`, `service-requests-4weeks.csv`, `artifact-prompt.md`, `capstone-test-set.csv`, `readout-template.md`. Also `demo-files/demo3/tool-catalog.csv` and your Lab 1 Skill.

**Context:** You design the connector on paper and use sample data as a stand-in for its read tool. The artifact is your small internal tool. Students connect a live connector only if IT pre-approved one before class. Otherwise use the sample file.

**Steps:**

1. Open `connector-spec-template.md`. Name the connector and write its purpose in one sentence.
2. Choose four to six tools from the catalog. Mark each read or write and write a one-sentence description for each.
3. List at least two tools you refused to expose, and why.
4. Fill in authentication, reach, and the approval path with an owner for each step.
5. Open `service-requests-4weeks.csv`. This is the stand-in output of your search tool.
6. Run your Lab 1 Skill on the file, or on the default brief task if you built a different Skill. Save the output.
7. Open `artifact-prompt.md`. Adapt it to your Skill and paste it into a new chat.
8. When the artifact renders, paste the file rows into it and press Brief.
9. Ask the eight questions in `capstone-test-set.csv` against the file, one at a time, in a new chat with the file attached. Score each 1 or 0.
10. Check the artifact output against the same known answers. Record its score separately.
11. Fix the largest error, in the Skill or the artifact prompt, and rerun the questions you missed.
12. Prepare your one-minute readout from `readout-template.md`.

**Checkpoint:** Each student gives a one-minute readout that includes the connector spec decisions and the pass rate from the test set.

**Common problems:**

- The artifact does not call Claude: ask Claude to rebuild it so the button sends the pasted text to Claude, and tell the instructor.
- The artifact returns invented counts: add "use only the pasted data, never estimate" to the prompt.
- The CSV is too long to paste: paste the first 40 rows only, which is the whole file.
- The connector spec lists a tool that returns tax IDs: remove it and say why in the Left out section.
- Time runs out on the readout: skip the optional fix in step 11.

**Facilitator note:** The known answers for `capstone-test-set.csv` are: 40 requests; 12 in Fees; 11 open; 4 open more than 5 days; Eastgate has the most (17); 5 open High priority; SR-4003 open longest (23 days); 5 Fees requests from Eastgate. A good connector spec exposes search, summary, fee schedule and hours as reads, defers writes, and refuses full records, free SQL, and money movement or external email. A good readout names one error category and one next step before a pilot. Billing for artifact calls is unconfirmed in the verified facts, so do not claim whose usage is charged. Any live connector use must be a sandbox or pre-approved one.

---

## Lab 4: Research Deep Dive (take-home)

**Learning objective:** Produce a cited, multi-source report on a real business question, with a log of which sources were kept or dropped and why. No class time.

**Files:** `demo-files/lab4/research-brief.md`, `write-up-template.md`, `source-log-template.csv`, `self-review-checklist.md`

**Context:** This repeats the Demo 4 method on your own question. You own the final report, not Claude.

**Steps:**

1. Choose one business question from `research-brief.md` or write your own.
2. Turn on web search and start Research from the plus menu.
3. Give Claude the question, the audience, and the rule to cite every figure.
4. Read the report and open at least five inline citations.
5. Log every source you opened in `source-log-template.csv`: date, publisher kind, method, reliability.
6. Mark each source kept or dropped, and write the reason.
7. Find one place two sources disagree. Check method, date, and definition, and write down how you resolved it.
8. Ask Claude to revise the report using only kept sources.
9. Fill in `write-up-template.md` with the revised answer, findings, disagreement note, and what you could not confirm.
10. Complete `self-review-checklist.md`.

**Checkpoint:** Each student ends with a report of two pages or fewer, a source log with at least one dropped source, a disagreement note, and a completed checklist.

**Common problems:**

- Research cannot start: check that web search is on and that you are on a paid plan.
- A citation does not support the claim: drop the claim or the source and log it.
- All sources agree: search for a second definition of the same figure.
- The report is too long: ask for the three findings that matter most.
- Research uses a lot of your usage allowance: run it once and revise in a normal chat.

**Facilitator note:** A good result has a short answer up front, three findings each with a dated source, at least one dropped source with a concrete reason such as "no method" or "stale," a disagreement note that compares method and definition, and an honest "could not confirm" section. Reject a report where every source is kept. Research behavior and quality vary by question, so judge the reasoning in the log and not the conclusion.
