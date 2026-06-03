# Dominate Person

**description**: Level 5 Enchantment (Bard, Sorcerer, Wizard) Casting Time: Action Range: 60 feet Components: V, S Duration: Concentration, up to 1 minute One Humanoid you can see within range must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The target has Advantage on the save if you or your allies are fighting it. Whenever the target takes damage, it repeats the save, ending the spell on itself on a success. You have a telepathic link with the Charmed target while the two of you are on the same plane of existence. On your turn, you can use this link to issue commands to the target (no action required), such as “Attack that creature,” “Move over there,” or “Fetch that object.” The target does its best to obey on its turn. If it completes an order and doesn’t receive further direction from you, it acts and moves as it likes, focusing on protecting itself. You can command the target to take a Reaction but must take your own Reaction to do so. Using a Higher-Level Spell Slot. Your Concentration can last longer with a spell slot of level 6 (up to 10 minutes), 7 (up to 1 hour), or 8+ (up to 8 hours).

**properties**:
- Category: Spells
- School: Enchantment
- Classes: Bard, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Wisdom Save, Inflict Condition, Charmed
- Spell Attack: None
- filter-Level: 5
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Dominate Person","level":"5","payload":"{\"type\":\"Spell\",\"name\":\"Dominate Person\",\"description\":\"One Humanoid you can see within range must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The target has Advantage on the save if you or your allies are fighting it. Whenever the target takes damage, it repeats the save, ending the spell on itself on a success.\\nYou have a telepathic link with the Charmed target while the two of you are on the same plane of existence. On your turn, you can use this link to issue commands to the target (no action required), such as 'Attack that creature,' 'Move over there,' or 'Fetch that object.' The target does its best to obey on its turn. If it completes an order and doesn't receive further direction from you, it acts and moves as it likes, focusing on protecting itself.\\nYou can command the target to take a Reaction but must take your own Reaction to do so.\",\"upcastText\":\"Using a Higher-Level Spell Slot. Your Concentration can last longer with a spell slot of level 6 (up to 10 minutes), 7 (up to 1 hour), or 8+ (up to 8 hours).\",\"level\":5,\"school\":\"Enchantment\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Dominate Person Condition","parent":"Dominate Person","payload":"{\"type\":\"Condition\",\"name\":\"Dominate Person\"}"},{"name":"Dominate Person Attack","parent":"Dominate Person","payload":"{\"type\":\"Attack\",\"name\":\"Dominate Person\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Target has the Charmed condition for the duration.\"}}"},{"name":"Dominate Person Reaction","parent":"Dominate Person Condition","payload":"{\"type\":\"Action\",\"name\":\"Dominate Person Reaction\",\"description\":\"You can command the target to take a Reaction but must take your own Reaction to do so.\",\"actionType\":\"Reaction\"}"},{"name":"Dominate Person Duration Upcast 6","parent":"Dominate Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":6,\"target\":\"$.duration\",\"value\":\"Concentration, up to 10 minutes\",\"changeMode\":\"Override\"}"},{"name":"Dominate Person Duration Upcast 7","parent":"Dominate Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":7,\"target\":\"$.duration\",\"value\":\"Concentration, up to 1 hour\",\"changeMode\":\"Override\"}"},{"name":"Dominate Person Duration Upcast 8","parent":"Dominate Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":8,\"target\":\"$.duration\",\"value\":\"Concentration, up to 8 hours\",\"changeMode\":\"Override\"}"},{"name":"Dominate Person Duration Upcast 9","parent":"Dominate Person","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Spell Level\",\"level\":9,\"target\":\"$.duration\",\"value\":\"Concentration, up to 8 hours\",\"changeMode\":\"Override\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Dominate Person
- data-description: One Humanoid you can see within range must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The target has Advantage on the save if you or your allies are fighting it. Whenever the target takes damage, it repeats the save, ending the spell on itself on a success.
You have a telepathic link with the Charmed target while the two of you are on the same plane of existence. On your turn, you can use this link to issue commands to the target (no action required), such as 'Attack that creature,' 'Move over there,' or 'Fetch that object.' The target does its best to obey on its turn. If it completes an order and doesn't receive further direction from you, it acts and moves as it likes, focusing on protecting itself.
You can command the target to take a Reaction but must take your own Reaction to do so.
- Level: 5
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. Your Concentration can last longer with a spell slot of level 6 (up to 10 minutes), 7 (up to 1 hour), or 8+ (up to 8 hours).
- data-CastNum: 2
- data-RangeNum: 60
- Save: Wisdom

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

