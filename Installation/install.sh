#!/bin/bash
pip3 install selenium
#adding geckodriver to your system
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xvfz geckodriver-v0.24.0-linux64.tar.gz
mv geckodriver ~/.local/bin
rm -rf geckodriver-v0.24.0-linux64.tar.gz
#Thats it, jai mata di
