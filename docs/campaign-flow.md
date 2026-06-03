# Campaign Flow

## Session Lifecycle

### 1. Pre-Session
- Review campaign story state: `dnd-agent campaign get-story-state <id> --json`
- Check party status: `dnd-agent character list`
- Review faction standings: `dnd-agent faction get-standing <char_id>`

### 2. In-Session Actions

#### Explore / Roleplay
- Log an action: `dnd-agent campaign add-action <id> "<description>" [location_id] [faction_id] [standing_impact]`
- Link actors: `dnd-agent campaign link-actor <action_id> char|npc <actor_id>`
- Update NPC location: `dnd-agent npc set-location <npc_id> <location_id>`

#### Combat
1. Track damage: `dnd-agent character damage <id> <amount>` / `dnd-agent npc damage <id> <amount>`
2. Handle temp HP automatically via `damage` command
3. Use spell data from `data/spells/` for adjudication

#### Resting
- Short rest: `dnd-agent character reset-resources <id> short_rest`
- Long rest: `dnd-agent character reset-resources <id> long_rest`

### 3. End Session
- Advance session count: `dnd-agent campaign next-session <id>`
- Review final story state: `dnd-agent campaign get-story-state <id>`

## Story State Report
The `campaign get-story-state` command outputs a comprehensive report:
- Session number and current location
- All character HP/status
- Faction standings
- Chronological action log

## NPC Relationships
- Set friendship: `dnd-agent npc set-relationship <npc1> <npc2> <level>` (-10 to +10)
- View relationships: `dnd-agent npc list-relationships <npc_id>`

## Faction Standing
- Create faction: `dnd-agent faction create <name> <desc>`
- Join: `dnd-agent faction join char|npc <actor_id> <faction_id>`
- Set standing: `dnd-agent faction set-standing <char_id> <faction_id> <value> [notes]`
- Standing range: -100 (hostile) to +100 (ally)