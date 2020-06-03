#!/usr/bin/python3
"""Lookup Task Module"""


def lookup(obj):
    """Lookup
    Returns the list of available attributes and methods of an obj

    Args:
        obj: object

    Return:
        list: contains the available attributes and methods of the obj
    """
    return dir(obj)
