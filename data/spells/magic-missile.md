# Magic Missile

**description**: Level 1 Evocation (Sorcerer, Wizard) Casting Time: Action Range: 120 feet Components: V, S Duration: Instantaneous You create three glowing darts of magical force. Each dart strikes a creature of your choice that you can see within range. A dart deals 1d4 + 1 Force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several. Using a Higher-Level Spell Slot. The spell creates one more dart for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Force Damage
- Spell Attack: None
- filter-Level: 1
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Magic Missile","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Magic Missile\",\"description\":\"You create three glowing darts of magical force. Each dart strikes a creature of your choice that you can see within range. A dart deals 1d4 + 1 Force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The spell creates one more dart for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Magic Missile Free Attack","parent":"Magic Missile","payload":"{\"type\":\"Attack\",\"name\":\"Magic Missile\",\"autoHit\":true,\"repeat\":3,\"range\":\"120 feet\"}"},{"name":"Magic Missile Damage","parent":"Magic Missile Free Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"_bonus\":1,\"damageType\":\"Force\",\"diceSize\":\"d4\"}"},{"name":"Magic Missle Upcast","parent":"Magic Missile Free Attack","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.repeat\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Magic Missile
- data-description: You create three glowing darts of magical force. Each dart strikes a creature of your choice that you can see within range. A dart deals 1d4 + 1 Force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.
- Level: 1
- Casting Time: Action
- Duration: Instantaneous
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The spell creates one more dart for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 120
- Damage: 1d4
- Damage Type: Force

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

