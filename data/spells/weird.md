# Weird

**description**: Level 9 Illusion (Warlock, Wizard) Casting Time: Action Range: 120 feet Components: V, S Duration: Concentration, up to 1 minute You try to create illusory terrors in others’ minds. Each creature of your choice in a 30-foot-radius Sphere centered on a point within range makes a Wisdom saving throw. On a failed save, a target takes 10d10 Psychic damage and has the Frightened condition for the duration. On a successful save, a target takes half as much damage only. A Frightened target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes 5d10 Psychic damage. On a successful save, the spell ends on that target.

**properties**:
- Category: Spells
- School: Illusion
- Classes: Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Wisdom Save, Psychic Damage, Frightened
- Spell Attack: None
- filter-Level: 9
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Weird","level":"9","payload":"{\"type\":\"Spell\",\"name\":\"Weird\",\"description\":\"You try to create illusory terrors in others' minds. Each creature of your choice in a 30-foot-radius Sphere centered on a point within range makes a Wisdom saving throw. On a failed save, a target takes 10d10 Psychic damage and has the Frightened condition for the duration. On a successful save, a target takes half as much damage only.\\nA Frightened target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes 5d10 Psychic damage. On a successful save, the spell ends on that target.\",\"level\":9,\"school\":\"Illusion\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"30 foot radius\"}}"},{"name":"Weird Initial Attack","parent":"Weird","payload":"{\"type\":\"Attack\",\"name\":\"Weird - Initial\",\"description\":\"Each creature of your choice in a 30-foot-radius Sphere centered on a point within range makes a Wisdom saving throw.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 10d10 Psychic damage and has the Frightened condition for the duration.\",\"onSucceed\":\"Half as much damage only.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"30 foot radius\"}}"},{"name":"Weird Initial Damage","parent":"Weird Initial Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Psychic\",\"diceCount\":10,\"diceSize\":\"d10\"}"},{"name":"Weird Frightened Attack","parent":"Weird","payload":"{\"type\":\"Attack\",\"name\":\"Weird - Frightened\",\"description\":\"A Frightened target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes 5d10 Psychic damage. On a successful save, the spell ends on that target.\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Takes 5d10 Psychic damage.\",\"onSucceed\":\"The spell ends on that target.\"},\"actionType\":\"Free Action\"}"},{"name":"Weird Frightened Damage","parent":"Weird Frightened Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Psychic\",\"diceCount\":5,\"diceSize\":\"d10\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Weird
- data-description: You try to create illusory terrors in others' minds. Each creature of your choice in a 30-foot-radius Sphere centered on a point within range makes a Wisdom saving throw. On a failed save, a target takes 10d10 Psychic damage and has the Frightened condition for the duration. On a successful save, a target takes half as much damage only.
A Frightened target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes 5d10 Psychic damage. On a successful save, the spell ends on that target.
- Level: 9
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 120 feet
- Components: V S
- data-CastNum: 2
- data-RangeNum: 120
- Save: Dexterity
- Damage: 10d10
- Damage Type: Psychic
- data-RangeAoe: 120 ft (30 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

