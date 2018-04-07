#!/usr/bin/env python
#
# This script generates the dehacked patch for htic4doom.
#
# The general idea here is to map all of Heretic's thing types into
# Doom thing types. Some of these are more difficult than others, and
# in some cases we have to duplicate things.

from deh9000 import *

def replacement(thing_type, **kwargs):
	return (thing_type, kwargs)

things = {
	# Teleport exit:
	14: replacement(MT_TELEPORTMAN),

	# -- Weapons:

	# Gauntlets of the Necromancer -> Chainsaw:
	2005: replacement(MT_MISC26),
	# Ethereal Crossbow -> Shotgun:
	2001: replacement(MT_SHOTGUN),
	# Dragon Claw -> Chaingun:
	53: replacement(MT_CHAINGUN),
	# Hellstaff -> Plasma Rifle:
	2004: replacement(MT_MISC28),
	# Phoenix Rod -> Rocket Launcher:
	2003: replacement(MT_MISC27),
	# Mace -> BFG9000:
	2002: replacement(MT_MISC25),

	# -- Ammo:
	# Heretic has more ammo types than Doom has, so some of these
	# end up getting duplicated, as appropriate for the weapon
	# substitutions listed above.

	# Wand Crystal -> Ammo clip:           [Wand]
	10: replacement(MT_CLIP),
	# Wand Geode -> Box of bullets:
	12: replacement(MT_MISC17),
	# Ethereal Arrows -> Shotgun shells:   [Ethereal Crossbow]
	18: replacement(MT_MISC22),
	# Ethereal Quiver -> Box of shells:
	19: replacement(MT_MISC23),
	# Claw Orb -> Ammo clip:               [Dragon claw]
	54: replacement(MT_CLIP),
	# Energy Orb -> Box of bullets:
	55: replacement(MT_MISC17),
	# Lesser Runes -> Plasma cell:         [Hellstaff]
	20: replacement(MT_MISC20),
	# Greater Runes -> Plasma pack:
	21: replacement(MT_MISC21),
	# Flame orb -> Rocket:                 [Phoenix rod]
	22: replacement(MT_MISC18),
	# Inferno orb -> Box of rockets:
	23: replacement(MT_MISC19),
	# Mace spheres -> Plasma cell:         [Mace]
	13: replacement(MT_MISC20),
	# Pile of mace spheres -> Plasma pack:
	16: replacement(MT_MISC21),
	# Bag of holding -> Backpack
	8: replacement(MT_MISC24),

	# -- Powerups:

	# Mystic urn -> Supercharge:
	32: replacement(MT_MISC12),
	# Quartz Flask -> Medikit:
	82: replacement(MT_MISC11),
	# Crystal vial -> Stimpack:
	81: replacement(MT_MISC10),
	# Shadowsphere -> Partial invisibility:
	75: replacement(MT_MISC16),
	# Ring of invulnerability -> Invulnerability:
	84: replacement(MT_INV),
	# Silver shield -> Green armor:
	85: replacement(MT_MISC0),
	# Enchanted shield -> Blue armor:
	31: replacement(MT_MISC1),
	# Map scroll -> Automap:
	35: replacement(MT_MISC15),

	# -- Keys:

	# Blue key -> Blue skull key:
	79: replacement(MT_MISC9),
	# Green key -> Red skull key:
	73: replacement(MT_MISC8),
	# Yellow key -> Yellow skull key:
	80: replacement(MT_MISC7),


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

