#!/usr/bin/python3
"""My List Task Module"""


class MyList(list):
    """Custom List Type Class"""

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
