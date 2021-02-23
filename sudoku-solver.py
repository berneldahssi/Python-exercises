# import random

grid = [
    [0, 0, 6, 1, 0, 2, 5, 0, 0],
    [0, 3, 9, 0, 0, 0, 1, 4, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [9, 0, 2, 0, 3, 0, 4, 0, 1],
    [0, 8, 0, 0, 0, 0, 0, 7, 0],
    [1, 0, 3, 0, 6, 0, 8, 0, 9],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 5, 4, 0, 0, 0, 9, 1, 0],
    [0, 0, 7, 5, 0, 3, 2, 0, 0]
]


# rewrite the print statement by using its end and start arguments and an additive for loop
def print_grid():
    global grid
    print('\n+-------+-------+-------+')
    for i in range(9):
        print('| {} {} {} | {} {} {} | {} {} {} |'.format(grid[i][0], grid[i][1], grid[i][2], grid[i][3], grid[i][4], grid[i][5], grid[i][6], grid[i][7], grid[i][8]))
        if i % 3 == 2:
            print('+-------+-------+-------+')


def possible(i, j, n):
    global grid
    for x in range(9):
        if grid[i][x] == n:
            return False
    for y in range(9):
        if grid[y][j] == n:
            return False
    x = (i//3)*3
    y = (j//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == n:
                return False
    return True


def find_zero():
    global grid
    blank_cells = list()
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                blank_cells.append((i, j))
    return blank_cells


def solve():
    global grid
    blank_cells = find_zero()
    if not blank_cells:
        return grid
    for i, j in blank_cells:
        for n in range(1, 10):
            if possible(i, j, n):
                grid[i][j] = n
                print_grid()
                solution = solve()
                if solution is not None:
                    return solution
                grid[i][j] = 0
        return None


print_grid()
if input():
    solve()
    print("I'm done! ^^")



# Snippet : generator of a 9 shuffled-list

# grid = [7, 3, 1, 9, 4, 2, 5, 6, 8]
# for i in range(9):
#     random.shuffle(grid)
#     print(grid)
