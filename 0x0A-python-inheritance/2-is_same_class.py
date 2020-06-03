#!/usr/bin/python3
"""Exact Same Object Task Module"""


def is_same_class(obj, a_class):
    """Checks if obj is a type of a_class

    Args:
        obj - object to be checked

        a_class - the type to compare to

    Return
        bool - True if obj is a type of a_class, False otherwise
    """

    return type(obj) is a_class
