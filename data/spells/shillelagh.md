# Shillelagh

**description**: Transmutation Cantrip (Druid) Casting Time: Bonus Action Range: Self Components: V, S, M (mistletoe) Duration: 1 minute A Club or Quarterstaff you are holding is imbued with nature’s power. For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon’s damage die becomes a d8. If the attack deals damage, it can be Force damage or the weapon’s normal damage type (your choice). The spell ends early if you cast it again or if you let go of the weapon. Cantrip Upgrade. The damage die changes when you reach levels 5 (d10), 11 (d12), and 17 (2d6).

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Buff
- Spell Attack: Melee
- filter-Level: Cantrip
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Shillelagh","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Shillelagh\",\"description\":\"A Club or Quarterstaff you are holding is imbued with nature's power. For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon's damage die becomes a d8. If the attack deals damage, it can be Force damage or the weapon's normal damage type (your choice).\\nThe spell ends early if you cast it again or if you let go of the weapon.\",\"upcastText\":\"Cantrip Upgrade. The damage die changes when you reach levels 5 (d10), 11 (d12), and 17 (2d6).\",\"level\":0,\"school\":\"Transmutation\",\"castingTime\":\"Bonus Action\",\"range\":\"Self\",\"duration\":\"1 minute\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"mistletoe\"}}"},{"name":"Shillelagh Condition","parent":"Shillelagh","payload":"{\"type\":\"Condition\",\"name\":\"Shillelagh\",\"description\":\"A Club or Quarterstaff you are holding is imbued with nature's power.\"}"},{"name":"Shillelagh Attack","parent":"Shillelagh","payload":"{\"type\":\"Attack\",\"name\":\"Shillelagh\",\"description\":\"For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon's damage die becomes a d8. If the attack deals damage, it can be Force damage or the weapon's normal damage type (your choice).\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Shillelagh Damage","parent":"Shillelagh Attack","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"damageType\":\"Bludgeoning or Force\",\"diceSize\":\"d8\"}"},{"name":"Shillelagh Damage Upcast 5","parent":"Shillelagh Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceSize\",\"value\":\"d10\",\"changeMode\":\"Override\"}"},{"name":"Shillelagh Damage Upcast 11","parent":"Shillelagh Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceSize\",\"value\":\"d12\",\"changeMode\":\"Override\"}"},{"name":"Shillelagh Damage Dice Size Upcast 17","parent":"Shillelagh Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceSize\",\"value\":\"d6\",\"changeMode\":\"Override\"}"},{"name":"Shillelagh Damage Dice Amount Upcast 17","parent":"Shillelagh Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Override\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Bonus Action
- filter-Concentration: No
- Name: Shillelagh
- data-description: A Club or Quarterstaff you are holding is imbued with nature's power. For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon's damage die becomes a d8. If the attack deals damage, it can be Force damage or the weapon's normal damage type (your choice).
The spell ends early if you cast it again or if you let go of the weapon.
- Level: 0
- Casting Time: Bonus Action
- Duration: 1 minute
- Range: Self
- Components: V S M
- Material: mistletoe
- Higher Spell Slot Desc: Cantrip Upgrade. The damage die changes when you reach levels 5 (d10), 11 (d12), and 17 (2d6).
- data-DurationNum: 4
- data-AttackType: Spell Attack
- Damage: 1d8
- Damage Type: Bludgeoning or Force

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

