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

    ops_2 = 2
    ops_1 = 1
    ops_d = ops_1 / 2
    ops = [0] * (n + 1)

    for i in range(ops_2, n + 1):
        ops[i] = i
        for _ in range(ops_1, int(i**ops_d) + ops_1):
            if i % _ == 0:
                ops[i] = min(ops[i], ops[_] + i // _)

    return ops[n]
