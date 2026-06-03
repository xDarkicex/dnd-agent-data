# Wind Walk

**description**: Level 6 Transmutation (Druid) Casting Time: 1 minute Range: 30 feet Components: V, S, M (a candle) Duration: 8 hours You and up to ten willing creatures of your choice within range assume gaseous forms for the duration, appearing as wisps of cloud. While in this cloud form, a target has a Fly Speed of 300 feet and can hover; it has Immunity to the Prone condition; and it has Resistance to Bludgeoning, Piercing, and Slashing damage. The only actions a target can take in this form are the Dash action or a Magic action to begin reverting to its normal form. Reverting takes 1 minute, during which the target has the Stunned condition. Until the spell ends, the target can revert to cloud form, which also requires a Magic action followed by a 1-minute transformation. If a target is in cloud form and flying when the effect ends, the target descends 60 feet per round for 1 minute until it lands, which it does safely. If it can’t land after 1 minute, it falls the remaining distance.

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Buff
- Spell Attack: None
- filter-Level: 6
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 8 hours
- data-datarecords: [{"name":"Wind Walk","level":"6","payload":"{\"type\":\"Spell\",\"name\":\"Wind Walk\",\"description\":\"You and up to ten willing creatures of your choice within range assume gaseous forms for the duration, appearing as wisps of cloud. While in this cloud form, a target has a Fly Speed of 300 feet and can hover; it has Immunity to the Prone condition; and it has Resistance to Bludgeoning, Piercing, and Slashing damage. The only actions a target can take in this form are the Dash action or a Magic action to begin reverting to its normal form. Reverting takes 1 minute, during which the target has the Stunned condition. Until the spell ends, the target can revert to cloud form, which also requires a Magic action followed by a 1-minute transformation.\\nIf a target is in cloud form and flying when the effect ends, the target descends 60 feet per round for 1 minute until it lands, which it does safely. If it can't land after 1 minute, it falls the remaining distance.\",\"level\":6,\"school\":\"Transmutation\",\"castingTime\":\"1 minute\",\"range\":\"30 feet\",\"duration\":\"8 hours\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a candle\"}}"},{"name":"Wind Walk Condition","parent":"Wind Walk","payload":"{\"type\":\"Condition\",\"name\":\"Wind Walk\",\"description\":\"You and up to ten willing creatures of your choice within range assume gaseous forms for the duration, appearing as wisps of cloud.\"}"},{"name":"Wind Walk Fly Speed","parent":"Wind Walk Condition","payload":"{\"type\":\"Speed\",\"speed\":\"Fly\",\"calculation\":\"Set Base\",\"valueFormula\":{\"flatValue\":300}}"},{"name":"Wind Walk Prone Immunity","parent":"Wind Walk Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Condition Immunity\",\"condition\":\"Prone\"}"},{"name":"Wind Walk Bludgeoning Resistance","parent":"Wind Walk Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Resistance\",\"damage\":\"Bludgeoning\"}"},{"name":"Wind Walk Piercing Resistance","parent":"Wind Walk Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Resistance\",\"damage\":\"Piercing\"}"},{"name":"Wind Walk Slashing Resistance","parent":"Wind Walk Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Resistance\",\"damage\":\"Slashing\"}"},{"name":"Wind Walk Solid Form Action","parent":"Wind Walk Condition","payload":"{\"type\":\"Action\",\"name\":\"Wind Walk - Solid Form\",\"description\":\"Reverting takes 1 minute, during which the target has the Stunned condition.\",\"actionType\":\"Action\"}"},{"name":"Wind Walk Cloud Form Action","parent":"Wind Walk Condition","payload":"{\"type\":\"Action\",\"name\":\"Wind Walk - Cloud Form\",\"description\":\"Until the spell ends, the target can revert to cloud form, which also requires a Magic action followed by a 1-minute transformation.\",\"actionType\":\"Action\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: 1 min
- filter-Concentration: No
- Name: Wind Walk
- data-description: You and up to ten willing creatures of your choice within range assume gaseous forms for the duration, appearing as wisps of cloud. While in this cloud form, a target has a Fly Speed of 300 feet and can hover; it has Immunity to the Prone condition; and it has Resistance to Bludgeoning, Piercing, and Slashing damage. The only actions a target can take in this form are the Dash action or a Magic action to begin reverting to its normal form. Reverting takes 1 minute, during which the target has the Stunned condition. Until the spell ends, the target can revert to cloud form, which also requires a Magic action followed by a 1-minute transformation.
If a target is in cloud form and flying when the effect ends, the target descends 60 feet per round for 1 minute until it lands, which it does safely. If it can't land after 1 minute, it falls the remaining distance.
- Level: 6
- Casting Time: 1 minute
- Duration: 8 hours
- Range: 30 feet
- Components: V S M
- Material: a candle
- data-CastNum: 4
- data-DurationNum: 12
- data-RangeNum: 30

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

