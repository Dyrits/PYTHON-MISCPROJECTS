#FUNCTIONS
def get_index_row(tracking_position):
    return tracking_position // 9


def get_row(grid, tracking_position):
    return grid[get_index_row(tracking_position)][0:9]


def get_index_column(tracking_position):
    return tracking_position % 9


def get_column(grid, tracking_position):
    return [row[get_index_column(tracking_position)] for row in grid]


def get_actual_value(grid, tracking_position):
    return grid[get_index_row(tracking_position)][get_index_column(tracking_position)]


def get_subgrid(grid, tracking_position):
    index_start_row = get_index_row(tracking_position) // 3 * 3
    index_start_column = get_index_column(tracking_position) // 3 * 3
    rows = [grid[index_start_row + row]
            [index_start_column:index_start_column+3] for row in range(0, 3)]
    return [cells for row in rows for cells in row]


# GRID
grid = [[0, 3, 2, 0, 0, 0, 5, 0, 0],
        [4, 0, 0, 2, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 4, 7, 0],
        [5, 2, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 5, 0, 0, 3, 9],
        [0, 9, 7, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 3, 0, 0, 5],
        [0, 0, 5, 0, 0, 0, 7, 9, 0]]


# MAIN FUNCTION
def main(grid):
    print(*grid, sep="\n")
    grid_copy = [row[:] for row in grid]
    tracking_position = 0
    tracking_way = 1
    while tracking_position < 81:

        actual_value_copy = get_actual_value(grid_copy, tracking_position)
        if actual_value_copy != 0:  # The cell is skipped is already filled by the user.
            tracking_position += tracking_way
            continue

        actual_index_row = get_index_row(tracking_position)
        actual_index_column = get_index_column(tracking_position)
        actual_value = get_actual_value(grid, tracking_position)

        # If the value is already equals to 9, it is set back to 0 and the loop is going back to the previous cell:
        if actual_value == 9:
            grid[actual_index_row][actual_index_column] = 0
            tracking_way = -1
            tracking_position += tracking_way
            continue

        actual_row = get_row(grid, tracking_position)
        actual_column = get_column(grid, tracking_position)
        actual_subgrid = get_subgrid(grid, tracking_position)

        for test_value in range(actual_value, 10):
            # If the value is already in the row, column or subgrid, the next value is tested:
            if test_value in actual_subgrid or test_value in actual_row or test_value in actual_column:
                # If the value is already equals to 9, it is set back to 0 and the loop is going back to the previous cell:
                if test_value == 9:
                    grid[actual_index_row][actual_index_column] = 0
                    tracking_way = -1
                    tracking_position += tracking_way
                continue
            # If the value is not found in the row, column or subgrid, the value is added to the grid, and the loop is going to the next cell.
            else:
                grid[actual_index_row][actual_index_column] = test_value
                tracking_way = 1
                tracking_position += tracking_way
                break

    print("The sudoku is solved!")
    print("Solution:")
    print(*grid, sep="\n")


if __name__ == "__main__":
    main(grid)
