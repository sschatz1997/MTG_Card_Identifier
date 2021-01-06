# functions.py

import os
import sys
import config
import imagehash
import pandas as pd
from PIL import Image


# get all card names that it can return a picture
def get_all_cards():
	data = pd.read_csv(config.master_cards, index_col=False)
	card_names = list(data['card_name'])
	del data
	return card_names

# get the set from the master cards file 
def get_set_by_card_name1(card):
	data = pd.read_csv(config.master_cards, index_col=False)
	card_names = list(data['card_name'])
	set1 = list(data['set'])
	
	places = []

	x = 0
	for cn in card_names:
		if str(cn) == card:
			places.append(x)
		x += 1

	possible_sets = []

	# return all the sets it could be from
	for p in places:
		possible_sets.append(set1[p])

	return possible_sets

# get the set from the master cards file 
def get_set_by_card_name2(card):
	data = pd.read_csv(config.master_cards, index_col=False)
	card_names = list(data['card_name'])
	set1 = list(data['set'])
	
	x = 0
	for cn in card_names:
		if str(cn) == card:
			place = x
		x += 1
	return set1[place]

# get image path per os
def img_path():
	if sys.platform == "win32":
		return "\\imgs\\"
	elif sys.platform == "linux":
		return "/imgs/"

# compare file by hash
def image_compare_hash(name, imported, p):
	try:
		#from_set = get_set_by_card_name(name.replace(".jpg", ""))
		file1 = config.data + p + img_path() + name + ".jpg"
		hash1 = imagehash.average_hash(Image.open(file1))
		hash2 = imagehash.average_hash(imported)
		return hash1, hash2, 'in-set' 
	except:
		return 0, 0, 'not-in-set'

# compare file by hash
def image_compare_hash2(name, imported):
	from_set = get_set_by_card_name2(name.replace(".jpg", ""))
	file1 = config.data + from_set + img_path() + name + ".jpg"
	hash1 = imagehash.average_hash(Image.open(file1))
	hash2 = imagehash.average_hash(imported)
	return hash1, hash2 

"""
print("Hash1 : ", hash1)
print('\n')
print("Hash2 : ", hash2)
print('\n')
print(hash1 - hash2)
#file2 = config.data + from_set + "\\imgs\\" + guess_file + ".jpg"
"""
#get_set_by_card_name1('Hedron Crab')
"""
# combine the two lists
comb = []
x = 0
while (x != len(data)):
	comb.append([card_names[x], set1[x]])
	x += 1
"""
