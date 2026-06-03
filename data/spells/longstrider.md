# Longstrider

**description**: Level 1 Transmutation (Bard, Druid, Ranger, Wizard) Casting Time: Action Range: Touch Components: V, S, M (a pinch of dirt) Duration: 1 hour You touch a creature. The target’s Speed increases by 10 feet until the spell ends. Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Bard, Druid, Ranger, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Buff
- Spell Attack: None
- filter-Level: 1
- filter-Range: Touch
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 hour
- data-datarecords: [{"name":"Longstrider","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Longstrider\",\"description\":\"You touch a creature. The target's Speed increases by 10 feet until the spell ends.\",\"upcastText\":\"Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 1.\",\"level\":1,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"Touch\",\"duration\":\"1 hour\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a pinch of dirt\"}}"},{"name":"Longstrider Upcast","parent":"Longstrider","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":\"\",\"target\":\"$.description\",\"value\":\"You can target one additional creature for each slot level.\",\"changeMode\":\"Add\"}"},{"name":"Longstrider Condition","parent":"Longstrider","payload":"{\"type\":\"Condition\",\"name\":\"Longstrider\"}"},{"name":"Longstrider Speed Increase","parent":"Longstrider Condition","payload":"{\"type\":\"Speed\",\"speed\":\"Walk\",\"calculation\":\"Modify\",\"valueFormula\":{\"flatValue\":10}}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Longstrider
- data-description: You touch a creature. The target's Speed increases by 10 feet until the spell ends.
- Level: 1
- Casting Time: Action
- Duration: 1 hour
- Range: Touch
- Components: V S M
- Material: a pinch of dirt
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 9

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

