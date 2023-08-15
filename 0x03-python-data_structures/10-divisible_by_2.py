#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiple of 2 in a list."""
    multiple = []
    for integer in range(len(my_list)):
        if my_list[integer] % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)

    return (multiple)
