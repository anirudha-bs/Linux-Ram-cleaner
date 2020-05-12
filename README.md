# Linux-Ram-cleaner

Every Linux System has three options to clear cache without interrupting any processes or services.
This app clear cache (pagecache, dentries and inodes) by writing 1,2,3 to drop_cache in proc/sys/vm/ directory
This will slow down the system for a moment until new pages are loaded into the Ram.

For further references - https://unix.stackexchange.com/questions/17936/setting-proc-sys-vm-drop-caches-to-clear-cache

Xterm and Htop needs are required for the app.

To install them follow the below procedure -

sudo apt-get install xtrem

sudo apt-get install htop

Download the package and then extract ram_cleaner.zip and run install.sh script to start using the app
