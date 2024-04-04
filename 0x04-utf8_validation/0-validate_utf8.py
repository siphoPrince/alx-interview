#!/usr/bin/python3
"""represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Step through the data list"""
    i = 0
    while i < len(data):
        """Get the number of bytes for the current character"""
        num_bytes = 0
        if (data[i] & 0b10000000) == 0:
            num_bytes = 1
        elif (data[i] & 0b11100000) == 0b11000000:
            num_bytes = 2
        elif (data[i] & 0b11110000) == 0b11100000:
            num_bytes = 3
        elif (data[i] & 0b11111000) == 0b11110000:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if (data[i+j] & 0b11000000) != 0b10000000:
                return False

        i += num_bytes

    return True
