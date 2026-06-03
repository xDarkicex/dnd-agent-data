# Conjure Animals

**description**: Level 3 Conjuration (Druid, Ranger) Casting Time: Action Range: 60 feet Components: V, S Duration: Concentration, up to 10 minutes You conjure nature spirits that appear as a Large pack of spectral, intangible animals in an unoccupied space you can see within range. The pack lasts for the duration, and you choose the spirits’ animal form, such as wolves, serpents, or birds. You have Advantage on Strength saving throws while you’re within 5 feet of the pack, and when you move on your turn, you can also move the pack up to 30 feet to an unoccupied space you can see. Whenever the pack moves within 10 feet of a creature you can see and whenever a creature you can see enters a space within 10 feet of the pack or ends its turn there, you can force that creature to make a Dexterity saving throw. On a failed save, the creature takes 3d10 Slashing damage. A creature makes this save only once per turn. Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 3.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Druid, Ranger
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Buff, Dexterity Save
- Spell Attack: None
- filter-Level: 3
- filter-Range: Medium (60 feet or less)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Conjure Animals","level":"3","payload":"{\"type\":\"Spell\",\"name\":\"Conjure Animals\",\"description\":\"You conjure nature spirits that appear as a Large pack of spectral, intangible animals in an unoccupied space you can see within range. The pack lasts for the duration, and you choose the spirits' animal form, such as wolves, serpents, or birds.\\nYou have Advantage on Strength saving throws while you're within 5 feet of the pack, and when you move on your turn, you can also move the pack up to 30 feet to an unoccupied space you can see.\\nWhenever the pack moves within 10 feet of a creature you can see and whenever a creature you can see enters a space within 10 feet of the pack or ends its turn there, you can force that creature to make a Dexterity saving throw. On a failed save, the creature takes 3d10 Slashing damage. A creature makes this save only once per turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 3.\",\"level\":3,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"60 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true}}"},{"name":"Conjure Animals Condition","parent":"Conjure Animals","payload":"{\"type\":\"Condition\",\"name\":\"Conjure Animals Pack Distance\",\"description\":\"You have Advantage on Strength saving throws while you're within 5 feet of the pack, and when you move on your turn, you can also move the pack up to 30 feet to an unoccupied space you can see.\"}"},{"name":"Conjure Animals Advantage","parent":"Conjure Animals Condition","payload":"{\"type\":\"Roll Bonus\",\"bonusCategory\":[\"Conjure Animals\"],\"bonusName\":[],\"bonusDetails\":\"Keep Highest\",\"bonusValue\":1,\"diceCount\":2,\"situation\":\"Advantage on Strength saving throws while you're within 5 feet of the pack.\"}"},{"name":"Conjure Animals Attack","parent":"Conjure Animals","payload":"{\"type\":\"Attack\",\"name\":\"Conjure Animals\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 3d10 Slashing damage.\"}}"},{"name":"Conjure Animals Damage","parent":"Conjure Animals Attack","payload":"{\"type\":\"Damage\",\"ability\":\"none\",\"damageType\":\"Slashing\",\"diceCount\":3,\"diceSize\":\"d10\"}"},{"name":"Conjure Animals Damage Upcast","parent":"Conjure Animals Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":4,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Conjure Animals
- data-description: You conjure nature spirits that appear as a Large pack of spectral, intangible animals in an unoccupied space you can see within range. The pack lasts for the duration, and you choose the spirits' animal form, such as wolves, serpents, or birds.
You have Advantage on Strength saving throws while you're within 5 feet of the pack, and when you move on your turn, you can also move the pack up to 30 feet to an unoccupied space you can see.
Whenever the pack moves within 10 feet of a creature you can see and whenever a creature you can see enters a space within 10 feet of the pack or ends its turn there, you can force that creature to make a Dexterity saving throw. On a failed save, the creature takes 3d10 Slashing damage. A creature makes this save only once per turn.
- Level: 3
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 60 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 3.
- data-CastNum: 2
- data-RangeNum: 60
- Save: Dexterity
- Damage: 3d10
- Damage Type: Slashing

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

