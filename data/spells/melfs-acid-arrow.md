# Melf's Acid Arrow

**description**: Level 2 Evocation (Wizard) Casting Time: Action Range: 90 feet Components: V, S, M (powdered rhubarb leaf) Duration: Instantaneous A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 Acid damage and 2d4 Acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage only. Using a Higher-Level Spell Slot. The damage (both initial and later) increases by 1d4 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Acid Damage, Attack vs AC
- Spell Attack: Ranged
- filter-Level: 2
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Melf's Acid Arrow","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Melf's Acid Arrow\",\"description\":\"A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 Acid damage and 2d4 Acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage only.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage (both initial and later) increases by 1d4 for each spell slot level above 2.\",\"level\":2,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"90 feet\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"powdered rhubarb leaf\"}}"},{"name":"Melf's Acid Arrow Attack","parent":"Melf's Acid Arrow","payload":"{\"type\":\"Attack\",\"name\":\"Melf's Acid Arrow\",\"range\":\"90 feet\",\"description\":\"Make a ranged spell attack against the target. On a hit, the target takes 4d4 Acid damage and 2d4 Acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage only.\",\"attack\":{\"type\":\"Spell Attack\"}}"},{"name":"Melf's Acid Arrow Initial Damage","parent":"Melf's Acid Arrow Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Acid\",\"diceCount\":4,\"diceSize\":\"d4\"}"},{"name":"Melf's Acid Arrow Initial Damage Upcast","parent":"Melf's Acid Arrow Initial Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Melf's Acid Arrow Next Round Free Attack","parent":"Melf's Acid Arrow Attack","payload":"{\"type\":\"Attack\",\"name\":\"Melf's Acid Arrow - Next Round\",\"autoHit\":true,\"description\":\"On a hit, the target takes 2d4 Acid damage at the end of its next turn.\",\"actionType\":\"Free Action\"}"},{"name":"Melf's Acid Arrow Next Round Free Damage","parent":"Melf's Acid Arrow Next Round Free Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Acid\",\"diceCount\":2,\"diceSize\":\"d4\"}"},{"name":"Melf's Acid Arrow Next Round Free Damage Upcast","parent":"Melf's Acid Arrow Next Round Free Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Melf's Acid Arrow
- data-description: A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 Acid damage and 2d4 Acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage only.
- Level: 2
- Casting Time: Action
- Duration: Instantaneous
- Range: 90 feet
- Components: V S M
- Material: powdered rhubarb leaf
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage (both initial and later) increases by 1d4 for each spell slot level above 2.
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 90
- data-AttackType: Spell Attack
- Damage: 4d4
- Damage Type: Acid

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

