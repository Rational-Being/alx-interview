#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    get the least # operations needed
    """
    if n < 0:
        return 0

    else:
        ops = 0
        while n > 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1
                ops += 1
        return ops

