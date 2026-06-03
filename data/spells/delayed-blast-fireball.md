# Delayed Blast Fireball

**description**: Level 7 Evocation (Sorcerer, Wizard) Casting Time: Action Range: 150 feet Components: V, S, M (a ball of bat guano and sulfure) Duration: Concentration, up to 1 minute A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one. The spell’s base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn’t ended. If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature’s space or collides with a solid object, the spell ends, and the bead explodes. When the bead explodes, flammable objects in the explosion that aren’t being worn or carried start burning. Using a Higher-Level Spell Slot. The base damage increases by 1d6 for each spell slot level above 7.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Fire Damage
- Spell Attack: None
- filter-Level: 7
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Delayed Blast Fireball","level":"7","payload":"{\"type\":\"Spell\",\"name\":\"Delayed Blast Fireball\",\"description\":\"A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.\\nThe spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.\\nIf a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.\\nWhen the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The base damage increases by 1d6 for each spell slot level above 7.\",\"level\":7,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"150 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a ball of bat guano and sulfur\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Delayed Blast Fireball Condition","parent":"Delayed Blast Fireball","payload":"{\"type\":\"Condition\",\"name\":\"Delayed Blast Fireball\",\"description\":\"A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw.\"}"},{"name":"Delayed Blast Fireball Attack Explosion","parent":"Delayed Blast Fireball","payload":"{\"type\":\"Attack\",\"name\":\"Delayed Blast Fireball Explosion\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes Fire damage equal to the total accumulated damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Delayed Blast Fireball Attack Touched","parent":"Delayed Blast Fireball","payload":"{\"type\":\"Attack\",\"name\":\"Delayed Blast Fireball Touched\",\"description\":\"If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Spell ends, causing the bead to explode.\",\"onSucceed\":\"The creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.\"}}"},{"name":"Delayed Blast Fireball Damage","parent":"Delayed Blast Fireball Attack Explosion","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":12,\"diceSize\":\"d6\"}"},{"name":"Delayed Blast Fireball Damage Upcast","parent":"Delayed Blast Fireball Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":8,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Delayed Blast Fireball Extra Damage","parent":"Delayed Blast Fireball Attack Explosion","payload":"{\"type\":\"Effect\",\"name\":\"Delayed Blast Fireball Additional Damage\",\"description\":\"The damage increases by 1d6 whenever your turn ends and the spell hasn't ended.\",\"category\":[\"Damage\"],\"diceValue\":\"1d6\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Delayed Blast Fireball
- data-description: A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.
The spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.
If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.
- Level: 7
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 150 feet
- Components: V S M
- Material: a ball of bat guano and sulfur
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The base damage increases by 1d6 for each spell slot level above 7.
- data-CastNum: 2
- data-RangeNum: 150
- Save: Dexterity
- Damage: 12d6
- Damage Type: Fire
- data-RangeAoe: 150 ft (20 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

