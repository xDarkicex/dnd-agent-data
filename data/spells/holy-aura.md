# Holy Aura

**description**: Level 8 Abjuration (Cleric) Casting Time: Action Range: Self Components: V, S, M (a reliquary worth 1,000+ GP) Duration: Concentration, up to 1 minute For the duration, you emit an aura in a 30-foot Emanation. While in the aura, creatures of your choice have Advantage on all saving throws, and other creatures have Disadvantage on attack rolls against them. In addition, when a Fiend or an Undead hits an affected creature with a melee attack roll, the attacker must succeed on a Constitution saving throw or have the Blinded condition until the end of its next turn.

**properties**:
- Category: Spells
- School: Abjuration
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Buff, Constitution Save, Blinded
- Spell Attack: None
- filter-Level: 8
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Holy Aura","level":"8","payload":"{\"type\":\"Spell\",\"name\":\"Holy Aura\",\"description\":\"For the duration, you emit an aura in a 30-foot Emanation. While in the aura, creatures of your choice have Advantage on all saving throws, and other creatures have Disadvantage on attack rolls against them. In addition, when a Fiend or an Undead hits an affected creature with a melee attack roll, the attacker must succeed on a Constitution saving throw or have the Blinded condition until the end of its next turn.\",\"level\":8,\"school\":\"Abjuration\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a reliquary worth 1,000+ GP\"},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"30 foot\"}}"},{"name":"Holy Aura Condition","parent":"Holy Aura","payload":"{\"type\":\"Condition\",\"name\":\"Holy Aura\",\"description\":\"For the duration, you emit an aura in a 30-foot Emanation.\"}"},{"name":"Holy Aura Save Advantages","parent":"Holy Aura Condition","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Saving Throws\"],\"bonusName\":[\"Strength\",\"Dexitery\",\"Constitution\",\"Intelligence\",\"Wisdom\",\"Charisma\"],\"bonusDetails\":\"Keep Highest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"Advantage on all saving throws.\"}"},{"name":"Holy Aura Fiend Undead Attack","parent":"Holy Aura","payload":"{\"type\":\"Attack\",\"name\":\"Holy Aura - Fiend or Undead\",\"description\":\"When a Fiend or an Undead hits an affected creature with a melee attack roll, the attacker must succeed on a Constitution saving throw or have the Blinded condition until the end of its next turn.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Have the Blinded condition until the end of its next turn.\"},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"30-foot\"}}"}]
- filter-Components: Verbal, Somatic, Material (Cost)
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Holy Aura
- data-description: For the duration, you emit an aura in a 30-foot Emanation. While in the aura, creatures of your choice have Advantage on all saving throws, and other creatures have Disadvantage on attack rolls against them. In addition, when a Fiend or an Undead hits an affected creature with a melee attack roll, the attacker must succeed on a Constitution saving throw or have the Blinded condition until the end of its next turn.
- Level: 8
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: Self
- Components: V S M
- Material: a reliquary worth 1,000+ GP
- data-CastNum: 2
- Save: Constitution
- data-RangeAoe: Self (30 ft ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

