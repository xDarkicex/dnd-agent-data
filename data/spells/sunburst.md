# Sunburst

**description**: Level 8 Evocation (Cleric, Druid, Sorcerer, Wizard) Casting Time: Action Range: 150 feet Components: V, S, M (a piece of sunstone) Duration: Instantaneous Brilliant sunlight flashes in a 60-foot-radius Sphere centered on a point you choose within range. Each creature in the Sphere makes a Constitution saving throw. On a failed save, a creature takes 12d6 Radiant damage and has the Blinded condition for 1 minute. On a successful save, it takes half as much damage only. A creature Blinded by this spell makes another Constitution saving throw at the end of each of its turns, ending the effect on itself on a success. This spell dispels Darkness in its area that was created by any spell.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Cleric, Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Inflict Condition, Constitution Save, Radiant Damage, Blinded
- Spell Attack: None
- filter-Level: 8
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Sunburst","level":"8","payload":"{\"type\":\"Spell\",\"name\":\"Sunburst\",\"description\":\"Brilliant sunlight flashes in a 60-foot-radius Sphere centered on a point you choose within range. Each creature in the Sphere makes a Constitution saving throw. On a failed save, a creature takes 12d6 Radiant damage and has the Blinded condition for 1 minute. On a successful save, it takes half as much damage only.\\nA creature Blinded by this spell makes another Constitution saving throw at the end of each of its turns, ending the effect on itself on a success.\\nThis spell dispels Darkness in its area that was created by any spell.\",\"level\":8,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"150 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a piece of sunstone\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"60 foot radius\"}}"},{"name":"Sunburst Attack","parent":"Sunburst","payload":"{\"type\":\"Attack\",\"name\":\"Sunburst\",\"description\":\"Each creature in the Sphere makes a Constitution saving throw.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Takes 12d6 Radiant damage and has the Blinded condition for 1 minute.\",\"onSucceed\":\"Half as much damage only.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"60 foot radius\"}}"},{"name":"Sunburst Damage","parent":"Sunburst Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceCount\":12,\"diceSize\":\"d6\"}"},{"name":"Sunburst Blinded Attack","parent":"Sunburst","payload":"{\"type\":\"Attack\",\"name\":\"Sunburst - Blinded Save\",\"description\":\"A creature Blinded by this spell makes another Constitution saving throw at the end of each of its turns, ending the effect on itself on a success.\",\"save\":{\"saveAbility\":\"Constitution\",\"onSucceed\":\"Ends the Blinded condition.\"},\"actionType\":\"Free Action\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Sunburst
- data-description: Brilliant sunlight flashes in a 60-foot-radius Sphere centered on a point you choose within range. Each creature in the Sphere makes a Constitution saving throw. On a failed save, a creature takes 12d6 Radiant damage and has the Blinded condition for 1 minute. On a successful save, it takes half as much damage only.
A creature Blinded by this spell makes another Constitution saving throw at the end of each of its turns, ending the effect on itself on a success.
This spell dispels Darkness in its area that was created by any spell.
- Level: 8
- Casting Time: Action
- Duration: Instantaneous
- Range: 150 feet
- Components: V S M
- Material: a piece of sunstone
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 150
- Save: Constitution
- Damage: 12d6
- Damage Type: Radiant
- data-RangeAoe: 150 ft (60 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

