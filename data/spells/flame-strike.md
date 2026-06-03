# Flame Strike

**description**: Level 5 Evocation (Cleric) Casting Time: Action Range: 60 feet Components: V, S, M (a pinch of sulfur) Duration: Instantaneous A vertical column of brilliant fire roars down from above. Each creature in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range makes a Dexterity saving throw, taking 5d6 Fire damage and 5d6 Radiant damage on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Fire Damage, Radiant Damage
- Spell Attack: None
- filter-Level: 5
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Flame Strike","level":"5","payload":"{\"type\":\"Spell\",\"name\":\"Flame Strike\",\"description\":\"A vertical column of brilliant fire roars down from above. Each creature in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range makes a Dexterity saving throw, taking 5d6 Fire damage and 5d6 Radiant damage on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.\",\"level\":5,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a pinch of sulfur\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"10 foot radius, 40 foot high\"}}"},{"name":"Flame Strike Attack","parent":"Flame Strike","payload":"{\"type\":\"Attack\",\"name\":\"Flame Strike\",\"range\":\"60 feet\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 5d6 Fire damage and 5d6 Radiant damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"10 foot radius, 40 foot high\"},\"actionType\":\"Action\"}"},{"name":"Flame Strike Damage Fire","parent":"Flame Strike Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":5,\"diceSize\":\"d6\"}"},{"name":"Flame Strike Damage Radiant","parent":"Flame Strike Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceCount\":5,\"diceSize\":\"d6\"}"},{"name":"Flame Strike Damage Fire Upcast","parent":"Flame Strike Damage Fire","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Flame Strike Damage Radiant Upcast","parent":"Flame Strike Damage Radiant","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Flame Strike
- data-description: A vertical column of brilliant fire roars down from above. Each creature in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range makes a Dexterity saving throw, taking 5d6 Fire damage and 5d6 Radiant damage on a failed save or half as much damage on a successful one.
- Level: 5
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V S M
- Material: a pinch of sulfur
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Dexterity
- Damage: 5d6
- Damage Type: Fire
- data-RangeAoe: 60 ft (10 ft radius, 40 foot high ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

