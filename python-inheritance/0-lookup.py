#!/usr/bin/python3
"""returns a list of avaibles atribute and a list of an object"""


def lookup(obj):
    """
    returns a list of avaible atribute and a list of an object

    Args :
        obj: object


    Retruns :
        list
    """
    return dir(obj)
