# Flame Blade

**description**: Level 2 Evocation (Druid, Sorcerer) Casting Time: Bonus Action Range: Self Components: V, S, M (a sumac leaf) Duration: Concentration, up to 10 minutes You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. If you let go of the blade, it disappears, but you can evoke it again as a Bonus Action. As a Magic action, you can make a melee spell attack with the fiery blade. On a hit, the target takes Fire damage equal to 3d6 plus your spellcasting ability modifier. The flaming blade sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Druid, Sorcerer
- Expansion: 33335
- data-List: false
- filter-Tags: Buff, Fire Damage
- Spell Attack: Melee
- filter-Level: 2
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Flame Blade","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Flame Blade\",\"description\":\"You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. If you let go of the blade, it disappears, but you can evoke it again as a Bonus Action.\\nAs a Magic action, you can make a melee spell attack with the fiery blade. On a hit, the target takes Fire damage equal to 3d6 plus your spellcasting ability modifier.\\nThe flaming blade sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.\",\"level\":2,\"school\":\"Evocation\",\"castingTime\":\"Bonus Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a sumac leaf\"}}"},{"name":"Flame Blade Condition","parent":"Flame Blade","payload":"{\"type\":\"Condition\",\"name\":\"Flame Blade\",\"description\":\"You evoke a fiery blade in your free hand.\"}"},{"name":"Flame Blade Bonus Action","parent":"Flame Blade Condition","payload":"{\"type\":\"Action\",\"name\":\"Flame Blade - Evoke Again\",\"description\":\"If you let go of the blade, it disappears, but you can evoke it again as a Bonus Action.\",\"actionType\":\"Bonus Action\"}"},{"name":"Flame Blade Attack","parent":"Flame Blade","payload":"{\"type\":\"Attack\",\"name\":\"Flame Blade\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Action\"}"},{"name":"Flame Blade Damage","parent":"Flame Blade Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"damageType\":\"Fire\",\"diceCount\":3,\"diceSize\":\"d6\"}"},{"name":"Flame Blade Damage Upcast","parent":"Flame Blade Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Bonus Action
- filter-Concentration: Yes
- Name: Flame Blade
- data-description: You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. If you let go of the blade, it disappears, but you can evoke it again as a Bonus Action.
As a Magic action, you can make a melee spell attack with the fiery blade. On a hit, the target takes Fire damage equal to 3d6 plus your spellcasting ability modifier.
The flaming blade sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet.
- Level: 2
- Casting Time: Bonus Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: Self
- Components: V S M
- Material: a sumac leaf
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.
- data-AttackType: Spell Attack
- Damage: 3d6
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

