# Lab 4: Data Plugin Dashboard (take-home)

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

**Learning objective:** Clean, analyze, and visualize a dataset on your own with a data plugin. No timed session.

**Files:** `demo-files/data-plugin-dashboard`: `loan-applications.csv` and `README.md`. Do not open the README until you finish a cleaning pass.

**Context:** `loan-applications.csv` holds 60 fictional loan applications with planted data problems. Use a data plugin to find them, clean the file, and build a dashboard. Use sample data only. Do not connect any account.

**Steps:**

1. Copy the folder to your Documents folder.
2. Give Claude access to the folder. Make sure a data plugin is installed on your account.
3. Ask Claude to profile the file and list every data quality problem it finds. Do not fix anything yet.
4. List the problems in your own words. Then open `README.md` and check how many you found.
5. Ask Claude to write a cleaned copy named `loan-applications-clean.csv` and a short change log. The original must stay unchanged.
6. Check the change log. Confirm that no row was silently dropped or invented.
7. Ask for approval rate and average days to decision by branch and by month.
8. Ask for a dashboard with three charts: applications by month, approval rate by branch, and average days to decision by product.
9. Check two numbers on the dashboard against the cleaned file by hand.
10. Write three sentences: what the data plugin did for you, what you still had to check yourself, and one thing you would not let it do unattended.

**Checkpoint:** A cleaned file, a change log, a dashboard, and your three sentences.

**Common problems:**

- The data plugin is not available on your plan or account. Do the same steps without it and note the difference.
- Claude fixes the typo branches but not the case problem. Ask for an exact list of distinct branch values after cleaning.
- The duplicate application ID is merged without a note. Require a change log entry for every row touched.
- The impossible date is guessed. Ask Claude to flag it, not repair it.

**Facilitator note:** The nine planted problems are listed in the folder README. A good result lists all nine, keeps the original file, logs each change, and does not invent values for the missing amount or the missing credit score. Whether a data plugin is available to students, and what it is called, is **unconfirmed**. If it is not available, the lab still works without one. Review submitted change logs first, since they show whether the student verified the work.
