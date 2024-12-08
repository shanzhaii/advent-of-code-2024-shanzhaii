def find_guard(grid):
    y = list(filter(lambda row: '^' in row[1], enumerate(grid)))[0][0]
    return y, grid[y].index('^')


def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def iterate_through_path(grid, guard_pos, root_path=True, direction_index=0):
    previous_positions = {}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while is_valid(guard_pos, grid):
        if guard_pos in previous_positions and direction_index in previous_positions.get(guard_pos):
            if root_path:
                raise Exception('Should not ever loop from root')
            return True
        in_front = guard_pos[0] + directions[direction_index][0], guard_pos[1] + directions[direction_index][1]
        if is_valid(in_front, grid) and grid[in_front[0]][in_front[1]] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            if root_path and is_valid(in_front, grid):
                modified_grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]  # deep copy
                modified_grid[guard_pos[0] + directions[direction_index][0]][guard_pos[1] + directions[direction_index][1]] = '#'
                if grid[guard_pos[0]][guard_pos[1]] != '^' and iterate_through_path(modified_grid, initial_pos, False):
                    grid[in_front[0]][in_front[1]] = 'O'

            if grid[guard_pos[0]][guard_pos[1]] != 'O':
                grid[guard_pos[0]][guard_pos[1]] = 'X'
            previous_positions.setdefault(guard_pos, []).append(direction_index)
            guard_pos = (guard_pos[0] + directions[direction_index][0], guard_pos[1] + directions[direction_index][1])
    if root_path:
        return grid
    return False


def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        initial_pos = find_guard(grid)
        grid = iterate_through_path(grid, initial_pos)
        print(f"part 1: {flatten(grid).count('X') + flatten(grid).count('O')}")

        print(f"part 2: {flatten(grid).count('O')}")
