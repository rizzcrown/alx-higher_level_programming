#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    new_tuple = ()

    if len1 < 2 or len2 < 2:
        tuple_a[1] = 0 or tuple_b[1] = 0
    elif len1 > 2 or len2 > 2:
        new_tuple[0] = tuple_a[0] + tuple_b[0]
        new_tuple[1] = tuple_a[1] + tuple_b[1]
    else:
        new_tuple[0] = tuple_a[0] + tuple_b[0]
        new_tuple[0] = tuple_a[1] +tuple_b[1]

    return new_tuple
