#!/usr/bin/env python
from sys import argv as args
from src.wikirider import WikiRider, RidePrinter
# IMPORTS

if __name__ == "__main__":
    printer = RidePrinter()
    printer.print_banner()
    if len(args) != 3:
        printer.print_help()
    else:
        rider = WikiRider(args[1], args[2])
