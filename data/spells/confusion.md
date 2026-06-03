# Confusion

**description**: Level 4 Enchantment (Bard, Druid, Sorcerer, Wizard) Casting Time: Action Range: 90 feet Components: V, S, M (three nut shells) Duration: Concentration, up to 1 minute Each creature in a 10-foot-radius Sphere centered on a point you choose within range must succeed on a Wisdom saving throw, or that target can’t take Bonus Actions or Reactions and must roll 1d10 at the start of each of its turns to determine its behavior for that turn, consulting the table below. 1d10 Behavior for the Turn 1 The target doesn’t take an action, and it uses all its movement to move. Roll 1d4 for the direction: 1, north; 2, east; 3, south; or 4, west. 2–6 The target doesn’t move or take actions. 7–8 The target doesn’t move, and it takes the Attack action to make one melee attack against a random creature within reach. If none are within reach, the target takes no action. 9–10 The target chooses its behavior. At the end of each of its turns, an affected target repeats the save, ending the spell on itself on a success. Using a Higher-Level Spell Slot. The Sphere’s radius increases by 5 feet for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Enchantment
- Classes: Bard, Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Condition, Wisdom Save
- Spell Attack: None
- filter-Level: 4
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Confusion","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Confusion\",\"description\":\"Each creature in a 10-foot-radius Sphere centered on a point you choose within range must succeed on a Wisdom saving throw, or that target can't take Bonus Actions or Reactions and must roll 1d10 at the start of each of its turns to determine its behavior for that turn, consulting the table below.\\n1d10 - Behavior for the Turn\\n1 - The target doesn't take an action, and it uses all its movement to move. Roll 1d4 for the direction: 1, north; 2, east; 3, south; or 4, west.\\n2-6 - The target doesn't move or take actions.\\n7-8 - The target doesn't move, and it takes the Attack action to make one melee attack against a random creature within reach. If none are within reach, the target takes no action.\\n9-10 - The target chooses its behavior.\\nAt the end of each of its turns, an affected target repeats the save, ending the spell on itself on a success.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The Sphere's radius increases by 5 feet for each spell slot level above 4.\",\"level\":4,\"school\":\"Enchantment\",\"castingTime\":\"Action\",\"range\":\"90 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"three nut shells\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"10 foot radius\"}}"},{"name":"Confusion Attack","parent":"Confusion","payload":"{\"type\":\"Attack\",\"name\":\"Confusion\",\"range\":\"90 feet\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Target can't take Bonus Actions or Reactions and must roll 1d10 at the start of each of its turns to determine its behavior for that turn, consulting the spell's table.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"10 foot radius\"},\"actionType\":\"Action\"}"},{"name":"Confusion AOE Size Upcast 1","parent":"Confusion","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":5,\"target\":\"$.aoe.size\",\"value\":\"15 ft radius\",\"changeMode\":\"Override\"}"},{"name":"Confusion AOE Size Upcast 2","parent":"Confusion","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":6,\"target\":\"$.aoe.size\",\"value\":\"20 ft radius\",\"changeMode\":\"Override\"}"},{"name":"Confusion AOE Size Upcast 3","parent":"Confusion","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":7,\"target\":\"$.aoe.size\",\"value\":\"25 ft radius\",\"changeMode\":\"Override\"}"},{"name":"Confusion AOE Size Upcast 4","parent":"Confusion","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":8,\"target\":\"$.aoe.size\",\"value\":\"30 ft radius\",\"changeMode\":\"Override\"}"},{"name":"Confusion AOE Size Upcast 5","parent":"Confusion","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":9,\"target\":\"$.aoe.size\",\"value\":\"35 ft radius\",\"changeMode\":\"Override\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Confusion
- data-description: Each creature in a 10-foot-radius Sphere centered on a point you choose within range must succeed on a Wisdom saving throw, or that target can't take Bonus Actions or Reactions and must roll 1d10 at the start of each of its turns to determine its behavior for that turn, consulting the table below.
1d10 - Behavior for the Turn
1 - The target doesn't take an action, and it uses all its movement to move. Roll 1d4 for the direction: 1, north; 2, east; 3, south; or 4, west.
2-6 - The target doesn't move or take actions.
7-8 - The target doesn't move, and it takes the Attack action to make one melee attack against a random creature within reach. If none are within reach, the target takes no action.
9-10 - The target chooses its behavior.
At the end of each of its turns, an affected target repeats the save, ending the spell on itself on a success.
- Level: 4
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 90 feet
- Components: V S M
- Material: three nut shells
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The Sphere's radius increases by 5 feet for each spell slot level above 4.
- data-CastNum: 2
- data-RangeNum: 90
- Save: Wisdom
- data-RangeAoe: 90 ft (10 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

