# dnd-agent-reference-pack — project rules

D&D 5e reference data, skills, and templates for AI agent DM pipelines.

## Repo structure

```
skills/              # AI skill definitions (Claude Code / agent instructions)
  dnd-dm-control/    # DM-facing skill
  dnd-player-character/  # Player-facing skill
docs/                # Human-readable reference docs
data/                # Machine-readable game data
  races/
  classes/
  backgrounds/
  items/
  spells/            # Parsed from srd-5.2-spells.json
templates/           # Seed templates for new campaigns / characters / NPCs
examples/            # Starter party example
```

## Skills format

Each `SKILL.md` follows the Skill spec:
- `name` — identifier
- `description` — one-liner
- `triggers` — when to activate
- `instructions` — step-by-step guidance
- `tools` — which CLI commands to invoke

## Data format

- JSON for structured data (spells, items, classes)
- Markdown for human-editable content
- All text fields are markdown-friendly

## Adding spells

Fetch from gist, parse into per-spell `.json` files in `data/spells/`.

## Build / validate

```sh
# No build needed — pure data repo
# Validate JSON files:
find data -name "*.json" -exec python3 -c "import json,sys; json.load(open(sys.argv[1]))" {} \;
```