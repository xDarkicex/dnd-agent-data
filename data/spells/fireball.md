# Fireball

**description**: Level 3 Evocation (Sorcerer, Wizard) Casting Time: Action Range: 150 feet Components: V, S, M (a ball of bat guano and sulfur) Duration: Instantaneous A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 8d6 Fire damage on a failed save or half as much damage on a successful one. Flammable objects in the area that aren’t being worn or carried start burning. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Fire Damage
- Spell Attack: None
- filter-Level: 3
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Fireball","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Fireball\",\"description\":\"A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 8d6 Fire damage on a failed save or half as much damage on a successful one.\\nFlammable objects in the area that aren't being worn or carried start burning.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.\",\"level\":3,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"150 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a ball of bat guano and sulfur\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Fireball Attack","parent":"Fireball","payload":"{\"type\":\"Attack\",\"name\":\"Fireball\",\"range\":\"150 feet\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 8d6 Fire damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"},\"actionType\":\"Action\"}"},{"name":"Fireball Damage","parent":"Fireball Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":8,\"diceSize\":\"d6\"}"},{"name":"Fireball Damage Upcast","parent":"Fireball Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Fireball
- data-description: A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 8d6 Fire damage on a failed save or half as much damage on a successful one.
Flammable objects in the area that aren't being worn or carried start burning.
- Level: 3
- Casting Time: Action
- Duration: Instantaneous
- Range: 150 feet
- Components: V S M
- Material: a ball of bat guano and sulfur
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 150
- Save: Dexterity
- Damage: 8d6
- Damage Type: Fire
- data-RangeAoe: 150 ft (20 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

