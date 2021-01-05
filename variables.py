from basic_functions import *

padded_armor = Armor(
	name='PADDED',
	armor_type='LIGHT',
	weight=8,
	armor_class=1,
	cost=5,
	stealth_disadvantage=True,
)

leather_armor = Armor(
	name='LEATHER',
	armor_type='LIGHT',
	weight=10,
	armor_class=1,
	cost=10,
)

studded_leather_armor = Armor(
	name='STUDDED LEATHER',
	armor_type='LIGHT',
	weight=13,
	armor_class=2,
	cost=45,
)

hide_armor = Armor(
	name='HIDE',
	armor_type='MEDIUM',
	weight=12,
	armor_class=2,
	cost=10,
	dex_max=2,
)

chain_shirt_armor = Armor(
	name='CHAIN SHIRT',
	armor_type='MEDIUM',
	weight=20,
	armor_class=3,
	cost=50,
	dex_max=2,
)

scale_mail_armor = Armor(
	name='SCALE MAIL',
	armor_type='MEDIUM',
	weight=45,
	armor_class=4,
	cost=50,
	stealth_disadvantage=True,
	dex_max=2,
)

breastplate_armor = Armor(
	name='BREASTPLATE',
	armor_type='MEDIUM',
	weight=20,
	armor_class=4,
	cost=400,
	dex_max=2,
)

half_plate_armor = Armor(
	name='HALF PLATE',
	armor_type='MEDIUM',
	weight=40,
	armor_class=5,
	cost=750,
	stealth_disadvantage=True,
	dex_max=2,
)

ring_mail_armor = Armor(
	name='RING MAIL',
	armor_type='HEAVY',
	weight=40,
	armor_class=4,
	cost=30,
	stealth_disadvantage=True,
	dex_max=0,
)

chain_mail_armor = Armor(
	name='CHAIN MAIL',
	armor_type='HEAVY',
	weight=55,
	armor_class=6,
	cost=75,
	stealth_disadvantage=True,
	dex_max=0,
	strength=13
)

splint_armor = Armor(
	name='SPLINT',
	armor_type='HEAVY',
	weight=60,
	armor_class=7,
	cost=200,
	stealth_disadvantage=True,
	dex_max=0,
	strength=15
)

plate_armor = Armor(
	name='PLATE',
	armor_type='HEAVY',
	weight=65,
	armor_class=8,
	cost=1500,
	stealth_disadvantage=True,
	dex_max=0,
	strength=15
)

shield = Armor(
	name='SHIELD',
	armor_type='SHIELD',
	weight=6,
	armor_class=2,
	cost=10,
)

club = Weapon(
	name='CLUB',
	damage_type='BLUDGEONING',
	melee=True,
	simple=True,
	cost=0.1,
	weight=2,
	properties=['LIGHT']
)

dagger = Weapon(
	name='DAGGER',
	damage_type='PIERCING',
	melee=True,
	simple=True,
	cost=2,
	weight=1,
	properties=['FINESSE', 'LIGHT', 'THROWN (RANGE 20/60)'],
)

greatclub = Weapon(
	name='GREATCLUB',
	damage_type='BLUDGEONING',
	melee=True,
	simple=True,
	cost=0.2,
	damage=Dice(maximum=8),
	weight=10,
	properties=['TWO-HANDED'],
)

handaxe = Weapon(
	name='HANDAXE',
	damage_type='SLASHING',
	melee=True,
	simple=True,
	cost=5,
	damage=Dice(maximum=6),
	weight=2,
	properties=['LIGHT', 'THROWN (RANGE 20/60)'],
)

javelin = Weapon(
	name='JAVELIN',
	damage_type='PIERCING',
	melee=True,
	simple=True,
	cost=0.5,
	damage=Dice(maximum=6),
	weight=2,
	properties=['THROWN (RANGE 30/120)'],
)

light_hammer = Weapon(
	name='LIGHT HAMMER',
	damage_type='BLUDGEONING',
	melee=True,
	simple=True,
	cost=2,
	weight=2,
	properties=['LIGHT', 'THROWN (RANGE 20/60)'],
)

mace = Weapon(
	name='MACE',
	damage_type='BLUDGEONING',
	melee=True,
	simple=True,
	cost=5,
	damage=Dice(maximum=6),
	weight=4,
)

quarterstaff = Weapon(
	name='QUARTERSTAFF',
	damage_type='BLUDGEONING',
	melee=True,
	simple=True,
	cost=0.2,
	damage=Dice(maximum=6),
	weight=4,
	properties=['VERSATILE (1D8)'],
)

sickle = Weapon(
	name='SICKLE',
	damage_type='SLASHING',
	melee=True,
	simple=True,
	cost=1,
	weight=2,
	properties=['LIGHT'],
)

spear = Weapon(
	name='SPEAR',
	damage_type='PIERCING',
	melee=True,
	simple=True,
	cost=1,
	damage=Dice(maximum=6),
	weight=3,
	properties=['THROWN (RANGE 20/60)', 'VERSATILE (1D8)'],
)

unarmed_strike = Weapon(
	name='UNARMED ATTACK',
	damage_type='BLUDGEONING',
	simple=True,
	melee=True,
	damage=Dice(maximum=1),
)

light_crossbow = Weapon(
	name='LIGHT CROSSBOW',
	damage_type='PIERCING',
	ranged=True,
	simple=True,
	cost=25,
	damage=Dice(maximum=8),
	weight=5,
	properties=['AMMUNITION (RANGE 80/320)', 'LOADING', 'TWO-HANDED'],
)

dart = Weapon(
	name='DART',
	damage_type='PIERCING',
	ranged=True,
	simple=True,
	cost=0.05,
	weight=0.25,
	properties=['FINESSE', 'THROWN (RANGE 20/60)'],
)

shortbow = Weapon(
	name='SHORTBOW',
	damage_type='PIERCING',
	ranged=True,
	simple=True,
	cost=25,
	damage=Dice(maximum=6),
	weight=2,
	properties=['AMMUNITION (RANGE 80/320)', 'TWO-HANDED'],
)

sling = Weapon(
	name='SLING',
	damage_type='BLUDGEONING',
	ranged=True,
	simple=True,
	cost=0.1,
	properties=['AMMUNITION (RANGE 30/120)'],
)

battleaxe = Weapon(
	name='BATTLEAXE',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=10,
	damage=Dice(maximum=8),
	weight=4,
	properties=['VERSATILE (1D10)'],
)

flail = Weapon(
	name='FLAIL',
	damage_type='BLUDGEONING',
	melee=True,
	martial=True,
	cost=10,
	damage=Dice(maximum=8),
	weight=2,
)

glaive = Weapon(
	name='GLAIVE',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=20,
	damage=Dice(maximum=10),
	weight=6,
	properties=['HEAVY', 'REACH', 'TWO-HANDED'],
)

greataxe = Weapon(
	name='GREATAXE',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=30,
	damage=Dice(maximum=12),
	weight=7,
	properties=['HEAVY', 'TWO-HANDED'],
)

greatsword = Weapon(
	name='GREATSWORD',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=50,
	damage=Dice(number=2, maximum=6),
	weight=6,
	properties=['HEAVY', 'TWO-HANDED'],
)

halberd = Weapon(
	name='HALBERD',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=20,
	damage=Dice(maximum=10),
	weight=6,
	properties=['HEAVY', 'REACH', 'TWO-HANDED'],
)

lance = Weapon(
	name='LANCE',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=10,
	damage=Dice(maximum=12),
	weight=6,
	properties=['REACH', 'SPECIAL'],
)

longsword = Weapon(
	name='LONGSWORD',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=15,
	damage=Dice(maximum=8),
	weight=3,
	properties=['VERSATILE (1D10)'],
)

maul = Weapon(
	name='MAUL',
	damage_type='BLUDGEONING',
	melee=True,
	martial=True,
	cost=10,
	damage=Dice(number=2, maximum=6),
	weight=10,
	properties=['HEAVY', 'TWO-HANDED'],
)

morningstar = Weapon(
	name='MORNINGSTAR',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=15,
	damage=Dice(maximum=8),
	weight=4,
)

pike = Weapon(
	name='PIKE',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=5,
	damage=Dice(maximum=10),
	weight=18,
	properties=['HEAVY', 'REACH', 'TWO-HANDED'],
)

rapier = Weapon(
	name='RAPIER',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=25,
	damage=Dice(maximum=8),
	weight=2,
	properties=['FINESSE'],
)

scimitar = Weapon(
	name='SCIMITAR',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=25,
	damage=Dice(maximum=6),
	weight=3,
	properties=['FINESSE', 'LIGHT'],
)

shortsword = Weapon(
	name='SHORTSWORD',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=10,
	damage=Dice(maximum=6),
	weight=2,
	properties=['FINESSE', 'LIGHT'],
)

trident = Weapon(
	name='TRIDENT',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=5,
	damage=Dice(maximum=6),
	weight=4,
	properties=['THROWN (RANGE 20/60)', 'VERSATILE (1D8)'],
)

war_pick = Weapon(
	name='WAR PICK',
	damage_type='PIERCING',
	melee=True,
	martial=True,
	cost=5,
	damage=Dice(maximum=8),
	weight=2,
)

warhammer = Weapon(
	name='WARHAMMER',
	damage_type='BLUDGEONING',
	melee=True,
	martial=True,
	cost=15,
	damage=Dice(maximum=8),
	weight=2,
	properties=['VERSATILE (1D10)'],
)

whip = Weapon(
	name='WHIP',
	damage_type='SLASHING',
	melee=True,
	martial=True,
	cost=2,
	weight=3,
	properties=['FINESSE', 'REACH'],
)

blowgun = Weapon(
	name='BLOWGUN',
	damage_type='PIERCING',
	ranged=True,
	martial=True,
	cost=10,
	damage=Dice(maximum=1),
	weight=1,
	properties=['AMMUNITION (RANGE 25/100', 'LOADING'],
)

hand_crossbow = Weapon(
	name='HAND CROSSBOW',
	damage_type='PIERCING',
	ranged=True,
	martial=True,
	cost=75,
	damage=Dice(maximum=6),
	weight=3,
	properties=['AMMUNITION (RANGE 30/120)', 'LIGHT', 'LOADING'],
)

heavy_crossbow = Weapon(
	name='HEAVY CROSSBOW',
	damage_type='PIERCING',
	ranged=True,
	martial=True,
	cost=50,
	damage=Dice(maximum=10),
	weight=18,
	properties=[
		'AMMUNITION (RANGE 100/400)', 'HEAVY', 'LOADING', 'TWO-HANDED'
	]
)

longbow = Weapon(
	name='LONGBOW',
	damage_type='PIERCING',
	ranged=True,
	martial=True,
	cost=50,
	damage=Dice(maximum=8),
	weight=2,
	properties=['AMMUNITION (RANGE 150/600)', 'HEAVY', 'TWO-HANDED'],
)

net = Weapon(
	name='NET',
	damage_type='NONE',
	ranged=True,
	martial=True,
	cost=1,
	damage=Dice(number=0),
	weight=3,
	properties=['SPECIAL', 'THROWN (RANGE 5/15)'],
)

abacus = AdventuringGear(
	name='ABACUS',
	cost=2,
	weight=2,
)

acid = AdventuringGear(
	name='ACID (VIAL)',
	cost=25,
	weight=1,
)

alchemists_fire = AdventuringGear(
	name='ALCHEMIST\'S FIRE',
	cost=50,
	weight=1,
)

ammunition = {
	'ARROWS': AdventuringGear(
		name='ARROWS',
		cost=1,
		weight=1,
		units=20
	),
	'BLOWGUN NEEDLES': AdventuringGear(
		name='BLOWGUN NEEDLES',
		cost=1,
		weight=1,
		units=50
	),
	'CROSSBOW BOLTS': AdventuringGear(
		name='CROSSBOW BOLTS',
		cost=1,
		weight=1.5,
		units=20
	),
	'SLING BULLETS': AdventuringGear(
		name='SLING BULLETS',
		cost=0.04,
		weight=1.5,
		units=20
	),
}

antitoxin = AdventuringGear(
	name='ANTITOXIN',
	cost=50,
)

arcane_focus = {
	'CRYSTAL': AdventuringGear(
		name='CRYSTAL (ARCANE FOCUS)',
		cost=10,
		weight=1,
	),
	'ORB': AdventuringGear(
		name='ORB (ARCANE FOCUS)',
		cost=20,
		weight=3,
	),
	'ROD': AdventuringGear(
		name='ROD (ARCANE FOCUS)',
		cost=10,
		weight=2,
	),
	'STAFF': AdventuringGear(
		name='STAFF (ARCANE FOCUS)',
		cost=5,
		weight=4,
	),
	'WAND': AdventuringGear(
		name='WAND (ARCANE FOCUS)',
		cost=10,
		weight=1,
	),
}

backpack = AdventuringGear(
	name='BACKPACK',
	cost=2,
	weight=5,
)

ball_bearings = AdventuringGear(
	name='BALL BEARINGS',
	cost=1,
	weight=2,
	units=1000,
)

barrel = AdventuringGear(
	name='BARREL',
	cost=2,
	weight=70,
)

basket = AdventuringGear(
	name='BASKET',
	cost=0.4,
	weight=2,
)

bedroll = AdventuringGear(
	name='BEDROLL',
	cost=1,
	weight=7,
)

bell = AdventuringGear(
	name='BELL',
	cost=1,
)

blanket = AdventuringGear(
	name='BLANKET',
	cost=0.5,
	weight=3,
)

block_and_tackle = AdventuringGear(
	name='BLOCK AND TACKLE',
	cost=1,
	weight=5,
)

book = AdventuringGear(
	name='BOOK',
	cost=25,
	weight=5,
)

glass_bottle = AdventuringGear(
	name='GLASS BOTTLE',
	cost=2,
	weight=2,
)

bucket = AdventuringGear(
	name='BUCKET',
	cost=0.05,
	weight=2,
)

caltrops = AdventuringGear(
	name='CALTROPS',
	cost=1,
	weight=2,
	units=20,
)

candle = AdventuringGear(
	name='CANDLE',
	cost=0.01,
)

crossbow_bolt_case = AdventuringGear(
	name='CROSSBOW BOLT CASE',
	cost=1,
	weight=1,
)

map_or_scroll_case = AdventuringGear(
	name='MAP OR SCROLL CASE',
	cost=1,
	weight=1,
)

chain = AdventuringGear(
	name='CHAIN',
	cost=5,
	weight=10,
	size=10
)

chalk = AdventuringGear(
	name='CHALK',
	cost=0.01,
)

chest = AdventuringGear(
	name='CHEST',
	cost=5,
	weight=25,
)

climbers_kit = AdventuringGear(
	name='CLIMBER\'S KIT',
	cost=25,
	weight=12,
)

clothes = {
	'COMMON': AdventuringGear(
		name='COMMON CLOTHES',
		cost=0.5,
		weight=3,
	),
	'COSTUME': AdventuringGear(
		name='COSTUME CLOTHES',
		cost=5,
		weight=4,
	),
	'FINE': AdventuringGear(
		name='FINE CLOTHES',
		cost=15,
		weight=6,
	),
	'TRAVELER\'S': AdventuringGear(
		name='TRAVELER\'S CLOTHES',
		cost=2,
		weight=4,
	),
}

component_pouch = AdventuringGear(
	name='COMPONENT POUCH',
	cost=25,
	weight=2,
)

crowbar = AdventuringGear(
	name='CROWBAR',
	cost=2,
	weight=5,
)

druidic_focus = {
	'SPRIG OF MISTLETOE': AdventuringGear(
		name='SPRIG OF MISTLETOE (DRUIDIC FOCUS)',
		cost=1,
	),
	'TOTEM': AdventuringGear(
		name='TOTEM (DRUIDIC FOCUS)',
		cost=1,
	),
	'WOODEN\'S STAFF': AdventuringGear(
		name='WOODEN\'S STAFF (DRUIDIC FOCUS)',
		cost=5,
		weight=4,
	),
	'YEW WAND': AdventuringGear(
		name='YEW BAND (DRUIDIC FOCUS)',
		cost=10,
		weight=1,
	),
}

fishing_tackle = AdventuringGear(
	name='FISHING TACKLE',
	cost=1,
	weight=4,
)

flask_or_tankard = AdventuringGear(
	name='FLASK OR TANKARD',
	cost=0.02,
	weight=1,
)

grappling_hook = AdventuringGear(
	name='GRAPPLING HOOK',
	cost=2,
	weight=4,
)

hammer = AdventuringGear(
	name='HAMMER',
	cost=1,
	weight=3,
)

sledge_hammer = AdventuringGear(
	name='SLEDGE HAMMER',
	cost=2,
	weight=10,
)

healers_kit = AdventuringGear(
	name='HEALER\'S KIT',
	cost=5,
	weight=3,
)

holy_symbol = {
	'AMULET': AdventuringGear(
		name='AMULET (HOLY SYMBOL)',
		cost=5,
		weight=1,
	),
	'EMBLEM': AdventuringGear(
		name='EMBLEM (HOLY SYMBOL)',
		cost=5,
	),
	'RELIQUARY': AdventuringGear(
		name='RELIQUARY (HOLY SYMBOL)',
		cost=5,
		weight=2,
	)
}

holy_water = AdventuringGear(
	name='HOLY WATER (FLASK)',
	cost=25,
	weight=1,
)

hourglass = AdventuringGear(
	name='HOURGLASS',
	cost=25,
	weight=1,
)

hunting_trap = AdventuringGear(
	name='HUNTING TRAP',
	cost=5,
	weight=25,
)

ink = AdventuringGear(
	name='INK',
	cost=10,
)

ink_pen = AdventuringGear(
	name='INK PEN',
	cost=0.02,
)

jug_or_pitcher = AdventuringGear(
	name='JUG OR PITCHER',
	cost=0.02,
	weight=4,
)

ladder = AdventuringGear(
	name='LADDER',
	cost=0.1,
	weight=25,
	size=10,
)

lamp = AdventuringGear(
	name='LAMP',
	cost=0.5,
	weight=1,
)

bullseye_lantern = AdventuringGear(
	name='BULLSEYE LANTERN',
	cost=10,
	weight=2,
)

hooded_lantern = AdventuringGear(
	name='HOODED LANTERN',
	cost=5,
	weight=2,
)

lock = AdventuringGear(
	name='LOCK',
	cost=10,
	weight=1,
)

magnifying_glass = AdventuringGear(
	name='MAGNIFYING GLASS',
	cost=100,
)

manacles = AdventuringGear(
	name='MANACLES',
	cost=2,
	weight=6,
)

mess_kit = AdventuringGear(
	name='MESS KIT',
	cost=0.2,
	weight=1,
)

steel_mirror = AdventuringGear(
	name='STEEL MIRROR',
	cost=5,
	weight=0.5,
)

oil = AdventuringGear(
	name='OIL (FLASK)',
	cost=0.1,
	weight=1,
)

paper = AdventuringGear(
	name='PAPER',
	cost=0.2,
)

parchment = AdventuringGear(
	name='PARCHMENT',
	cost=0.1,
)

perfume = AdventuringGear(
	name='PERFUME (VIAL)',
	cost=5,
)

miners_pick = AdventuringGear(
	name='MINER\'S PICK',
	cost=2,
	weight=10,
)

piton = AdventuringGear(
	name='PITON',
	cost=0.05,
	weight=0.25,
)

basic_poison = AdventuringGear(
	name='BASIC POISON (VIAL)',
	cost=100,
)

pole = AdventuringGear(
	name='POLE',
	cost=0.05,
	weight=7,
	size=10,
)

iron_pot = AdventuringGear(
	name='IRON POT',
	cost=2,
	weight=10,
)

potion_of_healing = AdventuringGear(
	name='POTION OF HEALING',
	cost=50,
	weight=0.5,
)

pouch = AdventuringGear(
	name='POUCH',
	cost=0.5,
	weight=1,
)

quiver = AdventuringGear(
	name='QUIVER',
	cost=1,
	weight=1,
)

portable_ram = AdventuringGear(
	name='PORTABLE RAM',
	cost=4,
	weight=35,
)

rations = AdventuringGear(
	name='RATIONS',
	cost=0.5,
	weight=2,
)

robes = AdventuringGear(
	name='ROBES',
	cost=1,
	weight=4,
)

hempen_rope = AdventuringGear(
	name='HEMPEN ROPE',
	cost=1,
	weight=10,
	size=50,
)

silk_rope = AdventuringGear(
	name='SILK ROPE',
	cost=10,
	weight=5,
	size=50
)

sack = AdventuringGear(
	name='SACK',
	cost=0.01,
	weight=0.5,
)

merchants_scale = AdventuringGear(
	name='MERCHANT\'S SCALE',
	cost=5,
	weight=3,
)

sealing_wax = AdventuringGear(
	name='SEALING WAX',
	cost=0.5,
)

shovel = AdventuringGear(
	name='SHOVEL',
	cost=2,
	weight=5,
)

signal_whistle = AdventuringGear(
	name='SIGNAL WHISTLE',
	cost=0.05,
)

signet_ring = AdventuringGear(
	name='SIGNET RING',
	cost=5,
)

soap = AdventuringGear(
	name='SOAP',
	cost=0.02,
)

spellbook = AdventuringGear(
	name='SPELLBOOK',
	cost=50,
	weight=3,
)

iron_spikes = AdventuringGear(
	name='IRON SPIKES',
	cost=1,
	weight=5,
	units=10,
)

spyglass = AdventuringGear(
	name='SPYGLASS',
	cost=1000,
	weight=1,
)

two_person_tent = AdventuringGear(
	name='TWO-PERSON TENT',
	cost=2,
	weight=20,
)

tinderbox = AdventuringGear(
	name='TINDERBOX',
	cost=0.5,
	weight=1,
)

torch = AdventuringGear(
	name='TORCH',
	cost=0.01,
	weight=1,
)

vial = AdventuringGear(
	name='VIAL',
	cost=1,
)

waterskin = AdventuringGear(
	name='WATERSKIN',
	cost=0.2,
	weight=5,
)

whetstone = AdventuringGear(
	name='WHETSTONE',
	cost=0.01,
	weight=1,
)

artisans_tools = {
	"ALCHEMIST'S SUPPLIES": Tool(
		name="ALCHEMIST'S SUPPLIES",
		cost=50,
		weight=8
	),
	"BREWER'S SUPPLIES": Tool(
		name="BREWER'S SUPPLIES",
		cost=20,
		weight=9
	),
	"CALLIGRAPHER'S SUPPLIES": Tool(
		name="CALLIGRAPHER'S SUPPLIES",
		cost=10,
		weight=5
	),
	"CARPENTER'S TOOLS": Tool(
		name="CARPENTER'S TOOLS",
		cost=8,
		weight=6
	),
	"CARTOGRAPHER'S TOOLS": Tool(
		name="CARTOGRAPHER'S TOOLS",
		cost=15,
		weight=6
	),
	"COBBLER'S TOOLS": Tool(
		name="COBBLER'S TOOLS",
		cost=5,
		weight=5
	),
	"COOK'S UTENSILS": Tool(
		name="COOK'S UTENSILS",
		cost=1,
		weight=8
	),
	"GLASSBOWER'S TOOLS": Tool(
		name="GLASSBOWER'S TOOLS",
		cost=30,
		weight=5
	),
	"JEWELER'S TOOLS": Tool(
		name="JEWELER'S TOOLS",
		cost=25,
		weight=2
	),
	"LEATHERWORKER'S TOOLS": Tool(
		name="LEATHERWORKER'S TOOLS",
		cost=5,
		weight=5
	),
	"MASON'S TOOLS": Tool(
		name="MASON'S TOOLS",
		cost=10,
		weight=8
	),
	"PAINTER'S SUPPLIES": Tool(
		name="PAINTER'S SUPPLIES",
		cost=10,
		weight=5
	),
	"POTTER'S TOOLS": Tool(
		name="POTTER'S TOOLS",
		cost=10,
		weight=3
	),
	"SMITH'S TOOLS": Tool(
		name="SMITH'S TOOLS",
		cost=20,
		weight=8
	),
	"TINKER'S TOOLS": Tool(
		name="TINKER'S TOOLS",
		cost=50,
		weight=10
	),
	"WEAVER'S TOOLS": Tool(
		name="WEAVER'S TOOLS",
		cost=1,
		weight=5
	),
	"WOODCARVER'S TOOLS": Tool(
		name="WOODCARVER'S TOOLS",
		cost=1,
		weight=5
	),
}

disguise_kit = Tool(
	name='DISGUISE KIT',
	cost=25,
	weight=3
)

forgery_kit = Tool(
	name='FORGERY KIT',
	cost=15,
	weight=5
)

gaming_set = {
	'DICE SET': Tool(
		name='DICE SET (GAMING SET)',
		cost=0.1,
	),
	'DRAGONCHESS SET': Tool(
		name='DRAGONCHESS SET (GAMING SET)',
		cost=1,
		weight=0.5
	),
	'PLAYING CARD SET': Tool(
		name='PLAYING CARD SET (GAMING SET)',
		cost=0.5,
	),
	'THREE-DRAGON ANTE SET': Tool(
		name='THREE-DRAGON ANTE SET (GAMING SET)',
		cost=1,
	)
}

herbalism_kit = Tool(
	name='HERBALISM KIT',
	cost=5,
	weight=3
)

musical_instrument = {
	'BAGPIPES': Tool(
		name='BAGPIPES (MUSICAL INSTRUMENT)',
		cost=30,
		weight=6
	),
	'DRUM': Tool(
		name='DRUM (MUSICAL INSTRUMENT)',
		cost=6,
		weight=3
	),
	'DULCIMER': Tool(
		name='DULCIMER (MUSICAL INSTRUMENT)',
		cost=25,
		weight=10
	),
	'FLUTE': Tool(
		name='FLUTE (MUSICAL INSTRUMENT)',
		cost=2,
		weight=1
	),
	'LUTE': Tool(
		name='LUTE (MUSICAL INSTRUMENT)',
		cost=35,
		weight=2
	),
	'LYRE': Tool(
		name='LYRE (MUSICAL INSTRUMENT)',
		cost=30,
		weight=2
	),
	'HORN': Tool(
		name='HORN (MUSICAL INSTRUMENT)',
		cost=3,
		weight=2
	),
	'PAN FLUTE': Tool(
		name='PAN FLUTE (MUSICAL INSTRUMENT)',
		cost=12,
		weight=2
	),
	'SHAWM': Tool(
		name='SHAWM (MUSICAL INSTRUMENT)',
		cost=2,
		weight=1
	),
	'VIOL': Tool(
		name='VIOL (MUSICAL INSTRUMENT)',
		cost=30,
		weight=1
	),
}

navigators_tools = Tool(
	name='NAVIGATOR\'S TOOLS',
	cost=25,
	weight=2
)

poisoners_kit = Tool(
	name='POISONER\'S KIT',
	cost=50,
	weight=2
)

thieves_kit = Tool(
	name='THIEVES\' TOOLS',
	cost=25,
	weight=1
)

tools_of_the_con = {
	'STOPPERED BOTTLES': AdventuringGear(
		name='STOPPERED BOTTLES FILLED WITH COLORED LIQUID',
		cost=0,
		units=10,
	),
	'WEIGHTED DICE': AdventuringGear(
		name='SET OF WEIGHTED DICE',
		cost=0
	),
	'MARKED CARDS': AdventuringGear(
		name='DECK OF MARKED CARDS',
		cost=0
	),
	'SIGNET RING': AdventuringGear(
		name='SIGNET RING OF AN IMAGINARY DUKE',
		cost=0
	)
}

packs = {
	'BURGLAR': [
		backpack, ball_bearings, bell, candle, candle, candle, candle, candle,
		crowbar, hammer, piton, piton, piton, piton, piton, piton, piton,
		piton, piton, piton, hooded_lantern, oil, oil, rations, rations,
		rations, rations, rations, tinderbox, waterskin, hempen_rope
	],
	'DIPLOMAT': [
		chest, map_or_scroll_case, map_or_scroll_case, clothes['FINE'], ink,
		ink_pen, lamp, oil, oil, paper, paper, paper, paper, paper, perfume,
		sealing_wax, soap
	],
	'DUNGEONEER': [
		backpack, crowbar, hammer, piton, piton, piton, piton, piton, piton,
		piton, piton, piton, piton, torch, torch, torch, torch, torch, torch,
		torch, torch, torch, torch, tinderbox, rations, rations, rations,
		rations, rations, rations, rations, rations, rations, rations,
		waterskin, hempen_rope
	],
	'ENTERTAINER': [
		backpack, bedroll, clothes['COSTUME'], clothes['COSTUME'], candle,
		candle, candle, candle, rations, rations, rations, rations, rations,
		waterskin, disguise_kit, candle,
	],
	'EXPLORER': [
		backpack, bedroll, mess_kit, tinderbox, torch, torch, torch,
		torch, torch, torch, torch, torch, torch, rations, rations, rations,
		rations, rations, rations, rations, rations, rations, rations,
		waterskin, hempen_rope, torch,
	],
	'PRIEST': [
		backpack, blanket, candle, candle, candle, candle, candle,
		candle, candle, candle, candle, tinderbox, rations, rations,
		waterskin, candle,
	],
	'SCHOLAR': [
		backpack, book, ink_pen, parchment, parchment, parchment, parchment,
		parchment, parchment, parchment, parchment, parchment, parchment, ink,
	]
}

camel = MountsAndVehicles(
	name='CAMEL',
	cost=50,
	speed=50,
	carrying_capacity=480
)

donkey_or_mule = MountsAndVehicles(
	name='DONKEY OR MULE',
	cost=8,
	speed=40,
	carrying_capacity=420
)

elephant = MountsAndVehicles(
	name='ELEPHANT',
	cost=200,
	speed=40,
	carrying_capacity=1320
)

draft_horse = MountsAndVehicles(
	name='DRAFT HORSE',
	cost=50,
	speed=40,
	carrying_capacity=540
)

riding_horse = MountsAndVehicles(
	name='RIDING HORSE',
	cost=75,
	speed=60,
	carrying_capacity=480
)

mastiff = MountsAndVehicles(
	name='MASTIFF',
	cost=25,
	speed=40,
	carrying_capacity=195
)

pony = MountsAndVehicles(
	name='PONY',
	cost=30,
	speed=40,
	carrying_capacity=225
)

warhorse = MountsAndVehicles(
	name='WARHORSE',
	cost=400,
	speed=60,
	carrying_capacity=540
)

galley = MountsAndVehicles(
	name='GALLEY',
	cost=30000,
	speed=4,
)

keelboat = MountsAndVehicles(
	name='KEELBOAT',
	cost=3000,
	speed=1,
)

longship = MountsAndVehicles(
	name='LONGSHIP',
	cost=10000,
	speed=3,
)

rowboat = MountsAndVehicles(
	name='ROWBOAT',
	cost=50,
	speed=1.5,
)

sailing_ship = MountsAndVehicles(
	name='SAILING SHIP',
	cost=10000,
	speed=2,
)

warship = MountsAndVehicles(
	name='WARSHIP',
	cost=25000,
	speed=2.5,
)

animal_trophy = Trinket('TROPHY FROM A ANIMAL YOU KILLED')

enemy_trophy = Trinket('TROPHY TAKEN FROM A FALLEN ENEMY')

quill = Trinket('QUILL')

small_knife = Trinket('SMALL KNIFE')

letter_from_colleague = Trinket(
	'LETTER FROM A DEAD COLLEAGUE POSING A QUESTION'
)

lucky_charm = Trinket('LUCKY CHARM')

insignia_rank = Trinket('INSIGNIA OF RANK')

city_map = Trinket('MAP OF THE CITY YOU GREW UP IN')

pet_mouse = Trinket('PET MOUSE')

parents_token = Trinket('TOKEN TO REMEMBER YOUR PARENTS BY')

incense = Trinket('INCENSE')

admirer_favor = {
	'LOVE LETTER': Trinket('LOVE LETTER'),
	'LOCK OF HAIR': Trinket('LOCK OF HAIR'),
	'TRINKET': Trinket('TRINKET')
}

guild_letter = Trinket('LETTER OF INTRODUCTION FROM YOUR GUILD')

winter_blanket = Trinket('WINTER BLANKET')

scroll_pedigree = Trinket('SCROLL OF PEDIGREE')

hill_dwarf = Race(
	name='HILL DWARF',
	ability_increase={'CON': 2, 'WIS': 1},
	size='MEDIUM',
	speed=25,
	languages=['COMMON', 'DWARVISH'],
	hit_point_increase=1,
	advantages=['SAVING THROWS AGAINST POISON'],
	resistances=['POISON DAMAGE'],
	weapon_proficiency=['BATTLEAXE', 'HANDAXE', 'HAMMER', 'WARHAMMER'],
	skills_proficiency=['HISTORY'],
	double_proficiency=['HISTORY'],
	tools_options=["SMITH'S TOOLS", "BREWER'S SUPPLIES", "MASON'S TOOLS"],
	features=['DARKVISION'],
	age=[50, 350],
	alignment='LAWFUL GOOD',
	height=[4, 5],
	magical_ability=MagicAbilities()
)

mountain_dwarf = Race(
	name='MOUNTAIN DWARF',
	ability_increase={'CON': 2, 'STR': 2},
	size='MEDIUM',
	speed=25,
	languages=['COMMON', 'DWARVISH'],
	advantages=['SAVING THROWS AGAINST POISON'],
	resistances=['POISON DAMAGE'],
	armor_proficiency=['LIGHT', 'MEDIUM'],
	weapon_proficiency=['BATTLEAXE', 'HANDAXE', 'HAMMER', 'WARHAMMER'],
	skills_proficiency=['HISTORY'],
	double_proficiency=['HISTORY'],
	tools_options=["SMITH'S TOOLS", "BREWER'S SUPPLIES", "MASON'S TOOLS"],
	features=['DARKVISION'],
	age=[50, 350],
	alignment='LAWFUL GOOD',
	height=[4, 5],
	magical_ability=MagicAbilities()
)

high_elf = Race(
	name='HIGH ELF',
	ability_increase={'DEX': 2, 'INT': 1},
	size='MEDIUM',
	speed=30,
	languages=['COMMON', 'ELVISH'],
	advantages=['SAVING THROWS AGAINST BEING CHARMED'],
	weapon_proficiency=['LONGSWORD', 'SHORTSWORD', 'SHORTBOW', 'LONGBOW'],
	skills_proficiency=['PERCEPTION'],
	features=['DARKVISION', 'TRANCE', 'EXTRA LANGUAGE'],
	age=[100, 750],
	alignment='CHAOTIC GOOD',
	height=[5, 6],
	magical_ability=MagicAbilities(
		has_magic=True,
		magical_ability='INT',
		cantrips_by_level={
			1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
			12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
		},
		cantrips_known=1,
		spell_list='WIZARD',
	)
)

wood_elf = Race(
	name='WOOD ELF',
	ability_increase={'DEX': 2, 'WIS': 1},
	size='MEDIUM',
	speed=35,
	languages=['COMMON', 'ELVISH'],
	advantages=['SAVING THROWS AGAINST BEING CHARMED'],
	weapon_proficiency=['LONGSWORD', 'SHORTSWORD', 'SHORTBOW', 'LONGBOW'],
	skills_proficiency=['PERCEPTION'],
	features=['DARKVISION', 'TRANCE', 'MASK OF THE WILD'],
	age=[100, 750],
	alignment='CHAOTIC GOOD',
	height=[5, 6],
)

dark_elf = Race(
	name='DARK ELF',
	ability_increase={'DEX': 2, 'CHA': 1},
	size='MEDIUM',
	speed=30,
	languages=['COMMON', 'ELVISH'],
	advantages=['SAVING THROWS AGAINST BEING CHARMED'],
	disadvantages=[
		'ATTACK ROLLS WHEN IN DIRECT SUNLIGHT',
		'PERCEPTION CHECKS WHEN IN DIRECT SUNLIGHT'
	],
	weapon_proficiency=['RAPIER', 'SHORTSWORD', 'HAND CROSSBOW'],
	skills_proficiency=['PERCEPTION'],
	features=['DROW MAGIC', 'SUPERIOR DARKVISION', 'TRANCE'],
	age=[100, 750],
	alignment='CHAOTIC EVIL',
	height=[5, 6],
	magical_ability=MagicAbilities(
		has_magic=True,
		magical_ability='CHA',
		cantrips_by_level={
			1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
			12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
		},
		spells_by_level={
			1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
			12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
		},
		spells_known=0,
		cantrips_known=1,
		highest_spell_level=2,
		cantrips=['DANCING LIGHTS', ]
	)
)

lightfoot_halfling = Race(
	name='LIGHTFOOT HALFLING',
	ability_increase={'DEX': 2, 'CHA': 1},
	size='SMALL',
	speed=25,
	languages=['COMMON', 'HALFLING'],
	advantages=['SAVING THROWS AGAINST BEING FRIGHTENED'],
	features=['LUCKY', 'HALFLING NIMBLENESS', 'NATURALLY STEALTHY'],
	age=[20, 250],
	alignment='LAWFUL GOOD',
	height=[3, 3]
)

stout_halfling = Race(
	name='STOUT HALFLING',
	ability_increase={'DEX': 2, 'CON': 1},
	size='SMALL',
	speed=25,
	languages=['COMMON', 'HALFLING'],
	advantages=[
		'SAVING THROWS AGAINST BEING FRIGHTENED',
		'SAVING THROWS AGAINST POISON'
	],
	resistances=['POISON DAMAGE'],
	features=['LUCKY', 'HALFLING NIMBLENESS'],
	age=[20, 250],
	alignment='LAWFUL GOOD',
	height=[3, 3]
)

human = Race(
	name='HUMAN',
	ability_increase={
		'STR': 1, 'DEX': 1, 'CON': 1, 'WIS': 1, 'INT': 1, 'CHA': 1
	},
	size='MEDIUM',
	speed=30,
	languages=['COMMON'],
	features=['EXTRA LANGUAGE'],
	age=[18, 90],
	alignment='ANY',
	height=[5, 6]
)

dragonborn = {
	'BLACK': Race(
		name='BLACK DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['ACID DAMAGE'],
		features=['BREATH WEAPON: 5 BY 30 FT LINE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'BLUE': Race(
		name='BLUE DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['LIGHTNING DAMAGE'],
		features=['BREATH WEAPON: 5 BY 30 FT LINE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'BRASS': Race(
		name='BRASS DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['FIRE DAMAGE'],
		features=['BREATH WEAPON: 5 BY 30 FT LINE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'BRONZE': Race(
		name='BRONZE DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['LIGHTNING DAMAGE'],
		features=['BREATH WEAPON: 5 BY 30 FT LINE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'COPPER': Race(
		name='COPPER DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['ACID DAMAGE'],
		features=['BREATH WEAPON: 5 BY 30 FT LINE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'GOLD': Race(
		name='GOLD DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['FIRE DAMAGE'],
		features=['BREATH WEAPON: 15 FT CONE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'GREEN': Race(
		name='GREEN DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['POISON DAMAGE'],
		features=['BREATH WEAPON: 15 FT CONE (CON SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'RED': Race(
		name='RED DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['FIRE DAMAGE'],
		features=['BREATH WEAPON: 15 FT CONE (DEX SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'SILVER': Race(
		name='SILVER DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['COLD DAMAGE'],
		features=['BREATH WEAPON: 15 FT CONE (CON SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	),
	'WHITE': Race(
		name='WHITE DRAGONBORN',
		ability_increase={'STR': 2, 'CHA': 1},
		size='MEDIUM',
		speed=30,
		languages=['COMMON', 'DRACONIC'],
		resistances=['COLD DAMAGE'],
		features=['BREATH WEAPON: 15 FT CONE (CON SAVE)'],
		age=[15, 80],
		alignment='GOOD',
		height=[6, 8]
	)
}

forest_gnome = Race(
	name='FOREST GNOME',
	ability_increase={'INT': 2, 'DEX': 1},
	size='SMALL',
	speed=25,
	languages=['COMMON', 'GNOMISH'],
	advantages=['INT, WIS, CHA SAVING THROWS AGAINST MAGIC'],
	features=['DARKVISION', 'SPEAK WITH SMALL BEASTS'],
	age=[40, 500],
	alignment='GOOD',
	height=[3, 4],
	magical_ability=MagicAbilities(
		has_magic=True,
		magical_ability='INT',
		cantrips_by_level={
			1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
			12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
		},
		cantrips_known=1,
		cantrips=['MINOR ILLUSION', ],
	)
)

rock_gnome = Race(
	name='ROCK GNOME',
	ability_increase={'INT': 2, 'CON': 1},
	size='SMALL',
	speed=25,
	languages=['COMMON', 'GNOMISH'],
	advantages=['INT, WIS, CHA SAVING THROWS AGAINST MAGIC'],
	tools_proficiency=['TINKER\'S TOOLS'],
	skills_proficiency=['HISTORY'],
	double_proficiency=['HISTORY'],
	features=['DARKVISION'],
	age=[40, 500],
	alignment='GOOD',
	height=[3, 4]
)

half_elf = Race(
	name='HALF-ELF',
	ability_increase={'CHA': 2},
	size='MEDIUM',
	speed=30,
	languages=['COMMON', 'ELVISH'],
	advantages=['SAVING THROWS AGAINST BEING CHARMED'],
	features=[
		'DARKVISION',
		'TWO ABILITIES INCREASE',
		'SKILL VERSATILITY',
		'EXTRA LANGUAGE'
	],
	age=[20, 180],
	alignment='CHAOTIC',
	height=[5, 6]
)

half_orc = Race(
	name='HALF-ORC',
	ability_increase={'STR': 2, 'CON': 1},
	size='MEDIUM',
	speed=30,
	languages=['COMMON', 'ORC'],
	skills_proficiency=['INTIMIDATION'],
	features=['DARKVISION', 'RELENTLESS ENDURANCE', 'SAVAGE ATTACKS'],
	age=[14, 75],
	alignment='CHAOTIC EVIL',
	height=[5, 7]
)

tiefling = Race(
	name='TIEFLING',
	ability_increase={'INT': 1, 'CHA': 2},
	size='MEDIUM',
	speed=30,
	languages=['COMMON', 'INFERNAL'],
	resistances=['FIRE DAMAGE'],
	features=['DARKVISION'],
	age=[18, 100],
	alignment='CHAOTIC EVIL',
	height=[5, 6],
	magical_ability=MagicAbilities(
		has_magic=True,
		magical_ability='CHA',
		cantrips_by_level={
			1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
			12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
		},
		spells_by_level={
			1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
			12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
		},
		cantrips_known=1,
		spells_known=0,
		highest_spell_level=2,
		cantrips=['THAUMATURGY']
	)
)

index = {
	'ABILITIES': {
		'STR': 'Strength',
		'DEX': 'Dexterity',
		'CON': 'Constitution',
		'INT': 'Intelligence',
		'WIS': 'Wisdom',
		'CHA': 'Charisma'
	},
	'RACES': {
		'HILL DWARF': hill_dwarf,
		'MOUNTAIN DWARF': mountain_dwarf,
		'HIGH ELF': high_elf,
		'WOOD ELF': wood_elf,
		'DARK ELF': dark_elf,
		'LIGHTFOOT HALFLING': lightfoot_halfling,
		'STOUT HALFLING': stout_halfling,
		'HUMAN': human,
		'DRAGONBORN': dragonborn,
		'FOREST GNOME': forest_gnome,
		'ROCK GNOME': rock_gnome,
		'HALF ELF': half_elf,
		'HALF ORC': half_orc,
		'TIEFLING': tiefling,
	},
	'DRAGONBORN': {
		'BLACK': dragonborn['BLACK'],
		'BLUE': dragonborn['BLUE'],
		'BRASS': dragonborn['BRASS'],
		'BRONZE': dragonborn['BRONZE'],
		'COPPER': dragonborn['COPPER'],
		'GOLD': dragonborn['GOLD'],
		'GREEN': dragonborn['GREEN'],
		'RED': dragonborn['RED'],
		'SILVER': dragonborn['SILVER'],
		'WHITE': dragonborn['WHITE'],
	},
	'CLASSES': [
		'BARBARIAN', 'BARD', 'CLERIC', 'DRUID', 'FIGHTER', 'MONK', 'PALADIN',
		'RANGER', 'ROGUE', 'SORCERER', 'WARLOCK', 'WIZARD',
	],
	'LANGUAGES': [
		'COMMON', 'DWARVISH', 'ELVISH', 'GIANT', 'GNOMISH', 'GOBLIN',
		'HALFLING', 'ORC', 'ABYSSAL', 'CELESTIAL', 'DRACONIC', 'DEEP SPEECH',
		'INFERNAL', 'PRIMORDIAL', 'SYLVAN', 'UNDERCOMMON',
	],
	'SKILLS': {
		'ATHLETICS': 'STR',
		'ACROBATICS': 'DEX',
		'SLEIGHT OF HAND': 'DEX',
		'STEALTH': 'DEX',
		'ARCANA': 'INT',
		'HISTORY': 'INT',
		'INVESTIGATION': 'INT',
		'NATURE': 'INT',
		'RELIGION': 'INT',
		'ANIMAL HANDLING': 'WIS',
		'INSIGHT': 'WIS',
		'MEDICINE': 'WIS',
		'PERCEPTION': 'WIS',
		'SURVIVAL': 'WIS',
		'DECEPTION': 'CHA',
		'INTIMIDATION': 'CHA',
		'PERFORMANCE': 'CHA',
		'PERSUASION': 'CHA',
	},
	'BACKGROUNDS': [
		'ACOLYTE', 'CHARLATAN', 'CRIMINAL', 'ENTERTAINER', 'FOLK HERO',
		'GUILD ARTISAN', 'HERMIT', 'NOBLE', 'OUTLANDER', 'SAGE', 'SAILOR',
		'SOLDIER', 'URCHIN',
	],
	'EQUIPMENT': {
		'ARMOR': {
			'LIGHT': {
				'PADDED': padded_armor,
				'LEATHER': leather_armor,
				'STUDDED LEATHER': studded_leather_armor,
			},
			'MEDIUM': {
				'HIDE': hide_armor,
				'CHAIN SHIRT': chain_shirt_armor,
				'SCALE MAIL': scale_mail_armor,
				'BREASTPLATE': breastplate_armor,
				'HALF PLATE': half_plate_armor,
			},
			'HEAVY': {
				'RING MAIL': ring_mail_armor,
				'CHAIN MAIL': chain_mail_armor,
				'SPLINT': splint_armor,
				'PLATE': plate_armor,
			},
			'SHIELD': shield,
		},
		'WEAPON': {
			'SIMPLE': {
				'MELEE': {
					'CLUB': club,
					'DAGGER': dagger,
					'GREATCLUB': greatclub,
					'HANDAXE': handaxe,
					'JAVELIN': javelin,
					'LIGHT HAMMER': light_hammer,
					'MACE': mace,
					'QUARTERSTAFF': quarterstaff,
					'SICKLE': sickle,
					'SPEAR': spear,
				},
				'RANGED': {
					'LIGHT CROSSBOW': light_crossbow,
					'DART': dart,
					'SHORTBOW': shortbow,
					'SLING': sling,
				},
			},
			'MARTIAL': {
				'MELEE': {
					'BATTLEAXE': battleaxe,
					'FLAIL': flail,
					'GLAIVE': glaive,
					'GREATAXE': greataxe,
					'GREATSWORD': greatsword,
					'HALBERD': halberd,
					'LANCE': lance,
					'LONGSWORD': longsword,
					'MAUL': maul,
					'MORNINGSTAR': morningstar,
					'PIKE': pike,
					'RAPIER': rapier,
					'SCIMITAR': scimitar,
					'SHORTSWORD': shortsword,
					'TRIDENT': trident,
					'WAR PICK': war_pick,
					'WARHAMMER': warhammer,
					'WHIP': whip,
				},
				'RANGED': {
					'BLOWGUN': blowgun,
					'HAND CROSSBOW': hand_crossbow,
					'HEAVY CROSSBOW': heavy_crossbow,
					'LONGBOW': longbow,
					'NET': net
				},
			}
		},
		'ADVENTURING GEAR': {
			'ABACUS': abacus,
			'ACID': acid,
			'ALCHEMIST\'S FIRE': alchemists_fire,
			'AMMUNITION': {
				'ARROWS': ammunition['ARROWS'],
				'BLOWGUN NEEDLES': ammunition['BLOWGUN NEEDLES'],
				'CROSSBOW BOLTS': ammunition['CROSSBOW BOLTS'],
				'SLING BULLETS': ammunition['SLING BULLETS'],
			},
			'ANTITOXIN': antitoxin,
			'ARCANE FOCUS': {
				'CRYSTAL': arcane_focus['CRYSTAL'],
				'ORB': arcane_focus['ORB'],
				'ROD': arcane_focus['ROD'],
				'STAFF': arcane_focus['STAFF'],
				'WAND': arcane_focus['WAND'],
			},
			'BACKPACK': backpack,
			'BALL BEARINGS': ball_bearings,
			'BARREL': barrel,
			'BASKET': basket,
			'BEDROLL': bedroll,
			'BELL': bell,
			'BLANKET': blanket,
			'BLOCK AND TACKLE': block_and_tackle,
			'BOOK': book,
			'GLASS BOTTLE': glass_bottle,
			'BUCKET': bucket,
			'CALTROPS': caltrops,
			'CANDLE': candle,
			'CROSSBOW BOLT CASE': crossbow_bolt_case,
			'MAP OR SCROLL CASE': map_or_scroll_case,
			'CHAIN': chain,
			'CHALK': chalk,
			'CHEST': chest,
			'CLIMBER\'S KIT': climbers_kit,
			'CLOTHES': {
				'COMMON CLOTHES': clothes['COMMON'],
				'COSTUME CLOTHES': clothes['COSTUME'],
				'FINE CLOTHES': clothes['FINE'],
				'TRAVELER\'S CLOTHES': clothes['TRAVELER\'S'],
			},
			'COMPONENT POUCH': component_pouch,
			'CROWBAR': crowbar,
			'DRUIDIC FOCUS': {
				'SPRIG OF MISTLETOE': druidic_focus['SPRIG OF MISTLETOE'],
				'TOTEM': druidic_focus['TOTEM'],
				'WOODEN STAFF': druidic_focus['WOODEN\'S STAFF'],
				'YEW WAND': druidic_focus['YEW WAND'],
			},
			'FISHING TACKLE': fishing_tackle,
			'FLASK OR TANKARD': flask_or_tankard,
			'GRAPPLING HOOK': grappling_hook,
			'HAMMER': hammer,
			'SLEDGE HAMMER': sledge_hammer,
			'HEALER\'S KIT': healers_kit,
			'HOLY SYMBOL': {
				'AMULET': holy_symbol['AMULET'],
				'EMBLEM': holy_symbol['EMBLEM'],
				'RELIQUARY': holy_symbol['RELIQUARY'],
			},
			'HOLY WATER': holy_water,
			'HOURGLASS': hourglass,
			'HUNTING TRAP': hunting_trap,
			'INK': ink,
			'INK PEN': ink_pen,
			'JUG OR PITCHER': jug_or_pitcher,
			'LADDER': ladder,
			'LAMP': lamp,
			'BULLSEYE LANTERN': bullseye_lantern,
			'HOODED LANTERN': hooded_lantern,
			'LOCK': lock,
			'MAGNIFYING GLASS': magnifying_glass,
			'MANACLES': manacles,
			'MESS KIT': mess_kit,
			'STEEL MIRROR': steel_mirror,
			'OIL': oil,
			'PAPER': paper,
			'PARCHMENT': parchment,
			'PERFUME': perfume,
			'MINER\'S PICK': miners_pick,
			'PITON': piton,
			'BASIC POISON': basic_poison,
			'POLE': pole,
			'IRON POT': iron_pot,
			'POTION OF HEALING': potion_of_healing,
			'POUCH': pouch,
			'QUIVER': quiver,
			'PORTABLE RAM': portable_ram,
			'RATIONS': rations,
			'ROBES': robes,
			'HEMPEN ROPE': hempen_rope,
			'SILK ROPE': silk_rope,
			'SACK': sack,
			'MERCHANT\'S SCALE': merchants_scale,
			'SEALING WAX': sealing_wax,
			'SHOVEL': shovel,
			'SIGNAL WHISTLE': signal_whistle,
			'SIGNET RING': signet_ring,
			'SOAP': soap,
			'SPELLBOOK': spellbook,
			'IRON SPIKES': iron_spikes,
			'SPYGLASS': spyglass,
			'TWO-PERSON TENT': two_person_tent,
			'TINDERBOX': tinderbox,
			'TORCH': torch,
			'VIAL': vial,
			'WATERSKIN': waterskin,
			'WHETSTONE': whetstone,
		},
		'TOOLS': {
			'ARTISAN\'S TOOLS': {
				"ALCHEMIST'S SUPPLIES": artisans_tools["ALCHEMIST'S SUPPLIES"],
				"BREWER'S SUPPLIES": artisans_tools["BREWER'S SUPPLIES"],
				"CALLIGRAPHER'S SUPPLIES": artisans_tools["CALLIGRAPHER'S SUPPLIES"],
				"CARPENTER'S TOOLS": artisans_tools["CARPENTER'S TOOLS"],
				"CARTOGRAPHER'S TOOLS": artisans_tools["CARTOGRAPHER'S TOOLS"],
				"COBBLER'S TOOLS": artisans_tools["COBBLER'S TOOLS"],
				"COOK'S UTENSILS": artisans_tools["COOK'S UTENSILS"],
				"GLASSBLOWER'S TOOLS": artisans_tools["GLASSBOWER'S TOOLS"],
				"JEWELER'S TOOLS": artisans_tools["JEWELER'S TOOLS"],
				"LEATHERWORKER'S TOOLS": artisans_tools["LEATHERWORKER'S TOOLS"],
				"MASON'S TOOLS": artisans_tools["MASON'S TOOLS"],
				"PAINTER'S SUPPLIES": artisans_tools["PAINTER'S SUPPLIES"],
				"POTTER'S TOOLS": artisans_tools["POTTER'S TOOLS"],
				"SMITH'S TOOLS": artisans_tools["SMITH'S TOOLS"],
				"TINKER'S TOOLS": artisans_tools["TINKER'S TOOLS"],
				"WEAVER'S TOOLS": artisans_tools["WEAVER'S TOOLS"],
				"WOODCARVER'S TOOLS": artisans_tools["WOODCARVER'S TOOLS"]
			},
			"DISGUISE'S KIT": disguise_kit,
			"FORGERY KIT": forgery_kit,
			"GAMING SET": {
				'DICE SET': gaming_set['DICE SET'],
				'DRAGONCHESS SET': gaming_set['DRAGONCHESS SET'],
				'PLAYING CAR SET': gaming_set['PLAYING CARD SET'],
				'THREE-DRAGON ANTE SET': gaming_set['THREE-DRAGON ANTE SET'],
			},
			"HERBALISM KIT": herbalism_kit,
			"MUSICAL INSTRUMENT": {
				"BAGPIPES": musical_instrument['BAGPIPES'],
				"DRUM": musical_instrument['DRUM'],
				"DULCIMER": musical_instrument['DULCIMER'],
				"FLUTE": musical_instrument['FLUTE'],
				"LUTE": musical_instrument['LUTE'],
				"LYRE": musical_instrument['LYRE'],
				"HORN": musical_instrument['HORN'],
				"PAN FLUTE": musical_instrument['PAN FLUTE'],
				"SHAWM": musical_instrument['SHAWM'],
				"VIOL": musical_instrument['VIOL'],
			},
			"NAVIGATOR'S TOOLS": navigators_tools,
			"POISONER'S KIT": poisoners_kit,
			"THIEVES' TOOLS": thieves_kit,
			"VEHICLES": {
				"LAND": {
					'CAMEL': camel,
					'DONKEY OR MULE': donkey_or_mule,
					'ELEPHANT': elephant,
					'DRAFT HORSE': draft_horse,
					'RIDING HORSE': riding_horse,
					'MASTIFF': mastiff,
					'PONY': pony,
					'WARHORSE': warhorse
				},
				"WATER": {
					'GALLEY': galley,
					'KEELBOAT': keelboat,
					'LONGSHIP': longship,
					'ROWBOAT': rowboat,
					'SAILING SHIP': sailing_ship,
					'WARSHIP': warship
				}
			}
		},
	},
	'TRINKET': {
		'ANIMAL TROPHY': animal_trophy,
		'QUILL': quill,
		'SMALL KNIFE': small_knife,
		'LETTER FROM DEAD COLLEAGUE': letter_from_colleague,
		'LUCKY CHARM': lucky_charm,
		'ENEMY TROPHY': enemy_trophy,
		'INSIGNIA RANK': insignia_rank,
		'CITY MAP': city_map,
		'PET MOUSE': pet_mouse,
		'PARENTS TOKEN': parents_token,
		'INCENSE': incense,
		'ADMIRER FAVOR': admirer_favor,
		'WINTER BLANKET': winter_blanket,
	},
	'CANTRIPS': {
		'BARD': [
				'FRIENDS', 'TRUE STRIKE', 'MENDING', 'DANCING LIGHTS', 'MESSAGE',
				'MINOR ILLUSION', 'LIGHT', 'MAGE HAND', 'VICIOUS MOCKERY',
				'PRESTIDIGITATION', 'BLADE WARD',
		],
		'CLERIC': [
				'SACRED FLAME', 'MENDING', 'SPARE THE DYING', 'LIGHT',
				'GUIDANCE', 'RESISTANCE', 'THAUMATURGY',
		],
		'DRUID': [
				'DRUIDCRAFT', 'GUIDANCE', 'MENDING', 'POISON SPRAY', 'PRODUCE '
				'FLAME', 'RESISTANCE', 'SHILLELAGH', 'THORN WHIP'
		],
		'SORCERER': [
				'ACID SPLASH', 'BLADE WARD', 'CHILL TOUCH', 'DANCING LIGHTS',
				'FIRE BOLT', 'FRIENDS', 'LIGHT', 'MAGE HAND', 'MENDING',
				'MESSAGE', 'MINOR ILLUSION', 'POISON SPRAY', 'PRESTIDIGITATION',
				'RAY OF FROST', 'SHOCKING GRASP', 'TRUE STRIKE',
		],
		'WARLOCK': [
				'BLADE WARD', 'CHILL TOUCH', 'ELDRITCH BLAST', 'FRIENDS',
				'MAGE HAND', 'MINOR ILLUSION', 'POISON SPRAY',
				'PRESTIDIGITATION', 'TRUE STRIKE',
		],
		'WIZARD': [
				'ACID SPLASH', 'BLADE WARD', 'CHILL TOUCH', 'DANCING LIGHTS',
				'FIRE BOLT', 'FRIENDS', 'LIGHT', 'MAGE HAND', 'MENDING',
				'MESSAGE', 'MINOR ILLUSION', 'POISON SPRAY', 'PRESTIDIGITATION',
				'RAY OF FROST', 'SHOCKING GRASP', 'TRUE STRIKE',
		],
	},
	'SPELLS': {
		'BARD': {
			1: [
				'ANIMAL FRIENDSHIP', 'COMPREHEND LANGUAGES', 'CURE WOUNDS',
				'DETECT MAGIC', 'DISGUISE SELF', 'CHARM PERSON',
				'ILLUSORY SCRIPT', 'SPEAK WITH ANIMALS', 'FAERIE FIRE',
				'HEROISM', 'IDENTIFY', 'SILENT IMAGE', 'THUNDERWAVE', 'HEALING '
				'WORD', 'LONGSTRIDER', 'BANE', 'FEATHER FALL',
				'TASHA\'S HIDEOUS LAUGHTER', 'UNSEEN SERVANT', 'SLEEP',
				'DISSONANT WHISPERS',
			],
			2: [
				'CALM EMOTIONS', 'ENHANCE ABILITY', 'KNOCK', 'MAGIC MOUTH',
				'ENTHRALL', 'BLINDNESS/DEAFNESS', 'CROWN OF MADNESS', 'SHATTER',
				'DETECT THOUGHTS', 'HEAT METAL', 'ZONE OF TRUTH',
				'PHANTASMAL FORCE', 'HOLD PERSON', 'INVISIBILITY',
				'LOCATE ANIMALS OR PLANTS', 'LOCATE OBJECT', 'ANIMAL MESSENGER',
				'CLOUD OF DAGGERS', 'LESSER RESTORATION',
				'SILENCE', 'SUGGESTION', 'SEE INVISIBILITY',
			],
			3: [
				'PLANT GROWTH', 'CLAIRVOYANCE', 'NONDETECTION', 'DISPEL MAGIC',
				'SENDING', 'SPEAK WITH DEAD', 'SPEAK WITH PLANTS',
				'GLYPH OF WARDING', ' TONGUES', 'MAJOR IMAGE', 'FEAR',
				'STINKING CLOUD', 'BESTOW CURSE', 'HYPNOTIC PATTERN',
				'LEOMUND\'S TINY HUT', 'FEIGN DEATH',
			],
			4: [
				'COMPULSION', 'CONFUSION', 'GREATER INVISIBILITY',
				'LOCATE CREATURE', 'POLYMORPH', 'FREEDOM OF MOVEMENT',
				'DIMENSION DOOR', 'HALLUCINATORY TERRAIN',
			],
			5: [
				'PLANAR BINDING', 'ANIMATE OBJECTS', 'TELEPORTATION CIRCLE',
				'LEGEND LORE', 'MASS CURE WOUNDS', 'AWAKEN', 'MISLEAD', 'DREAM',
				'DOMINATE PERSON', 'HOLD MONSTER', 'GEAS', 'MODIFY MEMORY',
				'GREATER RESTORATION', 'RAISE DEAD', 'SEEMING', 'SCRYING',
			],
			6: [
				'EYEBITE', 'OTTO\'S IRRESISTABLE DANCE', 'FIND THE PATH',
				'PROGRAMMED ILLUSION', 'GUARDS AND WARDS', 'MASS SUGGESTION',
				'TRUE SEEING'
			],
			7: [
				'MORDENKAINEN\'S SWORD', 'ETHEREALNESS', 'MORDENKAINEN\'S '
				'MAGNIFICENT MANSION', 'MIRAGE ARCANE', 'FORCECAGE', 'PROTECT '
				'IMAGE', 'REGENERATE', 'RESURRECTION', 'SYMBOL', 'TELEPORT',
			],
			8: [
				'DOMINATE MONSTER', 'FEEBLEMIND', 'MIND BLANK', 'GLIBNESS',
				'POWER WORD STUN',
			],
			9: [
				'TRUE POLYMORPH', 'POWER WORD HEAL',
				'POWER WORD KILL', 'FORESIGHT',
			],
		},
		'CLERIC': {
			1: [
				'BLESS', 'COMMAND', 'CREATE OR DESTROY WATER', 'INFLICT WOUNDS',
				'CURE WOUNDS', 'DETECT MAGIC', 'DETECT EVIL AND GOOD', 'BANE',
				'DETECT POISON AND DISEASE', 'SHIELD OF FAITH', 'HEALING WORD',
				'PROTECTION FROM EVIL AND GOOD', 'GUIDING BOLT', 'SANCTUARY',
				'PURIFY FOOD AND DRINK',
			],
			2: [
				'CALM EMOTIONS', 'AID', 'ENHANCE ABILITY', 'SPIRITUAL WEAPON',
				'AUGURY', 'BLINDNESS/DEAFNESS', 'CONTINUAL FLAME', 'FIND TRAPS',
				'HOLD PERSON', 'LOCATE OBJECT', 'PRAYER OF HEALING', 'SILENCE',
				'PROTECTION FROM POISON', 'GENTLE REPOSE', 'LESSER RESTORATION',
				'WARDING BOND', 'ZONE OF TRUTH',
			],
			3: [
				'WATER WALK', 'ANIMATE DEAD', 'MAGIC CIRCLE', 'REMOVE CURSE',
				'CLAIRVOYANCE', 'CREATE FOOD AND WATER', 'PROTECTION FROM ENERGY'
				'DISPEL MAGIC', 'SENDING', 'SPIRIT GUARDIANS', 'SPEAK WITH DEAD',
				'FEIGN DEATH', 'GLYPH OF WARDING', 'TONGUES', 'MELD INTO STONE',
				'DAYLIGHT', 'MASS HEALING WORD', 'REVIVIFY', 'BEACON OF HOPE',
				'BESTOW CURSE',
			],
			4: [
				'DIVINATION', 'BANISHMENT', 'CONTROL WATER', 'GUARDIAN OF FAITH',
				'LOCATE CREATURE', 'STONE SHAPE', 'FREEDOM OF MOVEMENT',
				'DEATH WARD',
			],
			5: [
				'PLANAR BINDING', 'FLAME STRIKE', 'GEAS', 'MASS CURE WOUNDS',
				'COMMUNE', 'LEGEND LORE', 'HALLOW', 'DISPEL EVIL AND GOOD',
				'CONTAGION', 'INSECT PLAGUE', 'GREATER RESTORATION', 'SCRYING',
				'RAISE DEAD',
			],
			6: [
				'BLADE BARRIER', 'CREATE UNDEAD', 'FIND THE PATH', 'FORBIDDANCE',
				'HARM', 'HEAL', 'HEROES\' FEAST', 'PLANAR ALLY', 'TRUE SEEING',
				'WORD OF RECALL',
			],
			7: [
				'CONJURE CELESTIAL', 'DIVINE WORD', 'ETHEREALNESS', 'FIRE STORM',
				'PLANE SHIFT', 'REGENERATE', 'RESURRECTION', 'SYMBOL',
			],
			8: [
				'ANTIMAGIC FIELD', 'CONTROL WEATHER', 'EARTHQUAKE', 'HOLY AURA',
			],
			9: [
				'ASTRAL PROJECTION', 'GATE', 'MASS HEAL', 'TRUE RESURRECTION',
			],
		},
		'DRUID': {
			1: [
				'ANIMAL FRIENDSHIP', 'CHARM PERSON', 'CREATE OR DESTROY WATER',
				'CURE WOUNDS', 'DETECT MAGIC', 'DETECT POISON AND DISEASE',
				'ENTANGLE', 'FAERIE FIRE', 'FOG CLOUD', 'GOODBERRY', 'HEALING '
				'WORD', 'JUMP', 'LONGSTRIDER', 'PURIFY FOOD AND DRINK', 'SPEAK '
				'WITH ANIMALS', 'THUNDERWAVE',
			],
			2: [
				'ANIMAL MESSENGER', 'BARKSKIN', 'BEAST SENSE', 'DARKVISION',
				'ENHANCE ABILITY', 'FIND TRAPS', 'FLAME BLADE', 'FLAMING SPHERE',
				'GUST OF WIND', 'HEAT METAL', 'HOLD PERSON', 'LESSER RESTORATION',
				'LOCATE ANIMALS OR PLANTS', 'LOCATE OBJECT', 'MOONBEAM', 'PASS '
				'WITHOUT TRACE', 'PROJECTION FROM POISON', 'SPIKE GROWTH',
			],
			3: [
				'CALL LIGHTNING', 'CONJURE ANIMALS', 'DAYLIGHT', 'DISPEL MAGIC',
				'FEIGN DEATH', 'MELD INTO STONE', 'PLANT GROWTH', 'PROTECTION '
				'FROM ENERGY', 'SLEET STORM', 'SPEAK WITH PLANTS', 'WATER '
				'BREATHING', 'WATER WALK', 'WIND WALL',
			],
			4: [
				'BLIGHT', 'CONFUSION', 'CONJURE MINOR ELEMENTALS',
				'CONJURE WOODLAND BEINGS', 'CONTROL WATER', 'DOMINATE BEAST',
				'FREEDOM OF MOVEMENT', 'GIANT INSECT', 'GRASPING VINE',
				'HALLUCINATORY TERRAIN', 'ICE STORM', 'LOCATE CREATURE',
				'POLYMORPH', 'STONE SHAPE', 'STONESKIN', 'WALL OF FIRE',
			],
			5: [
				'ANTILIFE SHELL', 'AWAKEN', 'COMMUNE WITH NATURE', 'CONJURE '
				'ELEMENTAL', 'CONTAGION', 'GEAS', 'GREATER RESTORATION',
				'INSECT PLAGUE', 'MASS CURE WOUNDS', 'PLANAR BINDING',
				'REINCARNATE', 'SCRYING', 'TREE STRIDE', 'WALL OF STONE',
			],
			6: [
				'CONJURE FEY', 'FIND THE PATH', 'HEAL', 'HEROES\' FEAST',
				'MOVE EARTH', 'SUNBEAM', 'TRANSPORT VIA PLANTS', 'WALL OF '
				'THORNS', 'WIND WALK',
			],
			7: [
				'FIRE STORM', 'MIRAGE ARCANE', 'PLANE SHIFT', 'REGENERATE',
				'REVERSE GRAVITY',
			],
			8: [
				'ANIMAL SHAPES', 'ANTIPATHY/SYMPATHY', 'CONTROL WEATHER',
				'EARTHQUAKE', 'FEEBLEMIND', 'SUNBURST', 'TSUNAMI',
			],
			9: [
				'FORESIGHT', 'SHAPECHANGE', 'STORM OF VENGEANCE',
				'TRUE RESURRECTION',
			],
		},
		'PALADIN': {
			1: [
				'BLESS', 'COMMAND', 'COMPELLED DUEL', 'CURE WOUNDS', 'DETECT '
				'EVIL AND GOOD', 'DETECT MAGIC', 'DETECT POISON AND DISEASE',
				'DIVINE FAVOR', 'HEROISM', 'PROTECTION FROM EVIL AND GOOD',
				'PURIFY FOOD AND DRINK', 'SEARING SMITE', 'SHIELD OF FAITH',
				'THUNDEROUS SMITE', 'WRATHFUL SMITE',
			],
			2: [
				'AID', 'BRANDING SMITE', 'FIND STEED', 'LESSER RESTORATION',
				'LOCATE OBJECT', 'MAGIC WEAPON', 'PROTECTION FROM POISON',
				'ZONE OF TRUTH',
			],
			3: [
				'AURA OF VITALITY', 'BLINDING SMITE', 'CREATE FOOD AND WATER',
				'CRUSADER\'S MANTLE', 'DAYLIGHT', 'DISPEL MAGIC', 'ELEMENTAL '
				'WEAPON', 'MAGIC CIRCLE', 'REMOVE CURSE', 'REVIVIFY',
			],
			4: [
				'AURA OF LIFE', 'AURA OF PURITY', 'BANISHMENT', 'DEATH WARD',
				'LOCATE CREATURE', 'STAGGERING SMITE',
			],
			5: [
				'BANISHING SMITE', 'CIRCLE OF POWER', 'DESTRUCTIVE SMITE',
				'DISPEL EVIL AND GOOD', 'GEAS', 'RAISE DEAD',
			],
			6: [],
			7: [],
			8: [],
			9: [],
		},
		'RANGER': {
			1: [
				'ALARM', 'ANIMAL FRIENDSHIP', 'CURE WOUNDS', 'DETECT MAGIC',
				'DETECT POISON AND DISEASE', 'ENSNARING STRIKE', 'FOG CLOUD',
				'GOODBERRY', 'HAIL OF THORNS', 'HUNTER\'S MARK', 'JUMP',
				'LONGSTRIDER', 'SPEAK WITH ANIMALS',
			],
			2: [
				'ANIMAL MESSENGER', 'BARKSKIN', 'BEAST SENSE', 'CORDON OF '
				'ARROWS', 'DARKVISION', 'FIND TRAPS', 'LESSER RESTORATION',
				'LOCATE ANIMALS OR PLANTS', 'LOCATE OBJECT', 'PASS WITHOUT '
				'TRACE', 'PROTECTION FROM POISON', 'SILENCE', 'SPIKE GROWTH',
			],
			3: [
				'CONJURE ANIMALS', 'CONJURE BARRAGE', 'DAYLIGHT', 'LIGHTNING '
				'ARROW', 'NONDETECTION', 'PLANT GROWTH', 'PROTECTION FROM ENERGY',
				'SPEAK WITH PLANTS', 'WATER BREATHING', 'WATER WALK', 'WIND WALL',
			],
			4: [
				'CONJURE WOODLAND BEINGS', 'FREEDOM OF MOVEMENT', 'GRASPING '
				'VINE', 'LOCATE CREATURE', 'STONESKIN',
			],
			5: [
				'COMMUNE WITH NATURE', 'CONJURE VOLLEY',
				'SWIFT QUIVER', 'TREE STRIDE',
			],
			6: [],
			7: [],
			8: [],
			9: [],
		},
		'SORCERER': {
			1: [
				'BURNING HANDS', 'CHARM PERSON', 'CHROSMATIC ORB', 'COLOR SPRAY',
				'COMPREHEND LANGUAGES', 'DETECT MAGIC', 'DISGUISE SELF',
				'EXPEDITIOUS RETREAT', 'FALSE LIFE', 'FEATHER FALL', 'JUMP',
				'FOG CLOUD', 'MAGE ARMOR', 'MAGIC MISSILE', 'RAY OF SICKNESS',
				'SHIELD', 'SILENT IMAGE', 'SLEEP', 'THUNDERWAVE', 'WITCH BOLT',
			],
			2: [
				'ALTER SELF', 'BLINDNESS/DEAFNESS', 'BLUR', 'CLOUD OF DAGGERS',
				'CROWN OF MADNESS', 'DARKNESS', 'DARKVISION', 'DETECT THOUGHTS',
				'ENHANCE ABILITY', 'ENLARGE/REDUCE', 'GUST OF WIND', 'KNOCK',
				'HOLD PERSON', 'INVISIBILITY', 'KNOCK', 'LEVITATE', 'SHATTER',
				'MIRROR IMAGE', 'MISTY STEP', 'PHANTASMAL FORCE', 'SUGGESTION',
				'SCORCHING RAY', 'SEE INVISIBILITY', 'SPIDER CLIMB', 'WEB',
			],
			3: [
				'BLINK', 'CLAIRVOYANCE', 'COUNTERSPELL', 'DAYLIGHT', 'FEAR',
				'DISPEL MAGIC', 'FIREBALL', 'FLY', 'GASEOUS FORM', 'HASTE',
				'HYPNOTIC PATTERN', 'LIGHTNING BOLT', 'MAJOR IMAGE', 'SLOW',
				'PROTECTION FROM ENERGY', 'SLEET STORM', 'STINKING CLOUD',
				'TONGUES', 'WATER BREATHING', 'WATER WALK',
			],
			4: [
				'BANISHMENT', 'BLIGHT', 'CONFUSION', 'DIMENSION DOOR',
				'DOMINATE BEAST', 'GREATER INVISIBILITY', 'ICE STORM',
				'POLYMORPH', 'STONESKIN', 'WALL OF FIRE',
			],
			5: [
				'ANIMATE OBJECTS', 'CLOUDKILL', 'CONE OF COLD', 'CREATION',
				'DOMINATE PERSON', 'HOLD MONSTER', 'INSECT PLAGUE', 'SEEMING',
				'TELEKINESIS', 'TELEPORTATION CIRCLE', 'WALL OF STONE',
			],
			6: [
				'ARCANE GATE', 'CHAIN LIGHTNING', 'CIRCLE OF DEATH', 'EYEBITE',
				'DISINTEGRATE', 'GLOBE OF INVULNERABILITY', 'MASS SUGGESTION',
				'MOVE EARTH', 'SUNBEAM', 'TRUE SEEING',
			],
			7: [
				'DELAYED BLAST FIREBALL', 'ETHEREALNESS', 'FINGER OF DEATH',
				'FIRE STORM', 'PLANE SHIFT', 'PRISMATIC SPRAY',
				'REVERSE GRAVITY', 'TELEPORT',
			],
			8: [
				'DOMINATE MONSTER', 'EARTHQUAKE', 'INCENDIARY CLOUD',
				'POWER WORD STUN', 'SUNBURST',
			],
			9: [
				'GATE', 'METEOR SWARM', 'POWER WORD KILL', 'TIME STOP', 'WISH',
			]
		},
		'WARLOCK': {
			1: [
				'ARMOR OF AGATHYS', 'ARMS OF HADAR', 'CHARM PERSON', 'HEX',
				'COMPREHEND LANGUAGES', 'EXPEDITIOUS RETREAT', 'HELLISH REBUKE',
				'ILLUSORY SCRIPT', 'PROTECTION FROM EVIL AND GOOD',
				'UNSEEN SERVANT', 'WITCH BOLT',
			],
			2: [
				'CLOUD OF DAGGERS', 'CROWN OF MADNESS', 'DARKNESS', 'ENTHRALL',
				'HOLD PERSON', 'INVISIBILITY', 'MIRROR IMAGE', 'MISTY STEP',
				'RAY OF ENFEEBLEMENT', 'SHATTER', 'SPIDER CLIMB', 'SUGGESTION',
			],
			3: [
				'COUNTERSPELL', 'DISPEL MAGIC', 'FEAR', 'FLY', 'GASEOUS FORM',
				'HUNGER OF HADAR', 'HYPNOTIC PATTERN', 'MAGIC CIRCLE',
				'MAJOR IMAGE', 'REMOVE CURSE', 'TONGUES', 'VAMPIRIC TOUCH',
			],
			4: [
				'BANISHMENT', 'BLIGHT', 'DIMENSION DOOR',
				'HALLUCINATORY TERRAIN',
			],
			5: [
				'CONTACT OTHER PLANE', 'DREAM', 'HOLD MONSTER', 'SCRYING',
			],
			6: [
				'ARCANE GATE', 'CIRCLE OF DEATH', 'CONJURE FEY', 'CREATE UNDEAD',
				'EYEBITE', 'FLESH TO STONE', 'MASS SUGGESTION', 'TRUE SEEING',
			],
			7: [
				'ETHEREALNESS', 'FINGER OF DEATH', 'FORCECAGE', 'PLANE SHIFT',
			],
			8: [
				'DEMIPLANE', 'DOMINATE MONSTER', 'FEEBLEMIND',
				'GLIBNESS', 'POWER WORD STUN',
			],
			9: [
				'ASTRAL PROJECTION', 'FORESIGHT', 'IMPRISONMENT',
				'POWER WORD KILL', 'TRUE POLYMORPH',
			],
		},
		'WIZARD': {
			1: [
				'ALARM', 'BURNING HANDS', 'CHARM PERSON', 'CHROSMATIC ORB',
				'COLOR SPRAY', 'COMPREHEND LANGUAGES', 'DETECT MAGIC', 'JUMP',
				'DISGUISE SELF', 'EXPEDITIOUS RETREAT', 'FALSE LIFE', 'GREASE',
				'FEATHER FALL', 'FIND FAMILIAR', 'FOG CLOUD', 'IDENTIFY',
				'ILLUSORY SCRIPT', 'LONGSTRIDER', 'MAGE ARMOR', 'MAGIC MISSILE',
				'PROTECTION FROM EVIL AND GOOD', 'RAY OF SICKNESS', 'SHIELD',
				'SILENT IMAGE', 'SLEEP', 'TASHA\'S HIDEOUS LAUGHTER',
				'TENSER\'S FLOATING DISK', 'THUNDERWAVE', 'UNSEEN SERVANT',
				'WITCH BOLT',
			],
			2: [
				'ALTER SELF', 'ARCANE LOCK', 'BLINDNESS/DEAFNESS', 'BLUR',
				'CLOUD OF DAGGERS', 'CONTINUAL FLAME', 'CROWN OF MADNESS',
				'DARKNESS', 'DARKVISION', 'DETECT THOUGHTS', 'ENLARGE/REDUCE',
				'FLAMING SPHERE', 'GENTLE REPOSE', 'GUST OF WIND', 'KNOCK',
				'HOLD PERSON', 'INVISIBILITY', 'LEVITATE', 'LOCATE OBJECT',
				'MAGIC MOUTH', 'MAGIC WEAPON', 'MELF\'S ACID ARROW', 'SHATTER',
				'MIRROR IMAGE', 'MISTY STEP', 'NYSTUL\'S MAGIC AURA', 'WEB',
				'PHANTASMAL FORCE', 'RAY OF ENFEEBLEMENT', 'ROPE TRICK',
				'SCORCHING RAY', 'SEE INVISIBILITY', 'SPIDER CLIMB', 'SUGGESTION'
			],
			3: [
				'ANIMATED DEAD', 'BESTOW CURSE', 'BLINK', 'CLAIRVOYANCE', 'FEAR',
				'COUNTERSPELL', 'DISPEL MAGIC', 'FEIGN DEATH', 'FIREBALL', 'FLY',
				'GASEOUS FORM', 'GLYPH OF WARDING', 'HASTE', 'HYPNOTIC PATTERN',
				'LEOMUND\'S TINY HUT', 'LIGHTNING BOLT', 'MAGIC CIRCLE', 'SLOW',
				'MAJOR IMAGE', 'NONDETECTION', 'PHANTOM STEED', 'PROTECTION '
				'FROM ENERGY', 'REMOVE CURSE', 'SENDING', 'SLEET STORM',
				'STINKING CLOUD', 'TONGUES', 'VAMPIRIC TOUCH', 'WATER BREATHING'
			],
			4: [
				'ARCANE EYE', 'BANISHMENT', 'BLIGHT', 'CONFUSION', 'CONJURE '
				'MINOR ELEMENTALS', 'CONTROL WATER', 'DIMENSION DOOR',
				'EVARD\'S BLACK TENTACLES', 'FABRICATE', 'FIRE SHIELD',
				'GREATER INVISIBILITY', 'HALLUCINATORY TERRAIN', 'ICE STORM',
				'LEOMUND\'S SECRET CHEST', 'LOCATE CREATURE', 'MORDENKAINEN\'S '
				'FAITHFUL HOUND', 'MORDENKAINEN\'S PRIVATE SANCTUM', 'STONESKIN',
				'OTILUKE\'S RESILIENT SPHERE', 'PHANTASMAL KILLER', 'POLYMORPH',
				'STONE SHAPE', 'WALL OF FIRE',
			],
			5: [
				'ANIMATE OBJECT', 'BIGBY\'S HAND', 'CLOUDKILL', 'CONE OF COLD',
				'CONJURE ELEMENTAL', 'CONTACT OTHER PLANE', 'CREATION',
				'DOMINATE PERSON', 'DREAM', 'GEAS', 'HOLD MONSTER', 'LEGEND '
				'LORE', 'MISLEAD', 'MODIFY MEMORY', 'PASSWALL', 'PLANAR BINDING',
				'RARY\'S TELEPATHIC BOND', 'SCRYING', 'SEEMING', 'TELEKINESIS',
				'TELEPORTATION CIRCLE', 'WALL OF FORCE', 'WALL OF STONE',
			],
			6: [
				'ARCANE GATE', 'CHAIN LIGHTNING', 'CIRCLE OF DEATH', 'EYEBITE',
				'CONTINGENCY', 'CREATE UNDEAD', 'DISINTEGRATE', 'DRAWMIJ\'S '
				'INSTANT SUMMONS', 'EYEBITE', 'FLESH TO STONE', 'GLOBE OF '
				'INVULNERABILITY', 'GUARDS AND WARDS', 'MAGIC JAR', 'MASS '
				'SUGGESTION', 'MOVE EARTH', 'OTILUKE\'S FREEZING SPHERE',
				'OTTO\'S IRRESISTABLE DANCE', 'PROGRAMMED ILLUSION', 'SUNBEAM',
				'TRUE SEEING', 'WALL OF ICE',
			],
			7: [
				'DELAYED BLAST FIREBALL', 'ETHEREALNESS', 'FINGER OF DEATH',
				'FORCECAGE', 'MIRAGE ARCANE', 'MORDENKAINEN\'S MAGNIFICENT '
				'MANSION', 'MORDENKAINEN\'S SWORD', 'PLANE SHIFT', 'PRISMATIC '
				'SPRAY', 'PROJECT IMAGE', 'REVERSE GRAVITY', 'SEQUESTER',
				'SIMULACRUM', 'SYMBOL', 'TELEPORT',
			],
			8: [
				'ANTIMAGIC FIELD', 'ANTIPATHY/SYMPATHY', 'CLONE', 'DEMIPLANE',
				'CONTROL WEATHER', 'DOMINATE MONSTER', 'FEEBLEMIND', 'MAZE',
				'INCENDIARY CLOUD', 'MIND BLANK', 'POWER WORD STUN', 'SUNBURST',
				'TELEPATHY', 'TRAP THE SOUL',
			],
			9: [
				'ASTRAL PROJECTION', 'FORESIGHT', 'GATE', 'IMPRISONMENT', 'WISH',
				'METEOR SWARM', 'POWER WORD KILL', 'PRISMATIC WALL', 'TIME STOP',
				'SHAPECHANGE', 'TRUE POLYMORPH', 'WEIRD',
			]
		}
	},
	'ALIGNMENTS': [
		'LAWFUL GOOD', 'NEUTRAL GOOD', 'CHAOTIC GOOD', 'LAWFUL NEUTRAL',
		'NEUTRAL', 'CHAOTIC NEUTRAL', 'LAWFUL EVIL', 'NEUTRAL EVIL',
		'CHAOTIC EVIL',
	],
}
