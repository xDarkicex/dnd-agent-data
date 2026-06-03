---
name: data-lookup
description: Search D&D 5e reference data — rules, spells, items, species, classes, feats, and more.
---

# Data Lookup

Use `scripts/find.py` to search the reference data when you need to look up rules, spells, items, species, classes, feats, or monsters.

## Quick Reference

```bash
# List all data categories
python3 scripts/find.py

# List all entries in a category
python3 scripts/find.py spells --list
python3 scripts/find.py classes --list
python3 scripts/find.py magic-items --list

# Search by keyword
python3 scripts/find.py <category> <query>
python3 scripts/find.py items sword
python3 scripts/find.py spells fire
python3 scripts/find.py rules combat
python3 scripts/find.py species dwarf
python3 scripts/find.py feats sentinel

# Limit results
python3 scripts/find.py spells fire --limit 10

# Exact filename match
python3 scripts/find.py spells "magic missile" --exact

# JSON output (for parsing)
python3 scripts/find.py items sword --json
```

## Categories

| Category | What to search |
|----------|---------------|
| `backgrounds` | Character backgrounds (acolyte, soldier, folk hero, etc.) |
| `classes` | Class features (barbarian, wizard, rogue, etc.) |
| `feats` | Feats (alert, sentinel, heavy armor master, etc.) |
| `items` | Equipment, gear, mundane items |
| `magic-items` | Magic items (vorpal sword, ring of invisibility, etc.) |
| `monsters` | Creatures (lich, ancient dragon, goblin, etc.) |
| `rules` | Game rules (actions in combat, conditions, exploration, etc.) |
| `species` | Playable species (dragonborn, elf, halfling, etc.) |
| `spells` | Spell descriptions (fireball, cure wounds, misty step, etc.) |

## Workflow

1. **Don't guess** — always look up rules, spells, items, or monster stats
2. Use `find.py` to locate the relevant file
3. Read the file to get precise rules/text
4. Apply the information

## Examples

**"What's the range of Fireball?"**
```bash
python3 scripts/find.py spells fireball
```

**"What armor does the Fighter get?"**
```bash
python3 scripts/find.py classes fighter
```

**"What are the trap rules?"**
```bash
python3 scripts/find.py rules trap
```

**"List all healing spells"**
```bash
python3 scripts/find.py spells healing --limit 20
```

**"Find all rings"**
```bash
python3 scripts/find.py magic-items ring --list
```
