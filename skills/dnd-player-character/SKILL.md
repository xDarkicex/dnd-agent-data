# Skill: dnd-player-character

## Meta
name: dnd-player-character
description: Manages a D&D 5e player character — creation, leveling, inventory, spellcasting
triggers:
  - "create a character"
  - "level up"
  - "manage inventory"
  - "cast a spell"
  - "rest"
  - "use an item"

## Instructions

You are a player in a D&D 5e session. Use the dnd-agent CLI to manage your character.

### Character Creation
1. **Create**: `dnd-agent character create <name> <class> <level> <max_hp>`
2. **Set details**: `dnd-agent character set-details <id> <ac> <race> <speed> [alignment] [size]`
3. **Assign stats**: `dnd-agent character set-stats <id> <str> <dex> <con> <int> <wis> <cha>`
4. **Set skills**: `dnd-agent character set-skill <id> <skill> <level>` (0=none, 1=proficient, 2=expertise)
5. **Set saving throws**: `dnd-agent character set-save-prof <id> <str> <dex> <con> <int> <wis> <cha>`
6. **Add to campaign**: `dnd-agent character set-campaign <char_id> <campaign_id>`

### Resting
- Short rest: `dnd-agent character reset-resources <id> short_rest`
- Long rest: `dnd-agent character reset-resources <id> long_rest`

### Spellcasting
1. Learn spell: `dnd-agent spell learn <char_id> <spell_id> [prepared]`
2. Prepare spell: `dnd-agent spell prepare <char_id> <spell_id> <0/1>`
3. Cast via narrative — the DM adjudicates

### Inventory
- Add item: `dnd-agent inventory add char <char_id> <item_id> <qty>`
- Remove item: `dnd-agent inventory remove char <char_id> <item_id> <qty>`
- Equip: `dnd-agent inventory equip char <char_id> <item_id> <0/1>`
- Attune: `dnd-agent inventory attune char <char_id> <item_id> <0/1>`
- View: `dnd-agent inventory get char <char_id>`

### Money
- Add: `dnd-agent character add-money <id> <gp> <sp> <cp> [pp] [ep]`
- Remove: `dnd-agent character remove-money <id> <gp> <sp> <cp> [pp] [ep]`

### Leveling Up
1. Add class: `dnd-agent character add-class <id> <class_name> <level>`
2. Update HP: `dnd-agent character heal <id> <max_hp>` (full heal on level up)
3. Award XP: `dnd-agent character add-xp <id> <amount>`

### Resources
- Set resource: `dnd-agent character set-resource <id> <name> <max> <current> [reset_condition]`
- Use resource: `dnd-agent character use-resource <id> <name> [amount]`

### Tools
```
dnd-agent character create <name> <class> <level> <max_hp>
dnd-agent character set-details <id> <ac> <race> <speed>
dnd-agent character set-stats <id> <str> <dex> <con> <int> <wis> <cha>
dnd-agent character set-skill <id> <skill> <level>
dnd-agent character add-class <id> <class> <level>
dnd-agent character add-xp <id> <amount>

dnd-agent character damage <id> <amount>
dnd-agent character heal <id> <amount>
dnd-agent character set-temp-hp <id> <amount>
dnd-agent character set-death-saves <id> <successes> <failures>
dnd-agent character set-exhaustion <id> <level>

dnd-agent character reset-resources <id> [short_rest|long_rest]
dnd-agent character set-resource <id> <name> <max> <current> [reset_condition]
dnd-agent character use-resource <id> <name> [amount]

dnd-agent spell learn <char_id> <spell_id> [prepared]
dnd-agent spell prepare <char_id> <spell_id> <0/1>
dnd-agent spell list-character <char_id>

dnd-agent inventory add char <char_id> <item_id> <qty>
dnd-agent inventory remove char <char_id> <item_id> <qty>
dnd-agent inventory equip char <char_id> <item_id> <0/1>
dnd-agent inventory attune char <char_id> <item_id> <0/1>
dnd-agent inventory get char <char_id>
```

## Output Modes
- Human play: use plain text output
- AI pipelines: append `--json` for structured data