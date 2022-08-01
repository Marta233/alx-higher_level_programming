#!/usr/bin/python3
# Marta A
"""Defin inherited class MYList."""


class MyList(list):
    """Implient sorted list for built-in class List."""
    def print_sorted(self):
        """print list in ascending order."""
        print(sorted(self))
