# Nine Lives Stealer Lance

**description**: Weapon (Lance), Very Rare (Requires Attunement) You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Life Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.

**properties**:
- Category: Items
- Theme: Armaments
- Mastery: Piercing
- Subtype: Weapon
- Expansion: 33335
- Item Type: martial
- data-List: false
- Properties: Two-Handed (unless mounted)
- Item Rarity: Yes
- filter-Lists: Melee Weapon, Martial Weapon, Yes
- filter-Damage: Reach
- filter-Charges: Multiple Uses
- data-datarecords: [{"name":"Nine Lives Stealer Lance","payload":"{\"type\":\"Item\",\"name\":\"Nine Lives Stealer Lance\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\\nLife Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.\",\"weight\":6,\"properties\":[\"Reach\",\"Special\"],\"cost\":\"40010 GP\",\"rarity\":\"Very Rare\",\"weaponData\":{\"category\":\"Melee\",\"training\":\"Martial\",\"type\":\"Lance\"},\"equipData\":{\"equippable\":true}}"},{"name":"Nine Lives Stealer Lance Attack","parent":"Nine Lives Stealer Lance","payload":"{\"type\":\"Attack\",\"name\":\"Nine Lives Stealer Lance\",\"onHitDisplay\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must make a DC 15 Constitution saving throw.\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\",\"attack\":{\"type\":\"Melee\",\"abilityBonus\":\"Strength\",\"bonus\":2}}"},{"name":"Nine Lives Stealer Lance Damage","parent":"Nine Lives Stealer Lance Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"bonus\":2,\"damageType\":\"Piercing\",\"diceSize\":\"d10\"}"},{"name":"Nine Lives Stealer Lance Attunement","parent":"Nine Lives Stealer Lance","payload":"{\"type\":\"Attunement\",\"requireEquip\":true}"},{"name":"Nine Lives Stealer Lance Life Stealing Resource","parent":"Nine Lives Stealer Lance Attunement","payload":"{\"type\":\"Resource\",\"name\":\"Life Stealing\",\"value\":\"full\",\"maxValueFormula\":{\"flatValue\":9},\"recoveryRate\":{\"Other\":{\"type\":\"None\"}}}"},{"name":"Nine Lives Stealer Lance Life Stealing Save","parent":"Nine Lives Stealer Lance Life Stealing Resource","use":"Nine Lives Stealer Lance Life Stealing Resource","payload":"{\"type\":\"Attack\",\"name\":\"Life Stealing Save\",\"description\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically.\",\"save\":{\"saveAbility\":\"Constitution\",\"saveFlat\":15,\"onFail\":\"The creature is slain instantly.\"}}"}]
- filter-Attunement: Very Rare
- filter-Consumable: Topple
- Name: Nine Lives Stealer Lance
- Weight: 6
- data-description: You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.
Life Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.
- Damage: 1d10
- Damage Type: Piercing
- data-RarityNum: 0

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

