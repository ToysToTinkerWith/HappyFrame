Setup Documentation for HappyFrames image retriever and slideshow.

Last Update: May 20, 2020

This tutorial assumes you have a Raspberry Pi straight out of the box, with no previous operating system installed.

Step 1: Install NOOBS

	- Format your SD card using any popular formatting application. This should erase all files curently stored on the card.
	it is recommended that you have an SD card with at least 8GB of space, but prefferably 16GB for other installs.
	- Download the full NOOBS package at https://www.raspberrypi.org/downloads/noobs/
	- Move all files extracted from the NOOBS download onto your SD card.
	- Put the SD into your Raspberry Pi and power it on. The Pi should prompt you to download the Debian/Raspian OS. This should take a bit of time to get everything installed, but after it's done it should take you to the Rasbian Desktop GUI.

Step 2: Installing the right packages

	- Open the terminal provided for the Rasbian OS.
	- Type the commands:
		pip3 install pymongo
		pip3 install pymongo[srv]
		sudo apt install feh -y
	hitting enter after each one and waiting for them to install.

Step 3: Running the PI program

	- Grab the ZIP file containing all the required files or download the git repository at https://gitlab.cs.wwu.edu/bergqua/happyframe.git
	- Open the python file called DBconnection.py
	- Near the top of the file are variables db, collection, and path.
	- db is essentially a cluster of collections in your database, change this to represent the facility that you want to pull from.
	- collection represents a specific frame/device within that facility.
	- path represents the path to your Pictures directory, this may or may not need to be changed depending on where your DBconnection.py file is located.

	- Open the terminal provided for the Rasbian OS.
	- Change your directory to the directory that contains DBconnection.py.
	- Type: "python3 DBconnection.py" in the command line and hit enter. This should pull the pictures stored under the specified collection onto your Pi, and begin displaying them in a slideshow fashion.

(Optional) Step 4: Setting up cron

- You may wish to automate the process of pulling images and running the slideshow. To do this open the terminal application.
- The Raspberry Pi foundation has provided a nice guide to automate when certain programs are run. Refer to more detailed instructions at https://www.raspberrypi.org/documentation/linux/usage/cron.md




