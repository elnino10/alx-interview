#!/usr/bin/python3
"""Island Perimeter"""


def check_val(n):
    """
    checks the value of the argument passed

    Args:
        n (integer): integer value to check

    Returns:
        integer: 1 if n is 0 and 0 otherwise
    """
    if (n == 0):
        return 1
    return 0


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid

    Args:
        grid (list): list of list of integers
    """

    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i][j-1])

                try:
                    x += check_val(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_val(grid[i][j+1])
                except IndexError:
                    x += 1

    return x
