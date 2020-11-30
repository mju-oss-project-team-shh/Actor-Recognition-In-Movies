#!/bin/bash

echo "*****************************************************"
echo "*****************************************************"
echo "***        Installer for Ubuntu 18.04 LTS         ***"
echo "*****************************************************"
echo "*****************************************************"
echo ""
echo "====================================================="
echo "***** Install or update Python to version 3.8.x *****"
echo "====================================================="
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.8 python3.8-dev
echo ""
echo "====================================================="
echo "*****      Install packages in virtualenv       *****"
echo "====================================================="
sudo apt update
sudo apt install virtualenv
virtualenv -p python3.8 venv
. venv/bin/activate
pip install cmake
pip install dlib pyqt5
pip install imutils jupyter scipy pandas opencv-python face-recognition sklearn numpy progressbar console-menu selenium bs4 requests
pip install chromedriver-autoinstaller
echo ""
echo "DONE. Run 'source venv/bin/activate' to activate virtualenv."
echo ""

