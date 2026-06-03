# Starry Wisp

**description**: Evocation Cantrip (Bard, Druid) Casting Time: Action Range: 60 feet Components: V, S Duration: Instantaneous You launch a mote of light at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d8 Radiant damage, and until the end of your next turn, it emits Dim Light in a 10-foot radius and can’t benefit from the Invisible condition. Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).

**properties**:
- Category: Spells
- Level: 0
- Range: 60 feet
- Damage: 1d8
- School: Evocation
- Target: one creature or object within range
- Classes: Bard, Druid
- Duration: Instantaneous
- Expansion: 33335
- data-List: false
- Components: V S
- Damage Type: Radiant
- filter-Tags: Attack vs AC, Radiant Damage
- Casting Time: Action
- Spell Attack: Ranged
- filter-Level: Cantrip
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Starry Wisp","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Starry Wisp\",\"description\":\"You launch a mote of light at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d8 Radiant damage, and until the end of your next turn, it emits Dim Light in a 10-foot radius and can't benefit from the Invisible condition.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).\",\"level\":0,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Starry Wisp Attack","parent":"Starry Wisp","payload":"{\"type\":\"Attack\",\"name\":\"Starry Wisp\",\"description\":\"Make a ranged spell attack against the target. On a hit, the target takes 1d8 Radiant damage, and until the end of your next turn, it emits Dim Light in a 10-foot radius and can't benefit from the Invisible condition.\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Action\"}"},{"name":"Starry Wisp Damage","parent":"Starry Wisp Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceSize\":\"d8\"}"},{"name":"Starry Wisp Damage Upcast 5","parent":"Starry Wisp Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Starry Wisp Damage Upcast 11","parent":"Starry Wisp Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Starry Wisp Damage Upcast 17","parent":"Starry Wisp Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Starry Wisp
- data-description: You launch a mote of light at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d8 Radiant damage, and until the end of your next turn, it emits Dim Light in a 10-foot radius and can't benefit from the Invisible condition.
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- data-AttackType: Spell Attack
- data-RangeAoe: 60 feet

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

