# Searing Smite

**description**: Level 1 Evocation (Paladin) Casting Time: Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike Range: Self Component: V Duration: 1 minute As you hit the target, it takes an extra 1d6 Fire damage from the attack. At the start of each of its turns until the spell ends, the target takes 1d6 Fire damage and then makes a Constitution saving throw. On a failed save, the spell continues. On a successful save, the spell ends. Using a Higher-Level Spell Slot. All the damage increases by 1d6 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Paladin
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Fire Damage, Constitution Save
- Spell Attack: Melee
- filter-Level: 1
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Searing Smite","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Searing Smite\",\"description\":\"Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike. As you hit the target, it takes an extra 1d6 Fire damage from the attack. At the start of each of its turns until the spell ends, the target takes 1d6 Fire damage and then makes a Constitution saving throw. On a failed save, the spell continues. On a successful save, the spell ends.\",\"upcastText\":\"Using a Higher-Level Spell Slot. All the damage increases by 1d6 for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Bonus Action\",\"range\":\"Self\",\"duration\":\"1 minute\",\"components\":{\"verbal\":true}}"},{"name":"Searing Smite Attack","parent":"Searing Smite","payload":"{\"type\":\"Attack\",\"name\":\"Searing Smite\",\"autoHit\":true,\"description\":\"As you hit the target, it takes an extra 1d6 Fire damage from the attack. At the start of each of its turns until the spell ends, the target takes 1d6 Fire damage and then makes a Constitution saving throw. On a failed save, the spell continues. On a successful save, the spell ends.\",\"save\":{\"saveAbility\":\"Constitution\"},\"actionType\":\"Bonus Action\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Searing Smite Damage","parent":"Searing Smite Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceSize\":\"d6\"}"},{"name":"Searing Smite Damage Upcast","parent":"Searing Smite Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal
- filter-Casting Time: Bonus Action
- filter-Concentration: No
- Name: Searing Smite
- data-description: Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike. As you hit the target, it takes an extra 1d6 Fire damage from the attack. At the start of each of its turns until the spell ends, the target takes 1d6 Fire damage and then makes a Constitution saving throw. On a failed save, the spell continues. On a successful save, the spell ends.
- Level: 1
- Casting Time: Bonus Action
- Duration: 1 minute
- Range: Self
- Components: V
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. All the damage increases by 1d6 for each spell slot level above 1.
- data-DurationNum: 4
- Save: Constitution
- data-AttackType: Spell Attack
- Damage: 1d6
- Damage Type: Fire

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

