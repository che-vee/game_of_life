import numpy as np

grid = np.array([
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0]
      ])

updated_grid = np.copy(grid)

def update_status(updated_grid):
    height = len(grid)
    width = len(grid[0])

    for row_index in range(0, width):
        for cell_index in range(0, height):
            updated_grid[row_index][cell_index] = make_step(row_index, cell_index, grid)

    return updated_grid


def make_step(row, cell, grid):
    neighbour_count = np.sum(grid[row - 1:row + 2, cell - 1:cell + 2]) - grid[row, cell]

 
    if neighbour_count <= 1:
        return 0
    elif neighbour_count <= 3 and grid[row][cell] == 1:
        return 1
    elif neighbour_count == 3 and grid[row][cell] == 0:
        return 1
    else:
        return 0
    
    
print(grid)   
print(update_status(updated_grid))



