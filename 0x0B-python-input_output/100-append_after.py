#!/usr/bin/python3
"""Search And Update Module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after each line"""

    lst = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lst.append(line)
    with open(filename, "w", encoding="utf-8") as f:
        for line in lst:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
