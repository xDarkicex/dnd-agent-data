# Aid

**description**: Level 2 Abjuration (Bard, Cleric, Druid, Paladin, Ranger) Casting Time: Action Range: 30 feet Components: V, S, M (a strip of white cloth) Duration: 8 hours Choose up to three creatures within range. Each target’s Hit Point maximum and current Hit Points increase by 5 for the duration. Using a Higher-Level Spell Slot. Each target’s Hit Points increase by 5 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Abjuration
- Classes: Bard, Cleric, Druid, Paladin, Ranger
- Expansion: 33335
- data-List: false
- filter-Tags: Buff, Healing
- Spell Attack: None
- filter-Level: 2
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 8 hours
- data-datarecords: [{"name":"Aid","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Aid\",\"description\":\"Choose up to three creatures within range. Each target's Hit Point maximum and current Hit Points increase by 5 for the duration.\",\"upcastText\":\"Using a Higher-Level Spell Slot. Each target's Hit Points increase by 5 for each spell slot level above 2.\",\"level\":2,\"school\":\"Abjuration\",\"castingTime\":\"Action\",\"range\":\"30 feet\",\"duration\":\"8 hours\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a strip of white cloth\"}}"},{"name":"Aid Condition","parent":"Aid","payload":"{\"type\":\"Condition\",\"name\":\"Aid Spell\",\"description\":\"Your Hit Point maximum and current Hit Points increase by 5 for the duration. If cast at a higher spell, increase by 5 for each spell slot level above 2.\"}"},{"name":"Aid Max HP Increase","parent":"Aid Condition","payload":"{\"type\":\"Hit Points\",\"calculation\":\"Modify\",\"hitpointType\":\"Maximum\",\"valueFormula\":{\"flatValue\":5}}"},{"name":"Aid Current HP Increase","parent":"Aid Condition","payload":"{\"type\":\"Hit Points\",\"calculation\":\"Modify\",\"hitpointType\":\"Current\",\"valueFormula\":{\"flatValue\":5}}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Aid
- data-description: Choose up to three creatures within range. Each target's Hit Point maximum and current Hit Points increase by 5 for the duration.
- Level: 2
- Casting Time: Action
- Duration: 8 hours
- Range: 30 feet
- Components: V S M
- Material: a strip of white cloth
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. Each target's Hit Points increase by 5 for each spell slot level above 2.
- data-CastNum: 2
- data-DurationNum: 12
- data-RangeNum: 30

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

