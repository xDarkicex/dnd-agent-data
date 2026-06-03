# Phantasmal Killer

**description**: Level 4 Illusion (Bard, Wizard) Casting Time: Action Range: 120 feet Components: V, S Duration: Concentration, up to 1 minute You tap into the nightmares of a creature you can see within range and create an illusion of its deepest fears, visible only to that creature. The target makes a Wisdom saving throw. On a failed save, the target takes 4d10 Psychic damage and has Disadvantage on ability checks and attack rolls for the duration. On a successful save, the target takes half as much damage, and the spell ends. For the duration, the target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes the Psychic damage again. On a successful save, the spell ends. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Illusion
- Classes: Bard, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Wisdom Save, Psychic Damage
- Spell Attack: None
- filter-Level: 4
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Phantasmal Killer","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Phantasmal Killer\",\"description\":\"You tap into the nightmares of a creature you can see within range and create an illusion of its deepest fears, visible only to that creature. The target makes a Wisdom saving throw. On a failed save, the target takes 4d10 Psychic damage and has Disadvantage on ability checks and attack rolls for the duration. On a successful save, the target takes half as much damage, and the spell ends.\\nFor the duration, the target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes the Psychic damage again. On a successful save, the spell ends.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 4.\",\"level\":4,\"school\":\"Illusion\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Phantasmal Killer Condition","parent":"Phantasmal Killer","payload":"{\"type\":\"Condition\",\"name\":\"Phantasmal Killer\",\"description\":\"For the duration, the target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes the Psychic damage again. On a successful save, the spell ends.\"}"},{"name":"Phantasmal Killer Attack","parent":"Phantasmal Killer","payload":"{\"type\":\"Attack\",\"name\":\"Phantasmal Killer\",\"description\":\"The target makes a Wisdom saving throw.\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Takes 4d10 Psychic damage and has Disadvantage on ability checks and attack rolls for the duration.\",\"onSucceed\":\"Half as much damage, and the spell ends.\"}}"},{"name":"Phantasmal Killer Damage","parent":"Phantasmal Killer Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Psychic\",\"diceCount\":4,\"diceSize\":\"d10\"}"},{"name":"Phantasmal Killer Damage Upcast","parent":"Phantasmal Killer Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":5,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Phantasmal Killer
- data-description: You tap into the nightmares of a creature you can see within range and create an illusion of its deepest fears, visible only to that creature. The target makes a Wisdom saving throw. On a failed save, the target takes 4d10 Psychic damage and has Disadvantage on ability checks and attack rolls for the duration. On a successful save, the target takes half as much damage, and the spell ends.
For the duration, the target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes the Psychic damage again. On a successful save, the spell ends.
- Level: 4
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 4.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Wisdom
- Damage: 4d10
- Damage Type: Psychic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

