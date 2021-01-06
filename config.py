# config.py
import os
import sys

main_path = os.path.dirname(os.path.realpath(__file__))
if sys.platform == "win32":
	main_path = main_path + "\\"
	data =  main_path + "data\\"
	color_path = data + 'color_symbols\\'
	active_image_paths = [
		data + 'Ravnica Allegiance\\imgs\\',
		data + 'Guilds of Ravnica\\imgs\\',
		data + 'Throne of Eldraine\\imgs\\',
		data + "Ikoria Lair of Behemoths\\imgs\\",
		data + "Zendikar Rising\\imgs\\",
		data + "Zendikar\\imgs\\",
		data + "Theros Beyond Death\\imgs\\",
		data + 'Dominaria\\imgs\\',
		data + 'Ixalan\\imgs\\',
		data + 'Hour of Devastation\\imgs\\',
		data + 'Amonkhet\\imgs\\',
		data + 'Aether Revolt\\imgs\\'
	]
	master_cards = main_path + "master_imgs.csv"
	
elif sys.platform == "linux":
	main_path = main_path + "/"
	data = main_path + "data/"
	color_path = data + 'color_symbols/'
	master_cards = main_path + "master_imgs.csv"
	active_image_paths = [
		data + 'Ravnica Allegiance/imgs/',
		data + 'Guilds of Ravnica/imgs/',
		data + 'Throne of Eldraine/imgs/',
		data + "Ikoria Lair of Behemoths/imgs/",
		data + "Zendikar Rising/imgs/",
		data + "Zendikar/imgs/",
		data + 'Theros Beyond Death/imgs/',
		data + 'Dominaria/imgs/',
		data + 'Ixalan/imgs/',
		data + 'Hour of Devastation/imgs/',
		data + 'Amonkhet/imgs/',
		data + 'Aether Revolt/imgs/'
	]


# set lists
active_sets = [
	'Aether Revolt',
	'Amonkhet',
	'Dominaria',
	'Guilds of Ravnica',
	'Hour of Devastation',
	'Ikoria Lair of Behemoths',
	'Ixalan',
	'Ravnica Allegiance',
	'Theros Beyond Death',
	'Throne of Eldraine',
	'Zendikar',
	'Zendikar Rising'
]

number_of_images = {
	'Aether Revolt': 54,
	'Amonkhet': 78,
	'Dominaria': 132,
    'Guilds of Ravnica': 176,
	'Hour of Devastation': 115,
	'Ixalan': 264,
	'Ikoria Lair of Behemoths': 163,
	'Ravnica Allegiance': 256,
	'Theros Beyond Death': 223,
	'Throne of Eldraine': 178,
	'Zendikar': 229,
	'Zendikar Rising': 231
}

# headers
base_core_set_header = [
	'Set',
	'Set symbol',
	'Set code',
	'Release date',
	'Total Cards',
	'Common',
	'Uncommon',
	'Rare',
	'Mythic Rare',
	'Basic Land',
	'Other',
	're stat code',
	'status',
	're stat code',
	'api url'
]

expansion_set_header = [
	'Set',
	'Expansion symbol',
	'Expansion code',
	'Release date',
	'Total Cards',
	'Common',
	'Uncommon',
	'Rare',
	'Mythic Rare',
	'Basic Land',
	'Other',
	'status',
	're stat code',
	'api url'
]
