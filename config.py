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
		data + "Zendikar\\imgs\\"
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
		data + "Zendikar/imgs/"
	]


active_sets = [
	'Ravnica Allegiance',
	'Guilds of Ravnica',
	'Throne of Eldraine',
	'Ikoria Lair of Behemoths',
	'Zendikar Rising',
	'Zendikar'
]

number_of_images = {
	'Ravnica Allegiance': 256,
    'Guilds of Ravnica': 176,
	'Throne of Eldraine': 178,
	'Ikoria Lair of Behemoths': 163,
	'Zendikar Rising': 231,
	'Zendikar':229
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
