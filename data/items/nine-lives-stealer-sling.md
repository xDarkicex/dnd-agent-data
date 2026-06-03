# Nine Lives Stealer Sling

**description**: Weapon (Sling), Very Rare (Requires Attunement) You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. Life Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.

**properties**:
- Category: Items
- Theme: Armaments
- Mastery: Bludgeoning
- Subtype: Weapon
- Expansion: 33335
- Item Type: simple
- data-List: false
- Properties: Ammunition (Range 30/120; Bullet)
- Item Rarity: Yes
- filter-Lists: Ranged Weapon, Simple Weapon, Yes
- filter-Damage: Ammunition
- filter-Charges: Multiple Uses
- data-datarecords: [{"name":"Nine Lives Stealer Sling","payload":"{\"type\":\"Item\",\"name\":\"Nine Lives Stealer Sling\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\\nLife Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.\",\"weight\":\"\",\"properties\":[\"Ammunition\"],\"cost\":\"40000 GP\",\"rarity\":\"Very Rare\",\"weaponData\":{\"category\":\"Ranged\",\"training\":\"Simple\",\"type\":\"Sling\"},\"equipData\":{\"equippable\":true}}"},{"name":"Nine Lives Stealer Sling Attack","parent":"Nine Lives Stealer Sling","payload":"{\"type\":\"Attack\",\"name\":\"Nine Lives Stealer Sling\",\"range\":\"30/120\",\"onHitDisplay\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must make a DC 15 Constitution saving throw.\",\"description\":\"You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.\",\"attack\":{\"type\":\"Ranged\",\"abilityBonus\":\"Dexterity\",\"bonus\":2}}"},{"name":"Nine Lives Stealer Sling Damage","parent":"Nine Lives Stealer Sling Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"bonus\":2,\"damageType\":\"Bludgeoning\",\"diceSize\":\"d4\"}"},{"name":"Nine Lives Stealer Sling Attunement","parent":"Nine Lives Stealer Sling","payload":"{\"type\":\"Attunement\",\"requireEquip\":true}"},{"name":"Nine Lives Stealer Sling Life Stealing Resource","parent":"Nine Lives Stealer Sling Attunement","payload":"{\"type\":\"Resource\",\"name\":\"Life Stealing\",\"value\":\"full\",\"maxValueFormula\":{\"flatValue\":9},\"recoveryRate\":{\"Other\":{\"type\":\"None\"}}}"},{"name":"Nine Lives Stealer Sling Life Stealing Save","parent":"Nine Lives Stealer Sling Life Stealing Resource","use":"Nine Lives Stealer Sling Life Stealing Resource","payload":"{\"type\":\"Attack\",\"name\":\"Life Stealing Save\",\"description\":\"When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically.\",\"save\":{\"saveAbility\":\"Constitution\",\"saveFlat\":15,\"onFail\":\"The creature is slain instantly.\"}}"}]
- filter-Attunement: Very Rare
- filter-Consumable: Slow
- Name: Nine Lives Stealer Sling
- data-description: You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.
Life Stealing. The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 Hit Points with this weapon and roll a 20 on the d20 for the attack roll, the creature must succeed on a DC 15 Constitution saving throw or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.
- Range: 30/120
- Damage: 1d4
- Damage Type: Bludgeoning
- data-RarityNum: 0

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

