# Managed policy files for Demo 9

- `managed-settings.json` is the team policy. It denies `git push`, `rm -rf` and reading `.env`, accepts only managed permission rules and managed hooks, and runs `block_dangerous.py` before every Bash command.
- `project-settings-attempt.json` is what a developer might put in a project `.claude/settings.json` to get around the policy: allow rules for the same commands, `bypassPermissions` as the default mode, and a hook that writes `project-hook-ran.txt`.

Copy `../hooks/block_dangerous.py` to `~/policy/block_dangerous.py` before you test.
