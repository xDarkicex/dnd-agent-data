# Detect Thoughts

**description**: Level 2 Divination (Bard, Sorcerer, Wizard) Casting Time: Action Range: Self Components: V, S, M (1 Copper Piece) Duration: Concentration, up to 1 minute You activate one of the effects below. Until the spell ends, you can activate either effect as a Magic action on your later turns. Sense Thoughts. You sense the presence of thoughts within 30 feet of yourself that belong to creatures that know languages or are telepathic. You don’t read the thoughts, but you know that a thinking creature is present. The spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead. Read Thoughts. Target one creature you can see within 30 feet of yourself or one creature within 30 feet of yourself that you detected with the Sense Thoughts option. You learn what is most on the target’s mind right now. If the target doesn’t know any languages and isn’t telepathic, you learn nothing. As a Magic action on your next turn, you can try to probe deeper into the target’s mind. If you probe deeper, the target makes a Wisdom saving throw. On a failed save, you discern the target’s reasoning, emotions, and something that looms large in its mind (such as a worry, love, or hate). On a successful save, the spell ends. Either way, the target knows that you are probing into its mind, and until you shift your attention away from the target’s mind, the target can take an action on its turn to make an Intelligence (Arcana) check against your spell save DC, ending the spell on a success.

**properties**:
- Category: Spells
- School: Divination
- Classes: Bard, Sorcerer, Wizard
- Expansion: 33335
- data-List: false
- filter-Tags: Utility, Wisdom Save
- Spell Attack: None
- filter-Level: 2
- filter-Range: Self
- filter-Ritual: No
- filter-Upcast: No
- filter-Duration: 1 min
- data-datarecords: [{"name":"Detect Thoughts","level":"2","payload":"{\"type\":\"Spell\",\"name\":\"Detect Thoughts\",\"description\":\"You activate one of the effects below. Until the spell ends, you can activate either effect as a Magic action on your later turns.\\nSense Thoughts. You sense the presence of thoughts within 30 feet of yourself that belong to creatures that know languages or are telepathic. You don't read the thoughts, but you know that a thinking creature is present.\\nThe spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead.\\nRead Thoughts. Target one creature you can see within 30 feet of yourself or one creature within 30 feet of yourself that you detected with the Sense Thoughts option. You learn what is most on the target's mind right now. If the target doesn't know any languages and isn't telepathic, you learn nothing.\\nAs a Magic action on your next turn, you can try to probe deeper into the target's mind. If you probe deeper, the target makes a Wisdom saving throw. On a failed save, you discern the target's reasoning, emotions, and something that looms large in its mind (such as a worry, love, or hate). On a successful save, the spell ends. Either way, the target knows that you are probing into its mind, and until you shift your attention away from the target's mind, the target can take an action on its turn to make an Intelligence (Arcana) check against your spell save DC, ending the spell on a success.\",\"level\":2,\"school\":\"Divination\",\"castingTime\":\"Action\",\"range\":\"Self\",\"duration\":\"Concentration, up to 1 minute\",\"concentration\":true,\"components\":{\"verbal\":true,\"somatic\":true,\"material\":true,\"materialDescription\":\"1 Copper Piece\"}}"},{"name":"Detect Thoughts Condition","parent":"Detect Thoughts","payload":"{\"type\":\"Condition\",\"name\":\"Detect Thoughts\",\"description\":\"You activate one of the effects: Sense Thoughts, Read Thoughts. Until the spell ends, you can activate either effect as a Magic action on your later turns.\"}"},{"name":"Sense Thoughts Action","parent":"Detect Thoughts Condition","payload":"{\"type\":\"Action\",\"name\":\"Sense Thoughts\",\"description\":\"You sense the presence of thoughts within 30 feet of yourself that belong to creatures that know languages or are telepathic. You don't read the thoughts, but you know that a thinking creature is present.\\n\\nThe spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead.\\n\",\"actionType\":\"Action\"}"},{"name":"Read Thoughts Action","parent":"Detect Thoughts Condition","payload":"{\"type\":\"Action\",\"name\":\"Read Thoughts\",\"description\":\"Target one creature you can see within 30 feet of yourself or one creature within 30 feet of yourself that you detected with the Sense Thoughts option. You learn what is most on the target's mind right now. If the target doesn't know any languages and isn't telepathic, you learn nothing.\",\"actionType\":\"Action\"}"},{"name":"Read Thoughts Condition","parent":"Read Thoughts Action","payload":"{\"type\":\"Condition\",\"name\":\"Read Thoughts Probe Deeper\"}"},{"name":"Read Thoughts Probe Deeper Action","parent":"Read Thoughts Condition","payload":"{\"type\":\"Action\",\"name\":\"Read Thoughts Probe Deeper\",\"description\":\"As a Magic action on your next turn, you can try to probe deeper into the target's mind. If you probe deeper, the target makes a Wisdom saving throw. On a failed save, you discern the target's reasoning, emotions, and something that looms large in its mind (such as a worry, love, or hate). On a successful save, the spell ends. Either way, the target knows that you are probing into its mind, and until you shift your attention away from the target's mind, the target can take an action on its turn to make an Intelligence (Arcana) check against your spell save DC, ending the spell on a success.\",\"actionType\":\"Action\"}"},{"name":"Read Thoughts Probe Deeper Attack","parent":"Detect Thoughts","payload":"{\"type\":\"Attack\",\"name\":\"Read Thoughts Probe Deeper\",\"save\":{\"saveAbility\":\"Wisdom\",\"onFail\":\"You discern the target's reasoning, emotions, and something that looms large in its mind (such as a worry, love, or hate).\",\"onSucceed\":\"Spell ends.\"}}"}]
- filter-Components: Verbal, Somatic, Material
- filter-Casting Time: Action
- filter-Concentration: Yes
- Name: Detect Thoughts
- data-description: You activate one of the effects below. Until the spell ends, you can activate either effect as a Magic action on your later turns.
Sense Thoughts. You sense the presence of thoughts within 30 feet of yourself that belong to creatures that know languages or are telepathic. You don't read the thoughts, but you know that a thinking creature is present.
The spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead.
Read Thoughts. Target one creature you can see within 30 feet of yourself or one creature within 30 feet of yourself that you detected with the Sense Thoughts option. You learn what is most on the target's mind right now. If the target doesn't know any languages and isn't telepathic, you learn nothing.
As a Magic action on your next turn, you can try to probe deeper into the target's mind. If you probe deeper, the target makes a Wisdom saving throw. On a failed save, you discern the target's reasoning, emotions, and something that looms large in its mind (such as a worry, love, or hate). On a successful save, the spell ends. Either way, the target knows that you are probing into its mind, and until you shift your attention away from the target's mind, the target can take an action on its turn to make an Intelligence (Arcana) check against your spell save DC, ending the spell on a success.
- Level: 2
- Casting Time: Action
- Concentration: Yes
- Duration: up to 1 minute
- Range: Self
- Components: V S M
- Material: 1 Copper Piece
- data-CastNum: 2
- Save: Wisdom

**publisher**: Wizards of the Coast

**book**: Free Basic Rules (2024)

