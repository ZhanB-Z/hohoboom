# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow [SemVer](https://semver.org/).
Before 1.0 the version is 0.<build>.<patch>.

## [0.38.0] — 2026-11-21
### Added
- New boss: the Giant Snowman on wave 15 in Standard and Hardcore. He throws fans of big snowballs, breaks off three snowmen with every quarter of health lost and shrinks. His Blizzard leaves Santa seeing only a small circle around himself.
- The Nutcracker throws fans of walnuts (they can be shot down), and every third throw a lump of caramel that leaves a sticky, slowing puddle.
- Boss reward: after a boss wave, pick any skill from the skill tree instead of four random upgrades.
- Skill details: click a skill on the skills screen (Tab) to see what each level gives.
- Classic look: open `index.html?classic` to see all characters drawn as in the first versions.
- Test mode: 5 gives Frost Nova, G summons the Giant Snowman.
### Changed
- Upgrade baubles are coloured by type: red for health, orange for damage, blue for bullets, green for movement, gold for gifts.
- Frost Shock hits up to 26 enemies instead of 16, jumps farther, thicker bolt.
- Garland sparks are thicker, glow and stay visible longer.
- Snow Whirlwind: larger radius, stronger push, reaches distant enemies too.
- Clearer upgrade descriptions with numbers per level.
- Kill-streak callouts are semi-transparent, smaller and shorter.
- Enemies stop at the edge of Santa's body instead of overlapping him; point-blank shots now hit.
- Snowmen throw off chunks of snow when hit.
- Frozen enemies are encased in a block of ice that cracks and shatters; the Snow Queen's ice spikes look three-dimensional.
### Fixed
- The subtitle on the skills screen was drawn in a huge font.

## [0.37.0] — 2026-11-19
### Added
- Three modes: Novice (15 waves), Standard (20) and Hardcore (25). Each mode ends with a victory screen.
- Bosses by mode: Krampus on wave 5, the Nutcracker on wave 10, the Snow Queen as the final boss. Standard ends with the Nutcracker and the Snow Queen together, Hardcore with all three bosses at once.
- Skills screen (Tab): every upgrade by branch (Weapons, Survival, Gifts and Luck) with its level. The game pauses while it is open.
- Each mode keeps its own record.
- Test mode: N ends the current wave, U jumps to the last wave.
### Changed
- Four upgrades to choose from after each wave instead of three.
- The wave counter shows the total, e.g. "Wave 7 / 20"; the last wave is announced as the finale.
- Esc on the game-over screen returns to mode selection.
### Removed
- The three unused upgrade-card designs (gifts, rarity cards, medals).
- The older Snow Queen versions kept in test mode for comparison.

## [0.36.0] — 2026-11-19
### Added
- Snow Queen images: walking, casting and two rage frames.
- Snow Queen fights in three phases, marked on her health bar. Second phase: she casts ice spikes that burst out of the ground under Santa or along his path. Third phase: she spins into a blizzard, vanishes and reappears next to Santa, and Santa is hurt and frozen if still there.
- Snow Queen moves smoothly: she glides, turns gradually and leans into her movement; her dress sways and trails behind her, leaving snow dust and frost marks.
- Test mode: K summons the Snow Queen, J takes a third of her health; the first waves show the Snow Queen alone, 10 lives.
- `tools/make_sprite_black.py` cuts a character out of a black background.
### Changed
- Snow Queen fires icicles instead of glowing balls.

## [0.35.0] — 2026-11-16
### Changed
- Ice Laser: one extra beam per Double Volley level (up to 4, fanned out); beam hits a 3× wider area.
- Ice Laser: steady pulsing hum instead of choppy blips; sizzle on hit.
- Christmas-Tree Mines: placed faster (every 0.35 s), up to 10 on the field, trigger from twice the distance, damage 9 instead of 7.
- Christmas-Tree Mines: an explosion sets off nearby mines; a mine explodes on its own after 7 s.
- Snowball Launcher: reload 0.45 s instead of 0.65 s, snowballs fly 1.4× faster.
### Added
- Slow motion in dangerous moments: a crowd right next to Santa, getting hit at 3 hearts or fewer, the last life.
- Slow motion after the Frost Shock, New Year Fireworks and Snow Whirlwind power-ups.
- Version number in the menu.

## [0.34.0]
### Added
- Slow motion for kill streaks: Massacre, Apocalypse, Dominating, Owning. At least 8 s between them.
### Changed
- Slow motion ends smoothly instead of snapping back.

## [0.33.0]
### Added
- Frost Shock power-up: an ice lightning bolt jumps across up to 16 enemies, damaging and freezing them.
### Changed
- Upgrade cards look like Christmas-tree baubles.
- Upgrade levels: the next level is marked green, the last level is labelled.
- Healing from kills is capped: at most 1 heart per wave from enemy drops and 1 per Christmas Spirit level.

## [0.32.0]
### Added
- Four upgrade-card designs to compare.
### Fixed
- The game no longer gets stuck on the upgrade screen when every upgrade is maxed out.

## [0.31.0]
### Changed
- No heart gift in the first wave.
- Garland goes up to level 5.

## [0.30.0]
### Added
- Power-ups: Snow Whirlwind (knocks enemies back), Round Dance (rings of bullets in all directions), Frozen Time (enemies slowed for 6 s).
- Upgrades: Garland (a spark jumps to nearby enemies) and Lucky Clover (more gifts).
### Changed
- Bigger lime crosshair that turns red and shrinks over an enemy.
- Menu subtitle: "Save the New Year from the Snow Queen's army!"

## [0.29.0]
### Added
- Test mode at `index.html?debug`.
- Separate music, effects and voice volume in the pause menu (remembered).
- Loading screen; R to restart; short death animation for monsters.
### Changed
- Faster lighting; the background is built once after images load.
- The interface no longer shrinks with the playing field.
### Fixed
- A repeated announcer line is no longer cut short.

## [0.28.0]
### Changed
- The thrower's snowball leaves from its hand and is smaller.
- Clear rules for which announcer line plays when events overlap.

## [0.27.0]
### Changed
- Images and sounds sorted into folders under `Media/`.

## [0.26.0]
### Added
- Announcer voice: Double kill, Triple kill, Massacre, Dominating, You are owning.

## [0.25.0]
### Changed
- The first wave uses the "snow with frozen grass" ground.

## [0.24.0]
### Added
- Five ground surfaces, a different one each wave.

## [0.23.0]
### Added
- Permanent ice patches; the field layout changes every wave.
### Changed
- Fewer decorations.

## [0.22.0]
### Added
- Decorations: rocks, boulders, bushes, stumps, logs, snowdrifts, grass.

## [0.21.0]
### Changed
- Ice patches spread across the whole field.

## [0.20.0]
### Added
- Ice: Santa and monsters slide on it; "Wind! Ice!" trap.

## [0.19.0]
### Added
- Snow texture, tree images, footprints for every character (filled in by snow after 2–3 s).

## [0.18.0]
### Added
- Krampus: walking and charging images; the charge goes farther and faster.

## [0.17.0]
### Changed
- Snowballs 15% smaller.

## [0.16.0]
### Added
- Snowball image; enemy snowballs have a red outline.

## [0.15.0]
### Changed
- The monster spawn order lives in a single table.

## [0.14.0]
### Added
- Snowball-throwing snowman: walking and throwing images.

## [0.13.0]
### Added
- Elf archer: idle and aiming poses.

## [0.12.0]
### Added
- Snowmen, two kinds.

## [0.11.0]
### Added
- Gingerbread men, two kinds.
### Changed
- The slowing trap is now called Sticky Caramel.

## [0.10.0]
### Added
- Goblins, two kinds.
- A separate cartoon kids' version saved.

## [0.9.0]
### Changed
- New Santa image (top-down, no legs); bullets leave exactly from the muzzle.

## [0.8.0]
### Changed
- Lives shown as hearts on a panel, pulsing on the last life; enemies drop a heart instead of a gingerbread cookie.

## [0.7.0]
### Changed
- The playing field is 1.25× roomier.

## [0.6.0]
### Added
- Santa image instead of a code-drawn Santa.

## [0.5.0]
### Added
- A heart gift every wave.

## [0.4.0]
### Added
- Dramatic boss entrance: slow motion, camera zoom, name and subtitle, ominous sound.
- Weapon switching (Q, mouse wheel, 1–4).

## [0.3.0]
### Added
- Night lighting, shading on characters, shadows.

## [0.2.0]
### Added
- 14 upgrades between waves; gift weapons: Snowball Launcher, Ice Laser, Christmas-Tree Mines; a boss every 5 waves.

## [0.1.0]
### Added
- First version: Santa fights off waves of monsters; gifts hold power-ups and traps.
