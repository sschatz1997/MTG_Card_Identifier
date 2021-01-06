# functions.py

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
	
	x = 0
	for cn in card_names:
		if str(cn) == card:
			place = x
		x += 1

	return set1[place]

# compare file by hash
def image_comapre_hash(name, imported):
	from_set = get_set_by_card_name1(name.replace(".jpg", ""))
	file1 = config.data + from_set + "\\imgs\\" + name + ".jpg"
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
