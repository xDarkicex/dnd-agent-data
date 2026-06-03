# dnd-agent-reference-pack

> Machine-readable D&D 5e SRD data, AI skill definitions, and templates for AI-driven DM pipelines.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Contents

### Skills (`skills/`)
AI agent instruction sets for running D&D sessions:
- **`dnd-dm-control/`** — DM-facing skill: session control, NPC behavior, combat pacing
- **`dnd-player-character/`** — Player-facing skill: character creation, inventory, leveling

### Reference Data (`data/`)
Machine-readable SRD 5.2 data:
- `races/` — playable races
- `classes/` — class features and progressions
- `backgrounds/` — character backgrounds
- `items/` — equipment and loot
- `spells/` — all SRD spells (parsed from [dmcb/srd-5.2-spells.json](https://gist.github.com/dmcb/4b67869f962e3adaa3d0f7e5ca8f4912))

### Templates (`templates/`)
Seed templates for quick campaign setup:
- `character-sheet.md` — blank character sheet
- `campaign-seed.md` — campaign premise scaffold
- `npc.md` — NPC quick-stat block

### Examples (`examples/`)
- `starter-party/` — pre-built starting party with balanced classes

## Using with dnd-agent CLI

```sh
# Initialize campaign
dnd-agent campaign create "Lost Mine of Phandelver"

# Use spells data to look up Fireball
cat data/spells/fireball.json

# Seed NPCs from template
dnd-agent npc create "Gundren Rockseeker" "DM's dwarf cousin" 12 1
```

## Sources

- SRD 5.2 spells: [dmcb/srd-5.2-spells.json](https://gist.github.com/dmcb/4b67869f962e3adaa3d0f7e5ca8f4912)
- Full SRD markdown: [downfallx/dnd-5e-srd-markdown](https://github.com/downfallx/dnd-5e-srd-markdown)
- Compatible with [compoodment/dnd-agent-reference-pack](https://github.com/compoodment/dnd-agent-reference-pack)