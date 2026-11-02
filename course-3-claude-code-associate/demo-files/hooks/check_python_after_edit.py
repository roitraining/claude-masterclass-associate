#!/usr/bin/env python3
"""PostToolUse hook for Edit and Write: syntax-check an edited Python file.

A stand-in for a formatter. Swap in your team's formatter command here.
Exit code 2 sends the error text back to Claude.
"""
import json
import py_compile
import sys


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    path = (data.get("tool_input") or {}).get("file_path", "")
    if not path.endswith(".py"):
        return 0
    try:
        py_compile.compile(path, doraise=True)
    except py_compile.PyCompileError as exc:
        print(f"Syntax error after edit: {exc.msg}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
