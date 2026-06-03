# Sunbeam

**description**: Level 6 Evocation (Cleric, Druid, Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S, M (a magnifying glass) Duration: Concentration, up to 1 minute You launch a sunbeam in a 5-foot-wide, 60-foot-long Line. Each creature in the Line makes a Constitution saving throw. On a failed save, a creature takes 6d8 Radiant damage and has the Blinded condition until the start of your next turn. On a successful save, it takes half as much damage only. Until the spell ends, you can take a Magic action to create a new Line of radiance. For the duration, a mote of brilliant radiance shines above you. It sheds Bright Light in a 30-foot radius and Dim Light for an additional 30 feet. This light is sunlight.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Cleric, Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Inflict Condition, Constitution Save, Radiant Damage, Blinded
- Spell Attack: None
- filter-Level: 6
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Sunbeam","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Sunbeam\",\"description\":\"You launch a sunbeam in a 5-foot-wide, 60-foot-long Line. Each creature in the Line makes a Constitution saving throw. On a failed save, a creature takes 6d8 Radiant damage and has the Blinded condition until the start of your next turn. On a successful save, it takes half as much damage only.\\nUntil the spell ends, you can take a Magic action to create a new Line of radiance.\\nFor the duration, a mote of brilliant radiance shines above you. It sheds Bright Light in a 30-foot radius and Dim Light for an additional 30 feet. This light is sunlight.\",\"level\":6,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a magnifying glass\"},\"aoe\":{\"shape\":\"Line\",\"size\":\"60 foot long\"}}"},{"name":"Sunbeam Attack","parent":"Sunbeam","payload":"{\"type\":\"Attack\",\"name\":\"Sunbeam\",\"description\":\"Each creature in the Line makes a Constitution saving throw.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 6d8 Radiant damage and has the Blinded condition until the start of your next turn.\",\"onSucceed\":\"Half as much damage only.\"},\"actionType\":\"Action\",\"aoe\":{\"shape\":\"Line\",\"size\":\"60 foot long\"}}"},{"name":"Sunbeam Damage","parent":"Sunbeam Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceCount\":6,\"diceSize\":\"d8\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Sunbeam
- data-description: You launch a sunbeam in a 5-foot-wide, 60-foot-long Line. Each creature in the Line makes a Constitution saving throw. On a failed save, a creature takes 6d8 Radiant damage and has the Blinded condition until the start of your next turn. On a successful save, it takes half as much damage only.
Until the spell ends, you can take a Magic action to create a new Line of radiance.
For the duration, a mote of brilliant radiance shines above you. It sheds Bright Light in a 30-foot radius and Dim Light for an additional 30 feet. This light is sunlight.
- Level: 6
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: Self
- Components: V S M
- Material: a magnifying glass
- data-CastNum: 2
- Save: Constitution
- Damage: 6d8
- Damage Type: Radiant
- data-RangeAoe: Self (60 ft long ⇧)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

