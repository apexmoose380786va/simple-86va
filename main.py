""" Simple 2D grid game prototype. """

WIDTH = 5
HEIGHT = 5

def create_grid():
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    grid[HEIGHT-1][WIDTH-1] = 'G'
    return grid

def display(grid, px, py):
    for y in range(HEIGHT):
        row = ''
        for x in range(WIDTH):
            if y == py and x == px:
                row += 'P'
            else:
                row += grid[y][x]
        print(row)
    print("Use w/a/s/d to move, q to quit.")

def move(key, px, py):
    if key == 'w' and py > 0: py -= 1