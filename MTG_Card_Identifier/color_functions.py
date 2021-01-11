# color_functions.py
import sys
from colorama import init, Fore, Back, Style

# import pytesseract for windows or linux
if sys.platform == "win32":
	init(convert=True, autoreset=True)  # only this init works on windows
elif sys.platform == "linux":
	from pytesseract import image_to_string
	init(autoreset=True)


def add_green(val):
	return Fore.GREEN + val + Style.RESET_ALL

def add_magenta(val):
	return Fore.MAGENTA + val + Style.RESET_ALL

def add_green_dim(val):
	return Style.DIM + Fore.GREEN + val + Style.RESET_ALL

def add_yellow(val):
	return Fore.YELLOW + val + Style.RESET_ALL

def add_red(val):
	return Fore.RED + val + Style.RESET_ALL

def color_heading(val):
	return Style.BRIGHT + Fore.CYAN + val + Style.RESET_ALL

def add_blue(val):
	return Fore.BLUE + val + Style.RESET_ALL