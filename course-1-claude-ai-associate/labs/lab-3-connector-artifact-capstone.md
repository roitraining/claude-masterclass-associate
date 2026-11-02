# Lab 3: Connector + Artifact Capstone

> Part of **[Claude.ai Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
