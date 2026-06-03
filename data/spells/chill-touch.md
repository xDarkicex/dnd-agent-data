# Chill Touch

**description**: Necromancy Cantrip (Sorcerer, Warlock, Wizard) Casting Time: Action Range: Touch Components: V, S Duration: Instantaneous Channeling the chill of the grave, make a melee spell attack against a target within reach. On a hit, the target takes 1d10 Necrotic damage, and it can’t regain Hit Points until the end of your next turn. Cantrip Upgrade. The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).

**properties**:
- Category: Spells
- School: Necromancy
- Classes: Sorcerer, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Necrotic Damage, Debuff, Inflict Condition
- Spell Attack: Melee
- filter-Level: Cantrip
- filter-Range: Touch
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Chill Touch","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Chill Touch\",\"description\":\"Channeling the chill of the grave, make a melee spell attack against a target within reach. On a hit, the target takes 1d10 Necrotic damage, and it can't regain Hit Points until the end of your next turn.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).\",\"level\":0,\"school\":\"Necromancy\",\"castingTime\":\"Action\",\"range\":\"Touch\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Chill Touch Attack","parent":"Chill Touch","payload":"{\"type\":\"Attack\",\"name\":\"Chill Touch\",\"attack\":{\"type\":\"Spell Attack\",\"proficiencyLevel\":\"Proficient\"}}"},{"name":"Chill Touch Damage","parent":"Chill Touch Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Necrotic\",\"diceSize\":\"d10\"}"},{"name":"Chill Touch Damage Upcast 5","parent":"Chill Touch Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Chill Touch Damage Upcast 11","parent":"Chill Touch Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Chill Touch Damage Upcast 17","parent":"Chill Touch Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Chill Touch
- data-description: Channeling the chill of the grave, make a melee spell attack against a target within reach. On a hit, the target takes 1d10 Necrotic damage, and it can't regain Hit Points until the end of your next turn.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: Touch
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).
- data-CastNum: 2
- data-DurationNum: 0
- data-AttackType: Spell Attack
- Damage: 1d10
- Damage Type: Necrotic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

