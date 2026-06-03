# Oathbow Shortbow

**description**: Weapon (Shortbow), Very Rare (Requires Attunement) When you nock an arrow on this bow, it whispers in Elvish, “Swift defeat to my enemies.” When you use this weapon to make a ranged attack, you can utter or sign the following command words: “Swift death to you who have wronged me.” The target of your attack becomes your sworn enemy until it dies or until dawn 7 days later. You can have only one such sworn enemy at a time. When your sworn enemy dies, you can choose a new one after the next dawn. When you make a ranged attack roll with this weapon against your sworn enemy, you have Advantage on the roll. In addition, your target gains no benefit from Half Cover or Three-Quarters Cover, and you suffer no Disadvantage due to long range. If the attack hits, your sworn enemy takes an extra 3d6 Piercing damage. While your sworn enemy lives, you have Disadvantage on attack rolls with all other weapons.

**properties**:
- Category: Items
- Theme: Armaments
- Mastery: Piercing
- Subtype: Weapon
- Expansion: 33335
- Item Type: simple
- data-List: false
- Properties: Two-Handed
- Item Rarity: No
- filter-Lists: Ranged Weapon, Simple Weapon, Yes
- filter-Damage: Ammunition
- filter-Charges: No
- data-datarecords: [{"name":"Oathbow Shortbow","payload":"{\"type\":\"Item\",\"name\":\"Oathbow Shortbow\",\"description\":\"When you nock an arrow on this bow, it whispers in Elvish, 'Swift defeat to my enemies.' When you use this weapon to make a ranged attack, you can utter or sign the following command words: 'Swift death to you who have wronged me.' The target of your attack becomes your sworn enemy until it dies or until dawn 7 days later. You can have only one such sworn enemy at a time. When your sworn enemy dies, you can choose a new one after the next dawn. When you make a ranged attack roll with this weapon against your sworn enemy, you have Advantage on the roll. In addition, your target gains no benefit from Half Cover or Three-Quarters Cover, and you suffer no Disadvantage due to long range. If the attack hits, your sworn enemy takes an extra 3d6 Piercing damage. While your sworn enemy lives, you have Disadvantage on attack rolls with all other weapons.\",\"weight\":2,\"properties\":[\"Ammunition\",\"Two-Handed\"],\"cost\":\"40025 GP\",\"rarity\":\"Very Rare\",\"weaponData\":{\"category\":\"Ranged\",\"training\":\"Simple\",\"type\":\"Shortbow\"},\"equipData\":{\"equippable\":true}}"},{"name":"Oathbow Shortbow Attack","parent":"Oathbow Shortbow","payload":"{\"type\":\"Attack\",\"name\":\"Oathbow Shortbow\",\"range\":\"80/320\",\"description\":\"When you use this weapon to make a ranged attack, you can utter or sign the following command words: 'Swift death to you who have wronged me.' The target of your attack becomes your sworn enemy until it dies or until dawn 7 days later. You can have only one such sworn enemy at a time.\",\"attack\":{\"type\":\"Ranged\",\"abilityBonus\":\"Dexterity\"},\"actionType\":\"Action\"}"},{"name":"Oathbow Shortbow Damage","parent":"Oathbow Shortbow Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"bonus\":\"0\",\"damageType\":\"Piercing\",\"diceSize\":\"d6\"}"},{"name":"Oathbow Shortbow Attunement","parent":"Oathbow Shortbow","payload":"{\"type\":\"Attunement\",\"requireEquip\":true}"},{"name":"Oathbow Shortbow Sworn Enemy Effect","parent":"Oathbow Shortbow Attunement","payload":"{\"type\":\"Effect\",\"name\":\"Sworn Enemy (Oathbow)\",\"description\":\"When you make a ranged attack roll with this weapon against your sworn enemy, you have Advantage on the roll. In addition, your target gains no benefit from Half Cover or Three-Quarters Cover, and you suffer no Disadvantage due to long range. If the attack hits, your sworn enemy takes an extra 3d6 Piercing damage. While your sworn enemy lives, you have Disadvantage on attack rolls with all other weapons.\",\"category\":[]}"},{"name":"Oathbow Shortbow Advantage vs Sworn Enemy","parent":"Oathbow Shortbow Sworn Enemy Effect","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Attacks\"],\"bonusName\":[],\"bonusDetails\":\"Keep Highest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"When you make a ranged attack roll with the Oathbow against your sworn enemy, you have Advantage on the roll.\"}"},{"name":"Oathbow Shortbow Disadvantage with Other Weapons","parent":"Oathbow Shortbow Sworn Enemy Effect","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Attacks\"],\"bonusName\":[],\"bonusDetails\":\"Keep Lowest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"While your sworn enemy lives, you have Disadvantage on attack rolls with all weapons besides the Oathbow.\"}"},{"name":"Oathbow Longbow Extra Damage vs Sworn Enemy Effect","parent":"Oathbow Shortbow Sworn Enemy Effect","payload":"{\"type\":\"Effect\",\"name\":\"Extra Damage against Sworn Enemy\",\"description\":\"When you make a ranged attack roll with this weapon against your sworn enemy and the attack hits, your sworn enemy takes an extra 3d6 Piercing damage.\",\"category\":[\"Damage\"],\"diceValue\":\"3d6\",\"situation\":\"Ranged attacks with the Oathbow against your Sworn Enemy deal an extra 3d6 piercing damage.\"}"}]
- filter-Attunement: Very Rare
- filter-Consumable: Vex
- Name: Oathbow Shortbow
- Weight: 2
- data-description: When you nock an arrow on this bow, it whispers in Elvish, 'Swift defeat to my enemies.' When you use this weapon to make a ranged attack, you can utter or sign the following command words: 'Swift death to you who have wronged me.' The target of your attack becomes your sworn enemy until it dies or until dawn 7 days later. You can have only one such sworn enemy at a time. When your sworn enemy dies, you can choose a new one after the next dawn. When you make a ranged attack roll with this weapon against your sworn enemy, you have Advantage on the roll. In addition, your target gains no benefit from Half Cover or Three-Quarters Cover, and you suffer no Disadvantage due to long range. If the attack hits, your sworn enemy takes an extra 3d6 Piercing damage. While your sworn enemy lives, you have Disadvantage on attack rolls with all other weapons.
- Range: 80/320
- Damage: 1d6
- Damage Type: Piercing
- data-RarityNum: 0

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

