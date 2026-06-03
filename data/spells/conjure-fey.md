# Conjure Fey

**description**: Level 6 Conjuration (Druid) Casting Time: Action Range: 60 feet Components: V, S Duration: Concentration, up to 10 minutes You conjure a Medium spirit from the Feywild in an unoccupied space you can see within range. The spirit lasts for the duration, and it looks like a Fey creature of your choice. When the spirit appears, you can make one melee spell attack against a creature within 5 feet of it. On a hit, the target takes Psychic damage equal to 3d12 plus your spellcasting ability modifier, and the target has the Frightened condition until the start of your next turn, with both you and the spirit as the source of the fear. As a Bonus Action on your later turns, you can teleport the spirit to an unoccupied space you can see within 30 feet of the space it left and make the attack against a creature within 5 feet of it. Using a Higher-Level Spell Slot. The damage increases by 2d12 for each spell slot level above 6.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Psychic Damage, Attack vs AC, Minions
- Spell Attack: None
- filter-Level: 6
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Conjure Fey","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Conjure Fey\",\"description\":\"You conjure a Medium spirit from the Feywild in an unoccupied space you can see within range. The spirit lasts for the duration, and it looks like a Fey creature of your choice. When the spirit appears, you can make one melee spell attack against a creature within 5 feet of it. On a hit, the target takes Psychic damage equal to 3d12 plus your spellcasting ability modifier, and the target has the Frightened condition until the start of your next turn, with both you and the spirit as the source of the fear.\\nAs a Bonus Action on your later turns, you can teleport the spirit to an unoccupied space you can see within 30 feet of the space it left and make the attack against a creature within 5 feet of it.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 2d12 for each spell slot level above 6.\",\"level\":6,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Conjure Fey Attack","parent":"Conjure Fey","payload":"{\"type\":\"Attack\",\"name\":\"Conjure Fey Attack\",\"description\":\"You can make one melee spell attack against a creature within 5 feet of it.\",\"attack\":{\"type\":\"Spell Attack\",\"proficiencyLevel\":\"Proficient\"}}"},{"name":"Conjure Fey Damage","parent":"Conjure Fey Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Psychic\",\"diceCount\":3,\"diceSize\":\"d12\"}"},{"name":"Conjure Fey Damage Upcast","parent":"Conjure Fey Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"},{"name":"Conjure Fey Condition","parent":"Conjure Fey","payload":"{\"type\":\"Condition\",\"name\":\"Conjure Fey\"}"},{"name":"Conjure Fey Bonus Action","parent":"Conjure Fey Condition","payload":"{\"type\":\"Action\",\"name\":\"Teleport Conjured Fey\",\"description\":\"You can teleport the spirit to an unoccupied space you can see within 30 feet of the space it left and make the attack against a creature within 5 feet of it.\",\"actionType\":\"Bonus Action\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Conjure Fey
- data-description: You conjure a Medium spirit from the Feywild in an unoccupied space you can see within range. The spirit lasts for the duration, and it looks like a Fey creature of your choice. When the spirit appears, you can make one melee spell attack against a creature within 5 feet of it. On a hit, the target takes Psychic damage equal to 3d12 plus your spellcasting ability modifier, and the target has the Frightened condition until the start of your next turn, with both you and the spirit as the source of the fear.
As a Bonus Action on your later turns, you can teleport the spirit to an unoccupied space you can see within 30 feet of the space it left and make the attack against a creature within 5 feet of it.
- Level: 6
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 2d12 for each spell slot level above 6.
- data-CastNum: 2
- data-RangeNum: 60
- data-AttackType: Spell Attack
- Damage: 3d12
- Damage Type: Psychic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

