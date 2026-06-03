# Wall of Thorns

**description**: Level 6 Conjuration (Druid) Casting Time: Action Range: 120 feet Components: V, S, M (a handful of thorns) Duration: Concentration, up to 10 minutes You create a wall of tangled brush bristling with needle-sharp thorns. The wall appears within range on a solid surface and lasts for the duration. You choose to make the wall up to 60 feet long, 10 feet high, and 5 feet thick or a circle that has a 20-foot diameter and is up to 20 feet high and 5 feet thick. The wall blocks line of sight. When the wall appears, each creature in its area makes a Dexterity saving throw, taking 7d8 Piercing damage on a failed save or half as much damage on a successful one. A creature can move through the wall, albeit slowly and painfully. For every 1 foot a creature moves through the wall, it must spend 4 feet of movement. Furthermore, the first time a creature enters a space in the wall on a turn or ends its turn there, the creature makes a Dexterity saving throw, taking 7d8 Slashing damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn. Using a Higher-Level Spell Slot. Both types of damage increase by 1d8 for each spell slot level above 6.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Dexterity Save, Inflict Damage, Utility, Piercing Damage
- Spell Attack: None
- filter-Level: 6
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Wall of Thorns","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Wall of Thorns\",\"description\":\"You create a wall of tangled brush bristling with needle-sharp thorns. The wall appears within range on a solid surface and lasts for the duration. You choose to make the wall up to 60 feet long, 10 feet high, and 5 feet thick or a circle that has a 20-foot diameter and is up to 20 feet high and 5 feet thick. The wall blocks line of sight.\\nWhen the wall appears, each creature in its area makes a Dexterity saving throw, taking 7d8 Piercing damage on a failed save or half as much damage on a successful one.\\nA creature can move through the wall, albeit slowly and painfully. For every 1 foot a creature moves through the wall, it must spend 4 feet of movement. Furthermore, the first time a creature enters a space in the wall on a turn or ends its turn there, the creature makes a Dexterity saving throw, taking 7d8 Slashing damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. Both types of damage increase by 1d8 for each spell slot level above 6.\",\"level\":6,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a handful of thorns\"},\"aoe\":{\"shape\":\"Wall\",\"size\":\"60 feet long, 10 feet high*\"}}"},{"name":"Wall of Thorns Condition","parent":"Wall of Thorns","payload":"{\"type\":\"Condition\",\"name\":\"Wall of Thorns\",\"description\":\"You create a wall of tangled brush bristling with needle-sharp thorns. The wall appears within range on a solid surface and lasts for the duration.\"}"},{"name":"Wall of Thorns On Creation Attack","parent":"Wall of Thorns","payload":"{\"type\":\"Attack\",\"name\":\"Wall of Thorns - On Creation\",\"description\":\"When the wall appears, each creature in its area makes a Dexterity saving throw, taking 7d8 Piercing damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 7d8 Piercing damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Wall\",\"size\":\"60 feet long, 10 feet high*\"}}"},{"name":"Wall of Thorns On Creation Damage","parent":"Wall of Thorns On Creation Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Piercing\",\"diceCount\":7,\"diceSize\":\"d8\"}"},{"name":"Wall of Thorns On Creation Damage Upcast","parent":"Wall of Thorns On Creation Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Wall of Thorns Walking Through Attack","parent":"Wall of Thorns","payload":"{\"type\":\"Attack\",\"name\":\"Wall of Thorns - Walking Through\",\"description\":\"Furthermore, the first time a creature enters a space in the wall on a turn or ends its turn there, the creature makes a Dexterity saving throw, taking 7d8 Slashing damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 7d8 Slashing damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Wall\",\"size\":\"60 feet long, 10 feet high*\"}}"},{"name":"Wall of Thorns Walking Through Damage","parent":"Wall of Thorns Walking Through Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Slashing\",\"diceCount\":7,\"diceSize\":\"d8\"}"},{"name":"Wall of Thorns Walking Through Damage Upcast","parent":"Wall of Thorns Walking Through Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Wall of Thorns
- data-description: You create a wall of tangled brush bristling with needle-sharp thorns. The wall appears within range on a solid surface and lasts for the duration. You choose to make the wall up to 60 feet long, 10 feet high, and 5 feet thick or a circle that has a 20-foot diameter and is up to 20 feet high and 5 feet thick. The wall blocks line of sight.
When the wall appears, each creature in its area makes a Dexterity saving throw, taking 7d8 Piercing damage on a failed save or half as much damage on a successful one.
A creature can move through the wall, albeit slowly and painfully. For every 1 foot a creature moves through the wall, it must spend 4 feet of movement. Furthermore, the first time a creature enters a space in the wall on a turn or ends its turn there, the creature makes a Dexterity saving throw, taking 7d8 Slashing damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn.
- Level: 6
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 120 feet
- Components: V S M
- Material: a handful of thorns
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. Both types of damage increase by 1d8 for each spell slot level above 6.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Dexterity
- Damage: 7d8
- Damage Type: Piercing
- data-RangeAoe: 120 ft (60 feet long, 10 feet high* ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

