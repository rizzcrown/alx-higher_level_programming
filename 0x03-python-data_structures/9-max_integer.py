#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    max = my_list[0]

    if length == 0:
        return None

    for i in range(length):
        if my_list[i] > max:
            max = my_list[i]
            return max
