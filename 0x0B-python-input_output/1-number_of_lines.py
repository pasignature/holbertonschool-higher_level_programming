#!/usr/bin/python3
"""Number Of Line Module"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""

    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for line in f)
