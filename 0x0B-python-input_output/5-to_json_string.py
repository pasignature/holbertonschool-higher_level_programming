#!/usr/bin/python3
from json import dumps

"""To JSON String"""


def to_json_string(my_obj):
    """Returns the JSON repr of an onject"""

    return dumps(my_obj)
