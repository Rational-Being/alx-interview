#!/usr/bin/python3

"""

"""

def isWinner(x, nums):
    """

    """
    if x <= 0 or not nums or x != len(nums):
        return None
    
    maria = 0
    ben = 0

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    

    count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        count[i] = count[i - 1] + (1 if is_prime[i] else 0)


    for n in nums:
        if count[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
