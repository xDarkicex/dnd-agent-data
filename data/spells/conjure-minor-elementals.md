# Conjure Minor Elementals

**description**: Level 4 Conjuration (Druid, Wizard) Casting Time: Action Range: Self Components: V, S Duration: Concentration, up to 10 minutes You conjure spirits from the Elemental Planes that flit around you in a 15-foot Emanation for the duration. Until the spell ends, any attack you make deals an extra 2d8 damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack). In addition, the ground in the Emanation is Difficult Terrain for your enemies. Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Inflict Damage, Acid Damage, Cold Damage, Fire Damage, Lightning Damage, Minions
- Spell Attack: None
- filter-Level: 4
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Conjure Minor Elementals","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Conjure Minor Elementals\",\"description\":\"You conjure spirits from the Elemental Planes that flit around you in a 15-foot Emanation for the duration. Until the spell ends, any attack you make deals an extra 2d8 damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack).\\nIn addition, the ground in the Emanation is Difficult Terrain for your enemies.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 4.\",\"level\":4,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"15 foot\"}}"},{"name":"Conjure Minor Elementals Condition","parent":"Conjure Minor Elementals","payload":"{\"type\":\"Condition\",\"name\":\"Conjure Minor Elementals\"}"},{"name":"Conjure Minor Elementals Attack","parent":"Conjure Minor Elementals","payload":"{\"type\":\"Attack\",\"name\":\"Conjure Minor Elementals Extra Damage\",\"autoHit\":true,\"description\":\"Until the spell ends, any attack you make deals an extra 2d8 damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack).\",\"actionType\":\"Free Action\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Conjure Minor Elementals Damage","parent":"Conjure Minor Elementals Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Acid, Cold, Fire, or Lightning\",\"diceCount\":2,\"diceSize\":\"d8\"}"},{"name":"Conjure Minor Elementals Damage Upcast","parent":"Conjure Minor Elementals Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":5,\"level\":1,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Conjure Minor Elementals
- data-description: You conjure spirits from the Elemental Planes that flit around you in a 15-foot Emanation for the duration. Until the spell ends, any attack you make deals an extra 2d8 damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack).
In addition, the ground in the Emanation is Difficult Terrain for your enemies.
- Level: 4
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: Self
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 4.
- data-CastNum: 2
- data-AttackType: Spell Attack
- Damage: 2d8
- Damage Type: Acid, Cold, Fire, or Lightning
- data-RangeAoe: Self (15 ft ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

