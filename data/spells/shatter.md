# Shatter

**description**: Level 2 Evocation (Bard, Sorcerer, Wizard) Casting Time: Action Range: 60 feet Components: V, S, M (a chip of mica) Duration: Instantaneous A loud noise erupts from a point of your choice within range. Each creature in a 10-foot-radius Sphere centered there makes a Constitution saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save. A nonmagical object that isn’t being worn or carried also takes the damage if it’s in the spell’s area. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Bard, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Thunder Damage
- Spell Attack: None
- filter-Level: 2
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Shatter","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Shatter\",\"description\":\"A loud noise erupts from a point of your choice within range. Each creature in a 10-foot-radius Sphere centered there makes a Constitution saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save.\\nA nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 2.\",\"level\":2,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a chip of mica\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"10 foot radius\"}}"},{"name":"Shatter Attack","parent":"Shatter","payload":"{\"type\":\"Attack\",\"name\":\"Shatter\",\"description\":\"Each creature in a 10-foot-radius Sphere centered there makes a Constitution saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 3d8 Thunder damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"10 foot radius\"}}"},{"name":"Shatter Damage","parent":"Shatter Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Thunder\",\"diceCount\":3,\"diceSize\":\"d8\"}"},{"name":"Shatter Damage Upcast","parent":"Shatter Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Shatter
- data-description: A loud noise erupts from a point of your choice within range. Each creature in a 10-foot-radius Sphere centered there makes a Constitution saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save.
A nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area.
- Level: 2
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V S M
- Material: a chip of mica
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 2.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Constitution
- Damage: 3d8
- Damage Type: Thunder
- data-RangeAoe: 60 ft (10 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

