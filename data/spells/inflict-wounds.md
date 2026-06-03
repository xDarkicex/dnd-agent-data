# Inflict Wounds

**description**: Level 1 Necromancy (Cleric) Casting Time: Action Range: Touch Components: V, S Duration: Instantaneous A creature you touch makes a Constitution saving throw, taking 2d10 Necrotic damage on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Necromancy
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Necrotic Damage
- Spell Attack: None
- filter-Level: 1
- filter-Range: Touch
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Inflict Wounds","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Inflict Wounds\",\"description\":\"A creature you touch makes a Constitution saving throw, taking 2d10 Necrotic damage on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 1.\",\"level\":1,\"school\":\"Necromancy\",\"castingTime\":\"Action\",\"range\":\"Touch\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Inflict Wounds Attack","parent":"Inflict Wounds","payload":"{\"type\":\"Attack\",\"name\":\"Inflict Wounds\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 2d10 Necrotic damage.\",\"onSucceed\":\"Half as much damage.\"}}"},{"name":"Inflict Wounds Damage","parent":"Inflict Wounds Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Necrotic\",\"diceCount\":2,\"diceSize\":\"d10\"}"},{"name":"Inflict Wounds Damage Upcast","parent":"Inflict Wounds Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Inflict Wounds
- data-description: A creature you touch makes a Constitution saving throw, taking 2d10 Necrotic damage on a failed save or half as much damage on a successful one.
- Level: 1
- Casting Time: Action
- Duration: Instantaneous
- Range: Touch
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 0
- Save: Constitution
- Damage: 2d10
- Damage Type: Necrotic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

