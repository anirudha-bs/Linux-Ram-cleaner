#!/bin/sh

if [ `whoami` != 'root' ]
then
echo "This script must be run as root."
exit 1;
fi
echo "Uninstalling Ram cleaner...."
sudo rm /usr/local/bin/ram_cleaner && sudo rm /usr/share/applications/ram_cleaner.desktop && sudo rm /usr/share/pixmaps/py.png
if [ $? -eq 0 ]
then
echo "Uninstall complete."
else
echo "Error deleting files, no files found or permissions denied"
fi

