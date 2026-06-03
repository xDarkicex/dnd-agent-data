# Blight

**description**: Level 4 Necromancy (Druid, Sorcerer, Warlock, Wizard) Casting Time: Action Range: 30 feet Components: V, S Duration: Instantaneous A creature that you can see within range makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one. A Plant creature automatically fails the save. Alternatively, target a nonmagical plant that isn’t a creature, such as a tree or shrub. It doesn’t make a save; it simply withers and dies. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Necromancy
- Classes: Druid, Sorcerer, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Necrotic Damage
- Spell Attack: None
- filter-Level: 4
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Blight","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Blight\",\"description\":\"A creature that you can see within range makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one. A Plant creature automatically fails the save.\\nAlternatively, target a nonmagical plant that isn't a creature, such as a tree or shrub. It doesn't make a save; it simply withers and dies.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.\",\"level\":4,\"school\":\"Necromancy\",\"castingTime\":\"Action\",\"range\":\"30 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Blight Attack","parent":"Blight","payload":"{\"type\":\"Attack\",\"name\":\"Blight\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 8d8 Necrotic damage. A Plant creature automatically fails the save.\",\"onSucceed\":\"Half as much damage. \"}}"},{"name":"Blight Damage","parent":"Blight Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Necrotic\",\"diceCount\":8,\"diceSize\":\"d8\"}"},{"name":"Blight Damage Upcast","parent":"Blight Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":5,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Blight
- data-description: A creature that you can see within range makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one. A Plant creature automatically fails the save.
Alternatively, target a nonmagical plant that isn't a creature, such as a tree or shrub. It doesn't make a save; it simply withers and dies.
- Level: 4
- Casting Time: Action
- Duration: Instantaneous
- Range: 30 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 30
- Save: Constitution
- Damage: 8d8
- Damage Type: Necrotic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

