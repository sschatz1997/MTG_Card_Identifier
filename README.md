![Generic badge](https://img.shields.io/badge/Python-3.7.3-informal.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/sschatz1997/MTG_Card_Identifier.png?branch=main)](https://travis-ci.org/{{sschatz1997}}/{{MTG_Card_Identifier}})
# MTG_Card_Identifier

MTG_Card_Identifier is a python based program to identify Magic: The Gathering cards based on their title.

## Installation

### Linux 
- Run the install.sh script

### Windows 
- Run:
```
pip3 install -r requirements.txt
```
- May have to install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)

## Usage 
```
$ python3 -img [ image ] -p [ percent of matching you want ]
  -h, --help            show this help message and exit
  -img IMAGE, --Image IMAGE
                        Insert path to the Image here.
  -p PERCENT, --Percent PERCENT
                        Enter the percent you want the comparison to be [whole numbers].
```

## Requirements
### Python:
- [opencv_python](https://pypi.org/project/opencv-python/)
- [pandas](https://pypi.org/project/pandas/)
- [progress](https://pypi.org/project/progress/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow](https://pypi.org/project/Pillow/)


## Sets included:
- Ravnica Allegiance
- Guilds of Ravnica
- Throne of Eldraine
- Ikoria Lair of Behemoths
- Zendikar Rising
- Zendikar







**NOTE: All images belong to Magic: The Gathering and Wizards of the Coast respectively**
