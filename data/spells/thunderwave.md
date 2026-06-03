# Thunderwave

**description**: Level 1 Evocation (Bard, Druid, Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S Duration: Instantaneous You unleash a wave of thunderous energy. Each creature in a 15-foot Cube originating from you makes a Constitution saving throw. On a failed save, a creature takes 2d8 Thunder damage and is pushed 10 feet away from you. On a successful save, a creature takes half as much damage only. In addition, unsecured objects that are entirely within the Cube are pushed 10 feet away from you, and a thunderous boom is audible within 300 feet. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Bard, Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Constitution Save, Inflict Damage, Thunder Damage
- Spell Attack: None
- filter-Level: 1
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Thunderwave","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Thunderwave\",\"description\":\"You unleash a wave of thunderous energy. Each creature in a 15-foot Cube originating from you makes a Constitution saving throw. On a failed save, a creature takes 2d8 Thunder damage and is pushed 10 feet away from you. On a successful save, a creature takes half as much damage only.\\nIn addition, unsecured objects that are entirely within the Cube are pushed 10 feet away from you, and a thunderous boom is audible within 300 feet.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Cube\",\"size\":\"15 foot\"}}"},{"name":"Thunderwave Attack","parent":"Thunderwave","payload":"{\"type\":\"Attack\",\"name\":\"Thunderwave\",\"description\":\"You unleash a wave of thunderous energy. Each creature in a 15-foot Cube originating from you makes a Constitution saving throw.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Takes 2d8 Thunder damage and is pushed 10 feet away from you.\",\"onSucceed\":\"Half as much damage only.\"},\"aoe\":{\"shape\":\"Cube\",\"size\":\"15 foot\"},\"actionType\":\"Action\"}"},{"name":"Thunderwave Damage","parent":"Thunderwave Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Thunder\",\"diceCount\":2,\"diceSize\":\"d8\"}"},{"name":"Thunderwave Damage Upcast","parent":"Thunderwave Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Thunderwave
- data-description: You unleash a wave of thunderous energy. Each creature in a 15-foot Cube originating from you makes a Constitution saving throw. On a failed save, a creature takes 2d8 Thunder damage and is pushed 10 feet away from you. On a successful save, a creature takes half as much damage only.
In addition, unsecured objects that are entirely within the Cube are pushed 10 feet away from you, and a thunderous boom is audible within 300 feet.
- Level: 1
- Casting Time: Action
- Duration: Instantaneous
- Range: Self
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 0
- Save: Constitution
- Damage: 2d8
- Damage Type: Thunder
- data-RangeAoe: Self (15 ft □)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

