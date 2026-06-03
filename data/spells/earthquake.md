# Earthquake

**description**: Level 8 Transmutation (Cleric, Druid, Sorcerer) Casting Time: Action Range: 500 feet Components: V, S, M (a fractured rock) Duration: Concentration, up to 1 minute Choose a point on the ground that you can see within range. For the duration, an intense tremor rips through the ground in a 100-foot-radius circle centered on that point. The ground there is Difficult Terrain. When you cast this spell and at the end of each of your turns for the duration, each creature on the ground in the area makes a Dexterity saving throw. On a failed save, a creature has the Prone condition, and its Concentration is broken. You can also cause the effects below. Fissures. A total of 1d6 fissures open in the spell’s area at the end of the turn you cast it. You choose the fissures’ locations, which can’t be under structures. Each fissure is 1d10 × 10 feet deep and 10 feet wide, and it extends from one edge of the spell’s area to another edge. A creature in the same space as a fissure must succeed on a Dexterity saving throw or fall in. A creature that successfully saves moves with the fissure’s edge as it opens. Structures. The tremor deals 50 Bludgeoning damage to any structure in contact with the ground in the area when you cast the spell and at the end of each of your turns until the spell ends. If a structure drops to 0 Hit Points, it collapses. A creature within a distance from a collapsing structure equal to half the structure’s height makes a Dexterity saving throw. On a failed save, the creature takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. On a successful save, the creature takes half as much damage only.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Cleric, Druid, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Dexterity Save, Inflict Condition, Prone, Inflict Damage, Bludgeoning Damage
- Spell Attack: None
- filter-Level: 8
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Earthquake","level":"8","payload":"{\"type\":\"Spell\",\"name\":\"Earthquake\",\"description\":\"Choose a point on the ground that you can see within range. For the duration, an intense tremor rips through the ground in a 100-foot-radius circle centered on that point. The ground there is Difficult Terrain.\\nWhen you cast this spell and at the end of each of your turns for the duration, each creature on the ground in the area makes a Dexterity saving throw. On a failed save, a creature has the Prone condition, and its Concentration is broken.\\nYou can also cause the effects below.\\nFissures. A total of 1d6 fissures open in the spell's area at the end of the turn you cast it. You choose the fissures' locations, which can't be under structures. Each fissure is 1d10 × 10 feet deep and 10 feet wide, and it extends from one edge of the spell's area to another edge. A creature in the same space as a fissure must succeed on a Dexterity saving throw or fall in. A creature that successfully saves moves with the fissure's edge as it opens.\\nStructures. The tremor deals 50 Bludgeoning damage to any structure in contact with the ground in the area when you cast the spell and at the end of each of your turns until the spell ends. If a structure drops to 0 Hit Points, it collapses.\\nA creature within a distance from a collapsing structure equal to half the structure's height makes a Dexterity saving throw. On a failed save, the creature takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. On a successful save, the creature takes half as much damage only.\",\"level\":8,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"500 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a fractured rock\"},\"aoe\":{\"shape\":\"Circle\",\"size\":\"100 foot radius\"}}"},{"name":"Earthquake Condition","parent":"Earthquake","payload":"{\"type\":\"Condition\",\"name\":\"Earthquake\"}"},{"name":"Earthquake Attack","parent":"Earthquake","payload":"{\"type\":\"Attack\",\"name\":\"Earthquake\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Creature has the Prone condition, and its Concentration is broken.\"},\"aoe\":{\"shape\":\"Circle\",\"size\":\"100 foot radius\"}}"},{"name":"Earthquake Attack Fissures","parent":"Earthquake","payload":"{\"type\":\"Attack\",\"name\":\"Earthquake - Fissures\",\"description\":\"A total of 1d6 fissures open in the spell's area at the end of the turn you cast it. You choose the fissures' locations, which can't be under structures. Each fissure is 1d10 × 10 feet deep and 10 feet wide, and it extends from one edge of the spell's area to another edge. A creature in the same space as a fissure must succeed on a Dexterity saving throw or fall in. A creature that successfully saves moves with the fissure's edge as it opens.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Fall in fissure.\",\"onSucceed\":\"Moves with fissure's edge as it opens.\"},\"aoe\":{\"shape\":\"Circle\",\"size\":\"100 foot radius\"}}"},{"name":"Earthquake Attack Structures","parent":"Earthquake","payload":"{\"type\":\"Attack\",\"name\":\"Earthquake - Structures\",\"description\":\"The tremor deals 50 Bludgeoning damage to any structure in contact with the ground in the area when you cast the spell and at the end of each of your turns until the spell ends. If a structure drops to 0 Hit Points, it collapses.\",\"aoe\":{\"shape\":\"Circle\",\"size\":\"100 foot radius\"}}"},{"name":"Earthquake Attack Collapseing Structures","parent":"Earthquake","payload":"{\"type\":\"Attack\",\"name\":\"Earthquake - Collapseing Structures\",\"description\":\"A creature within a distance from a collapsing structure equal to half the structure's height makes a Dexterity saving throw. On a failed save, the creature takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. On a successful save, the creature takes half as much damage only.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape.\",\"onSucceed\":\"Half as much damage only.\"}}"},{"name":"Earthquake Attack Collapseing Structures Damage","parent":"Earthquake Attack Collapseing Structures","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Bludgeoning\",\"diceCount\":12,\"diceSize\":\"d6\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Earthquake
- data-description: Choose a point on the ground that you can see within range. For the duration, an intense tremor rips through the ground in a 100-foot-radius circle centered on that point. The ground there is Difficult Terrain.
When you cast this spell and at the end of each of your turns for the duration, each creature on the ground in the area makes a Dexterity saving throw. On a failed save, a creature has the Prone condition, and its Concentration is broken.
You can also cause the effects below.
Fissures. A total of 1d6 fissures open in the spell's area at the end of the turn you cast it. You choose the fissures' locations, which can't be under structures. Each fissure is 1d10 × 10 feet deep and 10 feet wide, and it extends from one edge of the spell's area to another edge. A creature in the same space as a fissure must succeed on a Dexterity saving throw or fall in. A creature that successfully saves moves with the fissure's edge as it opens.
Structures. The tremor deals 50 Bludgeoning damage to any structure in contact with the ground in the area when you cast the spell and at the end of each of your turns until the spell ends. If a structure drops to 0 Hit Points, it collapses.
A creature within a distance from a collapsing structure equal to half the structure's height makes a Dexterity saving throw. On a failed save, the creature takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. On a successful save, the creature takes half as much damage only.
- Level: 8
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 500 feet
- Components: V S M
- Material: a fractured rock
- data-CastNum: 2
- data-RangeNum: 500
- Save: Dexterity
- Damage: 12d6
- Damage Type: Bludgeoning
- data-RangeAoe: 500 ft (100 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

