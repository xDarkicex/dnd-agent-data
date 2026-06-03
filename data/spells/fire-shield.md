# Fire Shield

**description**: Level 4 Evocation (Druid, Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S, M (a bit of phosphorus or a firefly) Duration: 10 minutes Wispy flames wreathe your body for the duration, shedding Bright Light in a 10-foot radius and Dim Light for an additional 10 feet. The flames provide you with a warm shield or a chill shield, as you choose. The warm shield grants you Resistance to Cold damage, and the chill shield grants you Resistance to Fire damage. In addition, whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Fire damage from a warm shield or 2d8 Cold damage from a chill shield.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Buff, Fire Damage, Cold Damage
- Spell Attack: None
- filter-Level: 4
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 10 min
- data-datarecords: [{"name":"Fire Shield","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Fire Shield\",\"description\":\"Wispy flames wreathe your body for the duration, shedding Bright Light in a 10-foot radius and Dim Light for an additional 10 feet.\\nThe flames provide you with a warm shield or a chill shield, as you choose. The warm shield grants you Resistance to Cold damage, and the chill shield grants you Resistance to Fire damage.\\nIn addition, whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Fire damage from a warm shield or 2d8 Cold damage from a chill shield.\",\"level\":4,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"10 minutes\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a bit of phosphorus or a firefly\"}}"},{"name":"Fire Shield Warm Shield Condition","parent":"Fire Shield","payload":"{\"type\":\"Condition\",\"name\":\"Fire Shield - Warm Shield\",\"description\":\"The warm shield grants you Resistance to Cold damage, and whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Fire damage.\"}"},{"name":"Fire Shield Warm Shield Resistance","parent":"Fire Shield Warm Shield Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Resistance\",\"damage\":\"Cold\"}"},{"name":"Fire Shield Warm Shield Attack","parent":"Fire Shield Warm Shield Condition","payload":"{\"type\":\"Attack\",\"name\":\"Warm Shield\",\"autoHit\":true,\"range\":\"5 ft\",\"onHitDisplay\":\"Whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame.\",\"description\":\"Whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame.\",\"actionType\":\"Free Action\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Warm Shield Damage","parent":"Fire Shield Warm Shield Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":2,\"diceSize\":\"d8\"}"},{"name":"Fire Shield Chill Shield Condition","parent":"Fire Shield","payload":"{\"type\":\"Condition\",\"name\":\"Fire Shield - Chill Shield\",\"description\":\"The warm shield grants you Resistance to Fire damage, and whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Cold damage.\"}"},{"name":"Fire Shield Chill Shield Resistance","parent":"Fire Shield Chill Shield Condition","payload":"{\"type\":\"Defense\",\"defense\":\"Resistance\",\"damage\":\"Fire\"}"},{"name":"Fire Shield Chill Shield Attack","parent":"Fire Shield","payload":"{\"type\":\"Attack\",\"name\":\"Chill Shield\",\"autoHit\":true,\"range\":\"5 ft\",\"onHitDisplay\":\"Whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame.\",\"description\":\"Whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame.\",\"actionType\":\"Free Action\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Chill Shield Damage","parent":"Fire Shield Chill Shield Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Cold\",\"diceCount\":2,\"diceSize\":\"d8\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Fire Shield
- data-description: Wispy flames wreathe your body for the duration, shedding Bright Light in a 10-foot radius and Dim Light for an additional 10 feet.
The flames provide you with a warm shield or a chill shield, as you choose. The warm shield grants you Resistance to Cold damage, and the chill shield grants you Resistance to Fire damage.
In addition, whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Fire damage from a warm shield or 2d8 Cold damage from a chill shield.
- Level: 4
- Casting Time: Action
- Duration: 10 minutes
- Range: Self
- Components: V S M
- Material: a bit of phosphorus or a firefly
- data-CastNum: 2
- data-DurationNum: 6
- data-AttackType: Spell Attack
- Damage: 2d8
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

