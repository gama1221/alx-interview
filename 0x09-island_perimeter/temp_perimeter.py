#!/usr/bin/python3
""" island perimeter """


def island_perimeter(grid):
    """ main function for task """
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                total += check((row, col), grid)
    return total


def check(index, grid):
    """ check perimeter num """
    perimeter = 4
    try:
        if grid[index[0]][index[1] - 1] == 1 or grid[index[0]][index[1] + 1] == 1:
            if grid[index[0]][index[1] + 1] == 1 and grid[index[0]][index[1] - 1] == 1:
                perimeter -= 2
            else:
                perimeter -= 1
        if grid[index[0] + 1][index[1]] == 1 or grid[index[0] - 1][index[1]] == 1:
            if grid[index[0] + 1][index[1]] == 1 and grid[index[0] - 1][index[1]] == 1:
                perimeter -= 2
            else:
                perimeter -= 1
    except:
       perimeter -= 1
    return perimeter
