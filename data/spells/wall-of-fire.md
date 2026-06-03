# Wall of Fire

**description**: Level 4 Evocation (Druid, Sorcerer, Wizard) Casting Time: Action Range: 120 feet Components: V, S, M (a piece of charcoal) Duration: Concentration, up to 1 minute You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration. When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one. One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Dexterity Save, Inflict Damage, Fire Damage
- Spell Attack: None
- filter-Level: 4
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Wall of Fire","level":"4","payload":"{\"type\":\"Spell\",\"name\":\"Wall of Fire\",\"description\":\"You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration.\\nWhen the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.\\nOne side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.\",\"level\":4,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a piece of charcoal\"},\"aoe\":{\"shape\":\"Wall\",\"size\":\"60 feet long, 20 feet high*\"}}"},{"name":"Wall of Fire Attack","parent":"Wall of Fire","payload":"{\"type\":\"Attack\",\"name\":\"Wall of Fire\",\"description\":\"When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.\\nOne side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 5d8 Fire damage.\",\"onSucceed\":\"Half damage.\"},\"aoe\":{\"shape\":\"Wall\",\"size\":\"60 feet long, 20 feet high*\"}}"},{"name":"Wall of Fire Damage","parent":"Wall of Fire Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":5,\"diceSize\":\"d8\"}"},{"name":"Wall of Fire Initial Damage Upcast","parent":"Wall of Fire Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":5,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Wall of Fire
- data-description: You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration.
When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.
One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.
- Level: 4
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 120 feet
- Components: V S M
- Material: a piece of charcoal
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 4.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Dexterity
- Damage: 5d8
- Damage Type: Fire
- data-RangeAoe: 120 ft (60 feet long, 20 feet high* ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

