#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    biggest_integer = my_list[0]
    for integer in range(len(my_list)):
        if my_list[integer] > biggest_integer:
            biggest_integer = my_list[integer]

    return (biggest_integer)
