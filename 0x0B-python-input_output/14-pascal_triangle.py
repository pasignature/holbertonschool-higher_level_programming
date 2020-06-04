#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """Returns a list of list of integers repr Pascal's Triangle of n"""

    ans = []
    if n > 0:
        ans.append([1])
        for r in range(1, n):
            prv = ans[-1]
            ans.append([1] + [prv[i - 1] + prv[i] for i in range(1, r)] + [1])
    return ans
