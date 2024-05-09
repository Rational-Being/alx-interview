#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    get the least # operations needed
    """
    if n <= 1:
        return 0

    return 3 + minOperations(n - 2)
