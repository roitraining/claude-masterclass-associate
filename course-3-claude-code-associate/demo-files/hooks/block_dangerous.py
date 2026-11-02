#!/usr/bin/env python3
"""PreToolUse hook for Bash: block risky commands.

Reads the hook input as JSON on stdin. Exit code 2 blocks the command and
sends the stderr text back to Claude. Exit code 0 lets it continue.
"""
import json
import re
import sys

BLOCKED = [
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f|\brm\s+-[a-zA-Z]*f[a-zA-Z]*r", "recursive force delete"),
    (r"\bgit\s+push\b", "git push (this course commits locally only)"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard discards work"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f", "git clean -f deletes untracked files"),
    (r"(curl|wget)[^|]*\|\s*(ba)?sh\b", "piping a download into a shell"),
    (r"\bchmod\s+-R\s+777\b", "world-writable permissions"),
]


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    command = (data.get("tool_input") or {}).get("command", "")
    for pattern, reason in BLOCKED:
        if re.search(pattern, command):
            print(f"Blocked by policy hook: {reason}. Use a safer approach or ask the user.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
