# Conjure Woodland Beings

**description**: Level 4 Conjuration (Druid, Ranger) Casting Time: Action Range: Self Components: V, S Duration: Concentration, up to 10 minutes You conjure nature spirits that flit around you in a 10-foot Emanation for the duration. Whenever the Emanation enters the space of a creature you can see and whenever a creature you can see enters the Emanation or ends its turn there, you can force that creature to make a Wisdom saving throw. The creature takes 5d8 Force damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn. In addition, you can take the Disengage action as a Bonus Action for the spell’s duration. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid, Ranger
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Force Damage, Wisdom Save, Minions
- Spell Attack: None
- filter-Level: 4
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Conjure Woodland Beings","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Conjure Woodland Beings\",\"description\":\"You conjure nature spirits that flit around you in a 10-foot Emanation for the duration. Whenever the Emanation enters the space of a creature you can see and whenever a creature you can see enters the Emanation or ends its turn there, you can force that creature to make a Wisdom saving throw. The creature takes 5d8 Force damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn.\\nIn addition, you can take the Disengage action as a Bonus Action for the spell's duration.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.\",\"level\":4,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"10 foot\"}}"},{"name":"Conjure Woodland Beings Condition","parent":"Conjure Woodland Beings","payload":"{\"type\":\"Condition\",\"name\":\"Conjure Woodland Beings\"}"},{"name":"Conjure Woodland Beings Attack","parent":"Conjure Woodland Beings","payload":"{\"type\":\"Attack\",\"name\":\"Conjure Woodland Beings\",\"description\":\"You can force that creature to make a Wisdom saving throw.\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Take 5d8 Force damage.\",\"onSucceed\":\"Half as much damage.\"},\"actionType\":\"Free Action\"}"},{"name":"Conjure Woodland Beings Damage","parent":"Conjure Woodland Beings Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Force\",\"diceCount\":5,\"diceSize\":\"d8\"}"},{"name":"Conjure Woodland Beings Damage Upcast","parent":"Conjure Woodland Beings Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Conjure Woodland Beings
- data-description: You conjure nature spirits that flit around you in a 10-foot Emanation for the duration. Whenever the Emanation enters the space of a creature you can see and whenever a creature you can see enters the Emanation or ends its turn there, you can force that creature to make a Wisdom saving throw. The creature takes 5d8 Force damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn.
In addition, you can take the Disengage action as a Bonus Action for the spell's duration.
- Level: 4
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: Self
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.
- data-CastNum: 2
- Save: Wisdom
- Damage: 5d8
- Damage Type: Force
- data-RangeAoe: Self (10 ft ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

