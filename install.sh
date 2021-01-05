#!/bin/sh
APPS = "libpng-dev libjpeg-dev libtiff-dev zlib1g-dev python3-opencv tesseract-ocr libtesseract-dev"

apt update 
apt install -y $APPS
pip3 install -r requirements.txt