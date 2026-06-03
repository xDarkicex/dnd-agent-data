# Sacred Flame

**description**: Evocation Cantrip (Cleric) Casting Time: Action Range: 60 feet Components: V, S Duration: Instantaneous Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 Radiant damage. The target gains no benefit from Half Cover or Three-Quarters Cover for this save. Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).

**properties**:
- Category: Spells
- School: Evocation
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Dexterity Save, Radiant Damage
- Spell Attack: None
- filter-Level: Cantrip
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Sacred Flame","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Sacred Flame\",\"description\":\"Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 Radiant damage. The target gains no benefit from Half Cover or Three-Quarters Cover for this save.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).\",\"level\":0,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Sacred Flame Attack","parent":"Sacred Flame","payload":"{\"type\":\"Attack\",\"name\":\"Sacred Flame\",\"range\":\"60 feet\",\"description\":\"The target must succeed on a Dexterity saving throw or take 1d8 Radiant damage. The target gains no benefit from Half Cover or Three-Quarters Cover for this save.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"The target takes 1d8 Radiant damage.\"},\"actionType\":\"Action\"}"},{"name":"Sacred Flame Damage","parent":"Sacred Flame Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceSize\":\"d8\"}"},{"name":"Sacred Flame Damage Upcast 5","parent":"Sacred Flame Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Sacred Flame Damage Upcast 11","parent":"Sacred Flame Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Sacred Flame Damage Upcast 17","parent":"Sacred Flame Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Sacred Flame
- data-description: Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 Radiant damage. The target gains no benefit from Half Cover or Three-Quarters Cover for this save.
- Level: 0
- Casting Time: Action
- Duration: Instantaneous
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- Save: Dexterity
- Damage: 1d8
- Damage Type: Radiant

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

