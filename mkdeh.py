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

	# -- Keys:

	# Blue key -> Blue skull key:
	79: replacement(sprite_to_mobj(SPR_BSKU)),
	# Green key -> Red skull key:
	73: replacement(sprite_to_mobj(SPR_RSKU)),
	# Yellow key -> Yellow skull key:
	80: replacement(sprite_to_mobj(SPR_YSKU)),


	# -- Hard to map artifacts
	#
	#     30	Artifact	Morph Ovum
	#     34	Artifact	Time Bomb
	#     23	Artifact	Wings of Wrath
	#     36	Artifact*	Chaos Device (random teleport)
	#     86	Artifact	Tome of Power
	#     33	Artifact	Torch
	30: None,
	34: None,
	23: None,
	36: None,
	86: None,
	33: None,

	# -- Decorations:

	# Barrel -> Barrel:
	44: replacement(MT_BARREL),
###     47	Blob*		Brown Pillar
###     -> Short green pillar
###     28	Blob		Chandelier			*NB
###     -> Candelabra
###     76	Blob		Fire Brazier
###     51	Blob*		Hanging Corpse
###     94	Blob		Blue Key Statue
###     -> Tall blue fire stick
###     95	Blob		Green Key Statue
###     -> Tall green fire stick
###     96	Blob		Yellow Key Statue
###     -> Tall red fire stick
###     48	Blob		Moss1				*NB
###     49	Blob		Moss2				*NB
###     27	Blob		Serpent Torch
###     26	Blob		Hanging Skull 35	 	*NB
###     25	Blob		Hanging Skull 45	 	*NB
###     24	Blob		Hanging Skull 60		*NB
###     17	Blob		Hanging Skull 70	 	*NB
###     29	Blob		Small Pillar
###     -> Short red pillar
###     40	Blob*		Stalactite (large)
###     39	Blob*		Stalactite (small)
###     38	Blob		Stalagmite (large)
###     37	Blob		Stalagmite (small)
###     87	Blob*		Volcano				*NB
###     50	Blob		Wall Torch		 	*NB
###    2035	Thingy		Pod
###     43	Thingy		Pod Generator
###     74	Teleport	Glitter
###     -> None (decorative; maybe recreate the effect somehow)
###     52	Teleport	Glitter Exit
###     -> None (decorative; maybe recreate the effect somehow)
###    
###    ## Monsters
###    
###     66	Monster		Gargoyle
###     -> Lost Soul?
###      5	Monster		Gargoyle Leader
###     68	Monster		Golem
###     -> Zombie
###     69	Monster		Golem Ghost
###     45	Monster		Golem Leader
###     -> Shotgun Guy
###     46	Monster		Golem Leader Ghost
###     64	Monster		Undead Warrior
###     -> Imp
###     65	Monster		Undead Warrior Ghost
###     15	Monster		Disciple
###     -> Cacodemon?
###     70	Monster*	Weredragon
###     -> Baron?
###     90	Monster*	Sabreclaw
###     -> Demon?
###      6	Monster		Ironlich
###     -> Cacodemon? But with more hit points
###      9	Monster*	Maulotaur
###     -> Baron?
###     92	Monster*	Ophidian
###     -> Imp?
###      7	Monster*	D'Sparil
###     -> Cyberdemon
###     56	Monster*	D'Sparil Spot
###     -> Nothing
###    
###    ## Map to empty objects (do nothing)
###    
###    1202	Sound A1 	Waterdrip
###    1203	Sound A1	Slow Footsteps
###    1204	Sound A1	Heartbeat
###    1205	Sound A1	Bells
###    1208	Sound A1	Laughter
###    1209	Sound A1	Fast Footsteps
###    1200	Sound A2*	Scream
###    1201	Sound A2*	Squish
###    1206	Sound A2*	Growl
###    1207	Sound A2*	Magic
###     42	Sound E1	Wind
###     41	Sound E2*	Waterfall
###    
###    
###    
}

