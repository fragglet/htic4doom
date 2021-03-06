#!/usr/bin/env python
#
# This script generates the dehacked patch for htic4doom.
#
# The general idea here is to map all of Heretic's thing types into
# Doom thing types. Some of these are more difficult than others, and
# in some cases we have to duplicate things.

from __future__ import print_function
from deh9000 import *

def sprite_to_mobj(sprite_num):
	"""Given a sprite used by a single mobj, get that mobj."""
	mobjtypes = set()
	for mobjtype, mobj in enumerate(mobjinfo):
		sprites = set()
		for statenum in dehfile.mobj_states(mobjtype):
			sprites.add(states[statenum].sprite)
		if sprite_num in sprites:
			mobjtypes.add(mobjtype)
	if len(mobjtypes) != 1:
		raise ValueError('want one mobj type for sprite %d, '
		                 'got multiple: %r' % (
			sprite_num, mobjtypes,
		))
	return list(mobjtypes)[0]

def replacement(thing_type, **kwargs):
	return (thing_type, kwargs)

heretic_to_doom = {
	# Teleport exit:
	14: replacement(MT_TELEPORTMAN),

	# -- Weapons:

	# Gauntlets of the Necromancer -> Chainsaw:
	2005: replacement(sprite_to_mobj(SPR_CSAW)),
	# Ethereal Crossbow -> Shotgun:
	2001: replacement(sprite_to_mobj(SPR_SHOT)),
	# Dragon Claw -> Chaingun:
	53: replacement(sprite_to_mobj(SPR_MGUN)),
	# Hellstaff -> Plasma Rifle:
	2004: replacement(sprite_to_mobj(SPR_PLAS)),
	# Phoenix Rod -> Rocket Launcher:
	2003: replacement(sprite_to_mobj(SPR_LAUN)),
	# Mace -> BFG9000:
	2002: replacement(sprite_to_mobj(SPR_BFUG)),

	# -- Ammo:
	# Heretic has more ammo types than Doom has, so some of these
	# end up getting duplicated, as appropriate for the weapon
	# substitutions listed above.

	# Wand Crystal -> Ammo clip:           [Wand]
	10: replacement(sprite_to_mobj(SPR_CLIP)),
	# Wand Geode -> Box of bullets:
	12: replacement(sprite_to_mobj(SPR_AMMO)),
	# Ethereal Arrows -> Shotgun shells:   [Ethereal Crossbow]
	18: replacement(sprite_to_mobj(SPR_SHEL)),
	# Ethereal Quiver -> Box of shells:
	19: replacement(sprite_to_mobj(SPR_SBOX)),
	# Claw Orb -> Ammo clip:               [Dragon claw]
	54: replacement(sprite_to_mobj(SPR_CLIP)),
	# Energy Orb -> Box of bullets:
	55: replacement(sprite_to_mobj(SPR_AMMO)),
	# Lesser Runes -> Plasma cell:         [Hellstaff]
	20: replacement(sprite_to_mobj(SPR_CELL)),
	# Greater Runes -> Plasma pack:
	21: replacement(sprite_to_mobj(SPR_CELP)),
	# Flame orb -> Rocket:                 [Phoenix rod]
	22: replacement(sprite_to_mobj(SPR_ROCK)),
	# Inferno orb -> Box of rockets:
	23: replacement(sprite_to_mobj(SPR_BROK)),
	# Mace spheres -> Plasma cell:         [Mace]
	13: replacement(sprite_to_mobj(SPR_CELL)),
	# Pile of mace spheres -> Plasma pack:
	16: replacement(sprite_to_mobj(SPR_CELP)),
	# Bag of holding -> Backpack
	8: replacement(sprite_to_mobj(SPR_BPAK)),

	# -- Powerups:

	# Mystic urn -> Supercharge:
	32: replacement(sprite_to_mobj(SPR_SOUL)),
	# Quartz Flask -> Medikit:
	82: replacement(sprite_to_mobj(SPR_MEDI)),
	# Crystal vial -> Stimpack:
	81: replacement(sprite_to_mobj(SPR_STIM)),
	# Shadowsphere -> Partial invisibility:
	75: replacement(sprite_to_mobj(SPR_PINS)),
	# Ring of invulnerability -> Invulnerability:
	84: replacement(sprite_to_mobj(SPR_PINV)),
	# Silver shield -> Green armor:
	85: replacement(sprite_to_mobj(SPR_ARM1)),
	# Enchanted shield -> Blue armor:
	31: replacement(sprite_to_mobj(SPR_ARM2)),
	# Map scroll -> Automap:
	35: replacement(sprite_to_mobj(SPR_PMAP)),
	# Torch -> Light amp goggles:
	33: replacement(sprite_to_mobj(SPR_PVIS)),
	# The following get very tenuous...
	# Wings of Wrath -> Rad suit:
	# (because you can use them to fly over lava?)
	83: replacement(sprite_to_mobj(SPR_SUIT)),
	# Tome of power -> Berserk pack:
	86: replacement(sprite_to_mobj(SPR_PSTR)),
	# Morph ovum -> Energy cell pack:
	30: replacement(sprite_to_mobj(SPR_CELP)),
	# Time bomb -> Rocket:
	34: replacement(sprite_to_mobj(SPR_ROCK)),
	# Chaos device -> Box of shells:
	36: replacement(sprite_to_mobj(SPR_SBOX)),

	# -- Keys:

	# Blue key -> Blue skull key:
	79: replacement(sprite_to_mobj(SPR_BSKU)),
	# Green key -> Red skull key:
	73: replacement(sprite_to_mobj(SPR_RSKU)),
	# Yellow key -> Yellow skull key:
	80: replacement(sprite_to_mobj(SPR_YSKU)),

	# -- Decorations:

	# Barrel -> Barrel:
	44: replacement(MT_BARREL),
	# Brown pillar -> Short green pillar:
	47: replacement(sprite_to_mobj(SPR_COL2)),
	# Serpent Torch -> Tech lamp:
	27: replacement(sprite_to_mobj(SPR_COLU)),
	# Candelabra -> delete (we have no equivalent):
	28: None,
	# Fire brazier -> Skull pillar:
	76: replacement(sprite_to_mobj(SPR_FSKU)),
	# Hanging corpse -> hanging corpse:
	51: replacement(MT_MISC60),
	# TODO: Match these to remapped key colors.
	# Blue key statue -> Tall blue fire stick:
	94: replacement(sprite_to_mobj(SPR_TBLU)),
	# Green key statue -> Tall red fire stick:
	95: replacement(sprite_to_mobj(SPR_TRED)),
	# Yellow key statue -> Yellow candelabra:
	96: replacement(sprite_to_mobj(SPR_CBRA)),
	# Hanging moss sprites:
	48: None,
	49: None,
	# Hanging skulls:
	26: replacement(MT_MISC57),
	25: replacement(MT_MISC57),
	24: replacement(MT_MISC57),
	17: replacement(MT_MISC57),
	# Small pillar -> Short red pillar:
	29: replacement(sprite_to_mobj(SPR_COL4)),
	# Stalactite (large):
	40: None,
	# Stalactite (small):
	39: None,
	# Stalagmite (large):
	38: replacement(sprite_to_mobj(SPR_SMIT)),
	# Stalagmite (small):
	37: replacement(sprite_to_mobj(SPR_SMIT),
	                spawnstate=S_STALAG),
	# Volcano:
	87: None,
	# Wall torch -> Small red torch:
	50: replacement(sprite_to_mobj(SPR_SMRT)),
	# Pod:
	2035: None,
	# Pod generator:
	43: None,
	# Teleport glitter:   -- TODO: Recreate using Doom frames?
	74: None,
	# Teleport glitter exit:
	52: None,

	# -- Monsters:
	# Health is overridden here to match the health of the associated
	# Heretic monsters. Radius is also overridden to match, so that
	# monsters cannot get stuck in spaces when Doom monster is larger.

	# Gargoyle -> Lost soul:
	66: replacement(
		MT_SKULL,
		damage=1,
		radius=16 * FRACUNIT,
		spawnhealth=40,
	),
	# Gargoyle leader -> Lost soul:
	5: replacement(
		MT_SKULL,
		damage=1,
		radius=16 * FRACUNIT,
		spawnhealth=80,
	),
	# Golem -> Zombieman:
	68: replacement(
		MT_POSSESSED,
		spawnhealth=80,
		radius=22 * FRACUNIT,
	),
	# Golem Ghost -> Zombieman:
	69: replacement(
		MT_POSSESSED,
		spawnhealth=80,
		flags=MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL|MF_SHADOW,
		radius=22 * FRACUNIT,
	),
	# Golem Leader -> Shotgun guy
	45: replacement(
		MT_SHOTGUY,
		spawnhealth=100,
		radius=22 * FRACUNIT,
	),
	# Golem Leader ghost -> Shotgun guy:
	46: replacement(
		MT_SHOTGUY,
		spawnhealth=100,
		flags=MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL|MF_SHADOW,
		radius=22 * FRACUNIT,
	),
	# Undead Warrior -> Imp:
	64: replacement(
		MT_TROOP,
		spawnhealth=200,
		radius=24 * FRACUNIT,
	),
	# Undead Warrior Ghost -> Imp:
	65: replacement(
		MT_TROOP,
		spawnhealth=200,
		radius=24 * FRACUNIT,
		flags=MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL|MF_SHADOW,
	),
	# Disciple -> Cacodemon:
	15: replacement(
		MT_HEAD,
		spawnhealth=180,
		radius=16 * FRACUNIT,
	),
	# Weredragon -> Imp:
	70: replacement(
		MT_TROOP,
		spawnhealth=220,
		radius=32 * FRACUNIT,
	),
	# Sabreclaw -> Demon:
	90: replacement(
		MT_SERGEANT,
		spawnhealth=150,
		radius=20 * FRACUNIT,
	),
	# Iron lich -> Cacodemon:
	6: replacement(
		MT_HEAD,
		spawnhealth=700,
		radius=40 * FRACUNIT,
		speed=6,
		flags=MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL|(3<<MF_TRANSSHIFT),
	),
	# Maulotaur -> Baron:
	9: replacement(
		MT_BRUISER,
		spawnhealth=3000,
		radius=28 * FRACUNIT,
		speed=16,
	),
	# Ophidian -> Imp:
	92: replacement(
		MT_TROOP,
		spawnhealth=280,
		radius=22 * FRACUNIT,
	),
	# D'Sparil -> Cyberdemon:
	7: replacement(
		MT_CYBORG,
	),
	# D'Sparil Spot:
	56: None,

	# Atmospheric sound objects:
	1200: None,
	1201: None,
	1202: None,
	1203: None,
	1204: None,
	1205: None,
	1206: None,
	1207: None,
	1208: None,
	1209: None,
	41: None,
	42: None,
}

# Build reverse mapping table.
doom_to_heretics = {}
for heretic, vals in heretic_to_doom.items():
	if vals is not None:
		doom, _ = vals
		doom_to_heretics.setdefault(doom, set()).add(heretic)

# Identify all objects with a doomednum (ie. can be placed via the editor).
# This is our working space of objects we will change.
placeable_objects = [mobjtype for mobjtype, mobj in enumerate(mobjinfo)
                     if mobj.doomednum >= 0]

# We need to assign Heretic objects to Doom ones, but in some cases multiple
# Heretic objects map to the same Doom object. We want to keep affinity so
# that (1) when there is a 1:1 mapping of h->d, d will be used for h;
# (2) when there is a N:1 mapping of [h]->d, one of h will be used for d.

# Do a first pass through doom_to_heretics of assigning a single Heretic
# object for each Doom one. This will ensure affinity.
for doom, heretics in doom_to_heretics.items():
	heretic = sorted(heretics)[0]
	_, overrides = heretic_to_doom[heretic]
	mobjinfo[doom].update(overrides)
	mobjinfo[doom].doomednum = heretic
	heretics.remove(heretic)
	placeable_objects.remove(doom)

def non_monster_object():
	"""Returns an object from placeable_objects that is not a monster."""
	while True:
		mobjnum = placeable_objects.pop()
		if (mobjinfo[mobjnum].flags & MF_COUNTKILL) == 0:
			return mobjnum
		# placeable_objects is treated as a circular buffer; keep
		# popping objects and rolling them round to the beginning
		# until we find one we can use.
		placeable_objects.insert(0, mobjnum)

# Now do a second pass assigning all remaining duplicates.
for doom, heretics in doom_to_heretics.items():
	for heretic in heretics:
		_, overrides = heretic_to_doom[heretic]
		mobjnum = non_monster_object()
		mobjinfo[mobjnum].copy_from(mobjinfo[doom].original)
		mobjinfo[mobjnum].update(overrides)
		mobjinfo[mobjnum].doomednum = heretic

# Some Heretic objects are marked as "None" which means we just want these
# objects to not appear in game. To make this happen we create a "null
# state" that lasts 1 tic before jumping directly to S_NULL which deletes
# the object.
null_state = list(dehfile.reclaim_states(1))[0]
states[null_state].update({
	'tics': 1,
	'sprite': SPR_TFOG,
	'frame': 6,
	'nextstate': S_NULL,
})
for heretic, vals in heretic_to_doom.items():
	if vals is None:
		mobjnum = placeable_objects.pop()
		mobjinfo[mobjnum].update({
			'spawnstate': null_state,
			'flags': 0,
			'doomednum': heretic,
		})

# We have some leftover objects which haven't been assigned to any Heretic
# object. To ensure their doomednums don't clash with Heretic ones, set
# them all to -1.
for mobjnum in placeable_objects:
	mobjinfo[mobjnum].doomednum = -1

dehfile.save("htc4doom.deh")


