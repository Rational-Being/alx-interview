#!/usr/bin/python3
"""
python script that prints the pascal's trinagle
"""

def pascal_triangle(n):
    """
    ccreates a pascal triangle
    """
    
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(len(result[i-1]) - 1):
                row.append(result[i-1][j] + result[i-1][j+1])
            row.append(1)
            result.append(row)

        return result