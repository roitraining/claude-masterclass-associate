# Lab 2: Scoring Guide

Score each candidate task from 1 to 5 on six criteria.

| Criterion | 1 means | 5 means |
|-----------|---------|---------|
| Impact | Small benefit | Large benefit to members or staff |
| Effort | Easy to build and test | Hard to build and test |
| Data sensitivity | Public or generic data | Regulated or personal data |
| Frequency | A few times a year | Daily |
| Reuse | One person uses it | Many people or teams use it |
| Review burden | Output needs a glance | Every output needs expert review |

## Score

Score = 2 x Impact + Frequency + Reuse + (6 - Effort) + (6 - Data sensitivity) + (6 - Review burden)

The maximum is 35. Effort, sensitivity and review burden count against a task, so they are flipped.

## Decision rule

1. Data sensitivity of 5: **Hold, governance first.** Do not build until a data owner approves.
2. Frequency 3 or more, Reuse 3 or more, and Score 22 or more: **Skill.**
3. Everything else: **One-off prompt.**

Break ties by the higher Impact, then the lower Data sensitivity.

## Business case sentence

For the top pick, write: "[Task] takes [baseline] minutes, happens [runs] times a week, and a Skill [what changes], so we expect to save about [hours] hours a week across [people] people."
