Heretic in many ways a reskin of Doom. Many technical details are
(almost) identical between the two games, including level format,
linedef and sector types. With this in mind, this project is a hack to
see if Heretic levels can be made loadable and playable with `doom.wad`.

The main components are:

* Replacement `TEXTURE1`/`TEXTURE2` lumps. These aim to recreate
  compatible versions of Heretic's wall textures using Doom's texture
  patches. Ideally, for the sake of minimalism no new patches should
  be included unless it proves absolutely necessary.

* Compatibly-named replacements for Heretic's flats (floor and ceiling
  textures). For the sake of consistency, we reuse textures from Doom.
  The distributed WAD will include the version from Freedoom.

* `ANIMATED` and `SWITCHES` lump, so that Heretic's switches and
  animated textures will animate as intended in Boom-compatible source
  ports.

* Dehacked patch to map `doomednum` for all of Heretic's thing types
  into equivalent thing types found in Doom.

### Limitations

The WAD has a number of limitations in practice:

* It won't work if another PWAD is loaded that contains its own
  `TEXTURE1`/`TEXTURE2` lumps, since the Heretic patches will be missing
  from the WAD directory.

* Because of some buggy code in `P_LoadThings()`, levels will fail to
  load with vanilla (or Chocolate) Doom. Usually it's possible to walk
  around the level but many monsters and items will be missing.
  This is caused by a clash between Heretic thing types and Doom II
  monster types. Levels will load fine if there are none of the
  following present: Golem; Undead Warrior; Golem Ghost; Undead Warrior
  Ghost; Gargoyle; Ring of Invulnerability. Unfortunately this includes
  some of the most common Heretic monsters.

* Heretic levels in practice can end up looking very ugly and
  repetitive. This is because Heretic itself has a very small set of
  textures, the replacements (constructed from Doom textures) can end up
  looking mismatched or inappropriate, and texture alignment inevitably
  ends up being messed up.

* Not all Heretic powerups map to Doom ones in any obvious way. In
  particular if levels rely on using the Wings of Wrath to make progress
  then they probably aren't completable.

* Sometimes line triggers don't work as intended. Heretic has a few
  linedef types which don't match Doom. These include the fast stair
  builder types (106/107), triple-speed door (100) and secret exit
  (105). This can sometimes make levels uncompletable or necessitate
  the use of cheats to finish them.

* Heretic has additional sector types which control friction, scrolling
  and wind effects. Doom doesn't support these and vanilla will crash if
  you walk into a sector of one of these types.

