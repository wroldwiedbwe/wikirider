# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from sys import argv as args
from src.wikirider import WikiRider
from src.view import RidePrinter


class TerminalApp:
    """Terminal application controller"""

    def __init__(self):
        self.printer = RidePrinter()
        self.args = args

    def start(self):
        self.printer.print_banner()
        if self._should_start():
            rider = WikiRider(self.args[1], int(self.args[2]))
            self.printer.print_start()
            for rider_state in rider.run():
                self.printer.print_rider_location(rider_state)
            self.printer.print_end()

    def _should_start(self):
        if len(self.args) != 3:
            self.printer.print_help()
            return False
        elif not WikiRider.valid_url(self.args[1]) or not valid_int(self.args[2]):
            self.printer.print_invalid_input_error()
            return False
        else:
            return True


def valid_int(num):
    try:
        int(num)
    except ValueError:
        return False
    else:
        return True
