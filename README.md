  ![Generic badge](https://img.shields.io/badge/Python-3.7.3-informal.svg)
  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
  [![Build Status](https://www.travis-ci.com/sschatz1997/MTG_Card_Identifier.svg?branch=main)](https://www.travis-ci.com/sschatz1997/MTG_Card_Identifier)
  [![PyPi Version](https://img.shields.io/pypi/v/MTG_Card_Identifier.svg)](https://pypi.python.org/pypi/MTG_Card_Identifier/)
  # MTG_Card_Identifier

  MTG_Card_Identifier is a python based program to identify Magic: The Gathering cards based on the Card name in the image that the user uploads.
```

    __  ___  ______   ______          ______                       __
   /  |/  / /_  __/  / ____/         / ____/  ____ _   _____  ____/ /
  / /|_/ /   / /    / / __          / /      / __ `/  / ___/ / __  /
 / /  / /   / /    / /_/ /         / /___   / /_/ /  / /    / /_/ /
/_/  /_/   /_/     \____/          \____/   \__,_/  /_/     \__,_/

    ____       __                 __     _     ____    _
   /  _/  ____/ /  ___    ____   / /_   (_)   / __/   (_)  ___    _____
   / /   / __  /  / _ \  / __ \ / __/  / /   / /_    / /  / _ \  / ___/
 _/ /   / /_/ /  /  __/ / / / // /_   / /   / __/   / /  /  __/ / /
/___/   \__,_/   \___/ /_/ /_/ \__/  /_/   /_/     /_/   \___/ /_/

   _____                   _             __     __
  / ___/  _____   _____   (_)    ____   / /_   / /
  \__ \  / ___/  / ___/  / /    / __ \ / __/  / /
 ___/ / / /__   / /     / /    / /_/ // /_   /_/
/____/  \___/  /_/     /_/    / .___/ \__/  (_)
                             /_/
```
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
### PIP
```
pip install MTG-Card-Identifier
```

## Usage 
```
# change into the script directory 
cd MTG_Card_Identifier
$ python3 main.py -img IMAGE [-url URL] [-dir DIR] [-batchFile BATCHFILE] [-p PERCENT] [-ci CI] [-show SHOW]

MTG_Card_Identifier: Find magic cards based on the Name on the card.

optional arguments:
  -h, --help            show this help message and exit
  -url URL, --URL URL   Tell the script that the -img is a url. Usage [ -url y ]
  -dir DIR, --DIR DIR   Batch directory check the script that the -dir is a directory. Usage [-dir y]
  -batchFile BATCHFILE, --BatchFile BATCHFILE
                        Batch File will process the contents. The args tell us if its local or remote.
  -p PERCENT, --Percent PERCENT
                        Enter the percent you want the comparison to be [whole numbers].
  -ci CI, --CI CI       Print out more information about a card if the script is 100 percent a match. 
                        [y or n]
  -show SHOW, --Show SHOW
                        Show guessed image. [y or n]

required named arguments:
  -img IMAGE, --Image IMAGE
                        Insert path to the Image here.
```

## Batch File format

### txt File
Just links for either local paths or URLs.
```
https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=916&type=card
```

### CSV Files
A header line then just links for either local paths or URLs.
```
header
https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=916&type=card
```
  ## Sets included:
| Set Name | Cards Available | Total Cards in Set | Set Name | Cards Available | Total Cards in Set |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| [Arabian Nights](https://magic.wizards.com/en/products/aether-revolt) | 92 | 92 | [Lorwyn](https://magic.wizards.com/en/products/legions) | 301 | 301 |
| [Antiquities](https://magic.wizards.com/en/products/alara-reborn) | 100 | 101 | [Morningtide](https://magic.wizards.com/en/products/lorwyn) | 150 | 150 |
| [Legends](https://magic.wizards.com/en/products/alliances) | 310 | 310 | [Shadowmoor](https://magic.wizards.com/en/products/mercadian-masques) | 301 | 302 |
| [The Dark](https://magic.wizards.com/en/products/amonkhet) | 119 | 122 | [Eventide](https://magic.wizards.com/en/products/mirage) | 180 | 180 |
| [Fallen Empires](https://magic.wizards.com/en/products/antiquities) | 187 | 187 | [Shards of Alara](https://magic.wizards.com/en/products/mirrodin) | 249 | 249 |
| [Ice Age](https://magic.wizards.com/en/products/apocalypse) | 383 | 383 | [Conflux](https://magic.wizards.com/en/content/mirrodin-besieged-card-set-archive-products-game-info) | 145 | 145 |
| [Homelands](https://magic.wizards.com/en/products/arabian-nights) | 140 | 140 | [Alara Reborn](https://magic.wizards.com/en/products/morningtide) | 145 | 145 |
| [Alliances](https://magic.wizards.com/en/products/avacyn-restored) | 199 | 199 | [Worldwake](https://magic.wizards.com/en/products/nemesis) | 145 | 145 |
| [Mirage](https://magic.wizards.com/en/content/battle-zendikar-cards) | 350 | 351 | [Rise of the Eldrazi](https://magic.wizards.com/en/products/new-phyrexia) | 248 | 248 |
| [Visions](https://magic.wizards.com/en/game-info/products/card-set-archive/betrayers-of-kamigawa) | 167 | 167 | [Scars of Mirrodin](https://magic.wizards.com/en/content/oath-gatewatch-cards) | 249 | 249 |
| [Weatherlight](https://magic.wizards.com/en/products/born-of-the-gods) | 167 | 167 | [Mirrodin Besieged](https://magic.wizards.com/en/products/odyssey) | 155 | 155 |
| [Tempest](https://magic.wizards.com/en/game-info/products/card-set-archive/champions-of-kamigawa) | 350 | 350 | [New Phyrexia](https://magic.wizards.com/en/products/onslaught) | 175 | 175 |
| [Stronghold](https://magic.wizards.com/en/products/coldsnap) | 143 | 143 | [Innistrad](https://magic.wizards.com/en/products/planar-chaos) | 284 | 284 |
| [Exodus](https://magic.wizards.com/en/products/conflux) | 143 | 143 | [Dark Ascension](https://magic.wizards.com/en/products/planeshift) | 171 | 171 |
| [Urza's Saga](https://magic.wizards.com/en/products/dark-ascension) | 350 | 356 | [Avacyn Restored](https://magic.wizards.com/en/content/productpagemasques3prophecy) | 244 | 244 |
| [Urza's Legacy](https://magic.wizards.com/en/products/darksteel) | 143 | 143 | [Return to Ravnica](https://magic.wizards.com/en/products/ravnica-allegiance) | 274 | 274 |
| [Urza's Destiny](https://magic.wizards.com/en/products/dissension) | 143 | 143 | [Gatecrash](https://magic.wizards.com/en/game-info/products/card-set-archive/ravnica-city-of-guilds) | 249 | 249 |
| [Mercadian Masques](https://magic.wizards.com/en/products/dominaria) | 350 | 350 | [Dragon's Maze](https://magic.wizards.com/en/products/return-to-ravnica) | 156 | 156 |
| [Nemesis](https://magic.wizards.com/en/products/dragons-maze) | 143 | 143 | [Theros](https://magic.wizards.com/en/game-info/products/card-set-archive/rise-of-the-eldrazi) | 249 | 249 |
| [Prophecy](https://magic.wizards.com/en/game-info/products/card-set-archive/dragons-of-tarkir) | 143 | 144 | [Born of the Gods](https://magic.wizards.com/en/products/rivals-ixalan) | 165 | 165 |
| [Invasion](https://magic.wizards.com/en/content/eldritch-moon-cards) | 355 | 356 | [Journey into Nyx](https://magic.wizards.com/en/game-info/products/card-set-archive/saviors-of-kamigawa) | 165 | 165 |
| [Planeshift](https://magic.wizards.com/en/products/eventide) | 146 | 146 | [Khans of Tarkir](https://magic.wizards.com/en/game-info/products/card-set-archive/scars-of-mirrodin) | 269 | 269 |
| [Apocalypse](https://magic.wizards.com/en/game-info/products/card-set-archive/exodus) | 148 | 148 | [Fate Reforged](https://magic.wizards.com/en/products/scourge) | 185 | 185 |
| [Odyssey](https://magic.wizards.com/en/products/fallen-empires) | 350 | 352 | [Dragons of Tarkir](https://magic.wizards.com/en/products/shadowmoor) | 264 | 264 |
| [Torment](https://magic.wizards.com/en/game-info/products/card-set-archive/fate-reforged) | 143 | 143 | [Oath of the Gatewatch](https://magic.wizards.com/en/content/shadows-over-innistrad-cards) | 186 | 187 |
| [Judgment](https://magic.wizards.com/en/products/fifth-dawn) | 143 | 143 | [Shadows over Innistrad](https://magic.wizards.com/en/game-info/products/card-set-archive/shards-of-alara) | 330 | 331 |
| [Onslaught](https://magic.wizards.com/en/products/future-sight) | 350 | 350 | [Eldritch Moon](https://magic.wizards.com/en/products/stronghold) | 223 | 223 |
| [Legions](https://magic.wizards.com/en/products/gatecrash) | 145 | 145 | [Kaladesh](https://magic.wizards.com/en/products/tempest) | 274 | 278 |
| [Scourge](https://magic.wizards.com/en/products/guildpact) | 143 | 143 | [Aether Revolt](https://magic.wizards.com/en/products/the-dark) | 194 | 197 |
| [Mirrodin](https://magic.wizards.com/en/products/guilds-ravnica) | 306 | 306 | [Amonkhet](https://magic.wizards.com/en/products/theros) | 287 | 287 |
| [Darksteel](https://magic.wizards.com/en/products/homelands) | 165 | 165 | [Hour of Devastation](https://magic.wizards.com/en/products/TherosBeyondDeath) | 209 | 209 |
| [Fifth Dawn](https://magic.wizards.com/en/products/hour-devastation) | 165 | 165 | [Ixalan](https://magic.wizards.com/en/products/time-spiral) | 299 | 299 |
| [Champions of Kamigawa](https://magic.wizards.com/en/products/ice-age) | 307 | 307 | [Rivals of Ixalan](https://magic.wizards.com/en/products/torment) | 212 | 212 |
| [Betrayers of Kamigawa](https://magic.wizards.com/en/products/Ikoria) | 165 | 165 | [Dominaria](https://magic.wizards.com/en/products/urzas-destiny) | 280 | 280 |
| [Saviors of Kamigawa](https://magic.wizards.com/en/products/innistrad) | 165 | 165 | [War of the Spark](https://magic.wizards.com/en/products/urzas-legacy) | 275 | 311 |
| [Ravnica City of Guilds](https://magic.wizards.com/en/products/invasion) | 306 | 306 | [Theros Beyond Death](https://magic.wizards.com/en/products/urzas-saga) | 283 | 356 |
| [Guildpact](https://magic.wizards.com/en/products/ixalan) | 165 | 165 | [Zendikar Rising](https://magic.wizards.com/en/products/visions) | 368 | 391 |
| [Dissension](https://magic.wizards.com/en/product/journey-nyx-card-set-archive-products-game-info) | 180 | 180 | [Zendikar](https://magic.wizards.com/en/products/warofthespark-bolas) | 269 | 269 |
| [Coldsnap](https://magic.wizards.com/en/game-info/products/card-set-archive/judgment) | 155 | 155 | [Ikoria Lair of Behemoths](https://magic.wizards.com/en/products/weatherlight) | 289 | 384 |
| [Time Spiral](https://magic.wizards.com/en/content/kaladesh-cards) | 301 | 301 | [Battle for Zendikar](https://magic.wizards.com/en/products/worldwake) | 299 | 299 |
| [Planar Chaos](https://magic.wizards.com/en/content/khans-tarkir-card-set-archive-products-game-info) | 165 | 165 | [Guilds of Ravnica](https://magic.wizards.com/en/products/zendikar) | 273 | 273 |
| [Future Sight](https://magic.wizards.com/en/products/legends) | 180 | 180 | [Ravnica Allegiance](https://magic.wizards.com/en/products/zendikar-rising) | 273 | 273 |







  **NOTE: All images belong to Magic: The Gathering and Wizards of the Coast respectively**
