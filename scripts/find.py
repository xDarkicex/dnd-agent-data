#!/usr/bin/env python3
"""Search dnd-agent reference data by type and query."""

import argparse
import os
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

VALID_TYPES = [
    "backgrounds", "classes", "feats", "items", "magic-items",
    "monsters", "rules", "species", "spells",
]


def search_files(data_dir, category, query, exact=False):
    """Search files in a category directory."""
    category_dir = data_dir / category
    if not category_dir.exists():
        return []

    results = []
    for filepath in sorted(category_dir.glob("*.md")):
        name = filepath.stem.replace("-", " ")

        if exact:
            if query.lower() == name.lower():
                results.append({"name": name, "file": str(filepath), "exact": True})
        else:
            # Fuzzy match on filename
            if query.lower() in name.lower():
                results.append({"name": name, "file": str(filepath), "exact": False})
            else:
                # Also search content
                try:
                    content = filepath.read_text()
                    if query.lower() in content.lower():
                        preview = content[:300].replace("\n", " ").strip()
                        results.append({
                            "name": name,
                            "file": str(filepath),
                            "exact": False,
                            "preview": preview[:200]
                        })
                except Exception:
                    pass

    return results


def list_all(data_dir, category, limit=50):
    """List all entries in a category."""
    category_dir = data_dir / category
    if not category_dir.exists():
        return []

    names = sorted([f.stem.replace("-", " ") for f in category_dir.glob("*.md")])
    return names[:limit]


def main():
    parser = argparse.ArgumentParser(description="Search D&D reference data")
    parser.add_argument("type", nargs="?", help=f"Data type: {', '.join(VALID_TYPES)}")
    parser.add_argument("query", nargs="?", default="", help="Search query")
    parser.add_argument("--exact", action="store_true", help="Exact filename match only")
    parser.add_argument("--list", action="store_true", help="List all entries in category")
    parser.add_argument("--limit", type=int, default=20, help="Limit results (default: 20)")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    # List categories if no type given
    if not args.type:
        print("Available data types:")
        for t in VALID_TYPES:
            t_path = DATA_DIR / t
            if t_path.exists():
                count = len(list(t_path.glob("*.md")))
            else:
                count = 0
            print(f"  {t}: {count} entries")
        return 0

    # Validate type
    if args.type not in VALID_TYPES:
        print(f"Unknown type: {args.type}", file=sys.stderr)
        print(f"Valid types: {', '.join(VALID_TYPES)}", file=sys.stderr)
        return 1

    # List mode
    if args.list:
        names = list_all(DATA_DIR, args.type, args.limit)
        if args.json:
            import json
            print(json.dumps(names, indent=2))
        else:
            for name in names:
                print(f"  {name}")
            if len(names) >= args.limit:
                print(f"  ... (showing first {args.limit})")
        return 0

    # Search mode
    if not args.query:
        print("Specify a query, or use --list to list all", file=sys.stderr)
        return 1

    results = search_files(DATA_DIR, args.type, args.query, args.exact)

    if not results:
        print(f"No results for '{args.query}' in {args.type}", file=sys.stderr)
        return 1

    if args.json:
        import json
        print(json.dumps(results, indent=2))
        return 0

    # Human-readable output
    print(f"Found {len(results)} result(s) in {args.type}:\n")
    for r in results[:args.limit]:
        print(f"[{r['name']}]")
        if r.get("preview"):
            print(f"  {r['preview'][:150]}...")
        print()

    if len(results) > args.limit:
        print(f"(showing {args.limit} of {len(results)} results)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
