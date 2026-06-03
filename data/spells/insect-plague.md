# Insect Plague

**description**: Level 5 Conjuration (Cleric, Druid, Sorcerer) Casting Time: Action Range: 300 feet Components: V, S, M (a locust) Duration: Concentration, up to 10 minutes Swarming locusts fill a 20-foot-radius Sphere centered on a point you choose within range. The Sphere remains for the duration, and its area is Lightly Obscured and Difficult Terrain. When the swarm appears, each creature in it makes a Constitution saving throw, taking 4d10 Piercing damage on a failed save or half as much damage on a successful one. A creature also makes this save when it enters the spell’s area for the first time on a turn or ends its turn there. A creature makes this save only once per turn. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 5.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Cleric, Druid, Sorcerer
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Piercing Damage
- Spell Attack: None
- filter-Level: 5
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Insect Plague","level":"5","payload":"{\"type\":\"Spell\",\"name\":\"Insect Plague\",\"description\":\"Swarming locusts fill a 20-foot-radius Sphere centered on a point you choose within range. The Sphere remains for the duration, and its area is Lightly Obscured and Difficult Terrain.\\nWhen the swarm appears, each creature in it makes a Constitution saving throw, taking 4d10 Piercing damage on a failed save or half as much damage on a successful one. A creature also makes this save when it enters the spell's area for the first time on a turn or ends its turn there. A creature makes this save only once per turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 5.\",\"level\":5,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"300 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a locust\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Insect Plague Condition","parent":"Insect Plague","payload":"{\"type\":\"Condition\",\"name\":\"Insect Plague\",\"description\":\"Swarming locusts fill a 20-foot-radius Sphere centered on a point you choose within range. The Sphere remains for the duration, and its area is Lightly Obscured and Difficult Terrain.\"}"},{"name":"Insect Plague Attack","parent":"Insect Plague","payload":"{\"type\":\"Attack\",\"name\":\"Insect Plague\",\"description\":\"When the swarm appears, each creature in it makes a Constitution saving throw, taking 4d10 Piercing damage on a failed save or half as much damage on a successful one. A creature also makes this save when it enters the spell's area for the first time on a turn or ends its turn there. A creature makes this save only once per turn.\\n\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 4d10 Piercing damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Insect Plague Damage","parent":"Insect Plague Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Piercing\",\"diceCount\":4,\"diceSize\":\"d10\"}"},{"name":"Insect Plague Damage Upcast","parent":"Insect Plague Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Insect Plague
- data-description: Swarming locusts fill a 20-foot-radius Sphere centered on a point you choose within range. The Sphere remains for the duration, and its area is Lightly Obscured and Difficult Terrain.
When the swarm appears, each creature in it makes a Constitution saving throw, taking 4d10 Piercing damage on a failed save or half as much damage on a successful one. A creature also makes this save when it enters the spell's area for the first time on a turn or ends its turn there. A creature makes this save only once per turn.
- Level: 5
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 300 feet
- Components: V S M
- Material: a locust
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 5.
- data-CastNum: 2
- data-RangeNum: 300
- Save: Constitution
- Damage: 4d10
- Damage Type: Piercing
- data-RangeAoe: 300 ft (20 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

