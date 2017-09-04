Heretic in many ways a reskin of Doom, completed in a very short
timeframe in early 1994.  This project aims to create a minimal
compatibility WAD to make Heretic levels playable with `doom.wad`.

The main components are:

* Replacement `TEXTURE1`/`TEXTURE2` lumps. These aim to recreate
  compatible versions of Heretic's wall textures using Doom's texture
  patches. Ideally, for the sake of minimalism no new patches should
  be included unless it proves absolutely necessary.

* Compatibly-named replacements for Heretic's flats (floor and ceiling
  textures). For the sake of consistency, we reuse textures from Doom.
  The distributed WAD will include the version from Freedoom.

* `ANIMATED` lump, so that Heretic's switches and animated textures will
  animate as intended in Boom-compatible source ports.

* Dehacked patch to map `doomednum` for all of Heretic's thing types
  into equivalent thing types found in Doom.

