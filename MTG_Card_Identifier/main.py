# main.py
import os
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
from tabulate import tabulate
from difflib import SequenceMatcher
from colorama import init, Fore, Back, Style

# my functions 
from functions import return_img_display
from functions import get_all_cards, image_compare_hash, get_set_by_card_name
from functions import get_json_by_set, get_set_by_card2, get_multiverse_id_card, get_card_info
from color_functions import add_green, add_yellow, add_magenta, add_green_dim, add_red, color_heading


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
		Script!''', font="slant")
	else:
		t1 = '''MTG Card Identifier Script!'''
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

# compare just 1
def compare(img, p1, og_image, get_ci_arg, showQ):
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
	"""
	returns a list with:
	0: text detected
	1: possible name of a card
	2: percent of a match
	"""
	options = split_text(text, p1) 

	card = 1

	for o in options:
		hash1, hash2 = image_compare_hash(o[1], og_image)
		comb = hash1 - hash2
		#if float(o[2]*100) == 100:
		print(Fore.RED + "Card option {}".format(card).center(os.get_terminal_size().columns, '='))

		#print(Fore.GREEN + "Text detected:", Fore.YELLOW + "{}".format(o[0]))
		#print(Fore.GREEN + "Card name closest: ", Fore.YELLOW + "{}".format(o[1]))
		#print(Fore.GREEN + "Percent Match: ",Fore.MAGENTA + "{}%".format(float(o[2]*100)))
		#print(Fore.GREEN + "From Set: ", Fore.YELLOW +"{}".format(get_set_by_card_name(str(o[1].replace(".jpg", "")))))
		#print(Fore.GREEN + "Hash from guessed Name: ",Fore.YELLOW + "{}".format(hash1))
		#print(Fore.GREEN + "Hash from guessed Name: ",Fore.YELLOW + "{}".format(hash1))
		#print(Fore.GREEN + "Hash difference: ",Fore.YELLOW + "{}\n".format(hash1 - hash2))
		#print(Fore.GREEN + "Hash from uploaded Image: ",Fore.YELLOW + "{}".format(hash2))


		table = []
		# table test 1
		table.append([add_green("Text detected:"), add_yellow("{}".format(o[0]))])
		table.append([add_green("Text detected:"), add_yellow("{}".format(o[0]))])
		table.append([add_green("Card name closest: "), add_yellow("{}".format(o[1]))])
		out_percent = round(float(o[2]*100), 2)
		table.append([add_green("Percent Match: "),  add_magenta("{}%".format(out_percent))])
		table.append([add_green("From Set: "), add_yellow("{}".format(get_set_by_card_name(str(o[1].replace(".jpg", "")))))])
		table.append([add_green("Hash from guessed Name: "), add_yellow("{}".format(hash1))])
		table.append([add_green("Hash from uploaded Name: "), add_yellow("{}".format(hash2))])
		table.append([add_green("Hash difference: "), add_yellow("{}".format(hash1-hash2))])

		header = [color_heading('Info'), color_heading('Value')]
		print(tabulate(table, header, tablefmt='grid'))

		if comb == 0:
			print(Fore.GREEN + "The file you uploaded is",Fore.RED + " {}\n".format(o[1].replace(".jpg", "")))
			# print info if yes
			if get_ci_arg == 'yes':
				print("\n\n")
				print(Fore.CYAN + "Displaying Card Info".center(os.get_terminal_size().columns, '-'))
				get_card_info(o[1])

			if showQ == 'yes':
				#print(o[1])
				status, img_import = return_img_display(o[1])
				if status == 'ok':
					img_import.show()
				else:
					print('Image not found')
		card += 1


	if len(options) < 1:
		print(Fore.RED + "File was less the a {}% match".format(p1*100))
		print(Fore.GREEN + "Make sure the card is in one of the following sets: ")
		as1 = config.active_sets2
		for a in as1:
			print(Fore.GREEN + "\t--+ {} || {}.".format(a[0], a[-1]))
	

# check the simularity between two strings
# credit: https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

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

	print(Fore.CYAN + "Starting the search".center(os.get_terminal_size().columns, '='))

	parser = argparse.ArgumentParser('python3', description=description)
	requiredArgs = parser.add_argument_group('required named arguments')
	requiredArgs.add_argument('-img', '--Image', help='Insert path to the Image here.', required=True)
	parser.add_argument('-p', '--Percent', help='Enter the percent you want the comparison to be [whole numbers].', required=False, default=72)
	parser.add_argument('-url', '--URL', help='Tell the script that the -img is a url. Usage [ -url y ]', required=False, default='n')
	parser.add_argument('-ci', '--CI', help='Print out more information about a card if the script is 100 percent a match. [y or n]', required=False, default='no')
	parser.add_argument('-show','--Show', help='Show guessed image. [y or n]', required=False, default='no')
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
				print(Fore.GREEN + "Checking File:",  Fore.LIGHTBLUE_EX + " {}\n".format(tail))
				percent = float(float(argument.Percent)/float(100))
				img = change_color(img)
				img = crop_image(img)

				# check get_ci_arg \ card info
				if argument.CI.lower() == 'y' or argument.CI.lower() == 'yes':
					# check image show
					if argument.Show.lower() == 'y' or argument.Show.lower() == 'yes':
						compare(img, percent, og_image, 'yes', 'yes')
					elif argument.Show.lower() == 'n' or argument.Show.lower() == 'no':
						compare(img, percent, og_image, 'yes', 'no')
				elif argument.CI.lower() == 'n' or argument.CI.lower() == 'no':
					# check image show
					if argument.Show.lower() == 'y' or argument.Show.lower() == 'yes':
						compare(img, percent, og_image, 'no', 'yes')
					elif argument.Show.lower() == 'n' or argument.Show.lower() == 'no':
						compare(img, percent, og_image, 'no', 'no')
				else:
					print("\n\n")
					dis_error()
					print(Fore.RED + "{} is not a valid arguement!".format(argument.CI).center(os.get_terminal_size().columns))
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
					print(Fore.GREEN + "Checking URL:",  Fore.LIGHTBLUE_EX + " {}\n".format(argument.Image))
					percent = float(float(argument.Percent)/float(100))
					img = change_color(img)
					img = crop_image(img)

					# check get_ci_arg \ card info
					if argument.CI.lower() == 'y' or argument.CI.lower() == 'yes':
						# check image show
						if argument.Show.lower() == 'y' or argument.Show.lower() == 'yes':
							compare(img, percent, og_image, 'yes', 'yes')
						elif argument.Show.lower() == 'n' or argument.Show.lower() == 'no':
							compare(img, percent, og_image, 'yes', 'no')
					elif argument.CI.lower() == 'n' or argument.CI.lower() == 'no':
						# check image show
						if argument.Show.lower() == 'y' or argument.Show.lower() == 'yes':
							compare(img, percent, og_image, 'no', 'yes')
						elif argument.Show.lower() == 'n' or argument.Show.lower() == 'no':
							compare(img, percent, og_image, 'no', 'no')

						#compare(img, percent, og_image, 'no')
					else:
						print("\n\n")
						dis_error()
						print(Fore.RED + "{} is not a valid arguement!".format(argument.CI).center(os.get_terminal_size().columns))
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

	print(Fore.CYAN + "Ending the search".center(os.get_terminal_size().columns, '='))

	
	


if __name__ == "__main__":
	main()


