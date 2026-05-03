#!/usr/bin/env python3
"""Minimal entrypoint for cmd-explainer.

This provides two modes:
 - Interactive REPL (no args)
 - Single command mode: pass a command string as an argument

The implementation intentionally keeps the feature set small so the
repository is runnable without the larger datasets mentioned in the
original README (man DB, index files, etc.).
"""
import argparse
import sys
from src import parser as _parser
from src import visualizer as _viz


def main():
    ap = argparse.ArgumentParser(prog="cmd_explainer")
    ap.add_argument("command", nargs="*", help="Command to explain (if omitted, enter interactive mode)")
    args = ap.parse_args()

    if not args.command:
        # interactive
        try:
            from src.shell import interactive_shell
        except Exception as e:
            print("Interactive shell dependencies are missing:", e)
            sys.exit(1)
        interactive_shell()
    else:
        cmd = " ".join(args.command)
        structure = _parser.parse_command(cmd)
        out = _viz.render(structure)
        print(out)


if __name__ == "__main__":
    main()
