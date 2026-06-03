# Ray of Frost

**description**: Evocation Cantrip (Sorcerer, Wizard) Casting Time: Action Range: 60 feet Components: V, S Duration: Instantaneous A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 Cold damage, and its Speed is reduced by 10 feet until the start of your next turn. Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Cold Damage
- Spell Attack: Ranged
- filter-Level: Cantrip
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Ray of Frost","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Ray of Frost\",\"description\":\"A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 Cold damage, and its Speed is reduced by 10 feet until the start of your next turn.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).\",\"level\":0,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Ray of Frost Attack","parent":"Ray of Frost","payload":"{\"type\":\"Attack\",\"name\":\"Ray of Frost\",\"range\":\"60 feet\",\"description\":\"A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 Cold damage, and its Speed is reduced by 10 feet until the start of your next turn.\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Ray of Frost Damage","parent":"Ray of Frost Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceSize\":\"d8\"}"},{"name":"Ray of Frost Damage Upcast 5","parent":"Ray of Frost Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Ray of Frost Damage Upcast 11","parent":"Ray of Frost Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Ray of Frost Damage Upcast 17","parent":"Ray of Frost Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Ray of Frost
- data-description: A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 Cold damage, and its Speed is reduced by 10 feet until the start of your next turn.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- data-AttackType: Spell Attack
- Damage: 1d8
- Damage Type: Cold

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

