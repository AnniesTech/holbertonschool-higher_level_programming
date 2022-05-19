#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list_of_integers
    le = len(li)
    if le == 0:
        return
    m = le // 2
    if (m == le - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != le - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
