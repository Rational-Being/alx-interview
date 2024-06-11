#!/usr/bin/python3
"""
this code hleps me get ready of interview
"""


def island_perimeter(grid):
    """
    funtion returns the perimeter of the island
    as described in 0-main.py
    """

    perimeter = 0
    row = len(grid)
    columns = len(grid[0])

    for i in range(row):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4

                if j < columns - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

                if i < row - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2
    return perimeter
