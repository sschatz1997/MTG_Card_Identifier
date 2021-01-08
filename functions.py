# functions.py
import os
import sys
import config
import requests
import imagehash
import pandas as pd
from PIL import Image

# get all card names that it can return a picture
def get_all_cards():
	data = pd.read_csv(config.all_good, index_col=False)
	card_names = list(data['card_name'])
	del data
	return card_names

# get the set from the master cards file
def get_set_by_card_name(card):
	data = pd.read_csv(config.all_good, index_col=False)
	card_names = list(data['card_name'])
	set1 = list(data['set'])

	places = []

	x = 0
	for cn in card_names:
		if str(cn) == card:
			places.append(x)
		x += 1
	return set1[places[-1]]

# compare file by hash
def image_compare_hash(name, imported):
	df1 = pd.read_csv(config.all_good, index_col=False)
	#df1 = pd.read_csv(config.all_bad, index_col=False)
	try:
		url = list(df1.loc[df1['card_name'] == str(name)]['image_url'])[-1]
		hash1 = imagehash.average_hash(
			Image.open(requests.get(url, stream=True).raw))
		hash2 = imagehash.average_hash(imported)
		return hash1, hash2
	except:
		return 0, 0
