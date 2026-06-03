# Scorching Ray

**description**: Level 2 Evocation (Sorcerer, Wizard) Casting Time: Action Range: 120 feet Components: V, S Duration: Instantaneous You hurl three fiery rays. You can hurl them at one target within range or at several. Make a ranged spell attack for each ray. On a hit, the target takes 2d6 Fire damage. Using a Higher-Level Spell Slot. You create one additional ray for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Fire Damage
- Spell Attack: Ranged
- filter-Level: 2
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Scorching Ray","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Scorching Ray\",\"description\":\"You hurl three fiery rays. You can hurl them at one target within range or at several. Make a ranged spell attack for each ray. On a hit, the target takes 2d6 Fire damage.\",\"upcastText\":\"Using a Higher-Level Spell Slot. You create one additional ray for each spell slot level above 2.\",\"level\":2,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Scorching Ray Attack","parent":"Scorching Ray","payload":"{\"type\":\"Attack\",\"name\":\"Scorching Ray\",\"repeat\":3,\"range\":\"120 feet\",\"description\":\"You hurl three fiery rays. You can hurl them at one target within range or at several. Make a ranged spell attack for each ray.\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Action\"}"},{"name":"Scorching Ray Damage","parent":"Scorching Ray Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":2,\"diceSize\":\"d6\"}"},{"name":"Scorching Ray Upcast","parent":"Scorching Ray Attack","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.repeat\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Scorching Ray
- data-description: You hurl three fiery rays. You can hurl them at one target within range or at several. Make a ranged spell attack for each ray. On a hit, the target takes 2d6 Fire damage.
- Level: 2
- Casting Time: Action
- Duration: Instantaneous
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. You create one additional ray for each spell slot level above 2.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 120
- data-AttackType: Spell Attack
- Damage: 2d6
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

