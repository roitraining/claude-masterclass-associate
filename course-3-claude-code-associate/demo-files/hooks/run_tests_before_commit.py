#!/usr/bin/env python3
"""PreToolUse hook for Bash: run the tests before any `git commit`.

Exit code 2 blocks the commit when the tests fail and sends the failure
summary back to Claude. Any other command passes straight through.
"""
import json
import os
import re
import subprocess
import sys


def python_for_tests():
    for candidate in (".venv/bin/python", ".venv/Scripts/python.exe"):
        if os.path.exists(candidate):
            return candidate
    return sys.executable


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    command = (data.get("tool_input") or {}).get("command", "")
    if not re.search(r"\bgit\s+commit\b", command):
        return 0
    result = subprocess.run(
        [python_for_tests(), "-m", "pytest", "-q", "-x"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        tail = "\n".join((result.stdout + result.stderr).splitlines()[-15:])
        print(f"Commit blocked: tests are failing. Fix them first.\n{tail}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
