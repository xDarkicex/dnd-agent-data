# Acid Splash

**description**: Evocation Cantrip (Sorcerer, Wizard) Casting Time: Action Range: 60 feet Components: V, S Duration: Instantaneous You create an acidic bubble at a point within range, where it explodes in a 5-foot-radius Sphere. Each creature in that Sphere must succeed on a Dexterity saving throw or take 1d6 Acid damage. Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).

**properties**:
- Category: Spells
- Save: Dexterity
- Level: 0
- Range: 60 feet
- Damage: 1d6
- School: Evocation
- Target: 5-foot-radius Sphere
- Classes: Sorcerer, Wizard
- Duration: Instantaneous
- Expansion: 33335
- data-List: false
- Components: V S
- Damage Type: Acid
- filter-Tags: Inflict Damage, Dexterity Save, Acid Damage
- Casting Time: Action
- Spell Attack: None
- filter-Level: Cantrip
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: Instantaneous
- data-datarecords: [{"name":"Acid Splash","level":"0","payload":"{\"type\":\"Spell\",\"name\":\"Acid Splash\",\"description\":\"You create an acidic bubble at a point within range, where it explodes in a 5-foot-radius Sphere. Each creature in that Sphere must succeed on a Dexterity saving throw or take 1d6 Acid damage.\",\"upcastText\":\"Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).\",\"level\":0,\"school\":\"Evocation\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Instantaneous\",\"cantripScale\":\"Dice\",\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"5 foot radius\"}}"},{"name":"Acid Splash Attack","parent":"Acid Splash","payload":"{\"type\":\"Attack\",\"name\":\"Acid Splash\",\"range\":\"60 ft.\",\"description\":\"You create an acidic bubble at a point within range, where it explodes in a 5-foot-radius Sphere.\",\"save\":{\"saveAbility\":\"Dexterity\",\"onSucceed\":\"No damage\"},\"aoe\":{\"shape\":\"Sphere\",\"size\":\"5 foot radius\"}}"},{"name":"Acid Splash Damage","parent":"Acid Splash Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Acid\",\"diceSize\":\"d6\"}"},{"name":"Acid Splash Damage Upcasting 5","parent":"Acid Splash Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":5,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Acid Splash Damage Upcasting 11","parent":"Acid Splash Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":11,\"target\":\"$.diceCount\",\"value\":2,\"changeMode\":\"Add\"}"},{"name":"Acid Splash Damage Upcasting 17","parent":"Acid Splash Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Specific Character Level\",\"level\":17,\"target\":\"$.diceCount\",\"value\":3,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- data-Cantrip Scaling: dice
- filter-Concentration: No
- Name: Acid Splash
- data-description: You create an acidic bubble at a point within range, where it explodes in a 5-foot-radius Sphere. Each creature in that Sphere must succeed on a Dexterity saving throw or take 1d6 Acid damage.
- Higher Spell Slot Desc: Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).
- data-CastNum: 2
- data-DurationNum: 0
- data-RangeNum: 60
- data-RangeAoe: 60 ft (5 ft radius ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

