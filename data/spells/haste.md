# Haste

**description**: Level 3 Transmutation (Sorcerer, Wizard) Casting Time: Action Range: 30 feet Components: V, S, M (a shaving of licorice root) Duration: Concentration, up to 1 minute Choose a willing creature that you can see within range. Until the spell ends, the target’s Speed is doubled, it gains a +2 bonus to Armor Class, it has Advantage on Dexterity saving throws, and it gains an additional action on each of its turns. That action can be used to take only the Attack (one attack only), Dash, Disengage, Hide, or Utilize action. When the spell ends, the target is Incapacitated and has a Speed of 0 until the end of its next turn, as a wave of lethargy washes over it.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Buff
- Spell Attack: None
- filter-Level: 3
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Haste","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Haste\",\"description\":\"Choose a willing creature that you can see within range. Until the spell ends, the target's Speed is doubled, it gains a +2 bonus to Armor Class, it has Advantage on Dexterity saving throws, and it gains an additional action on each of its turns. That action can be used to take only the Attack (one attack only), Dash, Disengage, Hide, or Utilize action.\\nWhen the spell ends, the target is Incapacitated and has a Speed of 0 until the end of its next turn, as a wave of lethargy washes over it.\",\"level\":3,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"30 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a shaving of licorice root\"}}"},{"name":"Haste Condition","parent":"Haste","payload":"{\"type\":\"Condition\",\"name\":\"Haste\",\"description\":\"The target's Speed is doubled, it gains a +2 bonus to Armor Class, it has Advantage on Dexterity saving throws, and it gains an additional action on each of its turns. That action can be used to take only the Attack (one attack only), Dash, Disengage, Hide, or Utilize action.\"}"},{"name":"Haste Speed","parent":"Haste Condition","payload":"{\"type\":\"Speed\",\"speed\":\"Walk\",\"calculation\":\"Multiplier\",\"valueFormula\":{\"flatValue\":2}}"},{"name":"Haste AC Bonus","parent":"Haste Condition","payload":"{\"type\":\"Armor Class\",\"calculation\":\"Modify\",\"source\":\"Other\",\"valueFormula\":{\"flatValue\":2}}"},{"name":"Haste Save Advantage","parent":"Haste Condition","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Saving Throws\"],\"bonusName\":[\"Dexterity\"],\"bonusDetails\":\"Keep Highest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"Advantage on Dexterity saving throws.\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Haste
- data-description: Choose a willing creature that you can see within range. Until the spell ends, the target's Speed is doubled, it gains a +2 bonus to Armor Class, it has Advantage on Dexterity saving throws, and it gains an additional action on each of its turns. That action can be used to take only the Attack (one attack only), Dash, Disengage, Hide, or Utilize action.
When the spell ends, the target is Incapacitated and has a Speed of 0 until the end of its next turn, as a wave of lethargy washes over it.
- Level: 3
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 30 feet
- Components: V S M
- Material: a shaving of licorice root
- data-CastNum: 2
- data-RangeNum: 30

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

