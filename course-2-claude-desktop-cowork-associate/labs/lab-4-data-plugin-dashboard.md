# Lab 4: Data Plugin Dashboard (take-home)

**Course:** Claude Desktop Associate
**Duration:** Untimed — no timed session, work at your own pace
**Format:** Take-home lab

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] `demo-files/data-plugin-dashboard`: `loan-applications.csv` and `README.md`
- [ ] A data plugin installed on your account. If one is not available, the lab still works without it
- [ ] Sample data only. **Do not connect any account**

> **Note:** do not open `README.md` until you finish a cleaning pass. It holds the answer key.

---

## Overview

`loan-applications.csv` holds 60 fictional loan applications with **nine planted data problems.** Use a data plugin to find them, clean the file, and build a dashboard.

The original file must survive unchanged. The change log is what proves you checked the work rather than accepting it.

---

## Part 1: Set Up

### Step 1: Copy the Folder

Copy the folder to your Documents folder.

### Step 2: Grant Access and Confirm the Plugin

Give Claude access to the folder. Make sure a data plugin is installed on your account.

> **Troubleshooting:** if the data plugin is not available on your plan or account, do the same steps without it and note the difference.

---

## Part 2: Profile Before Fixing

### Step 3: Profile the File and List Problems — Fix Nothing Yet

Ask Claude to profile the file and list every data quality problem it finds.

**Acceptance criteria:** a problem list produced with no changes made to the data.

### Step 4: Write the Problems in Your Own Words, Then Check the Key

List the problems in your own words. **Then** open `README.md` and check how many you found.

**Acceptance criteria:** your own list written before the key was opened.

---

## Part 3: Clean It

### Step 5: Write a Cleaned Copy and a Change Log

Ask Claude to write a cleaned copy named `loan-applications-clean.csv` and a short change log. **The original must stay unchanged.**

**Acceptance criteria:** two new files, and an untouched original.

> **Common Pitfall:** ask for an exact list of distinct branch values after cleaning. Claude often fixes typo branches but leaves the case problem.

### Step 6: Confirm No Row Was Dropped or Invented

Check the change log.

**Acceptance criteria:** a change log entry for every row touched, and no row silently dropped or invented.

> **Common Pitfall:** if the impossible date was repaired, ask Claude to flag it instead. A guess is worse than a flag.

> **Common Pitfall:** if the duplicate application ID was merged without a note, require a log entry for it.

---

## Part 4: Analyze and Visualize

### Step 7: Get the Two Headline Measures

Ask for approval rate and average days to decision, by branch and by month.

**Expected result:** both measures broken out two ways.

### Step 8: Build the Dashboard

Ask for three charts: applications by month, approval rate by branch, and average days to decision by product.

**Expected result:** a dashboard with all three charts.

### Step 9: Check Two Numbers by Hand

Check two numbers on the dashboard against the cleaned file yourself.

**Acceptance criteria:** two numbers verified by hand, not by asking Claude to confirm its own output.

---

## Part 5: Write the Reflection

### Step 10: Write Three Sentences

Cover what the data plugin did for you, what you still had to check yourself, and one thing you would not let it do unattended.

**Acceptance criteria:** all three sentences, specific to what happened in your run.

---

## Part 6: Checkpoint

### Step 11: Verify Your Progress

- [ ] The folder was copied and access granted
- [ ] The file was profiled before anything was fixed
- [ ] Your own problem list was written before opening `README.md`
- [ ] You know how many of the nine you found
- [ ] `loan-applications-clean.csv` exists
- [ ] The original file is unchanged
- [ ] A change log exists with an entry for every row touched
- [ ] No row was silently dropped or invented
- [ ] The distinct branch values after cleaning were checked explicitly, including case
- [ ] The impossible date was flagged, not repaired
- [ ] The duplicate application ID has a log entry
- [ ] No value was invented for the missing amount or the missing credit score
- [ ] Approval rate and average days to decision produced by branch and by month
- [ ] A dashboard with all three charts
- [ ] Two dashboard numbers verified by hand against the cleaned file
- [ ] Three sentences written on what the plugin did, what you checked, and what you would not automate

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| No data plugin | Not available on your plan or account | Do the same steps without it and note the difference |
| Case problem survives | Branch names still inconsistent | Ask for an exact list of distinct branch values after cleaning |
| Silent merge | Duplicate application ID merged with no note | Require a change log entry for every row touched |
| Date guessed | The impossible date was repaired | Ask Claude to flag it, not repair it |
| Values invented | A missing amount or credit score filled in | Require that missing stays missing and is reported as such |

---

## What You Built

Working at your own pace, you:

- Profiled a dataset before changing it, and wrote your own problem list before checking the answer key
- Kept the original file intact and produced a change log with an entry for every row touched
- Caught the failure modes that look like helpfulness: a guessed date, a silent merge, an invented value
- Verified two dashboard numbers by hand rather than trusting the chart
- Named one thing you would not let the tool do unattended

---

## What's Next

This is the final lab in Claude Desktop Associate. The change log is the habit to keep: it is the difference between a cleaned dataset and one you merely hope is clean.

---

## Facilitator Notes

The nine planted problems are listed in the folder README.

A good result lists all nine, keeps the original file, logs each change, and does not invent values for the missing amount or the missing credit score.

Whether a data plugin is available to students, and what it is called, is **unconfirmed**. If it is not available, the lab still works without one.

Review submitted change logs first, since they show whether the student verified the work.

---

*Lab 4 Complete*
