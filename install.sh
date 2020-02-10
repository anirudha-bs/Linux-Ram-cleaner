#!/bin/sh

if [ `whoami` != 'root' ]
then
echo "This script must be run as root."
exit 1;
fi
echo "Installing Ram cleaner...."
pwd=$(pwd)
sudo mv $pwd/dist/ram_cleaner /usr/local/bin && sudo mv $pwd/ram_cleaner.desktop /usr/share/applications && sudo mv py.png /usr/share/pixmaps
if [ $? -eq 0 ]
then
echo "Moved files"
echo "Installation complete."
else
echo "Error moving files to bin or permissions denied"
fi

