# Fire Bolt

**description**: Evocation Cantrip (Sorcerer, Wizard) Casting Time: Action Range: 120 feet Components: V, S Duration: Instantaneous You hurl a mote of fire at a creature or an object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Fire damage. A flammable object hit by this spell starts burning if it isn’t being worn or carried. Cantrip Upgrade. The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Inflict Damage, Fire Damage
- Spell Attack: Ranged
- filter-Level: Cantrip
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Fire Bolt","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Fire Bolt\",\"description\":\"You hurl a mote of fire at a creature or an object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Fire damage. A flammable object hit by this spell starts burning if it isn't being worn or carried.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).\",\"level\":0,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Fire Bolt Attack","parent":"Fire Bolt","payload":"{\"type\":\"Attack\",\"name\":\"Fire Bolt\",\"range\":\"120 feet\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Action\"}"},{"name":"Fire Bolt Damage","parent":"Fire Bolt Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceSize\":\"d10\"}"},{"name":"Fire Bolt Damage Upcast 5","parent":"Fire Bolt Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Fire Bolt Damage Upcast 11","parent":"Fire Bolt Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Fire Bolt Damage Upcast 17","parent":"Fire Bolt Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Fire Bolt
- data-description: You hurl a mote of fire at a creature or an object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Fire damage. A flammable object hit by this spell starts burning if it isn't being worn or carried.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 120
- data-AttackType: Spell Attack
- Damage: 1d10
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

