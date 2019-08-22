# Part 4: Graphs (Exercise 5)
# Note: Exercise 4 is in Part3.py because it was a part of the class definition


# Exercise 5: Number of islands
def nb_of_islands(island_map):
    """ Returns the number of 'islands' when given a 2d grid map of 1's (land) and 0's (water) """
    island_count = 0
    max_row = len(island_map) - 1
    max_col = len(island_map[max_row]) - 1
    for row in range(len(island_map)):
        for col in range(len(island_map[row])):
            if island_map[row][col] == 1:
                island_map = remove_island(island_map, row, col, max_row, max_col)
                island_count += 1
    return island_count


def remove_island(island_map, row, col, max_row, max_col):
    """ Helper function that removes an entire island """
    island_map[row][col] = 0  # Remove current element
    if row < max_row and island_map[row + 1][col] == 1:  # Check bottom neighbor
        return remove_island(island_map, row + 1, col, max_row, max_col)
    if row > 0 and island_map[row - 1][col] == 1:  # Check top neighbor
        return remove_island(island_map, row - 1, col, max_row, max_col)
    if col > 0 and island_map[row][col - 1] == 1:  # Check left neighbor
        return remove_island(island_map, row, col - 1, max_row, max_col)
    if col < max_col and island_map[row][col + 1] == 1:  # Check right neighbor
        return remove_island(island_map, row, col + 1, max_row, max_col)
    else:
        return island_map


# Tests for exercise 5
def sample_grid_map_1():
    return [[1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]


def sample_grid_map_2():
    return [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]]


def test_exercise_5():
    """ Runs all tests for exercise 5 """
    grid_map_1 = sample_grid_map_1()
    assert(nb_of_islands(grid_map_1) == 1)
    grid_map_2 = sample_grid_map_2()
    assert(nb_of_islands(grid_map_2) == 3)


if __name__ == "__main__":
    test_exercise_5()
