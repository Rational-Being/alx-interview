#!/usr/bin/python3
"""
gicen a oiule of coins of different values, determine the fewest numnber of
coins needed to meat a given amouint of total
"""


def makeChange(coins, total):
    """
    and of course, change come from within
    """

    if total <= 0:
        return 0

    change = 0
    amount = 0
    coins.sort(reverse=True)

    for coin in coins:
        while change + coin <= total:

            change += coin
            amount += 1

            if change == total:
                return amount
    return -1
