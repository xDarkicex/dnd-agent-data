#!/usr/bin/env python3
"""Small public-safe formatter around the diceroll CLI."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass


ROLL_RE = re.compile(r"^(?P<count>\d*)d(?P<sides>\d+)(?P<keep>k[hl]\d+)?(?P<mod>[+-]\d+)?$")


@dataclass
class RollResult:
    expression: str
    rolls: list[int]
    kept: list[int]
    modifier: int

    @property
    def total(self) -> int:
        return sum(self.kept) + self.modifier


def parse_expression(expr: str) -> tuple[int, int, str | None, int]:
    match = ROLL_RE.match(expr.replace(" ", ""))
    if not match:
        raise ValueError(f"unsupported dice expression: {expr}")

    count = int(match.group("count") or "1")
    sides = int(match.group("sides"))
    keep = match.group("keep")
    modifier = int(match.group("mod") or "0")
    if count <= 0 or sides <= 0:
        raise ValueError("dice count and sides must be positive")
    return count, sides, keep, modifier


def call_diceroll(count: int, sides: int) -> list[int]:
    if not shutil.which("diceroll"):
        raise RuntimeError("diceroll is not installed or not on PATH")

    spec = f"d{sides}"
    proc = subprocess.run(
        ["diceroll", "roll", spec, str(count), "--json"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    payload = json.loads(proc.stdout)

    if isinstance(payload, list):
        return [int(v) for v in payload]
    if isinstance(payload, dict):
        for key in ("rolls", "results", "values"):
            if key in payload:
                return [int(v) for v in payload[key]]
        if "total" in payload and count == 1:
            return [int(payload["total"])]

    raise RuntimeError(f"unrecognized diceroll JSON: {payload!r}")


def keep_rolls(rolls: list[int], keep: str | None) -> list[int]:
    if not keep:
        return rolls

    mode = keep[1]
    n = int(keep[2:])
    if n <= 0:
        raise ValueError("keep count must be positive")
    sorted_rolls = sorted(rolls, reverse=(mode == "h"))
    return sorted_rolls[:n]


def format_result(result: RollResult) -> str:
    mod = ""
    if result.modifier > 0:
        mod = f" +{result.modifier}"
    elif result.modifier < 0:
        mod = f" {result.modifier}"

    kept = ""
    if result.kept != result.rolls:
        kept = f" keep {result.kept}"

    return f"{result.expression} -> {result.rolls}{kept}{mod} = {result.total}"


def roll(expr: str) -> RollResult:
    count, sides, keep, modifier = parse_expression(expr)
    rolls = call_diceroll(count, sides)
    kept = keep_rolls(rolls, keep)
    return RollResult(expr, rolls, kept, modifier)


def main() -> int:
    parser = argparse.ArgumentParser(description="Format diceroll output for DnD agents.")
    parser.add_argument("expression", help="Dice expression, e.g. d20, 3d6, 2d20kh1+5")
    parser.add_argument("--json", action="store_true", help="Output structured JSON")
    args = parser.parse_args()

    try:
        result = roll(args.expression)
    except Exception as exc:
        print(f"roll error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result.__dict__ | {"total": result.total}, indent=2))
    else:
        print(format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
