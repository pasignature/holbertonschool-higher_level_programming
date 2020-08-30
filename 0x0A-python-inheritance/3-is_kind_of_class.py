#!/usr/bin/python3
"""Same Class or Inherit From"""


def is_kind_of_class(obj, a_class):
    """Checks to see if an object is an instance of another class

    Args:
        obj - the object to be checked

        a_class - class to compare against

    Return:
        bool - True if obj is an instance of a_class. False otherwise
    """

    return isinstance(obj, a_class)
