# functions.py

import os
import sys
import config
import requests
import imagehash
import pandas as pd
from PIL import Image
from tabulate import tabulate
from color_functions import add_green, add_yellow, add_magenta, add_green_dim, add_red, color_heading


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


# returns 1 set
def get_set_by_card2(card):
	df1 = pd.read_csv(config.all_good, index_col=False)
	try:
		set1 = list(df1.loc[df1['card_name'] == str(card)]['set'])[-1]
		return set1
	except:
		return "No set associated with that card."


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

# get card multiverse id by name
def get_multiverse_id_card(card):
	df1 = pd.read_csv(config.all_good, index_col=False)
	try:
		id1 = list(df1.loc[df1['card_name'] == str(card)]['multiverse_id'])[-1]
		return id1 # is an int
	except:
		return "No card by that name."

def get_json_by_set(set1):
	df1 = pd.read_csv(config.set_info)
	try:
		url1 = list(df1.loc[df1['set'] == set1]['api_url'])[-1]
		return url1 # json url
	except:
		return "No set by that name."

"""
gets set -> then gets the api url -> gets the data -> prints it out
"""
def get_card_info(card):
	print(color_heading('Getting Card {}'.format(card)))
	set1 = get_set_by_card2(card)
	#print("The set is {}".format(set1))
	api_json = get_json_by_set(set1)
	#print("The api url is {}".format(api_json))

	raw_data = get_api_data(api_json, card)
	#print(len(raw_data))
	process_raw_data(raw_data)


"""
list info : type :  
	name: str
	colorIdentity: list
	convertedManaCost: float
	manaCost: str
	type: str
	types: list
	supertypes: list
	text: str
	rarity: str
	power: str
	toughness: str
	availability: list
	printings: list
neds to be a list [key, value]
for nested list extend it to have a +1 for the key
"""
def process_raw_data(raw_data):
	keys = config.card_info_api_keys_ftable
	new_data = []
	new_data2 = []
	lables = []
	x = 0
	max1 = len(keys)
	while x != max1:
		val = raw_data[x]
		if type(val) == list:
			counter = 1
			for v in val:
				if str(keys[x]) == 'Name':
					new_data2.append([add_green(keys[x] + " {}".format(counter)), add_red(str(v))])
					print("?")

				new_data2.append(
					[add_green(keys[x] + " {}".format(counter)),  add_yellow(str(v))])
				new_data.append(str(v))
				lables.append(keys[x] + " {}:".format(counter))
				counter += 1
		else:
			if str(keys[x]) == 'Name':
				new_data2.append([add_green(keys[x]), add_red(str(val))])

			elif str(keys[x]) == 'Converted Mana Cost' or str(keys[x]) == 'Power' or str(keys[x]) == 'Toughness':
				new_data2.append([add_green(keys[x]), add_magenta(str(val))])

			else:
				new_data2.append([add_green(keys[x]), add_yellow(str(val))])
				new_data.append(str(val))
				lables.append(keys[x]+":")
		x += 1

	header = [color_heading('Key'), color_heading('Value')]
	print(tabulate(new_data2, header, tablefmt='fancy_grid'))
	print('\n')


"""
get the dataframe down to the card info from the api url with the cards info
"""
def get_api_data(url, name):
	re1 = requests.get(url) # get request
	j1 = re1.json() # json 
	df = pd.DataFrame.from_dict(j1) # dataframe all
	out_data = df['data']['cards'] # is a dict
	del df # save memory
	#print(out_data[-1].keys())
	raw_data = []
	#columns = []
	for o in out_data: # loop through all the nested dicts
		#print(o[name])
		if o['name'] == name:
			#print(o)
			#dict_keys = list(o.keys())
			keys = config.card_info_api_keys
			for k in keys:
				try:
					val = o[k]
					if k == 'colorIdentity':
						raw_data.append(color_change(val))
					else:
						raw_data.append(val)
				except:
					raw_data.append('None')
					#print("{}: {}\n".format(k, o[k]))
					#print("{} type: {}\n".format(k, type(o[k])))	
				#print("{}: {}\n".format(k, o[k]))
	return raw_data

# change the colors from one letter to a word
def color_change(color_list):
	newL = []
	for color_string in color_list:
		if color_string == 'B':
			newL.append('Black')
		elif color_string == 'U':
			newL.append('Blue')
		elif color_string == 'R':
			newL.append('Red')
		elif color_string == 'W':
			newL.append('White')
	return newL


# return image type to display
def return_img_display(name):
	df1 = pd.read_csv(config.all_good, index_col=False)
	try:
		url = list(df1.loc[df1['card_name'] == str(name)]['image_url'])[-1]
		img = Image.open(requests.get(url, stream=True).raw)
		return 'ok', img
	except:
		return 'no file found', 0
