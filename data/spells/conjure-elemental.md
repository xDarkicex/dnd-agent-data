# Conjure Elemental

**description**: Level 5 Conjuration (Druid, Wizard) Casting Time: Action Range: 60 feet Components: V, S Duration: Concentration, up to 10 minutes You conjure a Large, intangible spirit from the Elemental Planes that appears in an unoccupied space within range. Choose the spirit’s element, which determines its damage type: air (Lightning), earth (Thunder), fire (Fire), or water (Cold). The spirit lasts for the duration. Whenever a creature you can see enters the spirit’s space or starts its turn within 5 feet of the spirit, you can force that creature to make a Dexterity saving throw if the spirit has no creature Restrained. On failed save, the target takes 8d8 damage of the spirit’s type, and the target has the Restrained condition until the spell ends. At the start of each of its turns, the Restrained target repeats the save. On a failed save, the target takes 4d8 damage of the spirit’s type. On a successful save, the target isn’t Restrained by the spirit. Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 5.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Thunder Damage, Fire Damage, Lightning Damage, Cold Damage, Dexterity Save, Minions
- Spell Attack: None
- filter-Level: 5
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Conjure Elemental","level":"5","payload":"{\"type\":\"Spell\",\"name\":\"Conjure Elemental\",\"description\":\"You conjure a Large, intangible spirit from the Elemental Planes that appears in an unoccupied space within range. Choose the spirit's element, which determines its damage type: air (Lightning), earth (Thunder), fire (Fire), or water (Cold). The spirit lasts for the duration.\\nWhenever a creature you can see enters the spirit's space or starts its turn within 5 feet of the spirit, you can force that creature to make a Dexterity saving throw if the spirit has no creature Restrained. On failed save, the target takes 8d8 damage of the spirit's type, and the target has the Restrained condition until the spell ends. At the start of each of its turns, the Restrained target repeats the save. On a failed save, the target takes 4d8 damage of the spirit's type. On a successful save, the target isn't Restrained by the spirit.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 5.\",\"level\":5,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Conjure Elemental Initial Attack","parent":"Conjure Elemental","payload":"{\"type\":\"Attack\",\"name\":\"Elemental Inital Attack\",\"description\":\"Whenever a creature you can see enters the spirit's space or starts its turn within 5 feet of the spirit, you can force that creature to make a Dexterity saving throw if the spirit has no creature Restrained.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Target takes 8d8 damage of the spirit's type, and has the Restrained condition until the spell ends or a successful save.\",\"onSucceed\":\"Target isn't Restrained by the spirit.\"}}"},{"name":"Conjure Elemental Initial Damage","parent":"Conjure Elemental Initial Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"\",\"diceCount\":8,\"diceSize\":\"d8\"}"},{"name":"Conjure Elemental Initial Damage Upcast","parent":"Conjure Elemental Initial Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"},{"name":"Conjure Elemental Restrained Attack","parent":"Conjure Elemental","payload":"{\"type\":\"Attack\",\"name\":\"Elemental Restrained Attack\",\"description\":\"At the start of each of its turns, the Restrained target repeats the save. On a failed save, the target takes 4d8 damage of the spirit's type. On a successful save, the target isn't Restrained by the spirit.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Target takes 4d8 damage of the spirit's type, and has the Restrained condition until the spell ends or a successful save.\",\"onSucceed\":\"Target isn't Restrained by the spirit.\"}}"},{"name":"Conjure Elemental Restrained Damage","parent":"Conjure Elemental Restrained Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"\",\"diceCount\":4,\"diceSize\":\"d8\"}"},{"name":"Conjure Elemental Restrained Damage Upcast","parent":"Conjure Elemental Restrained Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Conjure Elemental
- data-description: You conjure a Large, intangible spirit from the Elemental Planes that appears in an unoccupied space within range. Choose the spirit's element, which determines its damage type: air (Lightning), earth (Thunder), fire (Fire), or water (Cold). The spirit lasts for the duration.
Whenever a creature you can see enters the spirit's space or starts its turn within 5 feet of the spirit, you can force that creature to make a Dexterity saving throw if the spirit has no creature Restrained. On failed save, the target takes 8d8 damage of the spirit's type, and the target has the Restrained condition until the spell ends. At the start of each of its turns, the Restrained target repeats the save. On a failed save, the target takes 4d8 damage of the spirit's type. On a successful save, the target isn't Restrained by the spirit.
- Level: 5
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 5.
- data-CastNum: 2
- data-RangeNum: 60
- Save: Dexterity
- Damage: 8d8

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

