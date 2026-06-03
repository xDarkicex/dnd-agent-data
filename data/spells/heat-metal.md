# Heat Metal

**description**: Level 2 Transmutation (Bard, Druid) Casting Time: Action Range: 60 feet Components: V, S, M (a piece of iron and a flame) Duration: Concentration, up to 1 minute Choose a manufactured metal object, such as a metal weapon or a suit of Heavy or Medium metal armor, that you can see within range. You cause the object to glow red-hot. Any creature in physical contact with the object takes 2d8 Fire damage when you cast the spell. Until the spell ends, you can take a Bonus Action on each of your later turns to deal this damage again if the object is within range. If a creature is holding or wearing the object and takes the damage from it, the creature must succeed on a Constitution saving throw or drop the object if it can. If it doesn’t drop the object, it has Disadvantage on attack rolls and ability checks until the start of your next turn. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Bard, Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Fire Damage, Constitution Save
- Spell Attack: None
- filter-Level: 2
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Heat Metal","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Heat Metal\",\"description\":\"Choose a manufactured metal object, such as a metal weapon or a suit of Heavy or Medium metal armor, that you can see within range. You cause the object to glow red-hot. Any creature in physical contact with the object takes 2d8 Fire damage when you cast the spell. Until the spell ends, you can take a Bonus Action on each of your later turns to deal this damage again if the object is within range.\\nIf a creature is holding or wearing the object and takes the damage from it, the creature must succeed on a Constitution saving throw or drop the object if it can. If it doesn't drop the object, it has Disadvantage on attack rolls and ability checks until the start of your next turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 2.\",\"level\":2,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a piece of iron and a flame\"}}"},{"name":"Heat Metal Condition","parent":"Heat Metal","payload":"{\"type\":\"Condition\",\"name\":\"Heat Metal\",\"description\":\"Choose a manufactured metal object, such as a metal weapon or a suit of Heavy or Medium metal armor, that you can see within range. You cause the object to glow red-hot.\"}"},{"name":"Heat Metal Bonus Action","parent":"Heat Metal Condition","payload":"{\"type\":\"Action\",\"name\":\"Heat Metal\",\"description\":\"Until the spell ends, you can take a Bonus Action on each of your later turns to deal this damage again if the object is within range.\",\"actionType\":\"Bonus Action\"}"},{"name":"Heat Metal Attack","parent":"Heat Metal","payload":"{\"type\":\"Attack\",\"name\":\"Heat Metal\",\"range\":\"60 feet\",\"actionType\":\"Free Action\"}"},{"name":"Heat Metal Damage","parent":"Heat Metal Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":2,\"diceSize\":\"d8\"}"},{"name":"Heat Metal Damage Upcast","parent":"Heat Metal Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Heat Metal Drop Object Attack","parent":"Heat Metal","payload":"{\"type\":\"Attack\",\"name\":\"Heat Metal - Drop Object\",\"range\":\"60 feet\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"If it doesn't drop the object, it has Disadvantage on attack rolls and ability checks until the start of your next turn.\",\"onSucceed\":\"Drop the object if it can.\"}}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Heat Metal
- data-description: Choose a manufactured metal object, such as a metal weapon or a suit of Heavy or Medium metal armor, that you can see within range. You cause the object to glow red-hot. Any creature in physical contact with the object takes 2d8 Fire damage when you cast the spell. Until the spell ends, you can take a Bonus Action on each of your later turns to deal this damage again if the object is within range.
If a creature is holding or wearing the object and takes the damage from it, the creature must succeed on a Constitution saving throw or drop the object if it can. If it doesn't drop the object, it has Disadvantage on attack rolls and ability checks until the start of your next turn.
- Level: 2
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 60 feet
- Components: V S M
- Material: a piece of iron and a flame
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 2.
- data-CastNum: 2
- data-RangeNum: 60
- Damage: 2d8
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

