# Conjure Celestial

**description**: Level 7 Conjuration (Cleric) Casting Time: Action Range: 90 feet Components: V, S Duration: Concentration, up to 10 minutes You conjure a spirit from the Upper Planes, which manifests as a pillar of light in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range. For each creature you can see in the Cylinder, choose which of these lights shines on it: Healing Light. The target regains Hit Points equal to 4d12 plus your spellcasting ability modifier. Searing Light. The target makes a Dexterity saving throw, taking 6d12 Radiant damage on a failed save or half as much damage on a successful one. Until the spell ends, Bright Light fills the Cylinder, and when you move on your turn, you can also move the Cylinder up to 30 feet. Whenever the Cylinder moves into the space of a creature you can see and whenever a creature you can see enters the Cylinder or ends its turn there, you can bathe it in one of the lights. A creature can be affected by this spell only once per turn. Using a Higher-Level Spell Slot. The healing and damage increase by 1d12 for each spell slot level above 7.

**properties**:
- Category: Spells
- School: Conjuration
- Classes: Cleric
- Expansion: 33335
- data-List: false
- filter-Tags: Inflict Damage, Healing, Radiant Damage, Minions
- Spell Attack: None
- filter-Level: 7
- filter-Range: Far (more than 60 feet)
- filter-Ritual: No
- filter-Upcast: Yes
- filter-Duration: 10 min
- data-datarecords: [{"name":"Conjure Celestial","level":"7","payload":"{\"type\":\"Spell\",\"name\":\"Conjure Celestial\",\"description\":\"You conjure a spirit from the Upper Planes, which manifests as a pillar of light in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range. For each creature you can see in the Cylinder, choose which of these lights shines on it:\\nHealing Light. The target regains Hit Points equal to 4d12 plus your spellcasting ability modifier.\\nSearing Light. The target makes a Dexterity saving throw, taking 6d12 Radiant damage on a failed save or half as much damage on a successful one.\\nUntil the spell ends, Bright Light fills the Cylinder, and when you move on your turn, you can also move the Cylinder up to 30 feet.\\nWhenever the Cylinder moves into the space of a creature you can see and whenever a creature you can see enters the Cylinder or ends its turn there, you can bathe it in one of the lights. A creature can be affected by this spell only once per turn.\",\"upcastText\":\"Using a Higher-Level Spell Slot. The healing and damage increase by 1d12 for each spell slot level above 7.\",\"level\":7,\"school\":\"Conjuration\",\"castingTime\":\"Action\",\"range\":\"90 feet\",\"duration\":\"Concentration, up to 10 minutes\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"10 foot radius, 40 foot high\"}}"},{"name":"Healing Light","parent":"Conjure Celestial","payload":"{\"type\":\"Healing\",\"ability\":\"auto\",\"isTemp\":false,\"diceCount\":4,\"diceSize\":\"d12\"}"},{"name":"Healing Light Upcast","parent":"Healing Light","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":8,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"},{"name":"Searing Light","parent":"Conjure Celestial","payload":"{\"type\":\"Attack\",\"name\":\"Searing Light\",\"save\":{\"saveAbility\":\"Dexterity\",\"onFail\":\"Take 6d12 Radiant damage.\",\"onSucceed\":\"Half as much damage.\"},\"aoe\":{\"shape\":\"Cylinder\",\"size\":\"10 foot radius, 40 foot high\"}}"},{"name":"Searing Light Damage","parent":"Searing Light","payload":"{\"type\":\"Damage\",\"ability\":\"auto\",\"damageType\":\"Radiant\",\"diceCount\":6,\"diceSize\":\"d12\"}"},{"name":"Searing Light Damage Upcast","parent":"Searing Light Damage","payload":"{\"type\":\"Upcasting\",\"mode\":\"Per X Spell Level\",\"startingLevel\":8,\"level\":1,\"target\":\"$.diceCount\",\"value\":1,\"changeMode\":\"Add\"}"}]
- filter-Components: Verbal, Somatic
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Conjure Celestial
- data-description: You conjure a spirit from the Upper Planes, which manifests as a pillar of light in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range. For each creature you can see in the Cylinder, choose which of these lights shines on it:
Healing Light. The target regains Hit Points equal to 4d12 plus your spellcasting ability modifier.
Searing Light. The target makes a Dexterity saving throw, taking 6d12 Radiant damage on a failed save or half as much damage on a successful one.
Until the spell ends, Bright Light fills the Cylinder, and when you move on your turn, you can also move the Cylinder up to 30 feet.
Whenever the Cylinder moves into the space of a creature you can see and whenever a creature you can see enters the Cylinder or ends its turn there, you can bathe it in one of the lights. A creature can be affected by this spell only once per turn.
- Level: 7
- Casting Time: Action
- Concentration: Yes
- Duration: up to 10 minutes
- Range: 90 feet
- Components: V S
- Higher Spell Slot Desc: Using a Higher-Level Spell Slot. The healing and damage increase by 1d12 for each spell slot level above 7.
- data-CastNum: 2
- data-RangeNum: 90
- Save: Dexterity
- Damage: 6d12
- Damage Type: Radiant
- data-RangeAoe: 90 ft (10 ft radius, 40 foot high ○)

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

