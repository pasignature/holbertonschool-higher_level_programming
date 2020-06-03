#!/usr/bin/python3
"""Only Sub Class Of Task Module"""


def inherits_from(obj, a_class):
    """Checks if obj is inherits from a_class

    Args:
        obj - object to be checked

        a_class - class to compare against

    Return:
        bool - True if obj is an instance of a_class, False otherwise
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
