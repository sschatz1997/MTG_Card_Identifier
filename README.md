![Generic badge](https://img.shields.io/badge/Python-3.7.3-informal.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/sschatz1997/MTG_Card_Identifier.png?branch=main)](https://travis-ci.com/{{sschatz1997}}/{{MTG_Card_Identifier}})
# MTG_Card_Identifier

MTG_Card_Identifier is a python based program to identify Magic: The Gathering cards based on the Card name in the image that the user uploads.

## Installation

### Linux 
```
# Run the install.sh script
$ sudo sh install.sh
```

### Windows 
- Run:
```
> pip3 install -r requirements.txt
```
- May have to install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)

## Usage 
```
$ python3 -img IMAGE [-p PERCENT] [-url URL]

MTG_Card_Identifier: Find magic cards based on the Name on the card.
 
Optional arguments:
  -h, --help            show this help message and exit
  -p PERCENT, --Percent PERCENT
                        Enter the percent you want the comparison to be [whole numbers].
  -url URL, --URL URL   Tell the script that the -img is a url. Usage [ -url y ]
  
required named arguments:
  -img IMAGE, --Image IMAGE
                        Insert path local or remote.
```

## Requirements
### Python:
- [opencv_python](https://pypi.org/project/opencv-python/)
- [pandas](https://pypi.org/project/pandas/)
- [progress](https://pypi.org/project/progress/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow](https://pypi.org/project/Pillow/)


## Sets included:
- Aether Revolt [MTG Official Link](https://magic.wizards.com/en/products/aether-revolt)
- Amonkhet [MTG Official Link](https://magic.wizards.com/en/products/amonkhet)
- Dominaria [MTG Official Link](https://magic.wizards.com/en/products/dominaria)
- Guilds of Ravnica [MTG Official Link](https://magic.wizards.com/en/products/guilds-ravnica)
- Hour of Devastation [MTG Official Link](https://magic.wizards.com/en/products/hour-devastation)
- Ikoria Lair of Behemoths [MTG Official Link](https://magic.wizards.com/en/products/ikoria)
- Ixalan [MTG Official Link](https://magic.wizards.com/en/products/ixalan)
- Ravnica Allegiance [MTG Official Link](https://magic.wizards.com/en/products/ravnica-allegiance)
- Theros Beyond Death [MTG Official Link](https://magic.wizards.com/en/products/TherosBeyondDeath)
- Throne of Eldraine [MTG Official Link](https://magic.wizards.com/en/products/throne-of-eldraine)
- Zendikar [MTG Official Link](https://magic.wizards.com/en/products/zendikar)
- Zendikar Rising [MTG Official Link](https://magic.wizards.com/en/products/zendikar-rising)







**NOTE: All images belong to Magic: The Gathering and Wizards of the Coast respectively**
