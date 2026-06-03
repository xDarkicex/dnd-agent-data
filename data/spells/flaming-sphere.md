# Flaming Sphere

**description**: Level 2 Conjuration (Druid, Sorcerer, Wizard) Casting Time: Action Range: 60 feet Components: V, S, M (a ball of wax) Duration: Concentration, up to 1 minute You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration. Any creature that ends its turn within 5 feet of the sphere makes a Dexterity saving throw, taking 2d6 Fire damage on a failed save or half as much damage on a successful one. As a Bonus Action, you can move the sphere up to 30 feet, rolling it along the ground. If you move the sphere into a creature’s space, that creature makes the save against the sphere, and the sphere stops moving for the turn. When you move the sphere, you can direct it over barriers up to 5 feet tall and jump it across pits up to 10 feet wide. Flammable objects that aren’t being worn or carried start burning if touched by the sphere, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet. Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Dexterity Save, Fire Damage
- Spell Attack: None
- filter-Level: 2
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 1 min
- data-datarecords: [{"name":"Flaming Sphere","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Flaming Sphere\",\"description\":\"You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration. Any creature that ends its turn within 5 feet of the sphere makes a Dexterity saving throw, taking 2d6 Fire damage on a failed save or half as much damage on a successful one.\\nAs a Bonus Action, you can move the sphere up to 30 feet, rolling it along the ground. If you move the sphere into a creature's space, that creature makes the save against the sphere, and the sphere stops moving for the turn.\\nWhen you move the sphere, you can direct it over barriers up to 5 feet tall and jump it across pits up to 10 feet wide. Flammable objects that aren't being worn or carried start burning if touched by the sphere, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.\",\"level\":2,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"a ball of wax\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"5 foot radius\"}}"},{"name":"Flaming Sphere Condition","parent":"Flaming Sphere","payload":"{\"type\":\"Condition\",\"name\":\"Flaming Sphere\",\"description\":\"You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration.\"}"},{"name":"Flaming Sphere Bonus Action","parent":"Flaming Sphere Condition","payload":"{\"type\":\"Action\",\"name\":\"Flaming Sphere - Move\",\"description\":\"As a Bonus Action, you can move the sphere up to 30 feet, rolling it along the ground. If you move the sphere into a creature's space, that creature makes the save against the sphere, and the sphere stops moving for the turn.\",\"actionType\":\"Bonus Action\"}"},{"name":"Flaming Sphere Attack","parent":"Flaming Sphere","payload":"{\"type\":\"Attack\",\"name\":\"Flaming Sphere\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Takes 2d6 Fire damage.\",\"onSucceed\":\"Half as much damage.\"}}"},{"name":"Flaming Sphere Damage","parent":"Flaming Sphere Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Fire\",\"diceCount\":2,\"diceSize\":\"d6\"}"},{"name":"Flaming Sphere Damage Upcast","parent":"Flaming Sphere Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":3,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Flaming Sphere
- data-description: You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration. Any creature that ends its turn within 5 feet of the sphere makes a Dexterity saving throw, taking 2d6 Fire damage on a failed save or half as much damage on a successful one.
As a Bonus Action, you can move the sphere up to 30 feet, rolling it along the ground. If you move the sphere into a creature's space, that creature makes the save against the sphere, and the sphere stops moving for the turn.
When you move the sphere, you can direct it over barriers up to 5 feet tall and jump it across pits up to 10 feet wide. Flammable objects that aren't being worn or carried start burning if touched by the sphere, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet.
- Level: 2
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: 60 feet
- Components: V S M
- Material: a ball of wax
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 2.
- data-CastNum: 2
- data-RangeNum: 60
- Save: Dexterity
- Damage: 2d6
- Damage Type: Fire
- data-RangeAoe: 60 ft (5 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

