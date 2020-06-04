#!/usr/bin/python3
"""Append To File"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8) and returns
    number of char appended"""

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
