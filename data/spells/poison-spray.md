# Poison Spray

**description**: Necromancy Cantrip (Druid, Sorcerer, Warlock, Wizard) Casting Time: Action Range: 30 feet Components: V, S Duration: Instantaneous You spray toxic mist at a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d12 Poison damage. Cantrip Upgrade. The damage increases by 1d12 when you reach levels 5 (2d12), 11 (3d12), and 17 (4d12).

**properties**:
- Category: Spells
- School: Necromancy
- Classes: Druid, Sorcerer, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Poison Damage
- Spell Attack: None
- filter-Level: Cantrip
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Poison Spray","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Poison Spray\",\"description\":\"You spray toxic mist at a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d12 Poison damage.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d12 when you reach levels 5 (2d12), 11 (3d12), and 17 (4d12).\",\"level\":0,\"school\":\"Necromancy\",\"castingTime\":\"Action\",\"range\":\"30 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Poison Spray Attack","parent":"Poison Spray","payload":"{\"type\":\"Attack\",\"name\":\"Poison Spray\",\"description\":\"Make a ranged spell attack against the target. On a hit, the target takes 1d12 Poison damage.\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Poison Spray Damage","parent":"Poison Spray Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Poison\",\"diceSize\":\"d12\"}"},{"name":"Poison Spray Damage Upcast 5","parent":"Poison Spray Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Poison Spray Damage Upcast 11","parent":"Poison Spray Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Poison Spray Damage Upcast 17","parent":"Poison Spray Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Poison Spray
- data-description: You spray toxic mist at a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d12 Poison damage.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: 30 feet
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d12 when you reach levels 5 (2d12), 11 (3d12), and 17 (4d12).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 30
- data-AttackType: Spell Attack
- Damage: 1d12
- Damage Type: Poison

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

