# C-SkillSystem designer options

This document is a local reference for every field in
[`configs/config.c`](../configs/config.c). The values match the upstream
[`designer-config.c`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Data/DesignerConfig/designer-config.c)
from [C-SkillSystem-Jester](https://github.com/JesterWizard/C-SkillSystem-Jester).

This file documents the **configuration surface**. It does not port kernel
implementations, assets, or headers into this decompilation.

Behavior comes from feature pages first, then `kernel-lib.h` / `designer-config.c`
comments. Where those are missing, the summary is **inferred** from named
`gpKernelDesignerConfig` call sites. A few fields are documented but appear
stale in the current upstream tree (`custom_menu_options`, `fe7_mode_select`,
`show_tutorial`).

Primary sources:

- [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md)
- [Abstract](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Abstract.md)
- [`kernel-lib.h`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/include/kernel/kernel-lib.h)
- [Documentation/Features](https://github.com/JesterWizard/C-SkillSystem-Jester/tree/main/Documentation/Features)

---

## AI and map

### `ai_dance_use`

- **Value:** `true`
- **Behavior:** When true, AI dancers can refresh allies that have already
  acted so those allies act again. When false, AI never dances.
- **Source:** `kernel-lib.h`; comment in `designer-config.c`.

### `ai_player_phase`

- **Value:** `false`
- **Behavior:** When enabled, permits AI control of the player phase.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `calculate_map_range_faster`

- **Value:** `true`
- **Behavior:** AI only ranges the 3 closest enemies.
- **Source:** Comment in `designer-config.c`.

### `rescue_drop_ai_use`

- **Value:** `true`
- **Behavior:** AI can rescue an adjacent ally below half HP, carry them
  toward the farthest reachable tile from hostiles, and drop on a legal
  adjacent tile. Falls back to normal heal/escape if rescue is unavailable.
- **Source:** [AI Rescue Retreat](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/AIRescueRetreat.md);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `rescue_drop_move_again`

- **Value:** `true`
- **Behavior:** After a drop, the rescued unit may move again if it has not
  already moved.
- **Source:** Inferred from named call sites; related
  [AI Rescue Retreat](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/AIRescueRetreat.md).

### `menu_skill_ai_use`

- **Value:** `false`
- **Behavior:** When true, enemies may use menu skills during AI phase after
  combat and healing logic finish. The AI takes the first usable skill. Left
  false by default because of AI-phase cost on large maps.
- **Source:** [Menu Skill AI](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/MenuSkillAI.md);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `gaiden_magic_ai_use`

- **Value:** `false`
- **Behavior:** When false, AI cannot use Gaiden black/white magic.
- **Source:** [Gaiden Magic](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/GaidenMagic.md);
  comment in `designer-config.c`.

### `enemy_fog_vision`

- **Value:** `true`
- **Behavior:** On fog chapters, non-player AI can only fight, staff, chase,
  or skill-target units its faction can currently see. Reuses per-class vision
  from Fog Vision. Does not rewrite player `gBmMapFog`. Off restores
  omniscient AI.
- **Source:** [Enemy Fog Vision](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/EnemyFogVision.md);
  `kernel-lib.h`.

### `custom_fog_sight`

- **Value:** `true`
- **Behavior:** Gates modular per-class fog vision ranges (vanilla is mostly
  1 tile, thieves +5). Same range table is consumed by enemy fog vision.
- **Source:** [Fog Vision](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/FogVision.md).
  The field name is not quoted on that page; the feature is the matching
  designer toggle.

### `multiple_fog_stages`

- **Value:** `true`
- **Behavior:** Player-facing fog uses four stages instead of all-or-nothing:
  full info, hidden stats, shadow sprite, or fully invisible. Stage 3 enemies
  are withheld from `gBmMapUnit`.
- **Source:** [Fog Stages](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/FogStages.md).

### `free_movement`

- **Value:** `true`
- **Behavior:** Enables JRPG-style D-pad map movement (ASM Sme implementation).
  Chapters still start it with `ASMC(EnableFreeMovementASMC)`. Limitations:
  disables after suspend; only the first deployed unit; no combat/trade/rescue
  while in free movement.
- **Source:** [Free Movement](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/FreeMovement.md).

### `fast_map_animations`

- **Value:** `false`
- **Behavior:** Speeds up map animations and also interacts with the in-game
  option bit. Config comment: broken with free movement.
- **Source:** Comment in `designer-config.c`; inferred from named call sites.

### `remove_move_path`

- **Value:** `false`
- **Behavior:** When true, disables move-path calculation and display. Vanilla
  path display only supports about 20 steps and can overflow on high-move
  units. Pathfinding ghost requires this to stay false.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  [Translucent Unit Sprite](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TranslucentUnitSprite.md).

### `alpha_blend_movement_sprites`

- **Value:** `true`
- **Behavior:** While pathfinding (and `remove_move_path` is off), shows a Lex
  Talionis-style faded moving-map-sprite ghost at the cursor tip. Cleared when
  A/B ends pathfinding.
- **Source:** [Translucent Unit Sprite](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TranslucentUnitSprite.md);
  `kernel-lib.h`.

### `flipped_enemy_sprites`

- **Value:** `true`
- **Behavior:** Mirrors eligible enemy map sprites.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `l_button_same_faction_cycling`

- **Value:** `true`
- **Behavior:** Not documented upstream beyond the field name.
- **Source:** Field in `kernel-lib.h` / `designer-config.c`.

### `no_suspend_in_aiphase`

- **Value:** `false`
- **Behavior:** When true, forbids suspend saves during AI phase. Abstract also
  notes suspend is saved at player-phase start.
- **Source:** Inferred from named call sites;
  [Abstract](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Abstract.md).

### `no_wait_after_trading`

- **Value:** `true`
- **Behavior:** Trading does not force the actor into a wait state.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `start_map_effects`

- **Value:** `false`
- **Behavior:** Pre-phase menu that lets the player pick one map-wide effect
  (stat/move, duration, target faction) before the chapter proceeds. One
  active effect per chapter.
- **Source:** [Start Map Effects](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/StartMapEffects.md);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `goal_escape`

- **Value:** `false`
- **Behavior:** Escape objective: units ending an action on an escape tile
  leave the map (kept in roster). Chapter ends when no deployed player units
  remain. Chapters must also set `GOAL_TYPE_ESCAPE`.
- **Source:** [Goal Escape](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ChapterGoals/Escape.md).

### `goal_timer`

- **Value:** `false`
- **Behavior:** Real-time countdown lose condition. Map HUD shows the clock;
  Status still shows the real objective. Per-chapter seconds live in
  `chapter_timers`. Zero seconds means no timer.
- **Source:** [Goal Timer](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ChapterGoals/Timer.md).

### `real_time_battle`

- **Value:** `false`
- **Behavior:** Enemies act on a timer during an open player phase. Upstream
  comment marks this broken.
- **Source:** `kernel-lib.h`; comment in `designer-config.c`.

### `real_time_enemy_interval_frames`

- **Value:** `60`
- **Behavior:** Frames between enemy action attempts when real-time battle is
  on. `60` is about 1 second.
- **Source:** `kernel-lib.h`; comment in `designer-config.c`.

### `real_time_refresh_frames`

- **Value:** `60 * 30`
- **Behavior:** Frames between soft unit refreshes / cooldown clears. `0`
  uses a 30-second default. Configured as 30 seconds.
- **Source:** `kernel-lib.h`; comment in `designer-config.c`.

### `lights_out_game`

- **Value:** `false`
- **Behavior:** Enables the Lights Out minigame. Off skips start and its
  event reward.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `fourth_allegiance`

- **Value:** `true`
- **Behavior:** Enables purple-faction gameplay. Off skips the purple phase;
  unit RAM/save layout stays expanded.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `vesly_danger_bones`

- **Value:** `false`
- **Behavior:** Enables danger-zone “bones” graphics.
- **Source:** Inferred from named call sites (no dedicated feature page).

---

## Battle and weapons

### `anima_weapon_triangle`

- **Value:** `false`
- **Behavior:** FE4/FE5 anima triangle: Fire beats Wind/Ice, Wind/Ice beats
  Thunder, Thunder beats Fire.
- **Source:** [Anima Triangle](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/AnimaTriangle.md).

### `apply_dynamic_nosferatu_battle_anim`

- **Value:** `true`
- **Behavior:** Marks dynamically detected Nosferatu-like attacks for HP-drain
  battle-animation effects (also applied to new spells).
- **Source:** Comment in `designer-config.c`; inferred from named call sites.

### `c03_do_not_flush_efx_status`

- **Value:** `true`
- **Behavior:** Keep status palette flashes through C03 (attack start). False
  is vanilla wipe of ids matching `0xC`.
- **Source:** Comment in `designer-config.c`.

### `display_status_flash_on_hit`

- **Value:** `true`
- **Behavior:** Battle-animation status flash comes from ext-hit, not
  `ANIM_ROUND_POISON`.
- **Source:** Comment in `designer-config.c`.

### `battle_max_damage`

- **Value:** `127`
- **Behavior:** Maximum calculated battle damage.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `battle_surrend_en`

- **Value:** `false`
- **Behavior:** Enables the surrounded-unit avoid penalty (Abstract:
  `avo -10%` per adjacent enemy side, plus `def -5` if boxed in; fliers
  outdoors are exempt).
- **Source:** Inferred from named call sites;
  [Abstract](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Abstract.md).

### `hit_decrease_on_range`

- **Value:** `false`
- **Behavior:** Three Houses-style hit loss for long-range attacks. Abstract
  specifies 10% hit lost per point of distance (non-ballista). Call sites
  apply the reduction beyond range 2.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  [Abstract](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Abstract.md);
  inferred from named call sites.

### `last_weapon_hit_crit`

- **Value:** `true`
- **Behavior:** Guarantees a critical when remaining weapon uses are less
  than or equal to that hit's durability cost. Unbreakable, `0xFF`-use, and
  special-slot weapons are excluded.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `s_rank_weapon_no_weight`

- **Value:** `true`
- **Behavior:** Removes weapon weight from attack-speed calculations at S
  rank. Abstract also notes S-rank weapons grant `atk +1`.
- **Source:** Inferred from named call sites;
  [Abstract](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Abstract.md).

### `dynamic_weapon_slots`

- **Value:** `true`
- **Behavior:** Remaps the eight `Unit::ranks` slots per class via
  `gClassWeaponSlotConf` so custom types (knives, guns) can occupy unused
  slots. False is vanilla slot `N` = type `N`.
- **Source:** [Dynamic Weapon Slots](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/DynamicWeaponSlots.md).

### `weapon_rank_skills`

- **Value:** `true`
- **Behavior:** Teaches table skills when a weapon letter rank is reached.
  Default Prowess chain is Lv1 at D through Lv5 at S; later levels replace
  earlier ones.
- **Source:** [Weapon Rank Skills](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/WeaponRankSkills.md).

### `wrank_bonux_rtext_auto_gen`

- **Value:** `true`
- **Behavior:** Automatically shows weapon-rank battle bonus information in
  the stat screen when available.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `infinite_durability`

- **Value:** `true`
- **Behavior:** Treats weapon durability as effectively unlimited in item
  display and use paths.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `auto_repair_weapons`

- **Value:** `false`
- **Behavior:** When enabled, repairs unit inventory weapons during the
  chapter-end / unit-refrain hook.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `arena_roster_menu`

- **Value:** `false`
- **Behavior:** Replaces the blind arena roll with a chapter-specific opponent
  board. Player picks a fight, sees wager/reward, and cleared entries gray
  out.
- **Source:** [Arena Roster](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ArenaRoster.md).

### `arena_show_opponent_in_advance`

- **Value:** `true`
- **Behavior:** Draws the chosen opponent's details before the wager is
  confirmed.
- **Source:** [Arena Roster](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ArenaRoster.md).

### `arena_let_player_use_upgraded_weapons`

- **Value:** `true`
- **Behavior:** Allows the player weapon generated for arena combat to
  upgrade from the base arena weapon.
- **Source:** [Arena Roster](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ArenaRoster.md).

### `arena_limits`

- **Value:** `false`
- **Behavior:** Applies chapter turn/level restrictions before arena access.
- **Source:** [Arena Roster](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ArenaRoster.md).

### `arena_calculate_weapon_based_on_level`

- **Value:** `true`
- **Behavior:** Selects the arena weapon upgrade stage from effective unit
  level; promoted units receive +20 effective levels.
- **Source:** Inferred from named call sites; related
  [Arena Roster](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ArenaRoster.md).

### `enemy_can_combo_attack`

- **Value:** `false`
- **Behavior:** Allows enemies to participate in combo attacks.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `engage_combo_attack`

- **Value:** `true`
- **Behavior:** Combo-attack path that requires `SID_ChainAttack`. Abstract
  describes combo attacks when an ally is in supporting range.
- **Source:** Comment in `designer-config.c`;
  [Abstract](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Abstract.md).

### `mokha_aoe_enabled`

- **Value:** `true`
- **Behavior:** Three Houses-style Gambit AOE on the unit menu. Eligible
  units (PID allowlist) pick an attack, choose a tile, and damage non-allied
  units in the area.
- **Source:** [Mokha AOE](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/MokhaAOE.md);
  `kernel-lib.h`.

### `banim_switcher_en`

- **Value:** `false`
- **Behavior:** Enables the Custom Banim Switcher patch (unit/class/weapon/
  target/skill/flag conditions can swap battle animations).
- **Source:** [Banim Features](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/BanimFeatures.md);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `vesly_fast_forward_battle_animations`

- **Value:** `false`
- **Behavior:** Enables fast-forward battle animations.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `vesly_draw_animations`

- **Value:** `true`
- **Behavior:** Plays extra map-action animations. Off keeps vanilla map
  anims; animation assets stay installed.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `ignore_stop_on_petrify_sleep`

- **Value:** `true`
- **Behavior:** Prevents petrify/sleep from automatically ending a battle
  sequence.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `show_heal_amount`

- **Value:** `true`
- **Behavior:** Displays the staff healing amount.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `show_true_2rn`

- **Value:** `true`
- **Behavior:** Permits the Options menu to display true 2RN hit rates. The
  player option must also be enabled.
- **Source:** `kernel-lib.h`; comment in `designer-config.c`; inferred from
  named call sites.

### `custom_staff_accuracy`

- **Value:** `100`
- **Behavior:** Replaces computed offensive-staff accuracy with this value,
  clamped to 0–100.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `modular_staff_exp`

- **Value:** `true`
- **Behavior:** Replaces hardcoded staff EXP with a `StaffEXP` table covering
  vanilla and custom staves, with room for conditional rules.
- **Source:** [Modular Staff EXP](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ModularStaffEXP.md).

### `summons_gain_exp`

- **Value:** `false`
- **Behavior:** When enabled, summoned units can grant EXP.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `leadership`

- **Value:** `true`
- **Behavior:** Enables Leadership stat and bonus handling. FEBuilder unit-page
  combo labels style `1` as "With LeaderShip".
- **Source:** Inferred from named call sites;
  [`combo.PageStyle_Unit.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.PageStyle_Unit.txt).

---

## Skills and progression

### `prep_menu_skills`

- **Value:** `true`
- **Behavior:** Enables Three Houses-style skill equipment in the prep
  screen. If disabled, the skill equip option is removed.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  [Skill System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillSys.md).

### `prep_menu_skill_synth`

- **Value:** `true`
- **Behavior:** Prep and world-map menu that combines two skill scrolls into
  a new scroll using `gSkillSynthRecipeTable`. Invalid pairs are rejected
  without consuming scrolls.
- **Source:** [Skill Synthesis](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillSynthesis.md).

### `gen_new_scroll`

- **Value:** `false`
- **Behavior:** When a unit uses a skill scroll with all equip slots full:
  `false`/`0` learns the skill for later prep equip (Three Houses style);
  `true`/`1` lets the player replace an equipped skill and generate a scroll.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  comment in `designer-config.c`.

### `max_equipable_skill`

- **Value:** `UNIT_RAM_SKILLS_LEN`
- **Behavior:** Maximum dynamically equipable skills per unit, from `0` to
  `7`.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  [Skill System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillSys.md).

### `debug_autoload_skills`

- **Value:** `false`
- **Behavior:** Debug option that fills a unit's learned skill list so skills
  can be freely equipped in prep.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `load_skills_through_feb_formatted_list`

- **Value:** `false`
- **Behavior:** FEBuilder-only skill list loading (old SkillSys `0x01-0xFF`
  list format).
- **Source:** Comment in `designer-config.c`;
  [Skill System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillSys.md).

### `skill_shop`

- **Value:** `false`
- **Behavior:** World-map node skill shop. Player spends BWL skill points on
  node-specific skills. Kill SP is granted when `skill_shop` or `skill_tree`
  is on.
- **Source:** [World Map Skill Shop](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/WorldMapSkillShop.md);
  [Skill Tree](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillTree.md).

### `skill_tree`

- **Value:** `false`
- **Behavior:** Enables the skill-tree system (including kill SP rewards
  shared with the skill shop). PoC tree is Eirika-only.
- **Source:** [Skill Tree](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillTree.md).

### `stat_page_skill_tree`

- **Value:** `false`
- **Behavior:** Registers the optional last status-screen page
  (`PAGE_SKILL_TREE = 7`).
- **Source:** [Skill Tree](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillTree.md).

### `tellius_skill_capacity_system`

- **Value:** `true`
- **Behavior:** FE9/FE10-style capacity: each skill has a cost, and a unit
  cannot learn a skill that would exceed remaining capacity. Known limits:
  only scroll learning checks capacity; capacity-reducing skills can overflow
  if removed.
- **Source:** [Tellius Skill Capacity](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TelliusSkillCapacity.md).

### `tellius_skill_capacity_base`

- **Value:** `50`
- **Behavior:** Starting skill capacity per unit.
- **Source:** [Tellius Skill Capacity](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TelliusSkillCapacity.md).

### `tellius_skill_capacity_promoted`

- **Value:** `25`
- **Behavior:** Extra capacity granted to promoted units.
- **Source:** [Tellius Skill Capacity](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TelliusSkillCapacity.md).

### `gaiden_magic`

- **Value:** `true`
- **Behavior:** Enables Gaiden-style black and white magic (HP-cost spells
  unless the MP system is also on).
- **Source:** [Gaiden Magic](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/GaidenMagic.md);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `gaiden_magic_must_be_magic`

- **Value:** `false`
- **Behavior:** When true, black-magic candidates must have `IA_MAGIC`. False
  allows non-magic items in those lists. System Config wording reverses this
  polarity.
- **Source:** Comment in `designer-config.c`; inferred from named call sites;
  [Gaiden Magic](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/GaidenMagic.md).

### `gaiden_magic_requires_wrank`

- **Value:** `false`
- **Behavior:** When true, normal weapon/staff rank usability is enforced.
  False means unrestricted Gaiden-magic use. System Config wording reverses
  this polarity.
- **Source:** Comment in `designer-config.c`; inferred from named call sites;
  [Gaiden Magic](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/GaidenMagic.md).

### `gaiden_magic_skill_extensions`

- **Value:** `true`
- **Behavior:** Enables the external `gGaidenChaxConfigs` magic-list table
  (character, class, level, faction, skill, event flag).
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  [Gaiden Magic](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/GaidenMagic.md).

### `mp_system`

- **Value:** `true`
- **Behavior:** Replaces Gaiden HP-cost casting with an FFTA2-style MP pool
  stored in BWL (up to 51 units). Units start chapters at 0 MP and gain MP
  each turn and/or after combat.
- **Source:** [MP System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/MpSystem.md).

### `max_level`

- **Value:** `UNIT_LEVEL_MAX_RE`
- **Behavior:** Maximum displayed unit level, from `0` to `25`.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `max_level_record`

- **Value:** `UNIT_RECORDED_LEVEL_MAX`
- **Behavior:** Maximum total level, including current and hidden level, from
  `0` to `80`.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  [Skill System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SkillSys.md).

### `guaranteed_lvup`

- **Value:** `false`
- **Behavior:** If a level-up would grant no stat gains, the kernel retries
  up to 10 times with a 10% growth bonus.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `lvup_mode_easy`

- **Value:** `0`
- **Behavior:** Per-difficulty growth mode. FEBuilder combo:
  `0` vanilla, `1` uncontrollable, `2` fixed, `3` 100%, `4` 0%. Config
  comment labels `1` as random.
- **Source:** [`combo.lvupmode.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.lvupmode.txt);
  comment in `designer-config.c`.

### `lvup_mode_normal`

- **Value:** `0`
- **Behavior:** Same modes as `lvup_mode_easy`, applied on Normal.
- **Source:** [`combo.lvupmode.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.lvupmode.txt).

### `lvup_mode_hard`

- **Value:** `0`
- **Behavior:** Same modes as `lvup_mode_easy`, applied on Hard.
- **Source:** [`combo.lvupmode.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.lvupmode.txt).

### `two_random_number_growths`

- **Value:** `false`
- **Behavior:** When enabled, uses the alternate two-random-number growth
  method.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `restore_hp_on_level_up`

- **Value:** `false`
- **Behavior:** When enabled, restores HP after a level-up.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `stat_gain_frame_speed`

- **Value:** `10`
- **Behavior:** Level-up stat-gain animation delay in frames.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `promotion_on_max_level`

- **Value:** `true`
- **Behavior:** Allows promotion when reaching the configured maximum level.
  Fires from the map level-up scroll-out path (same cleanup as in-chapter
  trainee promotion).
- **Source:** Inferred from named call sites;
  [Trainee In-Chapter Promotion](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TraineeInChapterPromotion.md).

### `promote_trainees_in_chapter`

- **Value:** `true`
- **Behavior:** Trainee classes (`CA_MAXLEVEL10`) promote immediately after
  the post-battle level-up screen at level 10, instead of waiting for the
  next chapter's prep screen.
- **Source:** [Trainee In-Chapter Promotion](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/TraineeInChapterPromotion.md).

### `promote_enemy_on_kill`

- **Value:** `true`
- **Behavior:** When an enemy kills a player unit and has a valid promotion,
  it promotes immediately and gains a flat stat boost.
- **Source:** [Enemies Promote When Killing a Unit](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/EnemiesPromoteWhenKillingUnit.md).

### `promote_enemy_boost`

- **Value:** `3`
- **Behavior:** Omni stat boost applied on enemy promotion-on-kill (default
  `+3` to all stats).
- **Source:** [Enemies Promote When Killing a Unit](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/EnemiesPromoteWhenKillingUnit.md).

### `prestige`

- **Value:** `true`
- **Behavior:** Unpromoted units at level 10+ can Prestige (max 3 times):
  reset to level 1 / base stats, clear status, refill HP, and gain `+10%`
  growths per prestige. Stars appear on the left stat page.
- **Source:** [Prestige](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Prestige.md).

### `vesly_reclass`

- **Value:** `false`
- **Behavior:** Makes the juna fruit a Heart Seal reclass item. Off uses
  vanilla juna fruit (name/icon stay Heart Seal).
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `laguz_bars`

- **Value:** `false`
- **Behavior:** Tellius laguz meter on the first 51 playable units (BWL).
  Bar size 30, start 10, +2/turn untransformed, −4/turn transformed;
  auto-revert at 0 and map end. Conflicts with the MP system are noted.
- **Source:** [Laguz Bars](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/LaguzBars.md).

### `biorhythm_mechanic`

- **Value:** `false`
- **Behavior:** FE9 biorhythm: per-character HIT/AVO cycle that advances one
  state per turn.
- **Source:** [Biorhythm](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Biorhythm.md).

### `pair_up_enabled`

- **Value:** `true`
- **Behavior:** Replaces Rescue with Pair Up, Shelter, Transfer, and Switch.
  Support unit contributes 30% of POW/MAG/SKL/SPD/LCK/DEF/RES/MOV. State is
  stored in vanilla rescue fields.
- **Source:** [Pair-Up](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/PairUp.md).

### `expanded_hp`

- **Value:** `true`
- **Behavior:** Raises HP maximum from 127 (UI-capped lower in vanilla) to
  254 in the minimug box and battle animations. Forecast/chapter screen still
  show `--` for large HP.
- **Source:** [Expanded HP](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ExpandedHP.md);
  `UNIT_MHP_MAX` in `kernel-lib.h`.

---

## Items, shops, and inventory

### `item_effect_revamp`

- **Value:** `true`
- **Behavior:** Item usability and effects dispatch from
  `ItemData::useEffectId` (`IERevamp` table) instead of item index. Also
  changes staff/vulnerary heal formulas and supports tonics.
- **Source:** [Item System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ItemSys.md).

### `custom_staves`

- **Value:** `true`
- **Behavior:** Enables custom staff items (Skill Staff, Aum, Phoenix,
  Arbalest, and others under `Data/CustomItems`).
- **Source:** [Skill Staff](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/CustomStaves/SkillStaff.md)
  and sibling Custom Staves pages.

### `custom_droppable_item_icon`

- **Value:** `true`
- **Behavior:** Uses the custom droppable-item icon.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `limited_shop_items`

- **Value:** `true`
- **Behavior:** Per-chapter purchase limits shared across all shops in that
  chapter, persisted in SRAM, shown in the shop UI (max 20 stocked items).
- **Source:** [Limited Shop Stock](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/LimitedShopStock.md).

### `prep_menu_infuse`

- **Value:** `true`
- **Behavior:** Prep forging that spends Dragon Glass to convert a convoy
  item using `gInfusionLookupTable`.
- **Source:** [Infuse Menu](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/InfuseMenu.md).

### `forge_mechanic`

- **Value:** `false`
- **Behavior:** Enables forged-item durability and stat bonuses. Separate from
  Infuse.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `shield_system`

- **Value:** `false`
- **Behavior:** Second equippable item that applies battle/unit/growth
  corrections and optional battle-only skills. Durability can consume on
  attack, defense, and/or only on hit.
- **Source:** [Shield Item](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ShieldItem.md).

### `shield_ext_equip_config_en`

- **Value:** `false`
- **Behavior:** Enables extended PID/class/event/skill shield-equipment rules
  used with the shield system.
- **Source:** Inferred from named call sites; related
  [Shield Item](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ShieldItem.md).

### `kill_rewards`

- **Value:** `true`
- **Behavior:** Awards a configured item when a specific killer/victim pair
  appears in combat (player survivor only). Complements vanilla drop flags.
- **Source:** [Kill Rewards](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/KillRewards.md).

### `send_inventory_on_death`

- **Value:** `true`
- **Behavior:** Transfers a dead unit’s inventory according to the custom
  death logic.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `collect_dead_units`

- **Value:** `true`
- **Behavior:** Retains dead units for systems such as Necromancy.
- **Source:** Inferred from named call sites (no dedicated feature page).

---

## Menus, UI, and stat screen

### `quality_of_life_fixes`

- **Value:** `true`
- **Behavior:** Bundle of UI/flow tweaks: Avd label, unit-name popups,
  smoother solo epilogue, crit clamped to 100, skip trade faces with
  `portraitId = 0`, compact weapon-rank helpbox, QoL support event, world-map
  Home command.
- **Source:** [Quality of Life](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/QualityOfLife.md).

### `auto_narrow_font`

- **Value:** `true`
- **Behavior:** Converts ASCII text to narrow font for skill descriptions,
  skill names, and menu items.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `skill_sub_menu_width`

- **Value:** `10`
- **Behavior:** Width of the action menu's Skills submenu.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `text_box_extension_layout`

- **Value:** `2`
- **Behavior:** Help-box overflow: `0` vanilla truncate (3 lines), `1`
  extended up to 5 lines, `2` paginated 3-line box (A cycles pages, gold
  `n/m`).
- **Source:** [Paginated Help Boxes](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/PaginatedHelpBoxes.md);
  `kernel-lib.h`.

### `unit_page_style`

- **Value:** `1`
- **Behavior:** Stat screen page 1 style. Source comments and the config
  comment treat `1` as the BWL page and `2` as Leadership. FEBuilder combo
  labels `0` With BWL and `1` With LeaderShip. Numbering is inconsistent
  across those sources.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  comment in `designer-config.c`;
  [`combo.PageStyle_Unit.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.PageStyle_Unit.txt).

### `stat_page_skill_style`

- **Value:** `0`
- **Behavior:** Skill page style. Config comment: `0` named list, `1`
  unnamed grid. FEBuilder combo: `0` Mokha plan A, `1` Mokha plan B.
- **Source:** Comment in `designer-config.c`;
  [`combo.PageStyle_Skill.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.PageStyle_Skill.txt);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md)
  (`skill_page_style`).

### `stat_screen_growths`

- **Value:** `2`
- **Behavior:** `1` letter grades, `2` numeric/bonus growths in green. Other
  values use the alternate numeric display.
- **Source:** Comment in `designer-config.c`; inferred from named call sites.

### `stat_screen_allegiance_colors`

- **Value:** `true`
- **Behavior:** Tints the stat screen background blue/red/green/gold from the
  unit's allegiance. Off uses the vanilla palette.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `display_terrain_bonuses_in_stat_screen`

- **Value:** `true`
- **Behavior:** Displays DEF/RES terrain bonuses on the stat screen.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `res_terrain_window`

- **Value:** `true`
- **Behavior:** Shows DEF, RES, and AVO on the map terrain window. Off uses
  vanilla DEF/AVO.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `stat_page_gaiden_magic`

- **Value:** `true`
- **Behavior:** Optional Gaiden Magic stat-screen page. Also chapter-locked
  until `CHAPTER_06` even when enabled.
- **Source:** [Stat Screen Chapter Locks](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/StatScreenChapterLocks.md);
  [MP System](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/MpSystem.md).

### `stat_page_personal_info`

- **Value:** `false`
- **Behavior:** Optional Personal Data stat-screen page. Chapter-locked until
  `CHAPTER_08` when enabled.
- **Source:** [Stat Screen Chapter Locks](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/StatScreenChapterLocks.md).

### `stat_page_promotions`

- **Value:** `true`
- **Behavior:** Dedicated stat-screen page showing up to three promotion
  options and up to three skills each, with R-text. Chapter-locked until
  `CHAPTER_10`.
- **Source:** [Stat Screen Promotions](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/StatScreenPromotions.md);
  [Stat Screen Chapter Locks](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/StatScreenChapterLocks.md).

### `deny_stat_screen_access`

- **Value:** `true`
- **Behavior:** Blocks stat-screen access under configured map/fog conditions
  (Fog Stages also uses `CanShowUnitStatScreen` for stages 1–3).
- **Source:** Inferred from named call sites;
  [Fog Stages](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/FogStages.md).

### `custom_menu_options`

- **Value:** `true`
- **Behavior:** Intended extra menu options, but no
  `gpKernelDesignerConfig->custom_menu_options` dereference was found in the
  current upstream tree. Treat as stale/inert until rewired.
- **Source:** Field in `kernel-lib.h` / `designer-config.c`; related
  [Unlimited Prep Menu Options](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/UnlimitedPrepMenuOptions.md).

### `menu_option_refuge`

- **Value:** `false`
- **Behavior:** Enables the Refuge menu skill.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `custom_guide`

- **Value:** `true`
- **Behavior:** Shows the custom Guide command and table. Off hides Guide.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `map_menu_character_biographies`

- **Value:** `false`
- **Behavior:** Map-menu Character Biographies command: scrollable playable
  list, per-character music, four CG/text pages each.
- **Source:** [Character Biographies](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/CharacterBiographies.md).

### `prep_menu_augury`

- **Value:** `true`
- **Behavior:** Prep Augury option: chapter-indexed hint text and optional
  BGM (`gAuguryTable`).
- **Source:** [Augury Menu](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/AuguryMenu.md).

### `prep_menu_base_conversations`

- **Value:** `false`
- **Behavior:** Prep base conversations with per-entry background, music, and
  optional item. Replays allowed; items awarded only once.
- **Source:** [Base Conversations Menu](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/BaseConversationsMenu.md).

### `prep_menu_bexp`

- **Value:** `true`
- **Behavior:** Prep Bonus EXP (FE9/FE10-style). Apply BEXP in increments of
  5; stronger units cost more. Grant via `ASMC(GrantBEXP)`.
- **Source:** [Bonus EXP Menu](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/BonusEXPMenu.md).

### `prep_menu_event_replay`

- **Value:** `false`
- **Behavior:** Prep Replay: two-level chapter/conversation list of already
  reached chapters, played through `StartTalkExt`.
- **Source:** [Conversation Viewer](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/ConversationViewer.txt).

### `vesly_custom_ui`

- **Value:** `true`
- **Behavior:** Enables Vesly custom UI / minimug rendering. Comment: about
  200KB per style (about 600KB so far).
- **Source:** Comment in `designer-config.c`; inferred from named call sites.

### `vesly_notification_window`

- **Value:** `false`
- **Behavior:** Shows map notification toasts. Off skips them; flag hooks
  stay installed.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `vesly_debugger`

- **Value:** `true`
- **Behavior:** Exposes the Vesly debugger map command. Prestige docs note it
  can inspect/edit BWL fields (including `prestigeAmt`) even when other flags
  are off.
- **Source:** Inferred from named call sites;
  [Prestige](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Prestige.md).

### `vesly_achievements`

- **Value:** `false`
- **Behavior:** Enables achievements and its menu option.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `chapter_names`

- **Value:** `true`
- **Behavior:** Draws FE7-style text chapter titles. Off uses vanilla
  chapter-title graphics.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `fe7_mode_select`

- **Value:** `false`
- **Behavior:** Documented as using the FE7 difficulty-select screen (off uses
  vanilla FE8 `NewNewGameDifficultySelect`). No active named runtime
  dereference was found in the current upstream tree.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `show_tutorial`

- **Value:** `1`
- **Behavior:** Documented as `0` never, `1` only on tutorial/easy mode, `2`
  always. Active source reads `gPlaySt.config.show_tutorial`; this designer
  field appears unused or only consumed by an unobserved offset.
- **Source:** [`combo.ktut_level.txt`](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Patches/combo.ktut_level.txt);
  comment in `designer-config.c`.

### `skip_intro`

- **Value:** `false`
- **Behavior:** When enabled, skips map intro effects.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `konami_style_bonus_screen`

- **Value:** `true`
- **Behavior:** If you press ↑↑↓↓←→←→BA at the title screen, then… (upstream
  page is intentionally a one-liner).
- **Source:** [Konami Code](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/KonamiCode.md);
  `kernel-lib.h`.

### `casual_mode`

- **Value:** `false`
- **Behavior:** Enables casual-mode death handling.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `use_chinese_character`

- **Value:** `false`
- **Behavior:** Uses the alternate Chinese-character stat-screen glyphs.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `fe8_rewritten_specific_changes`

- **Value:** `true`
- **Behavior:** Applies rewritten early-game Seth POW/SKL/SPD reductions.
- **Source:** Inferred from named call sites (no dedicated feature page).

---

## Dialogue, portraits, and world map

### `chatlog_enabled`

- **Value:** `true`
- **Behavior:** SELECT opens a Talk-scene overlay of the last 17 dialogue
  lines of the current chapter. Survives suspend, not normal saves. Off:
  vanilla SELECT, no glyph capture.
- **Source:** [Chatlog](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Chatlog.md);
  `kernel-lib.h`.

### `voice_acted_dialogue`

- **Value:** `true`
- **Behavior:** Enables WAV/DPCM voiced dialogue clips called from events
  (`SOUN`/`MUSC` of generated song IDs).
- **Source:** [Voice Acted Intros](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/VoiceActedIntros.md).

### `unit_selection_quotes`

- **Value:** `true`
- **Behavior:** Plays a random voiced clip when a unit is selected. Off skips
  playback; song-table assets stay installed.
- **Source:** [Unit Selection Quotes](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/UnitSelectionQuotes.md);
  [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md).

### `talk_on_level_up`

- **Value:** `true`
- **Behavior:** Units comment on level-ups: 0–2 points bad quote, 2–5 good,
  6+ great. Uses the text-engine rework for one-line boxes.
- **Source:** [Level Up Quotes](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/LevelUpQuotes.md).

### `custom_battle_quotes`

- **Value:** `true`
- **Behavior:** Selects the replacement battle-quote table. The
  `CustomBattleQuotes.md` page currently duplicates the defeat-quote writeup
  and does not describe this field.
- **Source:** Inferred from named call sites;
  [Custom Battle Quotes](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/CustomBattleQuotes.md)
  (stale contents).

### `custom_defeat_quotes`

- **Value:** `true`
- **Behavior:** Defeat quotes keyed on who died and who killed them, plus
  chapter/route/flag. Falls back to vanilla when off.
- **Source:** [Custom Defeat Quotes](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/CustomDefeatQuotes.md).

### `gameover_quotes`

- **Value:** `true`
- **Behavior:** Enables game-over quote playback. A preview GIF exists on the
  repo README; there is no dedicated Features page.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `custom_support_conversations`

- **Value:** `true`
- **Behavior:** Selects the replacement support-conversation table. The
  FEBuilder patch labels this field as DECIMAL, but the C header and call
  sites treat it as a Boolean.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `max_simultaneous_support_conversations`

- **Value:** `10`
- **Behavior:** Prep-screen support-conversation limit.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `unlock_all_supports`

- **Value:** `true`
- **Behavior:** Makes all configured supports available in the support viewer.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `support_rewards`

- **Value:** `true`
- **Behavior:** Grants support-conversation rewards.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `talk_conversation_exp_reward`

- **Value:** `10`
- **Behavior:** EXP awarded for talk conversations.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `vesly_support_after_battle`

- **Value:** `true`
- **Behavior:** Grants support progress after combat, dance, and staff
  actions, using the four rate fields below.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `vesly_support_after_battle_combat_rate`

- **Value:** `5`
- **Behavior:** Support gain after ordinary combat.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `vesly_support_after_battle_dance_rate`

- **Value:** `10`
- **Behavior:** Support gain after dancing.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `vesly_support_after_battle_kill_rate`

- **Value:** `10`
- **Behavior:** Support gain after a kill.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `vesly_support_after_battle_staff_rate`

- **Value:** `10`
- **Behavior:** Support gain after staff use.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `variable_unit_descriptions`

- **Value:** `false`
- **Behavior:** Unit descriptions can change from events/chapter (demo:
  Eirika). Up to three descriptions per unit. Call sites also vary
  descriptions with debuff/status state. Marked work-in-progress upstream.
- **Source:** [Variable Character Descriptions](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/VariableCharacterDescriptions.md);
  inferred from named call sites.

### `half_body_portraits`

- **Value:** `false`
- **Behavior:** FE9/FE10-style stacked halfbody portraits (32 colors via two
  16-color palettes) and shifted text boxes. False keeps vanilla portrait
  geometry. Incompatible with mixing mug formats; max two halfbodies at once.
- **Source:** [Halfbodies](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Halfbodies.md);
  `kernel-lib.h`.

### `portrait_32_color`

- **Value:** `false`
- **Behavior:** Pal1 overlay on the paired face VRAM/pal bank for 32-color
  mugs. Max two overlays. Incompatible with halfbodies on the same face.
- **Source:** [32-Color Portraits](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/Portrait32Color.md);
  `kernel-lib.h`.

### `custom_character_animations`

- **Value:** `true`
- **Behavior:** Enables custom per-character combat animations.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `custom_talk_icon`

- **Value:** `true`
- **Behavior:** Uses the custom talk icon.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `death_dance`

- **Value:** `true`
- **Behavior:** Changes rescue-drop handling so a rescued unit may remain
  selectable after the rescuer dies in applicable cases.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `max_color_backgrounds`

- **Value:** `true`
- **Behavior:** 224/256-color conversation backgrounds (IDs from `0x38`). Off
  loads BGs through the vanilla 16-color path.
- **Source:** [Max Color Backgrounds](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/MaxColorBackgrounds.md);
  `kernel-lib.h`.

### `show_cgs_like_fe7`

- **Value:** `true`
- **Behavior:** Lets `SHOWBG` events pick a 10-split ending CG by index. Off
  uses the `DisplayCGfx` idx argument only.
- **Source:** [System Config](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/SystemConfig.md);
  `kernel-lib.h`.

### `vesly_credits_cgs`

- **Value:** `true`
- **Behavior:** Enables CGs in Vesly credits.
- **Source:** Inferred from named call sites (no dedicated feature page).

### `base_chapters`

- **Value:** `false`
- **Behavior:** Dedicated base maps on world-map nodes (Three Houses
  monastery-style). First deployed unit enters free movement; talk/visit/shop/
  arena allowed, no field combat.
- **Source:** [Base Chapters](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/BaseChapters.md).

### `world_map_thought_bubbles`

- **Value:** `true`
- **Behavior:** Chapter-specific thought bubbles on selected world-map units.
  `R` cycles the prep roster; `A` on the unit's current node centers the
  camera.
- **Source:** [World Map Thoughts](https://github.com/JesterWizard/C-SkillSystem-Jester/blob/main/Documentation/Features/WorldMapThoughts.md).

### `reset_bwl_stats_each_chapter`

- **Value:** `true`
- **Behavior:** Not documented upstream beyond the field name.
- **Source:** Field in `kernel-lib.h` / `designer-config.c`.
