#!/usr/bin/python3
"""  finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """  finds a peak in a list of unsorted integers. """
    ln = len(list_of_integers)
    if ln == 0:
        return
    m = ln // 2
    pivot = list_of_integers[m]
    left = list_of_integers[m - 1]

    if (m == ln - 1 or pivot >= list_of_integers[m + 1]) and\
            (m == 0 or pivot >= left):
        return pivot
    elif m != ln - 1 and list_of_integers[m + 1] > pivot:
        return (find_peak(list_of_integers[m + 1:]))
    return (find_peak(list_of_integers[:m]))
