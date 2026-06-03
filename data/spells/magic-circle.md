# Magic Circle

**description**: Level 3 Abjuration (Cleric, Paladin, Warlock, Wizard) Casting Time: 1 minute Range: 10 feet Components: V, S, M (salt and powdered silver worth 100+ GP, which the spell consumes) Duration: 1 hour You create a 10-foot-radius, 20-foot-tall Cylinder of magical energy centered on a point on the ground that you can see within range. Glowing runes appear wherever the Cylinder intersects with the floor or other surface. Choose one or more of the following types of creatures: Celestials, Elementals, Fey, Fiends, or Undead. The circle affects a creature of the chosen type in the following ways: The creature can’t willingly enter the Cylinder by nonmagical means. If the creature tries to use teleportation or interplanar travel to do so, it must first succeed on a Charisma saving throw. The creature has Disadvantage on attack rolls against targets within the Cylinder. Targets within the Cylinder can’t be possessed by or gain the Charmed or Frightened condition from the creature. Each time you cast this spell, you can cause its magic to operate in the reverse direction, preventing a creature of the specified type from leaving the Cylinder and protecting targets outside it. Using a Higher-Level Spell Slot. The duration increases by 1 hour for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Abjuration
- Classes: Cleric, Paladin, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Utility
- Spell Attack: None
- filter-Level: 3
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 hour
- data-datarecords: [{"name":"Magic Circle","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Magic Circle\",\"description\":\"You create a 10-foot-radius, 20-foot-tall Cylinder of magical energy centered on a point on the ground that you can see within range. Glowing runes appear wherever the Cylinder intersects with the floor or other surface.\\nChoose one or more of the following types of creatures: Celestials, Elementals, Fey, Fiends, or Undead. The circle affects a creature of the chosen type in the following ways:\\nThe creature can't willingly enter the Cylinder by nonmagical means. If the creature tries to use teleportation or interplanar travel to do so, it must first succeed on a Charisma saving throw.\\nThe creature has Disadvantage on attack rolls against targets within the Cylinder.\\nTargets within the Cylinder can't be possessed by or gain the Charmed or Frightened condition from the creature.\\nEach time you cast this spell, you can cause its magic to operate in the reverse direction, preventing a creature of the specified type from leaving the Cylinder and protecting targets outside it.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The duration increases by 1 hour for each spell slot level above 3.\",\"level\":3,\"school\":\"Abjuration\",\"castingTime\":\"1 minute\",\"range\":\"10 feet\",\"duration\":\"1 hour\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"salt and powdered silver worth 100+ GP, which the spell consumes\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"10 foot radius, 20 foot tall*\"}}"},{"name":"Magic Circle Duration Upcast 4","parent":"Magic Circle","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":4,\"target\":\"$.duration\",\"value\":\"2 hours\",\"changeMode\":\"Override\"}"},{"name":"Magic Circle Duration Upcast 5","parent":"Magic Circle","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":5,\"target\":\"$.duration\",\"value\":\"3 hours\",\"changeMode\":\"Override\"}"},{"name":"Magic Circle Duration Upcast 6","parent":"Magic Circle","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":6,\"target\":\"$.duration\",\"value\":\"4 hours\",\"changeMode\":\"Override\"}"},{"name":"Magic Circle Duration Upcast 7","parent":"Magic Circle","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":7,\"target\":\"$.duration\",\"value\":\"5 hours\",\"changeMode\":\"Override\"}"},{"name":"Magic Circle Duration Upcast 8","parent":"Magic Circle","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":8,\"target\":\"$.duration\",\"value\":\"6 hours\",\"changeMode\":\"Override\"}"},{"name":"Magic Circle Duration Upcast 9","parent":"Magic Circle","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":9,\"target\":\"$.duration\",\"value\":\"7 hours\",\"changeMode\":\"Override\"}"},{"name":"Magic Circle Condition","parent":"Magic Circle","payload":"{\"type\":\"Condition\",\"name\":\"Magic Circle\"}"},{"name":"Magic Circle Immunities","parent":"Magic Circle Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Condition Immunity\",\"condition\":\"Charmed, Frightened, Possessed\",\"details\":\"Targets within the c⁠ylinder can't be charmed, frightened, or possessed by the creature.\"}"},{"name":"Magic Circle Defense","parent":"Magic Circle Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Resistance\",\"damage\":\"Magic Circle\",\"details\":\"The creature has disadvantage on attack rolls against targets within the cylinder.\"}"},{"name":"Magic Circle Attack","parent":"Magic Circle","payload":"{\"type\":\"Attack\",\"name\":\"Magic Circle - Blocked Creature Tries Accessing\",\"description\":\"If a blocked creature tries to use teleportation or interplanar travel to enter the Magic Circle, it must first succeed on a Charisma saving throw.\",\"save\":{\"saveAbility\":\"Charisma\",\"onSucceed\":\"Can use teleportation or interplanar travel to enter Magic Circle.\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"10-foot-radius, 20-foot-tall\"}}"}]
- filter-Components: Verbal, Somatic, Material (Consumed)
- filter-Casting Time: 1 min
- filter-Concentration: No
- Name: Magic Circle
- data-description: You create a 10-foot-radius, 20-foot-tall Cylinder of magical energy centered on a point on the ground that you can see within range. Glowing runes appear wherever the Cylinder intersects with the floor or other surface.
Choose one or more of the following types of creatures: Celestials, Elementals, Fey, Fiends, or Undead. The circle affects a creature of the chosen type in the following ways:
The creature can't willingly enter the Cylinder by nonmagical means. If the creature tries to use teleportation or interplanar travel to do so, it must first succeed on a Charisma saving throw.
The creature has Disadvantage on attack rolls against targets within the Cylinder.
Targets within the Cylinder can't be possessed by or gain the Charmed or Frightened condition from the creature.
Each time you cast this spell, you can cause its magic to operate in the reverse direction, preventing a creature of the specified type from leaving the Cylinder and protecting targets outside it.
- Level: 3
- Casting Time: 1 minute
- Duration: 1 hour
- Range: 10 feet
- Components: V S M
- Material: salt and powdered silver worth 100+ GP, which the spell consumes
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The duration increases by 1 hour for each spell slot level above 3.
- data-CastNum: 4
- data-DurationNum: 9
- data-RangeNum: 10
- Save: Charisma
- data-RangeAoe: 10 ft (10 ft radius, 20 foot tall* ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

