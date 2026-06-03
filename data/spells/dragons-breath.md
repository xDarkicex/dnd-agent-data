# Dragon's Breath

**description**: Level 2 Transmutation (Sorcerer, Wizard) Casting Time: Bonus Action Range: Touch Components: V, S, M (a hot pepper) Duration: Concentration, up to 1 minute You touch one willing creature, and choose Acid, Cold, Fire, Lightning, or Poison. Until the spell ends, the target can take a Magic action to exhale a 15-foot Cone. Each creature in that area makes a Dexterity saving throw, taking 3d6 damage of the chosen type on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Acid Damage, Inflict Damage, Dexterity Save, Cold Damage, Fire Damage, Poison Damage, Lightning Damage, Buff
- Spell Attack: None
- filter-Level: 2
- filter-Range: Touch
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Dragon's Breath","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Dragon's Breath\",\"description\":\"You touch one willing creature, and choose Acid, Cold, Fire, Lightning, or Poison. Until the spell ends, the target can take a Magic action to exhale a 15-foot Cone. Each creature in that area makes a Dexterity saving throw, taking 3d6 damage of the chosen type on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.\",\"level\":2,\"school\":\"Transmutation\",\"castingTime\":\"Bonus Action\",\"range\":\"Touch\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a hot pepper\"},\"aoe\":{\"shape\":\"Cone\",\"size\":\"15 foot\"}}"},{"name":"Dragon's Breath Condition","parent":"Dragon's Breath","payload":"{\"type\":\"Condition\",\"name\":\"Dragon's Breath\"}"},{"name":"Dragon's Breath Attack","parent":"Dragon's Breath","payload":"{\"type\":\"Attack\",\"name\":\"Dragon's Breath\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 3d6 damage of the chosen type.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Cone\",\"size\":\"15 foot\"},\"actionType\":\"Action\"}"},{"name":"Dragon's Breath Damage","parent":"Dragon's Breath Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Acid, Cold, Fire, Lightning, or Poison\",\"diceCount\":3,\"diceSize\":\"d6\"}"},{"name":"Dragon's Breath Damage Upcast","parent":"Dragon's Breath Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Bonus Action
- filter-Concentration: Yes
- Name: Dragon's Breath
- data-description: You touch one willing creature, and choose Acid, Cold, Fire, Lightning, or Poison. Until the spell ends, the target can take a Magic action to exhale a 15-foot Cone. Each creature in that area makes a Dexterity saving throw, taking 3d6 damage of the chosen type on a failed save or half as much damage on a successful one.
- Level: 2
- Casting Time: Bonus Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: Touch
- Components: V S M
- Material: a hot pepper
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.
- Save: Dexterity
- Damage: 3d6
- Damage Type: Acid, Cold, Fire, Lightning, or Poison
- data-RangeAoe: Touch (15 ft ▽)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

