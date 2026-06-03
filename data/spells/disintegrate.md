# Disintegrate

**description**: Level 6 Transmutation (Sorcerer, Wizard) Casting Time: Action Range: 60 feet Components: V, S, M (a lodestone and dust) Duration: Instantaneous You launch a green ray at a target you can see within range. The target can be a creature, a nonmagical object, or a creation of magical force, such as the wall created by Wall of Force. A creature targeted by this spell makes a Dexterity saving throw. On a failed save, the target takes 10d6 + 40 Force damage. If this damage reduces it to 0 Hit Points, it and everything nonmagical it is wearing and carrying are disintegrated into gray dust. The target can be revived only by a True Resurrection or a W ish spell. This spell automatically disintegrates a Large or smaller nonmagical object or a creation of magical force. If such a target is Huge or larger, this spell disintegrates a 10-foot-Cube portion of it. Using a Higher-Level Spell Slot. The damage increases by 3d6 for each spell slot level above 6.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Force Damage, Dexterity Save
- Spell Attack: None
- filter-Level: 6
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Disintegrate","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Disintegrate\",\"description\":\"You launch a green ray at a target you can see within range. The target can be a creature, a nonmagical object, or a creation of magical force, such as the wall created by Wall of Force.\\nA creature targeted by this spell makes a Dexterity saving throw. On a failed save, the target takes 10d6 + 40 Force damage. If this damage reduces it to 0 Hit Points, it and everything nonmagical it is wearing and carrying are disintegrated into gray dust. The target can be revived only by a True Resurrection or a Wish spell.\\nThis spell automatically disintegrates a Large or smaller nonmagical object or a creation of magical force. If such a target is Huge or larger, this spell disintegrates a 10-foot-Cube portion of it.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 3d6 for each spell slot level above 6.\",\"level\":6,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a lodestone and dust\"}}"},{"name":"Disintegrate Attack","parent":"Disintegrate","payload":"{\"type\":\"Attack\",\"name\":\"Disintegrate\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Target takes 10d6 + 40 Force damage.\"},\"actionType\":\"Action\"}"},{"name":"Disintegrate Damage","parent":"Disintegrate Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"_bonus\":40,\"damageType\":\"Force\",\"diceCount\":10,\"diceSize\":\"d6\"}"},{"name":"Disintegrate Damage Upcast","parent":"Disintegrate Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":3,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Disintegrate
- data-description: You launch a green ray at a target you can see within range. The target can be a creature, a nonmagical object, or a creation of magical force, such as the wall created by Wall of Force.
A creature targeted by this spell makes a Dexterity saving throw. On a failed save, the target takes 10d6 + 40 Force damage. If this damage reduces it to 0 Hit Points, it and everything nonmagical it is wearing and carrying are disintegrated into gray dust. The target can be revived only by a True Resurrection or a Wish spell.
This spell automatically disintegrates a Large or smaller nonmagical object or a creation of magical force. If such a target is Huge or larger, this spell disintegrates a 10-foot-Cube portion of it.
- Level: 6
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V S M
- Material: a lodestone and dust
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 3d6 for each spell slot level above 6.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Dexterity
- Damage: 10d6
- Damage Type: Force

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

