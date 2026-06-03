#!/usr/bin/env python3
"""DM orchestrator — calls roll.py for dice, dnd-agent for game state."""

import argparse
import json
import subprocess
import sys


def roll_dice(expr: str) -> dict:
    """Call roll.py for dice results."""
    proc = subprocess.run(
        ["python3", "scripts/roll.py", expr, "--json"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"roll.py failed: {proc.stderr}")
    return json.loads(proc.stdout)


def format_roll(result: dict, expr: str) -> str:
    rolls = result.get("rolls", result.get("kept", []))
    total = result.get("total", sum(rolls))
    note = result.get("note", "")
    return f"{expr} -> {rolls}{note} = {total}"


def cmd_roll(args):
    result = roll_dice(args.expr)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_roll(result, args.expr))


def cmd_damage_char(args):
    proc = subprocess.run(
        ["dnd-agent", "character", "damage", str(args.id), str(args.amount)] + (["--json"] if args.json else []),
        capture_output=True, text=True,
    )
    print(proc.stdout.strip() or proc.stderr.strip())


def cmd_heal_char(args):
    proc = subprocess.run(
        ["dnd-agent", "character", "heal", str(args.id), str(args.amount)] + (["--json"] if args.json else []),
        capture_output=True, text=True,
    )
    print(proc.stdout.strip() or proc.stderr.strip())


def cmd_damage_npc(args):
    proc = subprocess.run(
        ["dnd-agent", "npc", "damage", str(args.id), str(args.amount)] + (["--json"] if args.json else []),
        capture_output=True, text=True,
    )
    print(proc.stdout.strip() or proc.stderr.strip())


def cmd_story_state(args):
    proc = subprocess.run(
        ["dnd-agent", "campaign", "get-story-state", str(args.id)] + (["--json"] if args.json else []),
        capture_output=True, text=True,
    )
    print(proc.stdout.strip() or proc.stderr.strip())


def main():
    parser = argparse.ArgumentParser(description="dnd-agent DM helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("roll", help="Roll dice")
    p.add_argument("expr", help="Dice expression (e.g. d20, 2d6+3)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_roll)

    p = sub.add_parser("damage", help="Damage character")
    p.add_argument("id", type=int, help="Character ID")
    p.add_argument("amount", type=int, help="Damage amount")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_damage_char)

    p = sub.add_parser("heal", help="Heal character")
    p.add_argument("id", type=int, help="Character ID")
    p.add_argument("amount", type=int, help="Heal amount")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_heal_char)

    p = sub.add_parser("npc-damage", help="Damage NPC")
    p.add_argument("id", type=int, help="NPC ID")
    p.add_argument("amount", type=int, help="Damage amount")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_damage_npc)

    p = sub.add_parser("story-state", help="Get campaign story state")
    p.add_argument("id", type=int, help="Campaign ID")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_story_state)

    args = parser.parse_args()
    try:
        args.func(args)
        return 0
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
