#!/bin/sh

apt update 
apt install -y libpng-dev libjpeg-dev libtiff-dev zlib1g-dev python3-opencv tesseract-ocr libtesseract-dev
pip3 install -r requirements.txt