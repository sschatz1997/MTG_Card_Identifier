# main.pyimport os
import cv2
import sys
import time
import config
import os.path
import argparse
import requests
from art import *
import pandas as pd
from PIL import Image
from progress.bar import Bar
from difflib import SequenceMatcher
from colorama import init, Fore, Back, Style

# my functions 
from functions import get_all_cards, get_set_by_card_name1, image_compare_hash, image_compare_hash2
from functions import get_set_by_card_name2

# import pytesseract for windows or linux
if sys.platform == "win32":
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	init(convert=True, autoreset=True) # only this init works on windows
elif sys.platform == "linux":
	from pytesseract import image_to_string
	init(autoreset=True)


"""
pretty title 1
less then 150 pixel length for the title means that it will be stack and if not then it wont
"""
def pt1():
	size = int(os.get_terminal_size().columns)
	if size <= 150:
		tprint('''MTG Card 
		Identifier 
		Script''', font="slant")
	else:
		t1 = '''MTG Card Identifier Script'''
		tprint(t1, font="slant")

# this display error pretty begging
def dis_error():
	print(Fore.RED + "=====ERROR=====".center(os.get_terminal_size().columns))

def dis_error_end():
	print(Fore.RED + '==============='.center(os.get_terminal_size().columns))

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

"""
text splitlines text
splits the text and returns the list of options
"""
def split_text(text, p1):
	CN = get_all_cards()  # card names
	lines1 = text.splitlines()
	options = []
	for l in lines1:
		for c in CN:
			percent = similar(l, c)
			if percent > p1 or percent == p1:
				options.append([l, c, percent])  # text, name, percent

	return options

"""
text splitlines text
splits the text and returns the list of options
"""
def split_text2(text, p1):
	CN = get_all_cards()  # card names
	lines1 = text.splitlines()
	options = []
	for l in lines1:
		for c in CN:
			percent = similar(l, c)
			if percent > p1 or percent == p1:
				options.append([l, c, percent])  # text, name, percent

	return options

#compare the output of the AI and the actual names of the car if the ratio is above 0.9 as if its their card
def compare1(img, p1, og_image):
	# these chars can be stripped for better comparison
	stripable = ['=','!','?','-',"'",'.']

	# different systaxs for each system
	if sys.platform == "win32":
		text = pytesseract.image_to_string(img).strip()  # generated text || windows
	elif sys.platform == "linux":
		text = image_to_string(img).strip()  # generated text || linux

	# strip excess chars
	for strip in stripable:
		text = text.replace(strip, "")
	text = text.strip('\n')
	options = split_text(text, p1)

	x = 1

	for o in options:	
		# loop through possible sets
		ps = get_set_by_card_name1(str(o[1].replace(".jpg", "")))
		if len(ps) > 1: # if posible sets are greter then 1
			if o[2] >= p1:
				print(Fore.RED+"Guess: ", Fore.YELLOW+" {}".format(x))
				for p in ps:
					print(Fore.GREEN + "Text detected:", Fore.YELLOW + "{}".format(o[0]))
					print(Fore.GREEN + "Card name closest: ", Fore.YELLOW + "{}".format(o[1]))
					print(Fore.GREEN + "Percent Match: ", Fore.MAGENTA + "{}%".format(float(o[2]*100)))
					print(Fore.GREEN + "From Set: ", Fore.YELLOW + "{}.".format(p))
					hash1, hash2, checker = image_compare_hash(o[1], og_image, p)
					hash_dif = hash1 - hash2
					# only display hashes for in sets and where hash difference is more then percent
					if checker == 'in-set' and hash_dif == 0:
						comb = hash1 - hash2
						print(Fore.GREEN + "Hash from guessed Name: ", Fore.YELLOW + "{}".format(hash1))
						print(Fore.GREEN + "Hash from uploaded Image: ", Fore.YELLOW + "{}".format(hash2))
						print(Fore.GREEN + "Hash difference: ", Fore.YELLOW + "{}".format(hash1 - hash2))
						if comb == 0:
							print(Fore.GREEN + "The file you uploaded is", Fore.RED + " {}\n".format(o[1].replace(".jpg", "")))
							x += 1
					# else not in this set
					elif  checker == 'not-in-set':
						print(Fore.RED + "Not int this set, looping\n")
						x += 1
					else:
						print(Fore.RED + "Not int this set, looping\n")
						x += 1
		else:
			if o[2] >= p1:
				print(Fore.RED+"Guess: ", Fore.YELLOW+" {}".format(x))
				for p in ps:
					print(Fore.GREEN + "Text detected:", Fore.YELLOW + "{}".format(o[0]))
					print(Fore.GREEN + "Card name closest: ", Fore.YELLOW + "{}".format(o[1]))
					print(Fore.GREEN + "Percent Match: ", Fore.MAGENTA + "{}%".format(float(o[2]*100)))
					print(Fore.GREEN + "From Set: ", Fore.YELLOW + "{}.".format(p))
					hash1, hash2, checker = image_compare_hash(o[1], og_image, p)
					hash_dif = hash1 - hash2
					# only display hashes for in sets and where hash difference is more then percent
					if checker == 'in-set' and hash_dif == 0:
						comb = hash1 - hash2
						print(Fore.GREEN + "Hash from guessed Name: ", Fore.YELLOW + "{}".format(hash1))
						print(Fore.GREEN + "Hash from uploaded Image: ", Fore.YELLOW + "{}".format(hash2))
						print(Fore.GREEN + "Hash difference: ", Fore.YELLOW + "{}".format(hash1 - hash2))
						if comb == 0:
							print(Fore.GREEN + "The file you uploaded is", Fore.RED + " {}\n".format(o[1].replace(".jpg", "")))
							x += 1
					# else not in this set
					elif  checker == 'not-in-set':
						print(Fore.RED + "Not int this set, looping\n")
						x += 1
					else:
						print(Fore.RED + "Not int this set, looping\n")
						x += 1

	if len(options) < 1:
		print("File was less the a {}% match".format(p1*100))
		print("Make sure the card is in one of the following sets: ")
		as1 = config.active_sets
		for a in as1:
			print("\t--+ {} with {} entries.".format(a, config.number_of_images[a]))

# compare just 1
def compare2(img, p1, og_image):
	# these chars can be stripped for better comparison
	stripable = ['=', '!', '?', '-', "'", '.']

	# different systaxs for each system
	if sys.platform == "win32":
		text = pytesseract.image_to_string(img).strip()  # generated text || windows
	elif sys.platform == "linux":
		text = image_to_string(img).strip()  # generated text || linux

	# strip excess chars
	for strip in stripable:
		text = text.replace(strip, "")
	text = text.strip('\n')
	options = split_text2(text, p1)
	#options = options0[0]

	for o in options:
		print(Fore.GREEN + "Text detected:", Fore.YELLOW + "{}".format(o[0]))
		print(Fore.GREEN + "Card name closest: ", Fore.YELLOW + "{}".format(o[1]))
		print(Fore.GREEN + "Percent Match: ",Fore.MAGENTA + "{}%".format(float(o[2]*100)))
		print(Fore.GREEN + "From Set: ", Fore.YELLOW +"{}.".format(get_set_by_card_name2(str(o[1].replace(".jpg", "")))))
		hash1, hash2 = image_compare_hash2(o[1], og_image)
		comb = hash1 - hash2
		print(Fore.GREEN + "Hash from guessed Name: ",Fore.YELLOW + "{}".format(hash1))
		print(Fore.GREEN + "Hash from uploaded Image: ",Fore.YELLOW + "{}".format(hash2))
		print(Fore.GREEN + "Hash difference: ",Fore.YELLOW + "{}".format(hash1 - hash2))
		if comb == 0:
			print(Fore.GREEN + "The file you uploaded is",Fore.RED + " {}".format(o[1].replace(".jpg", "")))

	if len(options) < 1:
		print("File was less the a {}% match".format(p1*100))
		print("Make sure the card is in one of the following sets: ")
		as1 = config.active_sets
		for a in as1:
			print("\t--+ {} with {} entries.".format(a, config.number_of_images[a]))

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

# remote card testing with requests
def get_remote_card(url):
	im = Image.open(requests.get(url, stream=True).raw)
	return im

# check if the url is good
def check_url(url):
	stat_code = requests.get(url)
	return stat_code.status_code

"""
check if percent entered is:
	-+ equal or less 100 but not more
	-+ over 0.001
	-+ not a string
"""
def check_percent(per):
	try:
		per = float(per)
		if per <= 100:
			if per > 0:
				return True
			else:
				return "The percent can't be 0 or less, Exiting."
		else:
			return "The percent can't be over 100, Exiting."
	except:
		return "The percent can't be a string, Exiting."

# make sure the file type is acceptable
def check_file_type(f1):
	# good file types for imgs
	good_file_types = [
		'jpg',
		'jpeg',
		'png'
	]
	file_type = os.path.splitext(f1)[1][1:]
	if file_type in good_file_types:
		return True
	else:
		return "{} is not acceptable image type!".format(file_type)

def main():
	# break from the command some
	print("\n")

	# description
	description = "MTG_Card_Identifier: Find magic cards based on the Name on the card."
	# display the ascii title
	pt1()

	print(Fore.GREEN + "Starting the search:")

	parser = argparse.ArgumentParser('python3', description=description)
	requiredArgs = parser.add_argument_group('required named arguments')
	requiredArgs.add_argument('-img', '--Image', help='Insert path to the Image here.', required=True)
	parser.add_argument('-p', '--Percent', help='Enter the percent you want the comparison to be [whole numbers].', required=False, default=72)
	parser.add_argument('-url', '--URL', help='Tell the script that the -img is a url. Usage [ -url y ]', required=False, default='n')
	parser.add_argument('-num', '--Num', help='Just one of the possible cards or all of the cards within the percentage match. [ one or all ]', required=False, default='one')
	argument = parser.parse_args()

	# check if an image is an link or a path
	if argument.URL.lower() == 'n' or argument.URL.lower() == 'no':
		# check the file type
		if check_file_type(argument.Image) == True:
			img = str(argument.Image)  # user inputed file name
			head, tail = os.path.split(img)
			del head
			img = Image.open(img)
			og_image = img

			# check percent
			if check_percent(argument.Percent) == True:
				print(Fore.GREEN + "Checking File:",  Fore.LIGHTBLUE_EX + " {}".format(tail))
				percent = float(float(argument.Percent)/float(100))
				img = change_color(img)
				img = crop_image(img)
				if argument.Num.lower() == 'all':
					compare1(img, percent, og_image)
				elif argument.Num.lower() == 'one':
					compare2(img, percent, og_image)
				else:
					dis_error()
					print(Fore.RED + "{} isnt an option".format(argument.Num.lower().center(os.get_terminal_size().columns)))
					dis_error_end()

			else:
				print("\n\n")
				dis_error()
				print(Fore.RED + check_percent(argument.Percent).center(os.get_terminal_size().columns))
				dis_error_end()
		else:
			dis_error()
			print(Fore.RED + check_file_type(argument.Image).center(os.get_terminal_size().columns))
			dis_error_end()

	elif argument.URL.lower() == 'y' or argument.URL.lower() == 'yes':
		# this tru
		try:
			if int(check_url(argument.Image)) == 200:
				img = get_remote_card(argument.Image)
				og_image = img

				# check percent
				if check_percent(argument.Percent) == True:
					print(Fore.GREEN + "Checking URL:",  Fore.LIGHTBLUE_EX + " {}".format(argument.Image))
					percent = float(float(argument.Percent)/float(100))

					img = change_color(img)
					img = crop_image(img)

					if argument.Num.lower() == 'all':
						compare1(img, percent, og_image)
					elif argument.Num.lower() == 'one':
						compare2(img, percent, og_image)
					else:
						dis_error()
						print(Fore.RED +"{} isnt an option".format(argument.Num.lower().center(os.get_terminal_size().columns)))
						dis_error_end()
				else:
					dis_error()
					print(Fore.RED + check_percent(argument.Percent).center(os.get_terminal_size().columns))
					dis_error_end()

			else:
				dis_error()
				print('Bad URL returned a {} code. Exiting.'.format(check_url(argument.Image)))
				dis_error_end()

		except Exception as e:
			print(e)

		except:
			dis_error()
			print('Bad URL returned a {} code. Exiting.'.format(check_url(argument.Image)))
			dis_error_end()

	print(Fore.GREEN + "Ending the search\n")
	


if __name__ == "__main__":
	main()


