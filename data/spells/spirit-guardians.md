# Spirit Guardians

**description**: Level 3 Conjuration (Cleric) Casting Time: Action Range: Self Components: V, S, M (a prayer scroll) Duration: Concentration, up to 10 minutes Protective spirits flit around you in a 15-foot Emanation for the duration. If you are good or neutral, their spectral form appears angelic or fey (your choice). If you are evil, they appear fiendish. When you cast this spell, you can designate creatures to be unaffected by it. Any other creature’s Speed is halved in the Emanation, and whenever the Emanation enters a creature’s space and whenever a creature enters the Emanation or ends its turn there, the creature must make a Wisdom saving throw. On a failed save, the creature takes 3d8 Radiant damage (if you are good or neutral) or 3d8 Necrotic damage (if you are evil). On a successful save, the creature takes half as much damage. A creature makes this save only once per turn. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Wisdom Save, Radiant Damage, Necrotic Damage
- Spell Attack: None
- filter-Level: 3
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Spirit Guardians","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Spirit Guardians\",\"description\":\"Protective spirits flit around you in a 15-foot Emanation for the duration. If you are good or neutral, their spectral form appears angelic or fey (your choice). If you are evil, they appear fiendish.\\nWhen you cast this spell, you can designate creatures to be unaffected by it. Any other creature's Speed is halved in the Emanation, and whenever the Emanation enters a creature's space and whenever a creature enters the Emanation or ends its turn there, the creature must make a Wisdom saving throw. On a failed save, the creature takes 3d8 Radiant damage (if you are good or neutral) or 3d8 Necrotic damage (if you are evil). On a successful save, the creature takes half as much damage. A creature makes this save only once per turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 3.\",\"level\":3,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a prayer scroll\"},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"15 foot\"}}"},{"name":"Spirit Guardians Condition","parent":"Spirit Guardians","payload":"{\"type\":\"Condition\",\"name\":\"Spirit Guardians\",\"description\":\"Protective spirits flit around you in a 15-foot Emanation for the duration. If you are good or neutral, their spectral form appears angelic or fey (your choice). If you are evil, they appear fiendish.\"}"},{"name":"Spirit Guardians Attack","parent":"Spirit Guardians","payload":"{\"type\":\"Attack\",\"name\":\"Spirit Guardians\",\"description\":\"Whenever the Emanation enters a creature's space and whenever a creature enters the Emanation or ends its turn there, the creature must make a Wisdom saving throw. A creature makes this save only once per turn.\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Takes 3d8 Radiant damage (if you are good or neutral) or 3d8 Necrotic damage (if you are evil).\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"15 foot\"}}"},{"name":"Spirit Guardians Damage","parent":"Spirit Guardians Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant or Necrotic\",\"diceCount\":3,\"diceSize\":\"d8\"}"},{"name":"Spirit Guardians Damage Upcast","parent":"Spirit Guardians Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Spirit Guardians
- data-description: Protective spirits flit around you in a 15-foot Emanation for the duration. If you are good or neutral, their spectral form appears angelic or fey (your choice). If you are evil, they appear fiendish.
When you cast this spell, you can designate creatures to be unaffected by it. Any other creature's Speed is halved in the Emanation, and whenever the Emanation enters a creature's space and whenever a creature enters the Emanation or ends its turn there, the creature must make a Wisdom saving throw. On a failed save, the creature takes 3d8 Radiant damage (if you are good or neutral) or 3d8 Necrotic damage (if you are evil). On a successful save, the creature takes half as much damage. A creature makes this save only once per turn.
- Level: 3
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: Self
- Components: V S M
- Material: a prayer scroll
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 3.
- data-CastNum: 2
- Save: Wisdom
- Damage: 3d8
- Damage Type: Radiant or Necrotic
- data-RangeAoe: Self (15 ft ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

