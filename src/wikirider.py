# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
import re
from random import choice as rchoice
import requests as req
from bs4 import BeautifulSoup as Bs


class WikiRider(object):
    """Wikiruns maker"""

    WIKI_REGEX = re.compile(r"https://.*\.wikipedia\.org/wiki/.[^:#]{3,}$")
    WIKI_PAGE_REGEX = re.compile(r"^/wiki/.[^:#]+$")
    HREF_REGEX = re.compile(r"^/wiki/.*")

    def __init__(self, starting_url, depth):
        """WikiRider constructor

        Parameters
        ----------
        starting_url : str
            Url to any wikipedia web article, starting point for the wikirun
        depth : int
            Quantity of webpages to visit
        """
        self.depth = depth
        self.depth_counter = 0
        self.next_url = starting_url
        self.base_url = starting_url.split('/wiki/')[0]
        self.visited_urls = []
        self.possible_urls = []
        self.html_source = None

    def run(self):
        """Do a run across wikipedia articles

        Yields
        ------
        WikiRider
            Yield this instance for each time it visits a new webpage
        """
        if self.depth_counter < self.depth:
            self.visited_urls.append(self.next_url)
            self._scrape_html_source()
            yield self
            self._search_urls()
            self._set_destination()
            for rider_state in self.run():
                yield self

    def _scrape_html_source(self):
        """Scrape html soup from next url"""
        try:
            self.html_source = Bs(req.get(self.next_url).content, 'lxml')
        except req.RequestException:
            self.printer.print_connection_error()
            return None

    def _search_urls(self):
        """Look for possible urls"""
        self.possible_urls = []
        for a in self.html_source.find_all('a', href=self.HREF_REGEX):
            if (a.text and WikiRider.valid_url(a['href']) and a['href']
                    not in self.next_url):
                for visited_url in self.visited_urls:
                    if a['href'] not in visited_url:
                        self.possible_urls.append(a['href'])

    def _set_destination(self):
        """Randomly choose next url to travel"""
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


