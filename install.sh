#!/bin/sh

echo "Updating System"
sudo apt-get update
sudo apt-get upgrade

echo "Install Dependencies"
sudo apt-get install python3-all-dev
sudo apt-get install python3-pip
sudo pip3 install black

echo "Making Directories"
sudo mkdir ~/.local/share/
sudo mkdir ~/.local/share/gedit/
sudo mkdir ~/.local/share/gedit/plugins/
sudo mkdir ~/.local/share/gedit/plugins/adorn/



echo "Moving Files"
sudo cp gedit/adorn.plugin ~/.local/share/gedit/plugins/

echo "Moving Python Files"
sudo cp gedit/adorn/__init__.py ~/.local/share/gedit/plugins/adorn/


echo "Finished Installing"
