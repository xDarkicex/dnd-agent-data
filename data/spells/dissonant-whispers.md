# Dissonant Whispers

**description**: Level 1 Enchantment (Bard) Casting Time: Action Range: 60 feet Components: V Duration: Instantaneous One creature of your choice that you can see within range hears a discordant melody in its mind. The target makes a Wisdom saving throw. On a failed save, it takes 3d6 Psychic damage and must immediately use its Reaction, if available, to move as far away from you as it can, using the safest route. On a successful save, the target takes half as much damage only. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Enchantment
- Classes: Bard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Wisdom Save, Psychic Damage
- Spell Attack: None
- filter-Level: 1
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Dissonant Whispers","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Dissonant Whispers\",\"description\":\"One creature of your choice that you can see within range hears a discordant melody in its mind. The target makes a Wisdom saving throw. On a failed save, it takes 3d6 Psychic damage and must immediately use its Reaction, if available, to move as far away from you as it can, using the safest route. On a successful save, the target takes half as much damage only.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.\",\"level\":1,\"school\":\"Enchantment\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true}}"},{"name":"Dissonant Whispers Attack","parent":"Dissonant Whispers","payload":"{\"type\":\"Attack\",\"name\":\"Dissonant Whispers\",\"range\":\"60 feet\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"Takes 3d6 Psychic damage and must immediately use its Reaction, if available, to move as far away from you as it can, using the safest route.\",\"onSucceed\":\"Half as much damage only.\"},\"actionType\":\"Action\"}"},{"name":"Dissonant Whispers Damage","parent":"Dissonant Whispers Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Psychic\",\"diceCount\":3,\"diceSize\":\"d6\"}"},{"name":"Dissonant Whispers Damage Upcast","parent":"Dissonant Whispers Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Dissonant Whispers
- data-description: One creature of your choice that you can see within range hears a discordant melody in its mind. The target makes a Wisdom saving throw. On a failed save, it takes 3d6 Psychic damage and must immediately use its Reaction, if available, to move as far away from you as it can, using the safest route. On a successful save, the target takes half as much damage only.
- Level: 1
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Wisdom
- Damage: 3d6
- Damage Type: Psychic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

