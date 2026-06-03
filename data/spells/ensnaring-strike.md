# Ensnaring Strike

**description**: Level 1 Conjuration (Ranger) Casting Time: Bonus Action, which you take immediately after hitting a creature with a weapon Range: Self Components: V Duration: Concentration, up to 1 minute As you hit the target, grasping vines appear on it, and it makes a Strength saving throw. A Large or larger creature has Advantage on this save. On a failed save, the target has the Restrained condition until the spell ends. On a successful save, the vines shrivel away, and the spell ends. While Restrained, the target takes 1d6 Piercing damage at the start of each of its turns. The target or a creature within reach of it can take an action to make a Strength (Athletics) check against your spell save DC. On a success, the spell ends. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Ranger
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Condition, Strength Save, Restrained, Piercing Damage
- Spell Attack: None
- filter-Level: 1
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Ensnaring Strike","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Ensnaring Strike\",\"description\":\"Bonus Action, which you take immediately after hitting a creature with a weapon. As you hit the target, grasping vines appear on it, and it makes a Strength saving throw. A Large or larger creature has Advantage on this save. On a failed save, the target has the Restrained condition until the spell ends. On a successful save, the vines shrivel away, and the spell ends.\\nWhile Restrained, the target takes 1d6 Piercing damage at the start of each of its turns. The target or a creature within reach of it can take an action to make a Strength (Athletics) check against your spell save DC. On a success, the spell ends.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.\",\"level\":1,\"school\":\"Conjuration\",\"castingTime\":\"Bonus Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true}}"},{"name":"Ensnaring Strike Attack","parent":"Ensnaring Strike","payload":"{\"type\":\"Attack\",\"name\":\"Ensnaring Strike\",\"description\":\"As you hit the target, grasping vines appear on it, and it makes a Strength saving throw. A Large or larger creature has Advantage on this save.\",\"save\":{\"saveAbility\":\"Strength\",\"onFail\":\"Target has the Restrained condition until the spell ends.\",\"onSucceed\":\"Spell ends.\"},\"actionType\":\"Bonus Action\"}"},{"name":"Ensnaring Strike Restrained Condition","parent":"Ensnaring Strike","payload":"{\"type\":\"Condition\",\"name\":\"Ensnaring Strike - Restrained\",\"description\":\"While Restrained, the target takes 1d6 Piercing damage at the start of each of its turns. The target or a creature within reach of it can take an action to make a Strength (Athletics) check against your spell save DC. On a success, the spell ends.\"}"},{"name":"Ensnaring Strike Restrained Attack","parent":"Ensnaring Strike","payload":"{\"type\":\"Attack\",\"name\":\"Ensnaring Strike - Restrained\",\"autoHit\":true,\"description\":\"While Restrained, the target takes 1d6 Piercing damage at the start of each of its turns. The target or a creature within reach of it can take an action to make a Strength (Athletics) check against your spell save DC. On a success, the spell ends.\",\"actionType\":\"Free Action\"}"},{"name":"Ensnaring Strike Restrained Damage","parent":"Ensnaring Strike Restrained Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Piercing\",\"diceCount\":1,\"diceSize\":\"d6\"}"},{"name":"Ensnaring Strike Restrained Damage Upcast","parent":"Ensnaring Strike Restrained Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal
- filter-Casting Time: Bonus Action
- filter-Concentration: Yes
- Name: Ensnaring Strike
- data-description: Bonus Action, which you take immediately after hitting a creature with a weapon. As you hit the target, grasping vines appear on it, and it makes a Strength saving throw. A Large or larger creature has Advantage on this save. On a failed save, the target has the Restrained condition until the spell ends. On a successful save, the vines shrivel away, and the spell ends.
While Restrained, the target takes 1d6 Piercing damage at the start of each of its turns. The target or a creature within reach of it can take an action to make a Strength (Athletics) check against your spell save DC. On a success, the spell ends.
- Level: 1
- Casting Time: Bonus Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: Self
- Components: V
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.
- Save: Strength
- Damage: 1d6
- Damage Type: Piercing

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

