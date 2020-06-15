#!/bin/sh

echo "Updating System"
sudo apt-get update
#sudo apt-get upgrade

echo "Install Dependencies"
sudo apt-get install python3-all-dev
sudo apt-get install python3-pip
pip3 install black


echo "Moving Files"
cp Context.sublime-menu $HOME/.config/sublime-text-3/Packages/User/
cp Adorn.py $HOME/.config/sublime-text-3/Packages/User/


echo "Finished Installing"
