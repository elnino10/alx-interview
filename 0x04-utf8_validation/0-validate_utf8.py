#!/usr/bin/python3
""" 0-validate_utf8 module """


def validUTF8(data):
    """
    utf-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """
    a = 1 << 7
    b = 1 << 6
    count = 0
    for code_point in data:
        elon = 1 << 7
        if count == 0:
            while elon & code_point:
                count += 1
                elon = elon >> 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (code_point & a and not code_point & b):
                return False
        count -= 1
    return not count
