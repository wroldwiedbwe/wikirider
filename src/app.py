# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from sys import argv as args
from src.wikirider import WikiRider
from src.view import RidePrinter
import argparse


class TerminalApp:
    """Terminal application controller"""

    def __init__(self):
        self.printer = RidePrinter()
        self.args = TerminalApp.parse_arguments()

    def start(self):
        self.printer.print_banner()
        rider = WikiRider(self.args.url, self.args.depth)
        self.printer.print_start()
        for rider_state in rider.run():
            self.printer.print_rider_location(rider_state)
        self.printer.print_end()

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            description='Performs a wiki run on the provided url. The length of the run can be adjusted by providing a depth argument')
        parser.add_argument('url', metavar='url', type=str,
                            help='The wiki url that should be used')
        parser.add_argument('depth', metavar='depth',
                            type=int, default=5, help='The recursion depth')
        args = parser.parse_args()
        
        return args
