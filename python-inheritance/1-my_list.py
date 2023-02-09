#!/usr/bin/python3
"""Module for inherits"""

class MyList(list):
     """Representation of list"""
     def print_sorted(self):
        """Print the list by ascending sort"""
        print(sorted(self))
