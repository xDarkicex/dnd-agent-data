# Cone of Cold

**description**: Level 5 Evocation (Druid, Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S, M (a small crystal or glass cone) Duration: Instantaneous You unleash a blast of cold air. Each creature in a 60-foot Cone originating from you makes a Constitution saving throw, taking 8d8 Cold damage on a failed save or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Cold Damage
- Spell Attack: None
- filter-Level: 5
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Cone of Cold","level":"5","payload":"{\"type\":\"Spell\",\"name\":\"Cone of Cold\",\"description\":\"You unleash a blast of cold air. Each creature in a 60-foot Cone originating from you makes a Constitution saving throw, taking 8d8 Cold damage on a failed save or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.\",\"level\":5,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a small crystal or glass cone\"},\"aoe\":{\"shape\":\"Cone\",\"size\":\"60 foot\"}}"},{"name":"Cone of Cold Attack","parent":"Cone of Cold","payload":"{\"type\":\"Attack\",\"name\":\"Cone of Cold\",\"description\":\"You unleash a blast of cold air. Each creature in a 60-foot Cone originating from you makes a Constitution saving throw, taking 8d8 Cold damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 8d8 Cold damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Cone\",\"size\":\"60 ft\"},\"actionType\":\"Action\"}"},{"name":"Cone of Cold Damage","parent":"Cone of Cold Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceCount\":8,\"diceSize\":\"d8\"}"},{"name":"Cone of Cold Damage Upcast","parent":"Cone of Cold Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Cone of Cold
- data-description: You unleash a blast of cold air. Each creature in a 60-foot Cone originating from you makes a Constitution saving throw, taking 8d8 Cold damage on a failed save or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws.
- Level: 5
- Casting Time: Action
- Duration: Instantaneous
- Range: Self
- Components: V S M
- Material: a small crystal or glass cone
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.
- data-CastNum: 2
- data-DurationNum: 0
- Save: Constitution
- Damage: 8d8
- Damage Type: Cold
- data-RangeAoe: Self (60 ft ▽)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

