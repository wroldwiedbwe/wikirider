# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from colorama import Fore, Back, Style
import colorama
import requests as req
import re
from bs4 import BeautifulSoup as Bs
from random import choice as rchoice


class WikiRider(object):

    # CONSTANTS

    WIKI_REGEX = re.compile(r"https://.*\.wikipedia\.org/wiki/.[^:#]{3,}$")
    WIKI_PAGE_REGEX = re.compile(r"^/wiki/.[^:#]+$")
    HREF_REGEX = re.compile(r"^/wiki/.*")

    # CONSTRUCTOR

    def __init__(self, base_url, depth):
        self.depth = depth
        self.depth_counter = 0
        self.next_url = base_url
        self.base_url = base_url.split('/wiki/')[0]
        self.visited_urls = []
        self.possible_urls = []
        self.html_source = None

    def run(self):
        if self.depth_counter < self.depth:
            self.visited_urls.append(self.next_url)
            self.scrape_html_source()
            yield self
            self.search_urls()
            self.set_destination()
            for rider_state in self.run():
                yield self

    def scrape_html_source(self):
        # Scrapes html soup
        try:
            self.html_source = Bs(req.get(self.next_url).content, 'lxml')
        except req.RequestException:
            self.printer.print_connection_error()
            return None

    def search_urls(self):
        # Looks for possible urls
        self.possible_urls = []
        for a in self.html_source.find_all('a', href=self.HREF_REGEX):
            if (a.text and WikiRider.valid_url(a['href']) and a['href']
                    not in self.next_url):
                for visited_url in self.visited_urls:
                    if a['href'] not in visited_url:
                        self.possible_urls.append(a['href'])

    def set_destination(self):
        # Sets the next url to travel
        if not self.possible_urls:
            self.depth_counter = self.depth
        else:
            next_url_tail = rchoice(self.possible_urls)
            while next_url_tail in self.next_url:
                next_url_tail = rchoice(self.possible_urls)
            self.depth_counter += 1
            self.next_url = self.base_url + next_url_tail

    @staticmethod
    def valid_url(url):
        if "Main_Page" in url:
            return False
        return (WikiRider.WIKI_REGEX.match(url) is not None or
                WikiRider.WIKI_PAGE_REGEX.match(url) is not None)


class RidePrinter:

    COLOR_MAP = {
        5: Fore.MAGENTA,
        4: Fore.CYAN,
        3: Fore.BLUE,
        2: Fore.GREEN,
        1: Fore.YELLOW,
        0: Fore.RED
    }

    def __init__(self):
        colorama.init()
        self.curr_color_num = 0

    def print_rider_location(self, rider):
        # Prints current page
        page_title = rider.html_source.find('h1', id="firstHeading").text
        next_color = self.COLOR_MAP[self.curr_color_num]
        dash_counter = rider.depth_counter + 1 \
            if rider.depth_counter + 1 < 25 else 25
        self.curr_color_num = self.curr_color_num + 1 \
            if self.curr_color_num < len(self.COLOR_MAP) - 1 else 0
        print(Style.BRIGHT + Fore.WHITE + ("-" * dash_counter)
              + page_title + " - " + next_color + rider.next_url
              + Style.RESET_ALL)

    def print_end(self):
        print(Style.BRIGHT + Back.WHITE + Fore.BLACK +
              "You rode the wiki!" + Style.RESET_ALL)

    def print_start(self):
        print("\n" + Style.BRIGHT + Back.WHITE + Fore.BLACK +
              "Starting the track!" + Style.RESET_ALL)

    def print_banner(self):
        print(Style.BRIGHT + Fore.WHITE)
        print("        (_\\")
        print("       / \\")
        print("  `== / /\\=,_")
        print("   ;--==\\\\  \\\\o")
        print("   /____//__/__\\")
        print(" @=`(0)     (0) ")
        print("\t-WikiRider" + Style.RESET_ALL)

    def print_help(self):
        print(Style.BRIGHT + Fore.WHITE + "\nUsage: " + Fore.YELLOW +
              "./wikirun.py <starting url> <depth>" + Style.RESET_ALL)

    def print_invalid_input_error(self):
        print(Style.BRIGHT + Fore.RED +
              "\nDepth must be a number!\nStarting URL must be a valid "
              "WikiPedia URL!\n(You might me missing https:// and special "
              "pages aren't allowed)!" + Style.RESET_ALL)

    def print_connection_error(self):
        print(Style.BRIGHT + Fore.RED +
              'Cannot connect to WikiPedia.' + Style.RESET_ALL)
