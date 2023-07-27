#!/usr/bin/python3
""" This is a bad way to get island perimeter """


def island_perimeter(grid):
    """ Islands perimeter and i am ashamed"""
    sum = 0
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == 1 and (i < (len(grid) - 1) and i > 0):
                fb_ver2 = (grid[i + 1][x] != 1 or grid[i - 1][x] != 1)
                fb_ver_n = (grid[i + 1][x] != 1 and grid[i - 1][x] != 1)
                fb_ver = (grid[i + 1][x] == 1 and grid[i - 1][x] == 1)
                sum += total(grid, i, x, fb_ver, fb_ver2, fb_ver_n)
            elif grid[i][x] == 1 and (i == (len(grid) - 1)):
                fb_ver2 = (grid[i - 1][x] != 1 or True)
                fb_ver_n = (grid[i - 1][x] != 1 and True)
                fb_ver = (grid[i - 1][x] == 1 and False)
                sum += total(grid, i, x, fb_ver, fb_ver2, fb_ver_n)
            elif grid[i][x] == 1 and (i == 0):
                fb_ver2 = (True or grid[i + 1][x] != 1)
                fb_ver_n = (True and grid[i + 1][x] != 1)
                fb_ver = (False and grid[i + 1][x] == 1)
                sum += total(grid, i, x, fb_ver, fb_ver2, fb_ver_n)
    return sum


def total(grid, i, x, fb_ver, fb_ver2, fb_ver_n):
    """ get total perimeter now """
    sum = 0
    if x == 0 and grid[i][x] == 1:
        if fb_ver2 and (not fb_ver_n) and grid[i][x + 1] != 1:
            sum += 3
        elif fb_ver_n and grid[i][x + 1] != 1:
            sum += 4
        elif fb_ver_n and grid[i][x + 1] == 1:
            sum += 3
        elif fb_ver2 and (not fb_ver_n) and grid[i][x + 1] == 1:
            sum += 2
        elif fb_ver and grid[i][x + 1] != 1:
            sum += 2
        elif fb_ver and grid[i][x + 1] == 1:
            sum += 1
    elif (x != len(grid[i]) - 1) and grid[i][x] == 1:
        fb_hor = (grid[i][x + 1] == 1 and grid[i][x - 1] == 1)
        fb_hor_n = (grid[i][x + 1] != 1 and grid[i][x - 1] != 1)
        fb_hor2 = (grid[i][x + 1] != 1 or grid[i][x - 1] != 1)
        if (fb_hor2 and (not fb_hor_n)) and (fb_ver2 and (not fb_ver_n)):
            sum += 2
        elif (fb_hor2 and (not fb_hor_n)) and fb_ver_n:
            sum += 3
        elif (fb_hor2 and (not fb_hor_n)) and fb_ver:
            sum += 1
        elif fb_hor and fb_ver_n:
            sum += 2
        elif fb_hor and (fb_ver2 and (not fb_ver_n)):
            sum += 1
        elif fb_hor_n and fb_ver_n:
            sum += 4
        elif fb_hor_n and fb_ver:
            sum += 2
        elif fb_hor_n and (fb_ver2 and (not fb_ver_n)):
            sum += 3
    elif grid[i][x] == 1:
        if fb_ver2 and (not fb_ver_n) and grid[i][x - 1] != 1:
            sum += 3
        elif fb_ver2 and (not fb_ver_n) and grid[i][x - 1] == 1:
            sum += 2
        elif fb_ver_n and grid[i][x - 1] != 1:
            sum += 4
        elif fb_ver_n and grid[i][x - 1] == 1:
            sum += 3
        elif fb_ver and grid[i][x - 1] != 1:
            sum += 2
        elif fb_ver and grid[i][x - 1] == 1:
            sum += 1
    return sum
