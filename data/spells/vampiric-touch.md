# Vampiric Touch

**description**: Level 3 Necromancy (Sorcerer, Warlock, Wizard) Casting Time: Action Range: Self Components: V, S Duration: Concentration, up to 1 minute The touch of your shadow-wreathed hand can siphon life force from others to heal your wounds. Make a melee spell attack against one creature within reach. On a hit, the target takes 3d6 Necrotic damage, and you regain Hit Points equal to half the amount of Necrotic damage dealt. Until the spell ends, you can make the attack again on each of your turns as a Magic action, targeting the same creature or a different one. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Necromancy
- Classes: Sorcerer, Warlock, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Attack vs AC, Necrotic Damage
- Spell Attack: Melee
- filter-Level: 3
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Vampiric Touch","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Vampiric Touch\",\"description\":\"The touch of your shadow-wreathed hand can siphon life force from others to heal your wounds. Make a melee spell attack against one creature within reach. On a hit, the target takes 3d6 Necrotic damage, and you regain Hit Points equal to half the amount of Necrotic damage dealt.\\nUntil the spell ends, you can make the attack again on each of your turns as a Magic action, targeting the same creature or a different one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.\",\"level\":3,\"school\":\"Necromancy\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Vampiric Touch Condition","parent":"Vampiric Touch","payload":"{\"type\":\"Condition\",\"name\":\"Vampire Touch\",\"description\":\"Until the spell ends, you can make the attack again on each of your turns as a Magic action, targeting the same creature or a different one.\"}"},{"name":"Vampiric Touch Attack","parent":"Vampiric Touch","payload":"{\"type\":\"Attack\",\"name\":\"Vampiric Touch\",\"description\":\"Make a melee spell attack against one creature within reach.\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Vampiric Touch Damage","parent":"Vampiric Touch Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Necrotic\",\"diceCount\":3,\"diceSize\":\"d6\"}"},{"name":"Vampiric Touch Damage Upcast","parent":"Vampiric Touch Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Vampiric Touch
- data-description: The touch of your shadow-wreathed hand can siphon life force from others to heal your wounds. Make a melee spell attack against one creature within reach. On a hit, the target takes 3d6 Necrotic damage, and you regain Hit Points equal to half the amount of Necrotic damage dealt.
Until the spell ends, you can make the attack again on each of your turns as a Magic action, targeting the same creature or a different one.
- Level: 3
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: Self
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.
- data-CastNum: 2
- data-AttackType: Spell Attack
- Damage: 3d6
- Damage Type: Necrotic

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

