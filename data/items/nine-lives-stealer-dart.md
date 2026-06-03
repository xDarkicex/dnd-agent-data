# Nine Lives Stealer Dart

**description**: Weapon (Dart), Very Rare (Requires Attunement) You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Life Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.

**properties**:
- Category: Items
- Theme: Armaments
- Mastery: Piercing
- Subtype: Weapon
- Expansion: 33335
- Item Type: simple
- data-List: false
- Properties: Thrown
- Item Rarity: Yes
- filter-Lists: Ranged Weapon, Simple Weapon, Yes
- filter-Damage: Finesse
- filter-Charges: Multiple Uses
- data-datarecords: [{"name":"Nine Lives Stealer Dart","payload":"{\"type\":\"Item\",\"name\":\"Nine Lives Stealer Dart\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\\nLife Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.\",\"weight\":0.25,\"properties\":[\"Finesse\",\"Thrown\"],\"cost\":\"40000 GP\",\"rarity\":\"Very Rare\",\"weaponData\":{\"category\":\"Ranged\",\"training\":\"Simple\",\"type\":\"Dart\"},\"equipData\":{\"equippable\":true}}"},{"name":"Nine Lives Stealer Dart Attack","parent":"Nine Lives Stealer Dart","payload":"{\"type\":\"Attack\",\"name\":\"Nine Lives Stealer Dart\",\"range\":\"20/60\",\"onHitDisplay\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must make a DC 15 Constitution saving throw.\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\",\"attack\":{\"type\":\"Ranged\",\"abilityBonus\":\"Dexterity\",\"bonus\":2}}"},{"name":"Nine Lives Stealer Dart Damage","parent":"Nine Lives Stealer Dart Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"bonus\":2,\"damageType\":\"Piercing\",\"diceSize\":\"d4\"}"},{"name":"Nine Lives Stealer Dart (STR) Attack","parent":"Nine Lives Stealer Dart","payload":"{\"type\":\"Attack\",\"name\":\"Nine Lives Stealer Dart (Finesse)\",\"range\":\"20/60\",\"onHitDisplay\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must make a DC 15 Constitution saving throw.\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\",\"attack\":{\"type\":\"Ranged\",\"abilityBonus\":\"Strength\",\"bonus\":2}}"},{"name":"Nine Lives Stealer Dart (STR) Damage","parent":"Nine Lives Stealer Dart (STR) Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"bonus\":2,\"damageType\":\"Piercing\",\"diceSize\":\"d4\"}"},{"name":"Nine Lives Stealer Dart Attunement","parent":"Nine Lives Stealer Dart","payload":"{\"type\":\"Attunement\",\"requireEquip\":true}"},{"name":"Nine Lives Stealer Dagger Life Stealing Resource","parent":"Nine Lives Stealer Dart Attunement","payload":"{\"type\":\"Resource\",\"name\":\"Life Stealing\",\"value\":\"full\",\"maxValueFormula\":{\"flatValue\":9},\"recoveryRate\":{\"Other\":{\"type\":\"None\"}}}"},{"name":"Nine Lives Stealer Dart Life Stealing Save","parent":"Nine Lives Stealer Dart Life Stealing Resource","use":"Nine Lives Stealer Dagger Life Stealing Resource","payload":"{\"type\":\"Attack\",\"name\":\"Life Stealing Save\",\"description\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically.\",\"save\":{\"saveAbility\":\"Constitution\",\"saveFlat\":15,\"onFail\":\"The creature is slain instantly.\"}}"}]
- filter-Attunement: Very Rare
- filter-Consumable: Vex
- Name: Nine Lives Stealer Dart
- Weight: 0.25
- data-description: You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.
Life Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.
- Range: 20/60
- Damage: 1d4
- Damage Type: Piercing
- data-RarityNum: 0

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

