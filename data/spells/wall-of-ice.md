# Wall of Ice

**description**: Level 6 Evocation (Wizard) Casting Time: Action Range: 120 feet Components: V, S, M (a piece of quartz) Duration: Concentration, up to 10 minutes You create a wall of ice on a solid surface within range. You can form it into a hemispherical dome or a globe with a radius of up to 10 feet, or you can shape a flat surface made up of ten 10-foot-square panels. Each panel must be contiguous with another panel. In any form, the wall is 1 foot thick and lasts for the duration. If the wall cuts through a creature’s space when it appears, the creature is pushed to one side of the wall (you choose which side) and makes a Dexterity saving throw, taking 10d6 Cold damage on a failed save or half as much damage on a successful one. The wall is an object that can be damaged and thus breached. It has AC 12 and 30 Hit Points per 10-foot section, and it has Immunity to Cold, Poison, and Psychic damage and Vulnerability to Fire damage. Reducing a 10-foot section of wall to 0 Hit Points destroys it and leaves behind a sheet of frigid air in the space the wall occupied. A creature moving through the sheet of frigid air for the first time on a turn makes a Constitution saving throw, taking 5d6 Cold damage on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The damage the wall deals when it appears increases by 2d6 and the damage from passing through the sheet of frigid air increases by 1d6 for each spell slot level above 6.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Cold Damage, Utility
- Spell Attack: None
- filter-Level: 6
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Wall of Ice","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Wall of Ice\",\"description\":\"You create a wall of ice on a solid surface within range. You can form it into a hemispherical dome or a globe with a radius of up to 10 feet, or you can shape a flat surface made up of ten 10-foot-square panels. Each panel must be contiguous with another panel. In any form, the wall is 1 foot thick and lasts for the duration.\\nIf the wall cuts through a creature's space when it appears, the creature is pushed to one side of the wall (you choose which side) and makes a Dexterity saving throw, taking 10d6 Cold damage on a failed save or half as much damage on a successful one.\\nThe wall is an object that can be damaged and thus breached. It has AC 12 and 30 Hit Points per 10-foot section, and it has Immunity to Cold, Poison, and Psychic damage and Vulnerability to Fire damage. Reducing a 10-foot section of wall to 0 Hit Points destroys it and leaves behind a sheet of frigid air in the space the wall occupied.\\nA creature moving through the sheet of frigid air for the first time on a turn makes a Constitution saving throw, taking 5d6 Cold damage on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage the wall deals when it appears increases by 2d6 and the damage from passing through the sheet of frigid air increases by 1d6 for each spell slot level above 6.\",\"level\":6,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a piece of quartz\"}}"},{"name":"Wall of Ice Creation Attack","parent":"Wall of Ice","payload":"{\"type\":\"Attack\",\"name\":\"Wall of Ice - On Creation\",\"description\":\"If the wall cuts through a creature's space when it appears, the creature is pushed to one side of the wall (you choose which side) and makes a Dexterity saving throw, taking 10d6 Cold damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 10d6 Cold damage.\",\"onSucceed\":\"Half as much damage.\"}}"},{"name":"Wall of Ice Creation Damage","parent":"Wall of Ice Creation Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceCount\":10,\"diceSize\":\"d6\"}"},{"name":"Wall of Ice Creation Damage Upcast","parent":"Wall of Ice Creation Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"},{"name":"Wall of Ice Condition","parent":"Wall of Ice","payload":"{\"type\":\"Condition\",\"name\":\"Wall of Ice\",\"description\":\"The wall is an object that can be damaged and thus breached. It has AC 12 and 30 Hit Points per 10-foot section, and it has Immunity to Cold, Poison, and Psychic damage and Vulnerability to Fire damage. Reducing a 10-foot section of wall to 0 Hit Points destroys it and leaves behind a sheet of frigid air in the space the wall occupied.\"}"},{"name":"Wall of Ice Frigid Air Attack","parent":"Wall of Ice","payload":"{\"type\":\"Attack\",\"name\":\"Wall of Ice - Frigid Air\",\"description\":\"Reducing a 10-foot section of wall to 0 Hit Points destroys it and leaves behind a sheet of frigid air in the space the wall occupied. A creature moving through the sheet of frigid air for the first time on a turn makes a Constitution saving throw, taking 5d6 Cold damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Takes 5d6 Cold damage.\",\"onSucceed\":\"Half as much damage.\"}}"},{"name":"Wall of Ice Frigid Air Damage","parent":"Wall of Ice Frigid Air Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceCount\":5,\"diceSize\":\"d6\"}"},{"name":"Wall of Ice Frigid Air Damage Upcast","parent":"Wall of Ice Frigid Air Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Wall of Ice
- data-description: You create a wall of ice on a solid surface within range. You can form it into a hemispherical dome or a globe with a radius of up to 10 feet, or you can shape a flat surface made up of ten 10-foot-square panels. Each panel must be contiguous with another panel. In any form, the wall is 1 foot thick and lasts for the duration.
If the wall cuts through a creature's space when it appears, the creature is pushed to one side of the wall (you choose which side) and makes a Dexterity saving throw, taking 10d6 Cold damage on a failed save or half as much damage on a successful one.
The wall is an object that can be damaged and thus breached. It has AC 12 and 30 Hit Points per 10-foot section, and it has Immunity to Cold, Poison, and Psychic damage and Vulnerability to Fire damage. Reducing a 10-foot section of wall to 0 Hit Points destroys it and leaves behind a sheet of frigid air in the space the wall occupied.
A creature moving through the sheet of frigid air for the first time on a turn makes a Constitution saving throw, taking 5d6 Cold damage on a failed save or half as much damage on a successful one.
- Level: 6
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 120 feet
- Components: V S M
- Material: a piece of quartz
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage the wall deals when it appears increases by 2d6 and the damage from passing through the sheet of frigid air increases by 1d6 for each spell slot level above 6.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Dexterity
- Damage: 10d6
- Damage Type: Cold

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

