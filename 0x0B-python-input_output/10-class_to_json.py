#!/usr/bin/python3
"""Class To JSON Module"""


def class_to_json(obj):
    """Returns a dict description"""
    return obj.__dict__
