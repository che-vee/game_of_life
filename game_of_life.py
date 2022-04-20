import numpy as np


class Playground:
    def __init__(self, grid):
        self.grid = grid

    def step(self):
        updated_grid = self.grid.copy()
        height, width = self.grid.shape

        for row_index in range(height):
            for col_index in range(width):
                updated_grid[row_index, col_index] = self.step_one_cell(
                    row_index, col_index
                )

        self.grid = updated_grid

    def step_one_cell(self, row, col):
        neighbour_count = (
            np.sum(self.grid[row - 1 : row + 2, col - 1 : col + 2])
            - self.grid[row, col]
        )

        if neighbour_count <= 1:
            return 0
        elif neighbour_count <= 3 and self.grid[row, col] == 1:
            return 1
        elif neighbour_count == 3 and self.grid[row, col] == 0:
            return 1
        else:
            return 0


if __name__ == "__main__":

    playground = Playground(
        np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    for step in range(10):
        print(playground.grid, end="\n-------------\n")
        playground.step()

    print(playground.grid, end="\n-------------\n")
