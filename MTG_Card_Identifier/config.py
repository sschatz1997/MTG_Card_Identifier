# config.py
import os
import sys

main_path = os.path.dirname(os.path.realpath(__file__))
if sys.platform == "win32":
	main_path = main_path + "\\"
	data = main_path + "data\\"
	#color_path = data + 'color_symbols\\'
	#master_cards = main_path + "master_imgs.csv"
	separator = "\\"  # for windows

elif sys.platform == "linux":
	main_path = main_path + "/"
	data = main_path + "data/"
	#color_path = data + 'color_symbols/'
	#master_cards = main_path + "master_imgs.csv"
	separator = "/"  # for linux

# for batch file checks
acceptable_file_formats = ['txt', 'csv']

# all aval image urls
all_good = data + "all.csv"
all_bad = data + "no_url.csv"
set_info = data + "set_info.csv"

# color dict
colors1 = {
	'B': 'Black',
	'U': 'Blue',
	'R': 'Red',
	'W': 'White'
}

# yes no dict
y_n_d = {
	'y': 'yes',
	'n': 'no'
}


# pprint
active_sets3 = [
	['Aether Revolt', 'Alara Reborn', 'Alliances', 'Amonkhet'],
	['Antiquities', 'Apocalypse', 'Arabian Nights', 'Betrayers of Kamigawa'],
	['Champions of Kamigawa', 'Coldsnap', 'Conflux', 'Darksteel'],
	['Dissension', 'Dominaria', 'Eventide', 'Exodus'],
	['Fallen Empires', 'Fifth Dawn', 'Future Sight', 'Guildpact'],
	['Homelands', 'Hour of Devastation', 'Ice Age', 'Invasion'],
	['Ixalan', 'Judgment', 'Kaladesh', 'Legends'],
	['Legions', 'Lorwyn', 'Mercadian Masques', 'Mirage'],
	['Mirrodin', 'Mirrodin Besieged', 'Morningtide', 'Nemesis'],
	['New Phyrexia', 'Odyssey', 'Onslaught', 'Planar Chaos'],
	['Planeshift', 'Prophecy', 'Ravnica City of Guilds', 'Rise of the Eldrazi'],
	['Saviors of Kamigawa', 'Scars of Mirrodin', 'Weatherlight', 'Worldwake'],
	['Scourge', 'Shadowmoor', 'Shards of Alara', 'Stronghold'],
	['Tempest', 'The Dark', 'Theros Beyond Death', 'Torment'],
	["Urza's Destiny", "Urza's Legacy", "Urza's Saga", 'Visions'],
]


card_info_api_keys = [
	'name',
	'colorIdentity',
	'convertedManaCost',
	'manaCost',
	'type',
	'types',
	'supertypes',
	#'originalText',
	#'colors',
	#'number',
	'rarity',
	'power',
	'toughness',
	'availability',
	'printings',
	'text'
]

# for table
card_info_api_keys_ftable = [
	'Name',
	'Color Identity',
	'Converted Mana Cost',
	'Mana Cost',
	'Type',
	'Other Types',
	'Super Types',
	'Rarity',
	'Power',
	'Toughness',
	'Formats Allowed',
	'Set Printings',
	'Text'
]

"""
original
card_info_api_keys = [
	'artist',
	'asciiName',
	'availability',
	'borderColor',
	'colorIdentity',
	'colors',
	'convertedManaCost',
	'edhrecRank',
	'foreignData',
	'frameVersion',
	'hasFoil',
	'hasNonFoil',
	'identifiers',
	'isReserved',
	'layout',
	'legalities',
	'manaCost',
	'name',
	'number',
	'originalText',
	'originalType',
	'power',
	'printings',
	'purchaseUrls',
	'rarity',
	'rulings',
	'setCode',
	'subtypes',
	'supertypes',
	'text',
	'toughness',
	'type',
	'types',
	'uuid'
]
"""
