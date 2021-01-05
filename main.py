# main.py

import os
import cv2
import sys
import time
import config
import argparse
import pandas as pd
from PIL import Image
from progress.bar import Bar
from difflib import SequenceMatcher
#from PIL.ExifTags import TAGS

# import pytesseract for windows or linux
if sys.platform == "win32":
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
elif sys.platform == "linux":
	from pytesseract import image_to_string

# change the images color


def change_color(img):
	black = (0, 0, 0)
	white = (255, 255, 255)
	threshold = (160, 160, 160)
	img = img.convert('LA')  # more grayscale
	img = make_bigger(img)  # may need to change location where this happens

	# pixel comparison
	pixels = img.getdata()
	newPixels = []

	# Compare each pixel
	for pixel in pixels:
		if pixel < threshold:
			newPixels.append(black)
		else:
			newPixels.append(white)

	return img

# make image 600x600


def make_bigger(img):
	im2 = img.resize((600, 600))
	return im2

# crop image


def crop_image(img):
	tup1 = (0, 15, 400, 80)  # new demensions
	cropped = img.crop(tup1)  # crop for title
	return cropped


# get all card names that it can return a picture
def get_all_cards():
	data = pd.read_csv(config.master_cards, index_col=False)
	card_names = list(data['card_name'])
	del data
	return card_names

#compare the output of the AI and the actual names of the car if the ratio is above 0.9 as if its their card


def compare1(img, p1):
	CN = get_all_cards()  # card names

	# different systaxs for each system
	if sys.platform == "win32":
		text = pytesseract.image_to_string(img).strip()  # generated text || windows
	elif sys.platform == "linux":
		text = image_to_string(img).strip()  # generated text || linux

	text = text.strip('\n')
	options = []
	for c in CN:
		percent = similar(text, c)
		if percent > p1 or percent == p1:
			options.append([text, c, percent])  # text, name, percent

	for o in options:
		print("{} and {} are {} percent a match\n".format(o[0], o[1], o[2]*100))

	if len(options) < 1:
		print("File was less the a {}% match".format(p1*100))
		print("Make sure the card is in one of the following sets: ")
		as1 = config.active_sets
		for a in as1:
			print("\t--+ {} with {} entries.".format(a, config.number_of_images[a]))


def output(to_log):
	file1 = config.main_path + "compare1.csv"
	# make 4 lists
	text = []
	name = []
	percent = []

	for t in to_log:
		text.append(t[0])
		name.append(t[1])
		percent.append(t[2])

	# make a dataframe
	NDF = {
		"text": text,
		"name": name,
		"percent": percent,
	}

	dataOut = pd.DataFrame(NDF, columns=['text', 'name', 'percent'])
	dataOut.to_csv(file1, encoding="utf-8", index=False)

# check the simularity between two strings
# credit: https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# get all images


def all_img():
	data = pd.read_csv(config.master_cards, index_col=False)
	card_names = list(data['images'])
	del data
	return card_names


def main():
	#img = str(sys.argv[1])  # user inputed file name
	parser = argparse.ArgumentParser(
		description='Arguments for the MTG Card Identifier.')
	parser.add_argument(
		'-img', '--Image', help='Insert path to the Image here.', required=True)
	parser.add_argument(
		'-p', '--Percent', help='Enter the percent you want the comparison to be [whole numbers].', required=False, default=72)
	argument = parser.parse_args()
	img = str(argument.Image)  # user inputed file name
	head, tail = os.path.split(img)
	percent = float(argument.Percent/100)
	print("Checking {}".format(tail))
	del head, tail
	img = Image.open(img)
	img = change_color(img)
	img = crop_image(img)
	compare1(img, percent)


if __name__ == "__main__":
	main()
