# Burning Hands

**description**: Level 1 Evocation (Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S Duration: Instantaneous A thin sheet of flames shoots forth from you. Each creature in a 15-foot Cone makes a Dexterity saving throw, taking 3d6 Fire damage on a failed save or half as much damage on a successful one. Flammable objects in the Cone that aren’t being worn or carried start burning. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.

**properties**:
- Category: Spells
- School: Evocation
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Fire Damage, Dexterity Save
- Spell Attack: None
- filter-Level: 1
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Burning Hands","level":"1","payload":"{\"type\":\"Spell\",\"name\":\"Burning Hands\",\"description\":\"A thin sheet of flames shoots forth from you. Each creature in a 15-foot Cone makes a Dexterity saving throw, taking 3d6 Fire damage on a failed save or half as much damage on a successful one.\\nFlammable objects in the Cone that aren't being worn or carried start burning.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.\",\"level\":1,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Instantaneous\",\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Cone\",\"size\":\"15 foot\"}}"},{"name":"Burning Hands Attack","parent":"Burning Hands","payload":"{\"type\":\"Attack\",\"name\":\"Burning Hands\",\"description\":\"A thin sheet of flames shoots forth from you. Each creature in a 15-foot Cone makes a Dexterity saving throw, taking 3d6 Fire damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 3d6 Fire damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Cone\",\"size\":\"15 foot\"}}"},{"name":"Burning Hands Damage","parent":"Burning Hands Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":3,\"diceSize\":\"d6\"}"},{"name":"Burning Hands Damage Upcast","parent":"Burning Hands Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":2,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: No
- Name: Burning Hands
- data-description: A thin sheet of flames shoots forth from you. Each creature in a 15-foot Cone makes a Dexterity saving throw, taking 3d6 Fire damage on a failed save or half as much damage on a successful one.
Flammable objects in the Cone that aren't being worn or carried start burning.
- Level: 1
- Casting Time: Action
- Duration: Instantaneous
- Range: Self
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.
- data-CastNum: 2
- data-DurationNum: 0
- Save: Dexterity
- Damage: 3d6
- Damage Type: Fire
- data-RangeAoe: Self (15 ft ▽)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

