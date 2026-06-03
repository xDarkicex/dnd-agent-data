# Storm of Vengeance

**description**: Level 9 Conjuration (Druid) Casting Time: Action Range: 1 mile Components: V, S Duration: Concentration, up to 1 minute A churning storm cloud forms for the duration, centered on a point within range and spreading to a radius of 300 feet. Each creature under the cloud when it appears must succeed on a Constitution saving throw or take 2d6 Thunder damage and have the Deafened condition for the duration. At the start of each of your later turns, the storm produces different effects, as detailed below. Turn 2. Acidic rain falls. Each creature and object under the cloud takes 4d6 Acid damage. Turn 3. You call six bolts of lightning from the cloud to strike six different creatures or objects beneath it. Each target makes a Dexterity saving throw, taking 10d6 Lightning damage on a failed save or half as much damage on a successful one. Turn 4. Hailstones rain down. Each creature under the cloud takes 2d6 Bludgeoning damage. Turns 5–10. Gusts and freezing rain assail the area under the cloud. Each creature there takes 1d6 Cold damage. Until the spell ends, the area is Difficult Terrain and Heavily Obscured, ranged attacks with weapons are impossible there, and strong wind blows through the area.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Thunder Damage, Deafened, Acid Damage, Lightning Damage, Dexterity Save, Bludgeoning Damage, Cold Damage
- Spell Attack: None
- filter-Level: 9
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Storm of Vengeance","level":"9","payload":"{\"type\":\"Spell\",\"name\":\"Storm of Vengeance\",\"description\":\"A churning storm cloud forms for the duration, centered on a point within range and spreading to a radius of 300 feet. Each creature under the cloud when it appears must succeed on a Constitution saving throw or take 2d6 Thunder damage and have the Deafened condition for the duration.\\nAt the start of each of your later turns, the storm produces different effects, as detailed below.\\nTurn 2. Acidic rain falls. Each creature and object under the cloud takes 4d6 Acid damage.\\nTurn 3. You call six bolts of lightning from the cloud to strike six different creatures or objects beneath it. Each target makes a Dexterity saving throw, taking 10d6 Lightning damage on a failed save or half as much damage on a successful one.\\nTurn 4. Hailstones rain down. Each creature under the cloud takes 2d6 Bludgeoning damage.\\nTurns 5 - 10. Gusts and freezing rain assail the area under the cloud. Each creature there takes 1d6 Cold damage. Until the spell ends, the area is Difficult Terrain and Heavily Obscured, ranged attacks with weapons are impossible there, and strong wind blows through the area.\",\"level\":9,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"1 mile\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"300 foot\"}}"},{"name":"Storm of Vengeance Condition","parent":"Storm of Vengeance","payload":"{\"type\":\"Condition\",\"name\":\"Storm of Vengeance\"}"},{"name":"Storm of Vengeance Initial Attack","parent":"Storm of Vengeance","payload":"{\"type\":\"Attack\",\"name\":\"Storm of Vengeance - Initial Attack\",\"description\":\"Each creature under the cloud when it appears must succeed on a Constitution saving throw or take 2d6 Thunder damage and have the Deafened condition for the duration.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Have the Deafened condition for the duration.\"},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"300 foot\"}}"},{"name":"Storm of Vengeance Initial Damage","parent":"Storm of Vengeance Initial Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Thunder\",\"diceCount\":2,\"diceSize\":\"d6\"}"},{"name":"Storm of Vengeance Acid Rain Attack","parent":"Storm of Vengeance","payload":"{\"type\":\"Attack\",\"name\":\"Storm of Vengeance - Acid Rain\",\"description\":\"Acidic rain falls. Each creature and object under the cloud takes 4d6 Acid damage.\",\"actionType\":\"Free Action\",\"aoe\":{\"shape\":\"Emanation\",\"size\":\"300 foot\"}}"},{"name":"Storm of Vengeance Acid Rain Damage","parent":"Storm of Vengeance Acid Rain Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Acid\",\"diceCount\":4,\"diceSize\":\"d6\"}"},{"name":"Storm of Vengeance Lightning Attack","parent":"Storm of Vengeance","payload":"{\"type\":\"Attack\",\"name\":\"Storm of Vengeance - Lightning\",\"description\":\"You call six bolts of lightning from the cloud to strike six different creatures or objects beneath it. Each target makes a Dexterity saving throw, taking 10d6 Lightning damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 10d6 Lightning damage.\",\"onSucceed\":\"Half as much damage.\"},\"actionType\":\"Free Action\"}"},{"name":"Storm of Vengeance Lightning Damage","parent":"Storm of Vengeance Lightning Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Lightning\",\"diceCount\":10,\"diceSize\":\"d6\"}"},{"name":"Storm of Vengeance Hailstones Attack","parent":"Storm of Vengeance","payload":"{\"type\":\"Attack\",\"name\":\"Storm of Vengeance - Hailstones\",\"description\":\"Hailstones rain down. Each creature under the cloud takes 2d6 Bludgeoning damage.\",\"actionType\":\"Free Action\",\"aoe\":{\"shape\":\"Emanation\",\"size\":\"300 foot\"}}"},{"name":"Storm of Vengeance Hailstones Damage","parent":"Storm of Vengeance Hailstones Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Bludgeoning\",\"diceCount\":2,\"diceSize\":\"d6\"}"},{"name":"Storm of Vengeance Freezing Rain Attack","parent":"Storm of Vengeance","payload":"{\"type\":\"Attack\",\"name\":\"Storm of Vengeance - Freezing Rain\",\"description\":\"Gusts and freezing rain assail the area under the cloud. Each creature there takes 1d6 Cold damage. Until the spell ends, the area is Difficult Terrain and Heavily Obscured, ranged attacks with weapons are impossible there, and strong wind blows through the area.\",\"actionType\":\"Free Action\",\"aoe\":{\"shape\":\"Emanation\",\"size\":\"300 foot\"}}"},{"name":"Storm of Vengeance Freezing Rain Damage","parent":"Storm of Vengeance Freezing Rain Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceSize\":\"d6\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Storm of Vengeance
- data-description: A churning storm cloud forms for the duration, centered on a point within range and spreading to a radius of 300 feet. Each creature under the cloud when it appears must succeed on a Constitution saving throw or take 2d6 Thunder damage and have the Deafened condition for the duration.
At the start of each of your later turns, the storm produces different effects, as detailed below.
Turn 2. Acidic rain falls. Each creature and object under the cloud takes 4d6 Acid damage.
Turn 3. You call six bolts of lightning from the cloud to strike six different creatures or objects beneath it. Each target makes a Dexterity saving throw, taking 10d6 Lightning damage on a failed save or half as much damage on a successful one.
Turn 4. Hailstones rain down. Each creature under the cloud takes 2d6 Bludgeoning damage.
Turns 5 - 10. Gusts and freezing rain assail the area under the cloud. Each creature there takes 1d6 Cold damage. Until the spell ends, the area is Difficult Terrain and Heavily Obscured, ranged attacks with weapons are impossible there, and strong wind blows through the area.
- Level: 9
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 1 mile
- Components: V S
- data-CastNum: 2
- data-RangeNum: 1
- Save: Constitution
- Damage: 2d6
- Damage Type: Thunder
- data-RangeAoe: 1 mile (300 ft ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

