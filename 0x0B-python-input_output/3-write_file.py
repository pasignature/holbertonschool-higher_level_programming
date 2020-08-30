#!/usr/bin/python3
"""Write To A File Module"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns num chars written"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
