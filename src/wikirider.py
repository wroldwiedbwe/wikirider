# -*- coding: utf-8 -*-
from __future__ import print_function,absolute_import
from colorama import Fore,Back,Style
import requests as req
import re
import sys
from bs4 import BeautifulSoup as bs
from random import choice as rchoice

class WikiRider(object):
	############################# VARIABLES #############################
	WikiRegex = re.compile(r"https://.*\.wikipedia\.org/wiki/.[^:#]{3,}$")
	WikiPageRegex = re.compile(r"^/wiki/.[^:#]{1,}$")
	hrefRegex = re.compile(r"^/wiki/.*")
	BaseURL = ""
	NextUrl = ""
	VisitedUrls = list()
	ColorMap = {5:Fore.MAGENTA,4:Fore.CYAN,3:Fore.BLUE,2:Fore.GREEN,1:Fore.YELLOW,0:Fore.RED}
	currColorNum = 0;
	Depth = 0
	DepthCounter = 0
	########### CONSTRUCTOR ###########
	def __init__(self,BaseUrl,Depth):
		if WikiRider.validInt(Depth) and WikiRider.validUrl(BaseUrl):
			self.Depth = int(Depth)
			self.NextUrl = BaseUrl
			self.BaseURL = BaseUrl.split('/wiki/')[0]
			print("\n" + Style.BRIGHT + Back.WHITE + Fore.BLACK + "Starting the track!" + Style.RESET_ALL)
			self.run()
		else:
			WikiRider.printError()
	def run(self):
		if self.DepthCounter >= self.Depth:
			print(Style.BRIGHT + Back.WHITE + Fore.BLACK + "You rode the wiki!" + Style.RESET_ALL)
			return
		else:
			self.VisitedUrls.append(self.NextUrl)
			possibleUrls = list()
			try:
				HtmlSource = bs(req.get(self.NextUrl).content,'lxml')
			except:
				print(Style.BRIGHT + Fore.RED + 'Cannot connect to WikiPedia.' + Style.RESET_ALL)
				return			
			PageTitle = HtmlSource.find('h1',id="firstHeading").text
			nextColor = self.ColorMap[self.currColorNum]
			dashCounter = self.DepthCounter + 1 if self.DepthCounter + 1 < 25 else 25
			self.currColorNum = self.currColorNum + 1 if self.currColorNum < len(self.ColorMap) - 1 else 0
			print((Style.BRIGHT + Fore.WHITE + ("-" * (dashCounter)) + PageTitle + " - " + nextColor + self.NextUrl + Style.RESET_ALL))
			for a in HtmlSource.find_all('a',href=self.hrefRegex):
				if a.text and WikiRider.validUrl(a['href']) and a['href'] not in self.NextUrl:
					for VisitedUrl in self.VisitedUrls:
						if a['href'] not in VisitedUrl: #or self.VisitedUrls == list(): ..not needed
							possibleUrls.append(a['href'])
			if possibleUrls == list():
				self.DepthCounter = self.Depth
				self.run()
			else:
				nextURLTail = rchoice(possibleUrls)
				while nextURLTail in self.NextUrl:
					nextURLTail = rchoice(possibleUrls)
				self.DepthCounter+=1
				self.NextUrl = self.BaseURL + nextURLTail
				self.run()
			#except:
			#	self.DepthCounter = self.Depth
			#	self.run()
	######## CHECK IF VALID INT ########
	@staticmethod
	def validInt(num):
		try:
			int(num)
		except:
			return False
		finally:
			return True
	########### PRINT BANNER ###########
	@staticmethod
	def printBanner():
		print(Style.BRIGHT + Fore.WHITE)
		print("        (_\\")
		print("       / \\")
		print("  `== / /\\=,_")
		print("   ;--==\\\\  \\\\o")
		print("   /____//__/__\\")
		print(" @=`(0)     (0) ")
		print("\t-WikiRider" + Style.RESET_ALL)
	########### PRINT HELP ############
	@staticmethod
	def printHelp():
		print(Style.BRIGHT + Fore.WHITE + "\nUsage: " + Fore.YELLOW + "./wikirun.py <starting url> <depth>" + Style.RESET_ALL)
	########### PRINT ERROR ###########
	@staticmethod
	def printError():
		print(Style.BRIGHT + Fore.RED + "\nDepth must be a number!\nStarting URL must be a valid WikiPedia URL!\n(You might me missing https:// and special pages aren't allowed)!" + Style.RESET_ALL)
	############ CHECK URL ############
	@staticmethod
	def validUrl(url):
		if "Main_Page" in url:
			return False
		return WikiRider.WikiRegex.match(url) != None or WikiRider.WikiPageRegex.match(url) != None
