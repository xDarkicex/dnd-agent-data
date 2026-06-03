# Moonbeam

**description**: Level 2 Evocation (Druid) Casting Time: Action Range: 120 feet Components: V, S, M (a moonseed leaf) Duration: Concentration, up to 1 minute A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high Cylinder centered on a point within range. Until the spell ends, Dim Light fills the Cylinder, and you can take a Magic action on later turns to move the Cylinder up to 60 feet. When the Cylinder appears, each creature in it makes a Constitution saving throw. On a failed save, a creature takes 2d10 Radiant damage, and if the creature is shape-shifted (as a result of the Polymorph spell, for example), it reverts to its true form and can’t shape-shift until it leaves the Cylinder. On a successful save, a creature takes half as much damage only. A creature also makes this save when the spell’s area moves into its space and when it enters the spell’s area or ends its turn there. A creature makes this save only once per turn. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Radiant Damage
- Spell Attack: None
- filter-Level: 2
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Moonbeam","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Moonbeam\",\"description\":\"A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high Cylinder centered on a point within range. Until the spell ends, Dim Light fills the Cylinder, and you can take a Magic action on later turns to move the Cylinder up to 60 feet.\\nWhen the Cylinder appears, each creature in it makes a Constitution saving throw. On a failed save, a creature takes 2d10 Radiant damage, and if the creature is shape-shifted (as a result of the Polymorph spell, for example), it reverts to its true form and can't shape-shift until it leaves the Cylinder. On a successful save, a creature takes half as much damage only. A creature also makes this save when the spell's area moves into its space and when it enters the spell's area or ends its turn there. A creature makes this save only once per turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 2.\",\"level\":2,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a moonseed leaf\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"5 foot radius, 40 foot high\"}}"},{"name":"Moonbeam Condition","parent":"Moonbeam","payload":"{\"type\":\"Condition\",\"name\":\"Moonbeam\",\"description\":\"A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high Cylinder centered on a point within range.\"}"},{"name":"Moonbeam Action","parent":"Moonbeam Condition","payload":"{\"type\":\"Action\",\"name\":\"Move Moonbeam\",\"description\":\"Until the spell ends, Dim Light fills the Cylinder, and you can take a Magic action on later turns to move the Cylinder up to 60 feet.\",\"actionType\":\"Action\"}"},{"name":"Moonbeam Attack","parent":"Moonbeam","payload":"{\"type\":\"Attack\",\"name\":\"Moonbeam\",\"description\":\"When the Cylinder appears, each creature in it makes a Constitution saving throw. A creature also makes this save when the spell's area moves into its space and when it enters the spell's area or ends its turn there. A creature makes this save only once per turn.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Takes 2d10 Radiant damage, and if the creature is shape-shifted (as a result of the Polymorph spell, for example), it reverts to its true form and can't shape-shift until it leaves the Cylinder.\",\"onSucceed\":\"Takes half as much damage only.\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"5 foot radius, 40 foot high\"}}"},{"name":"Moonbeam Damage","parent":"Moonbeam Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceCount\":2,\"diceSize\":\"d10\"}"},{"name":"Moonbeam Damage Upcast","parent":"Moonbeam Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Moonbeam
- data-description: A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high Cylinder centered on a point within range. Until the spell ends, Dim Light fills the Cylinder, and you can take a Magic action on later turns to move the Cylinder up to 60 feet.
When the Cylinder appears, each creature in it makes a Constitution saving throw. On a failed save, a creature takes 2d10 Radiant damage, and if the creature is shape-shifted (as a result of the Polymorph spell, for example), it reverts to its true form and can't shape-shift until it leaves the Cylinder. On a successful save, a creature takes half as much damage only. A creature also makes this save when the spell's area moves into its space and when it enters the spell's area or ends its turn there. A creature makes this save only once per turn.
- Level: 2
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 120 feet
- Components: V S M
- Material: a moonseed leaf
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 2.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Constitution
- Damage: 2d10
- Damage Type: Radiant
- data-RangeAoe: 120 ft (5 ft radius, 40 foot high ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

