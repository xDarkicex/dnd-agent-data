# Divine Smite

**description**: Level 1 Evocation (Paladin) Casting Time: Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike Range: Self Components: V Duration: Instantaneous The target takes an extra 2d8 Radiant damage from the attack. The damage increases by 1d8 if the target is a Fiend or an Undead. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Paladin
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Radiant Damage
- Spell Attack: Melee
- filter-Level: 1
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Divine Smite","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Divine Smite\",\"description\":\"Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike. The target takes an extra 2d8 Radiant damage from the attack. The damage increases by 1d8 if the target is a Fiend or an Undead.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Bonus Action\",\"range\":\"Self\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true}}"},{"name":"Divine Smite Attack","parent":"Divine Smite","payload":"{\"type\":\"Attack\",\"name\":\"Divine Smite\",\"autoHit\":true,\"description\":\"The target takes an extra 2d8 Radiant damage from the attack. The damage increases by 1d8 if the target is a Fiend or an Undead.\",\"attack\":{\"type\":\"Spell Attack\"},\"actionType\":\"Bonus Action\"}"},{"name":"Divine Smite Damage","parent":"Divine Smite Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Radiant\",\"diceCount\":2,\"diceSize\":\"d8\"}"},{"name":"Divine Smite Damage Upcast","parent":"Divine Smite Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Divine Smite Fiend Or Undead Effect","parent":"Divine Smite Attack","payload":"{\"type\":\"Effect\",\"name\":\"Divine Smite - Fiend or Undead\",\"description\":\"The damage increases by 1d8 if the target is a Fiend or an Undead.\",\"category\":[\"Damage\"],\"diceValue\":\"1d8\"}"}]
- filter-Components: Verbal
- filter-Casting Time: Bonus Action
- filter-Concentration: No
- Name: Divine Smite
- data-description: Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike. The target takes an extra 2d8 Radiant damage from the attack. The damage increases by 1d8 if the target is a Fiend or an Undead.
- Level: 1
- Casting Time: Bonus Action
- Duration: Instantaneous
- Range: Self
- Components: V
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 1.
- data-DurationNum: 0
- data-AttackType: Spell Attack
- Damage: 2d8
- Damage Type: Radiant

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

