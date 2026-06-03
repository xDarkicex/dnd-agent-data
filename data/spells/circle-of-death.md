# Circle of Death

**description**: Level 6 Necromancy (Sorcerer, Warlock, Wizard) Casting Time: Action Range: 150 feet Components: V, S, M (the powder of a crushed black pearl worth 500+ GP) Duration: Instantaneous Negative energy ripples out in a 60-foot-radius Sphere from a point you choose within range. Each creature in that area makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 6.

**properties**:
- Category: Spells
- School: Necromancy
- Classes: Sorcerer, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Necrotic Damage
- Spell Attack: None
- filter-Level: 6
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Circle of Death","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Circle of Death\",\"description\":\"Negative energy ripples out in a 60-foot-radius Sphere from a point you choose within range. Each creature in that area makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 6.\",\"level\":6,\"school\":\"Necromancy\",\"castingTime\":\"Action\",\"range\":\"150 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"the powder of a crushed black pearl worth 500+ GP\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"60 foot radius\"}}"},{"name":"Circle of Death Attack","parent":"Circle of Death","payload":"{\"type\":\"Attack\",\"name\":\"Circle of Death\",\"range\":\"150 feet\",\"description\":\"Negative energy ripples out in a 60-foot-radius Sphere from a point you choose within range.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 8d8 Necrotic damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"60 foot radius\"}}"},{"name":"Circle of Death Damage","parent":"Circle of Death Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Necrotic\",\"diceCount\":8,\"diceSize\":\"d8\"}"},{"name":"Circle of Death Damage Upcast","parent":"Circle of Death Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":7,\"level\":1,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material (Cost)
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Circle of Death
- data-description: Negative energy ripples out in a 60-foot-radius Sphere from a point you choose within range. Each creature in that area makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one.
- Level: 6
- Casting Time: Action
- Duration: Instantaneous
- Range: 150 feet
- Components: V S M
- Material: the powder of a crushed black pearl worth 500+ GP
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 2d8 for each spell slot level above 6.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 150
- Save: Constitution
- Damage: 8d8
- Damage Type: Necrotic
- data-RangeAoe: 150 ft (60 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

