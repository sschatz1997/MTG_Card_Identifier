# dir_functions.py

import os
import csv
import sys
import config
#from os import path


# make sure the file type is acceptable
def check_file_type(f1):
	# good file types for imgs
	good_file_types = ['jpg','jpeg','png']
	file_type = os.path.splitext(f1)[1][1:]
	if file_type in good_file_types:
		return True
	elif os.path.isdir(f1) == True:
		return "Can not read from sub directories!"
	else:
		return ".{} is not acceptable image type!".format(file_type)

# function to check if a file exists
def check_exists(f1):
	if os.path.isfile(f1) == True:
		return True
	elif os.path.isdir(f1) == True:
		return "Path returned not file!"
	else:
		return False

"""
check to see wether the script needs to add paths to dir
"""
def check_target_dir(path1): #, file1):
	# first check if path is in the dir of the script
	script_path = os.path.dirname(os.path.realpath(__file__))
	
	# create a test path by adding main and separator
	tp = config.main_path + path1
	if script_path == path1:
		return script_path
	elif os.path.isdir(tp) == True:
		return tp + config.separator
	else:
		return path1 + config.separator


"""
batch dir checker function
	-- takes in a dir, and list of all file
	-- loops through the list checks the file
	-- returns the good ones and tells the user which ones cant be searched for
"""
def dir_checker(mainP, path1):
		# turn into a managable path test || maybe add this back later
		#manageable_path = config.main_path + uploaded_path + config.separator + path1
		
		good_files = [] # a good file list
		bad_files = [] # bad file list
		total_files = len(path1) # number of total file
		bad_files_c = 0
		target_path = check_target_dir(mainP)
		for p in path1:
			# temp var 
			tv = target_path + p
			# check if exists
			if check_exists(tv) == True:
				# check the file type
				if check_file_type(tv) == True:
					good_files.append(tv)
				else:
					bad_files.append(tv)
					bad_files_c += 1
			else:
				bad_files.append(tv)
				bad_files_c += 1

		for b in bad_files:
			print('File {} can not be checked'.format(b))
		
		return total_files, good_files

# just returns a basic csv file
def in_csv(file1):
	data = []
	with open(file1, 'r', newline='') as f:
		r1 = csv.reader(f)
		for row in r1:
			data.append(row[-1])
	f.close()
	# delete the first row for the header 
	del data[0]
	return data


# this is for a batch file that contains path links
def read_batch_txt_path(file1):
	# check if file is real
	#print(os.path.splitext(file1)[1][1:])
	#print(os.path.isfile(file1))
	if os.path.isfile(file1) == True:
		file1 = open(file1, 'r')
		Lines = file1.readlines()
		good_files = []
		bad_files = []
		bad_files_c = 0
		total_files = len(Lines)
		for l in Lines:
			# temp var
			tv = l.rstrip('\n')
			if check_exists(tv) == True:
				# check the file type
				if check_file_type(tv) == True:
					good_files.append(tv)
				else:
					bad_files.append(tv)
					bad_files_c += 1
			else:
				bad_files.append(tv)
				bad_files_c += 1
	else:
		print('File does not exist!')
	del Lines

	for b in bad_files:
		print('File {} can not be checked'.format(b))

	return total_files, good_files

# this is for a batch file that contains url links
def read_batch_txt_url(file1):
	from functions import check_url
	# check if link file is real
	#print(os.path.splitext(file1)[1][1:])
	#print(os.path.isfile(file1))
	if os.path.isfile(file1) == True:
		file1 = open(file1, 'r')
		Lines = file1.readlines()
		good_files = []
		bad_files = []
		bad_files_c = 0
		total_files = len(Lines)
		for l in Lines:
			# temp var
			tv = l.rstrip('\n')
			# check if link is good
			if int(check_url(tv)) == 200: # its gonna check it twice 
				good_files.append(tv)
			elif int(check_url(tv)) != 200:
				bad_files.append(tv)
				bad_files_c += 1

	else:
		print('File does not exist!')
	del Lines

	for b in bad_files:
		print('File {} can not be checked'.format(b))

	return total_files, good_files


# this is for a batch file that contains path links
def read_batch_csv_path(file1):
	if os.path.isfile(file1) == True:
		# read in data from csv
		Lines = in_csv(file1)
		good_files = []
		bad_files = []
		bad_files_c = 0
		total_files = len(Lines)
		for l in Lines:
			# temp var
			tv = l.rstrip('\n')
			#print(check_exists(tv))
			if check_exists(tv) == True:
				# check the file type
				if check_file_type(tv) == True:
					good_files.append(tv)
				else:
					bad_files.append(tv)
					bad_files_c += 1
			else:
				bad_files.append(tv)
				bad_files_c += 1
	else:
		print('File does not exist!')
	del Lines

	for b in bad_files:
		print('File {} can not be checked'.format(b))

	return total_files, good_files


# this is for a batch file that contains url links
def read_batch_csv_url(file1):
	from functions import check_url
	if os.path.isfile(file1) == True:
		# read in data from csv
		Lines = in_csv(file1)
		good_files = []
		bad_files = []
		bad_files_c = 0
		total_files = len(Lines)
		for l in Lines:
			# temp var
			tv = l.rstrip('\n')
			# check if link is good
			if int(check_url(tv)) == 200:  # its gonna check it twice
				good_files.append(tv)
			elif int(check_url(tv)) != 200:
				bad_files.append(tv)
				bad_files_c += 1

	else:
		print('File does not exist!')
	del Lines

	for b in bad_files:
		print('File {} can not be checked'.format(b))

	return total_files, good_files
