#!/usr/bin/python3


"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """intergers a and b"""

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    result = a + b
    return int(result)
