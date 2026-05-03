"""Small interactive shell using prompt_toolkit for line editing.

If prompt_toolkit is not installed the shell falls back to a basic
read-eval-print loop using input().
"""
from .parser import parse_command
from .visualizer import render


def interactive_shell():
    try:
        from prompt_toolkit import PromptSession
    except Exception:
        PromptSession = None

    banner = "cmd-explainer> (type 'exit' or Ctrl-D to quit)"
    print(banner)

    if PromptSession:
        session = PromptSession()
        while True:
            try:
                text = session.prompt("cmd-explainer> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not text:
                continue
            if text.strip() in ("exit", "quit"):
                break
            parsed = parse_command(text)
            print(render(parsed))
    else:
        # basic loop
        while True:
            try:
                text = input("cmd-explainer> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not text:
                continue
            if text.strip() in ("exit", "quit"):
                break
            parsed = parse_command(text)
            print(render(parsed))
