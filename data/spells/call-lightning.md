# Call Lightning

**description**: Level 3 Conjuration (Druid) Casting Time: Action Range: 120 feet Components: V, S Duration: Concentration, up to 10 minutes A storm cloud appears at a point within range that you can see above yourself. It takes the shape of a Cylinder that is 10 feet tall with a 60-foot radius. When you cast the spell, choose a point you can see under the cloud. A lightning bolt shoots from the cloud to that point. Each creature within 5 feet of that point makes a Dexterity saving throw, taking 3d10 Lightning damage on a failed save or half as much damage on a successful one. Until the spell ends, you can take a Magic action to call down lightning in that way again, targeting the same point or a different one. If you’re outdoors in a storm when you cast this spell, the spell gives you control over that storm instead of creating a new one. Under such conditions, the spell’s damage increases by 1d10. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Lightning Damage
- Spell Attack: None
- filter-Level: 3
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Call Lightning","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Call Lightning\",\"description\":\"A storm cloud appears at a point within range that you can see above yourself. It takes the shape of a Cylinder that is 10 feet tall with a 60-foot radius.\\nWhen you cast the spell, choose a point you can see under the cloud. A lightning bolt shoots from the cloud to that point. Each creature within 5 feet of that point makes a Dexterity saving throw, taking 3d10 Lightning damage on a failed save or half as much damage on a successful one.\\nUntil the spell ends, you can take a Magic action to call down lightning in that way again, targeting the same point or a different one.\\nIf you're outdoors in a storm when you cast this spell, the spell gives you control over that storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 3.\",\"level\":3,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"60 foot radius\"}}"},{"name":"Call Lightning Attack","parent":"Call Lightning","payload":"{\"type\":\"Attack\",\"name\":\"Call Lightning\",\"description\":\"A lightning bolt shoots from the cloud to that point. Each creature within 5 feet of that point makes a Dexterity saving throw, taking 3d10 Lightning damage on a failed save or half as much damage on a successful one.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 3d10 Lightning damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Emanation\",\"size\":\"5 foot\"}}"},{"name":"Call Lightning Damage","parent":"Call Lightning Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Lightning\",\"diceCount\":3,\"diceSize\":\"d10\"}"},{"name":"Call Lightning Damage Upcasting","parent":"Call Lightning Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Call Lightning Effect","parent":"Call Lightning","payload":"{\"type\":\"Effect\",\"name\":\"Call Lightning Spell\",\"description\":\"Until Call Lighning ends, you can take a Magic action to call down lightning again, targeting the same point or a different one.\"}"},{"name":"Call Lightning Outside Damage Effect","parent":"Call Lightning Effect","payload":"{\"type\":\"Effect\",\"name\":\"Call Lightning Outside\",\"description\":\"If you're outdoors in a storm when you cast this spell, the spell gives you control over that storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.\",\"category\":[\"Damage\"],\"diceValue\":\"1d10\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Call Lightning
- data-description: A storm cloud appears at a point within range that you can see above yourself. It takes the shape of a Cylinder that is 10 feet tall with a 60-foot radius.
When you cast the spell, choose a point you can see under the cloud. A lightning bolt shoots from the cloud to that point. Each creature within 5 feet of that point makes a Dexterity saving throw, taking 3d10 Lightning damage on a failed save or half as much damage on a successful one.
Until the spell ends, you can take a Magic action to call down lightning in that way again, targeting the same point or a different one.
If you're outdoors in a storm when you cast this spell, the spell gives you control over that storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.
- Level: 3
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 3.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Dexterity
- Damage: 3d10
- Damage Type: Lightning
- data-RangeAoe: 120 ft (60 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

