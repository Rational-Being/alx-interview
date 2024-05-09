def minOperations(n):

    if n <= 1:
        return 0

    return 3 + minOperations(n-2)