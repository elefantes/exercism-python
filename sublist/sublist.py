"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.


SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(a: list, b: list) -> int:
    if len(a) == len(b) and a == b:
        result = EQUAL
        return result
    elif len(a) == len(b) and a != b:
        result = UNEQUAL
        return result
    elif len(a) > len(b):
        result = SUPERLIST
        larger = a
        smaller = b
    elif len(a) < len(b):
        result = SUBLIST
        larger = b
        smaller = a
    else:
        raise Exception("Not possible!")

    if len(a) == 0 or len(b) == 0:
        return result

    for idx, item in enumerate(larger):
        if smaller[0] == item and len(larger[idx::]) >= len(smaller):
            start, stop = idx, idx + len(smaller)
            compare_to = larger[start:stop]
            if smaller == compare_to:
                return result

    result = UNEQUAL
    return result
