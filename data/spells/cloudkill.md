# Cloudkill

**description**: Level 5 Conjuration (Sorcerer, Wizard) Casting Time: Action Range: 120 feet Components: V, S Duration: Concentration, up to 10 minutes You create a 20-foot-radius Sphere of yellow-green fog centered on a point within range. The fog lasts for the duration or until strong wind (such as the one created by Gust of Wind ) disperses it, ending the spell. Its area is Heavily Obscured. Each creature in the Sphere makes a Constitution saving throw, taking 5d8 Poison damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn. The Sphere moves 10 feet away from you at the start of each of your turns. Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Constitution Save, Poison Damage
- Spell Attack: None
- filter-Level: 5
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Cloudkill","level":"5","payload":"{\"type\":\"Spell\",\"name\":\"Cloudkill\",\"description\":\"You create a 20-foot-radius Sphere of yellow-green fog centered on a point within range. The fog lasts for the duration or until strong wind (such as the one created by Gust of Wind) disperses it, ending the spell. Its area is Heavily Obscured.\\nEach creature in the Sphere makes a Constitution saving throw, taking 5d8 Poison damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn.\\nThe Sphere moves 10 feet away from you at the start of each of your turns.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.\",\"level\":5,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"120 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Cloudkill Attack","parent":"Cloudkill","payload":"{\"type\":\"Attack\",\"name\":\"Cloudkill\",\"range\":\"120 feet\",\"description\":\"You create a 20-foot-radius Sphere of yellow-green fog centered on a point within range. The fog lasts for the duration or until strong wind (such as the one created by Gust of Wind) disperses it, ending the spell. Its area is Heavily Obscured.\",\"save\":{\"saveAbility\":\"Constitution\",\"onFail\":\"Take 5d8 Poison damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"20 foot radius\"}}"},{"name":"Cloudkill Damage","parent":"Cloudkill Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Poison\",\"diceCount\":5,\"diceSize\":\"d8\"}"},{"name":"Cloudkill Damage Upcast","parent":"Cloudkill Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":6,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Cloudkill
- data-description: You create a 20-foot-radius Sphere of yellow-green fog centered on a point within range. The fog lasts for the duration or until strong wind (such as the one created by Gust of Wind) disperses it, ending the spell. Its area is Heavily Obscured.
Each creature in the Sphere makes a Constitution saving throw, taking 5d8 Poison damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn.
The Sphere moves 10 feet away from you at the start of each of your turns.
- Level: 5
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 120 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.
- data-CastNum: 2
- data-RangeNum: 120
- Save: Constitution
- Damage: 5d8
- Damage Type: Poison
- data-RangeAoe: 120 ft (20 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

