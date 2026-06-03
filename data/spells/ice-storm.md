# Ice Storm

**description**: Level 4 Evocation (Druid, Sorcerer, Wizard) Casting Time: Action Range: 300 feet Components: V, S, M (a mitten) Duration: Instantaneous Hail falls in a 20-foot-radius, 40-foot-high Cylinder centered on a point within range. Each creature in the Cylinder makes a Dexterity saving throw. A creature takes 2d10 Bludgeoning damage and 4d6 Cold damage on a failed save or half as much damage on a successful one. Hailstones turn ground in the Cylinder into Difficult Terrain until the end of your next turn. Using a Higher-Level Spell Slot. The Bludgeoning damage increases by 1d10 for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Bludgeoning Damage, Cold Damage
- Spell Attack: None
- filter-Level: 4
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Ice Storm","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Ice Storm\",\"description\":\"Hail falls in a 20-foot-radius, 40-foot-high Cylinder centered on a point within range. Each creature in the Cylinder makes a Dexterity saving throw. A creature takes 2d10 Bludgeoning damage and 4d6 Cold damage on a failed save or half as much damage on a successful one.\\nHailstones turn ground in the Cylinder into Difficult Terrain until the end of your next turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The Bludgeoning damage increases by 1d10 for each spell slot level above 4.\",\"level\":4,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"300 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a mitten\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"20 foot radius, 40 foot high\"}}"},{"name":"Ice Storm Attack","parent":"Ice Storm","payload":"{\"type\":\"Attack\",\"name\":\"Ice Storm\",\"description\":\"Hail falls in a 20-foot-radius, 40-foot-high Cylinder centered on a point within range. Each creature in the Cylinder makes a Dexterity saving throw.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 2d10 Bludgeoning damage and 4d6 Cold damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"20 foot radius, 40 foot high\"}}"},{"name":"Ice Storm Bludgeoning Damage","parent":"Ice Storm Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Bludgeoning\",\"diceCount\":2,\"diceSize\":\"d10\"}"},{"name":"Ice Storm Cold Damage","parent":"Ice Storm Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceCount\":4,\"diceSize\":\"d6\"}"},{"name":"Ice Storm Bludgeoning Damage Upcast","parent":"Ice Storm Bludgeoning Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":5,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Ice Storm
- data-description: Hail falls in a 20-foot-radius, 40-foot-high Cylinder centered on a point within range. Each creature in the Cylinder makes a Dexterity saving throw. A creature takes 2d10 Bludgeoning damage and 4d6 Cold damage on a failed save or half as much damage on a successful one.
Hailstones turn ground in the Cylinder into Difficult Terrain until the end of your next turn.
- Level: 4
- Casting Time: Action
- Duration: Instantaneous
- Range: 300 feet
- Components: V S M
- Material: a mitten
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The Bludgeoning damage increases by 1d10 for each spell slot level above 4.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 300
- Save: Dexterity
- Damage: 2d10
- Damage Type: Bludgeoning
- data-RangeAoe: 300 ft (20 ft radius, 40 foot high ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

