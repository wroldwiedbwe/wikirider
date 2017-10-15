from __future__ import print_function,absolute_import
import colorama as clr
import requests as req
import re
import sys
from bs4 import BeautifulSoup as bs
from random import choice as rchoice
######## INIT COLORAMA #######
clr.init()
##############################
########### GLOBALS ##########
WIKIREGEX = re.compile(r"https://.*\.wikipedia\.org/wiki/.[^:#]{3,}$")
WIKIPAGEREGEX = re.compile(r"^/wiki/.[^:#]{1,}$")
HREFREGEX = re.compile(r"^/wiki/.*")
BASE_URL = "" # yet...
DONE = list() # yet... will be used later
HTML = None # yet...
##############################
########### PRINT BANNER ##########
def printBanner():
	print(clr.Style.BRIGHT + clr.Fore.WHITE)
	print("        (_\\")
	print("       / \\")
	print("  `== / /\\=,_")
	print("   ;--==\\\\  \\\\o")
	print("   /____//__/__\\")
	print(" @=`(0)     (0) ")
	print("\t-WikiRider" + clr.Style.RESET_ALL)
########### PRINT HELP ############
def printHelp():
	print(clr.Style.BRIGHT + clr.Fore.WHITE + "Usage: " + clr.Fore.YELLOW + "./wikirun.py <starting url> <depth (default: 5)>" + clr.Style.RESET_ALL)
########### VALIDATOR ##########
def validUrl(url):
	if "Main_Page" in url:
		return False
	return WIKIREGEX.match(url) != None or WIKIPAGEREGEX.match(url) != None
def run(url,depth,i):
	global BASE_URL
	global DONE
	if i > depth:
		print(clr.Style.BRIGHT + "You rode the wiki!" + clr.Style.RESET_ALL)
	else:
		DONE.append(url)
		POSSIBLE_URLS = list()
		HTML = bs(req.get(url).content,'lxml')
		PAGE_TITLE = HTML.find('h1',id="firstHeading").text
		print(clr.Style.BRIGHT + clr.Fore.YELLOW + ("-" * (i + 1)) + PAGE_TITLE + " - " + clr.Fore.GREEN + url  + clr.Style.RESET_ALL)
		for a in HTML.find_all('a',href=HREFREGEX):
			if a.text and validUrl(a['href']) and a['href'] not in url:
				POSSIBLE_URLS.append(a['href'])
		SEC_URL = rchoice(POSSIBLE_URLS)
		while SEC_URL == url:
			SEC_URL = rchoice(POSSIBLE_URLS)
		URL = BASE_URL + SEC_URL
		if POSSIBLE_URLS == list():
			run("",depth,depth)
		else:
			run(URL,depth,i+1)
		
########### MAIN #############
def runTheWiki(args):
	global BASE_URL
	if len(args) != 3:
		printHelp()
	else:
		START_URL = args[1]
		if validUrl(START_URL):
			BASE_URL = START_URL.split('/wiki')[0]
			try:
				DEPTH = int(args[2])
			except ValueError:
				print(clr.Style.BRIGHT + clr.Fore.RED + "\nPlease specify depth as a number..." + clr.Style.RESET_ALL)
				sys.exit(-1)
			print(clr.Style.BRIGHT + "\nStarting the track!" + clr.Style.RESET_ALL)
			run(START_URL,DEPTH,0)
		else:
			print(clr.Style.BRIGHT + clr.Fore.RED + "\nNot a valid Wiki URL! (must start with https://)" + clr.Style.RESET_ALL)
			
