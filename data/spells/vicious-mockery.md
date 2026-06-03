# Vicious Mockery

**description**: Enchantment Cantrip (Bard) Casting Time: Action Range: 60 feet Components: V Duration: Instantaneous You unleash a string of insults laced with subtle enchantments at one creature you can see or hear within range. The target must succeed on a Wisdom saving throw or take 1d6 Psychic damage and have Disadvantage on the next attack roll it makes before the end of its next turn. Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).

**properties**:
- Category: Spells
- School: Enchantment
- Classes: Bard
- Expansion: 33335
- data-List: false
- filter-Tags: Wisdom Save, Inflict Damage, Debuff, Psychic Damage
- Spell Attack: None
- filter-Level: Cantrip
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Vicious Mockery","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Vicious Mockery\",\"description\":\"You unleash a string of insults laced with subtle enchantments at one creature you can see or hear within range. The target must succeed on a Wisdom saving throw or take 1d6 Psychic damage and have Disadvantage on the next attack roll it makes before the end of its next turn.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).\",\"level\":0,\"school\":\"Enchantment\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true}}"},{"name":"Vicious Mockery Attack","parent":"Vicious Mockery","payload":"{\"type\":\"Attack\",\"name\":\"Vicious Mockery\",\"description\":\"The target must succeed on a Wisdom saving throw.\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Take 1d6 Psychic damage and have Disadvantage on the next attack roll it makes before the end of its next turn.\"},\"actionType\":\"Action\"}"},{"name":"Vicious Mockery Damage","parent":"Vicious Mockery Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Psychic\",\"diceSize\":\"d6\"}"},{"name":"Vicious Mockery Damage Upcast 5","parent":"Vicious Mockery Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Vicious Mockery Damage Upcast 11","parent":"Vicious Mockery Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Vicious Mockery Damage Upcast 17","parent":"Vicious Mockery Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Vicious Mockery
- data-description: You unleash a string of insults laced with subtle enchantments at one creature you can see or hear within range. The target must succeed on a Wisdom saving throw or take 1d6 Psychic damage and have Disadvantage on the next attack roll it makes before the end of its next turn.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Wisdom
- Damage: 1d6
- Damage Type: Psychic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

