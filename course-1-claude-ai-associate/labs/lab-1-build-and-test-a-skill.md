# Lab 1: Build and Test a Skill

> Part of **[Claude.ai Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
