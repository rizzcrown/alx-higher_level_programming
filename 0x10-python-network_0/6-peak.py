#!/usr/bin/python3

def find_peak(list_of_integer):
    peak = None

    for num in list_of_integer:
        if peak is None or num > peak:
            peak = num

    return peak
