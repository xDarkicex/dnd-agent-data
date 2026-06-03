# Lightning Bolt

**description**: Level 3 Evocation (Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S, M (a bit of fur and a crystal rod) Duration: Instantaneous A stroke of lightning forming a 100-foot-long, 5-foot-wide Line blasts out from you in a direction you choose. Each creature in the Line makes a Dexterity saving throw, taking 8d6 Lightning damage on a failed save or half as much damage on a successful one. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Dexterity Save, Lightning Damage, Inflict Damage
- Spell Attack: None
- filter-Level: 3
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Lightning Bolt","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Lightning Bolt\",\"description\":\"A stroke of lightning forming a 100-foot-long, 5-foot-wide Line blasts out from you in a direction you choose. Each creature in the Line makes a Dexterity saving throw, taking 8d6 Lightning damage on a failed save or half as much damage on a successful one.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.\",\"level\":3,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a bit of fur and a crystal rod\"},\"aoe\":{\"shape\":\"Line\",\"size\":\"100 foot long\"}}"},{"name":"Lightning Bolt Attack","parent":"Lightning Bolt","payload":"{\"type\":\"Attack\",\"name\":\"Lightning Bolt\",\"description\":\"A stroke of lightning forming a 100-foot-long, 5-foot-wide Line blasts out from you in a direction you choose. Each creature in the Line makes a Dexterity saving throw, taking 8d6 Lightning damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 8d6 Lightning damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Line\",\"size\":\"100 foot long\"}}"},{"name":"Lightning Bolt Damage","parent":"Lightning Bolt Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Lightning\",\"diceCount\":8,\"diceSize\":\"d6\"}"},{"name":"Lightning Bolt Damage Upcast","parent":"Lightning Bolt Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Lightning Bolt
- data-description: A stroke of lightning forming a 100-foot-long, 5-foot-wide Line blasts out from you in a direction you choose. Each creature in the Line makes a Dexterity saving throw, taking 8d6 Lightning damage on a failed save or half as much damage on a successful one.
- Level: 3
- Casting Time: Action
- Duration: Instantaneous
- Range: Self
- Components: V S M
- Material: a bit of fur and a crystal rod
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 3.
- data-CastNum: 2
- data-DurationNum: 0
- Save: Dexterity
- Damage: 8d6
- Damage Type: Lightning
- data-RangeAoe: Self (100 ft long ⇧)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

