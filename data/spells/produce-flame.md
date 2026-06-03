# Produce Flame

**description**: Conjuration Cantrip (Druid) Casting Time: Bonus Action Range: Self Components: V, S Duration: 10 minutes A flickering flame appears in your hand and remains there for the duration. While there, the flame emits no heat and ignites nothing, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet. The spell ends if you cast it again. Until the spell ends, you can take a Magic action to hurl fire at a creature or an object within 60 feet of you. Make a ranged spell attack. On a hit, the target takes 1d8 Fire damage. Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Fire Damage
- Spell Attack: Ranged
- filter-Level: Cantrip
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 10 min
- data-datarecords: [{"name":"Produce Flame","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Produce Flame\",\"description\":\"A flickering flame appears in your hand and remains there for the duration. While there, the flame emits no heat and ignites nothing, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet. The spell ends if you cast it again.\\nUntil the spell ends, you can take a Magic action to hurl fire at a creature or an object within 60 feet of you. Make a ranged spell attack. On a hit, the target takes 1d8 Fire damage.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).\",\"level\":0,\"school\":\"Conjuration\",\"castingTime\":\"Bonus Action\",\"range\":\"Self\",\"duration\":\"10 minutes\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Produce Flame Attack","parent":"Produce Flame","payload":"{\"type\":\"Attack\",\"name\":\"Produce Flame\",\"range\":\"60 feet\",\"description\":\"You can take a Magic action to hurl fire at a creature or an object within 60 feet of you. Make a ranged spell attack. On a hit, the target takes 1d8 Fire damage.\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Produce Flame Damage","parent":"Produce Flame Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceSize\":\"d8\"}"},{"name":"Produce Flame Damage Upcast 5","parent":"Produce Flame Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Produce Flame Damage Upcast 11","parent":"Produce Flame Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Produce Flame Damage Upcast 17","parent":"Produce Flame Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Bonus Action
- filter-Concentration: No
- Name: Produce Flame
- data-description: A flickering flame appears in your hand and remains there for the duration. While there, the flame emits no heat and ignites nothing, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet. The spell ends if you cast it again.
Until the spell ends, you can take a Magic action to hurl fire at a creature or an object within 60 feet of you. Make a ranged spell attack. On a hit, the target takes 1d8 Fire damage.
- Level: 0
- Casting Time: Bonus Action
- Duration: 10 minutes
- Range: Self
- Components: V S
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
- data-DurationNum: 6
- data-AttackType: Spell Attack
- Damage: 1d8
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

