# Guiding Bolt

**description**: Level 1 Evocation (Cleric) Casting Time: Action Range: 120 feet Components: V, S Duration: 1 round You hurl a bolt of light toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 4d6 Radiant damage, and the next attack roll made against it before the end of your next turn has Advantage. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Radiant Damage, Attack vs AC
- Spell Attack: Ranged
- filter-Level: 1
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 turn
- data-datarecords: [{"name":"Guiding Bolt","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Guiding Bolt\",\"description\":\"You hurl a bolt of light toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 4d6 Radiant damage, and the next attack roll made against it before the end of your next turn has Advantage.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"1 round\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Guiding Bolt Attack","parent":"Guiding Bolt","payload":"{\"type\":\"Attack\",\"name\":\"Guiding Bolt\",\"range\":\"120 feet\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Action\"}"},{"name":"Guiding Bolt Damage","parent":"Guiding Bolt Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceCount\":4,\"diceSize\":\"d6\"}"},{"name":"Guiding Bolt Damage Upcast","parent":"Guiding Bolt Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Guiding Bolt
- data-description: You hurl a bolt of light toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 4d6 Radiant damage, and the next attack roll made against it before the end of your next turn has Advantage.
- Level: 1
- Casting Time: Action
- Duration: 1 round
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 2
- data-RangeNum: 120
- data-AttackType: Spell Attack
- Damage: 4d6
- Damage Type: Radiant

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

