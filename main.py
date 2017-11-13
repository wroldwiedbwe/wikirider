#!/usr/bin/env python
from sys import argv as args
from colorama import init as color_init
from mod.wikirider import WikiRider
######### IMPORTS ########
color_init() # Initialize colors
WikiRider.printBanner() # Print the cool ASCII art

if __name__ == "__main__":
	if len(args) != 3:
		WikiRider.printHelp()
	else:
		rider = WikiRider(args[1],args[2])