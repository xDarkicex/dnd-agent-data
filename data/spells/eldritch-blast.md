# Eldritch Blast

**description**: Evocation Cantrip (Warlock) Casting Time: Action Range: 120 feet Components: V, S Duration: Instantaneous You hurl a beam of crackling energy. Make a ranged spell attack against one creature or object in range. On a hit, the target takes 1d10 Force damage. Cantrip Upgrade. The spell creates two beams at level 5, three beams at level 11, and four beams at level 17. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Warlock
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Inflict Damage, Force Damage
- Spell Attack: Ranged
- filter-Level: Cantrip
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Eldritch Blast","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Eldritch Blast\",\"description\":\"You hurl a beam of crackling energy. Make a ranged spell attack against one creature or object in range. On a hit, the target takes 1d10 Force damage.\",\"upcastText\":\"Cantrip Upgrade. The spell creates two beams at level 5, three beams at level 11, and four beams at level 17. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.\",\"level\":0,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Attacks\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Eldritch Blast Attack","parent":"Eldritch Blast","payload":"{\"type\":\"Attack\",\"name\":\"Eldritch Blast\",\"repeat\":1,\"range\":\"120 feet\",\"description\":\"You hurl a beam of crackling energy.\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Action\"}"},{"name":"Eldritch Blast Damage","parent":"Eldritch Blast Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Force\",\"diceCount\":1,\"diceSize\":\"d10\"}"},{"name":"Eldritch Blast Upcast 5","parent":"Eldritch Blast Attack","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.repeat\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Eldritch Blast Upcast 11","parent":"Eldritch Blast Attack","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.repeat\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Eldritch Blast Upcast 17","parent":"Eldritch Blast Attack","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.repeat\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Eldritch Blast
- data-description: You hurl a beam of crackling energy. Make a ranged spell attack against one creature or object in range. On a hit, the target takes 1d10 Force damage.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The spell creates two beams at level 5, three beams at level 11, and four beams at level 17. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 120
- data-AttackType: Spell Attack
- Damage: 1d10
- Damage Type: Force

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

