# Enlarge Reduce

**description**: Level 2 Transmutation (Bard, Druid, Sorcerer, Wizard) Casting Time: Action Range: 30 feet Components: V, S, M (a pinch of powdered iron) Duration: Concentration, up to 1 minute For the duration, the spell enlarges or reduces a creature or an object you can see within range (see the chosen effect below). A targeted object must be neither worn nor carried. If the target is an unwilling creature, it can make a Constitution saving throw. On a successful save, the spell has no effect. Everything that a targeted creature is wearing and carrying changes size with it. Any item it drops returns to normal size at once. A thrown weapon or piece of ammunition returns to normal size immediately after it hits or misses a target. Enlarge. The target’s size increases by one category—from Medium to Large, for example. The target also has Advantage on Strength checks and Strength saving throws. The target’s attacks with its enlarged weapons or Unarmed Strikes deal an extra 1d4 damage on a hit. Reduce. The target’s size decreases by one category—from Medium to Small, for example. The target also has Disadvantage on Strength checks and Strength saving throws. The target’s attacks with its reduced weapons or Unarmed Strikes deal 1d4 less damage on a hit (this can’t reduce the damage below 1).

**properties**:
- Category: Spells
- School: Transmutation
- Classes: Bard, Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Buff, Debuff
- Spell Attack: None
- filter-Level: 2
- filter-Range: Close (30 feet or less)
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Enlarge Reduce","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Enlarge/Reduce\",\"description\":\"For the duration, the spell enlarges or reduces a creature or an object you can see within range (see the chosen effect below). A targeted object must be neither worn nor carried. If the target is an unwilling creature, it can make a Constitution saving throw. On a successful save, the spell has no effect.\\nEverything that a targeted creature is wearing and carrying changes size with it. Any item it drops returns to normal size at once. A thrown weapon or piece of ammunition returns to normal size immediately after it hits or misses a target.\\nEnlarge. The target's size increases by one category-from Medium to Large, for example. The target also has Advantage on Strength checks and Strength saving throws. The target's attacks with its enlarged weapons or Unarmed Strikes deal an extra 1d4 damage on a hit.\\nReduce. The target's size decreases by one category-from Medium to Small, for example. The target also has Disadvantage on Strength checks and Strength saving throws. The target's attacks with its reduced weapons or Unarmed Strikes deal 1d4 less damage on a hit (this can't reduce the damage below 1).\",\"level\":2,\"school\":\"Transmutation\",\"castingTime\":\"Action\",\"range\":\"30 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a pinch of powdered iron\"}}"},{"name":"Enlarge Reduce Unwilling Target Attack","parent":"Enlarge Reduce","payload":"{\"type\":\"Attack\",\"name\":\"Enlarge Reduce Unwilling Target\",\"description\":\"If the target is an unwilling creature, it can make a Constitution saving throw. On a successful save, the spell has no effect.\",\"save\":{\"saveAbility\":\"Constitution\",\"onSucceed\":\"Has no effect.\"}}"},{"name":"Enlarged Condition","parent":"Enlarge Reduce","payload":"{\"type\":\"Condition\",\"name\":\"Enlarged Condition\",\"description\":\"The target's size increases by one category-from Medium to Large, for example. The target also has Advantage on Strength checks and Strength saving throws. The target's attacks with its enlarged weapons or Unarmed Strikes deal an extra 1d4 damage on a hit.\"}"},{"name":"Enlarged Strength Advantage","parent":"Enlarged Condition","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Ability Checks\",\"Saving Throws\"],\"bonusName\":[\"Strength\"],\"bonusDetails\":\"Keep Highest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"Advantage on Strength checks and Strength saving throws.\"}"},{"name":"Enlarged Extra Damage Effect","parent":"Enlarged Condition","payload":"{\"type\":\"Effect\",\"name\":\"Enlarged Extra Damage\",\"description\":\"The target's attacks with its enlarged weapons or Unarmed Strikes deal an extra 1d4 damage on a hit.\",\"category\":[\"Damage\"],\"diceValue\":\"1d4\"}"},{"name":"Reduced Condition","parent":"Enlarge Reduce","payload":"{\"type\":\"Condition\",\"name\":\"Reduced Condition\",\"description\":\"The target's size decreases by one category-from Medium to Small, for example. The target also has Disadvantage on Strength checks and Strength saving throws. The target's attacks with its reduced weapons or Unarmed Strikes deal 1d4 less damage on a hit (this can't reduce the damage below 1).\"}"},{"name":"Reduced Strength Disadvantage","parent":"Reduced Condition","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Ability Checks\",\"Saving Throws\"],\"bonusName\":[\"Strength\"],\"bonusDetails\":\"Keep Lowest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"Disadvantage on Strength checks and Strength saving throws.\"}"},{"name":"Reduced Less Damage Effect","parent":"Reduced Condition","payload":"{\"type\":\"Effect\",\"name\":\"Reduced - Less Damage\",\"description\":\"The target's attacks with its enlarged weapons or Unarmed Strikes deal an extra 1d4 damage on a hit.\",\"category\":[\"Damage\"],\"diceValue\":\"-1d4\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Enlarge Reduce
- data-description: For the duration, the spell enlarges or reduces a creature or an object you can see within range (see the chosen effect below). A targeted object must be neither worn nor carried. If the target is an unwilling creature, it can make a Constitution saving throw. On a successful save, the spell has no effect.
Everything that a targeted creature is wearing and carrying changes size with it. Any item it drops returns to normal size at once. A thrown weapon or piece of ammunition returns to normal size immediately after it hits or misses a target.
Enlarge. The target's size increases by one category-from Medium to Large, for example. The target also has Advantage on Strength checks and Strength saving throws. The target's attacks with its enlarged weapons or Unarmed Strikes deal an extra 1d4 damage on a hit.
Reduce. The target's size decreases by one category-from Medium to Small, for example. The target also has Disadvantage on Strength checks and Strength saving throws. The target's attacks with its reduced weapons or Unarmed Strikes deal 1d4 less damage on a hit (this can't reduce the damage below 1).
- Level: 2
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 30 feet
- Components: V S M
- Material: a pinch of powdered iron
- data-CastNum: 2
- data-RangeNum: 30
- Save: Constitution

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

