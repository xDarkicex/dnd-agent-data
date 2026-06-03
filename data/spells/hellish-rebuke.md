# Hellish Rebuke

**description**: Level 1 Evocation (Warlock) Casting Time: Reaction, which you take in response to taking damage from a creature that you can see within 60 feet of yourself Range: 60 feet Components: V, S Duration: Instantaneous The creature that damaged you is momentarily surrounded by green flames. It makes a Dexterity saving throw, taking 2d10 Fire damage on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Warlock
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Fire Damage
- Spell Attack: None
- filter-Level: 1
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Hellish Rebuke","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Hellish Rebuke\",\"description\":\"Reaction, which you take in response to taking damage from a creature that you can see within 60 feet of yourself. The creature that damaged you is momentarily surrounded by green flames. It makes a Dexterity saving throw, taking 2d10 Fire damage on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Reaction\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Hellish Rebuke Attack","parent":"Hellish Rebuke","payload":"{\"type\":\"Attack\",\"name\":\"Hellish Rebuke\",\"range\":\"60 feet\",\"description\":\"The creature that damaged you is momentarily surrounded by green flames. It makes a Dexterity saving throw.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onSucceed\":\"Half damage.\"},\"actionType\":\"Reaction\"}"},{"name":"Hellish Rebuke Damage","parent":"Hellish Rebuke Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":2,\"diceSize\":\"d10\"}"},{"name":"Hellish Rebuke Damage Upcast","parent":"Hellish Rebuke Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Reaction
- filter-Concentration: No
- Name: Hellish Rebuke
- data-description: Reaction, which you take in response to taking damage from a creature that you can see within 60 feet of yourself. The creature that damaged you is momentarily surrounded by green flames. It makes a Dexterity saving throw, taking 2d10 Fire damage on a failed save or half as much damage on a successful one.
- Level: 1
- Casting Time: Reaction
- Duration: Instantaneous
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 1.
- data-CastNum: 1
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Dexterity
- Damage: 2d10
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

