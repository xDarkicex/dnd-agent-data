# Meteor Swarm

**description**: Level 9 Evocation (Sorcerer, Wizard) Casting Time: Action Range: 1 mile Components: V, S Duration: Instantaneous Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius Sphere centered on each of those points makes a Dexterity saving throw. A creature takes 20d6 Fire damage and 20d6 Bludgeoning damage on a failed save or half as much damage on a successful one. A creature in the area of more than one fiery Sphere is affected only once. A nonmagical object that isn’t being worn or carried also takes the damage if it’s in the spell’s area, and the object starts burning if it’s flammable.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Fire Damage, Bludgeoning Damage
- Spell Attack: None
- filter-Level: 9
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Meteor Swarm","level":"9","payload":"{\"type\":\"Spell\",\"name\":\"Meteor Swarm\",\"description\":\"Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius Sphere centered on each of those points makes a Dexterity saving throw. A creature takes 20d6 Fire damage and 20d6 Bludgeoning damage on a failed save or half as much damage on a successful one. A creature in the area of more than one fiery Sphere is affected only once.\\nA nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area, and the object starts burning if it's flammable.\",\"level\":9,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"1 mile\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"40 foot radius\"}}"},{"name":"Meteor Swarm Attack","parent":"Meteor Swarm","payload":"{\"type\":\"Attack\",\"name\":\"Meteor Swarm\",\"description\":\"Each creature in a 40-foot-radius Sphere centered on each of those points makes a Dexterity saving throw.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 20d6 Fire damage and 20d6 Bludgeoning damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"40 foot radius\"}}"},{"name":"Meteor Swarm Fire Damage","parent":"Meteor Swarm Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":20,\"diceSize\":\"d6\"}"},{"name":"Meteor Swarm Bludgeoning Damage","parent":"Meteor Swarm Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Bludgeoning\",\"diceCount\":20,\"diceSize\":\"d6\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Meteor Swarm
- data-description: Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius Sphere centered on each of those points makes a Dexterity saving throw. A creature takes 20d6 Fire damage and 20d6 Bludgeoning damage on a failed save or half as much damage on a successful one. A creature in the area of more than one fiery Sphere is affected only once.
A nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area, and the object starts burning if it's flammable.
- Level: 9
- Casting Time: Action
- Duration: Instantaneous
- Range: 1 mile
- Components: V S
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 1
- Save: Dexterity
- Damage: 20d6
- Damage Type: Fire
- data-RangeAoe: 1 mile (40 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

