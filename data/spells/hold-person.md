# Hold Person

**description**: Level 2 Enchantment (Bard, Cleric, Druid, Sorcerer, Warlock, Wizard) Casting Time: Action Range: 60 feet Components: V, S, M (a straight piece of iron) Duration: Concentration, up to 1 minute Choose a Humanoid that you can see within range. The target must succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success. Using a Higher-Level Spell Slot. You can target one additional Humanoid for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Enchantment
- Classes: Bard, Cleric, Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Wisdom Save, Paralyzed, Inflict Condition
- Spell Attack: None
- filter-Level: 2
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Hold Person","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Hold Person\",\"description\":\"Choose a Humanoid that you can see within range. The target must succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success.\",\"upcastText\":\"Using a Higher-Level Spell Slot. You can target one additional Humanoid for each spell slot level above 2.\",\"level\":2,\"school\":\"Enchantment\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a straight piece of iron\"}}"},{"name":"Hold Person Attack","parent":"Hold Person","payload":"{\"type\":\"Attack\",\"name\":\"Hold Person\",\"range\":\"60 feet\",\"description\":\"The target must succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success.\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Have the Paralyzed condition for the duration.\",\"onSucceed\":\"Ends the spell.\"}}"},{"name":"Hold Person Upcast 3","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":3,\"target\":\"$.description\",\"value\":\"Choose two Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"},{"name":"Hold Person Upcast 4","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":4,\"target\":\"$.description\",\"value\":\"Choose three Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"},{"name":"Hold Person Upcast 5","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":5,\"target\":\"$.description\",\"value\":\"Choose four Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"},{"name":"Hold Person Upcast 6","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":6,\"target\":\"$.description\",\"value\":\"Choose five Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"},{"name":"Hold Person Upcast 7","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":7,\"target\":\"$.description\",\"value\":\"Choose six Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"},{"name":"Hold Person Upcast 8","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":8,\"target\":\"$.description\",\"value\":\"Choose seven Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"},{"name":"Hold Person Upcast 9","parent":"Hold Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":9,\"target\":\"$.description\",\"value\":\"Choose eight Humanoids that you can see within range. The targets must each succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, each target repeats the save, ending the spell on itself on a success.\",\"changeMode\":\"Override\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Hold Person
- data-description: Choose a Humanoid that you can see within range. The target must succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success.
- Level: 2
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 60 feet
- Components: V S M
- Material: a straight piece of iron
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. You can target one additional Humanoid for each spell slot level above 2.
- data-CastNum: 2
- data-RangeNum: 60
- Save: Wisdom

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

