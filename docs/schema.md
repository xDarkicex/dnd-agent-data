# Schema Notes

This repo expects the `dnd-agent` SQLite schema to own durable game state.

Core entity groups:

- `campaigns`, `locations`
- `characters`, `character_classes`, `character_skills`, `character_resources`
- `npcs`, `npc_relationships`
- `creatures`
- `items`, `inventory`
- `factions`, `faction_standings`
- `spells`, `character_spells`
- `features`, `character_features`
- `story_actions`, `story_action_actors`

Do not duplicate live state into Markdown except as generated preview/export text.
