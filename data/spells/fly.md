# Fly

**description**: Level 3 Transmutation (Sorcerer, Warlock, Wizard) Casting Time: Action Range: Touch Components: V, S, M (a feather) Duration: Concentration, up to 10 minutes You touch a willing creature. For the duration, the target gains a Fly Speed of 60 feet and can hover. When the spell ends, the target falls if it is still aloft unless it can stop the fall. Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Sorcerer, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Buff
- Spell Attack: None
- filter-Level: 3
- filter-Range: Touch
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Fly","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Fly\",\"description\":\"You touch a willing creature. For the duration, the target gains a Fly Speed of 60 feet and can hover. When the spell ends, the target falls if it is still aloft unless it can stop the fall.\",\"upcastText\":\"Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 3.\",\"level\":3,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"Touch\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a feather\"}}"},{"name":"Fly Upcast","parent":"Fly","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":\"\",\"target\":\"$.description\",\"value\":\"You can target one additional creature for each slot level above 3rd.\",\"changeMode\":\"Add\"}"},{"name":"Fly Condition","parent":"Fly","payload":"{\"type\":\"Condition\",\"name\":\"Fly\",\"description\":\"For the duration, the target gains a Fly Speed of 60 feet and can hover. When the spell ends, the target falls if it is still aloft unless it can stop the fall.\"}"},{"name":"Fly Speed","parent":"Fly Condition","payload":"{\"type\":\"Speed\",\"speed\":\"Fly\",\"calculation\":\"Set Base\",\"valueFormula\":{\"flatValue\":60}}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Fly
- data-description: You touch a willing creature. For the duration, the target gains a Fly Speed of 60 feet and can hover. When the spell ends, the target falls if it is still aloft unless it can stop the fall.
- Level: 3
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: Touch
- Components: V S M
- Material: a feather
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 3.
- data-CastNum: 2

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

