def find_guard(grid):
    y = list(filter(lambda row: '^' in row[1], enumerate(grid)))[0][0]
    return y, grid[y].index('^')


def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def iterate_through_path(grid):
    guard_pos = find_guard(grid)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    while is_valid(guard_pos, grid):
        in_front = guard_pos[0] + directions[direction_index][0], guard_pos[1] + directions[direction_index][1]
        if is_valid(in_front, grid) and grid[in_front[0]][in_front[1]] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            grid[guard_pos[0]][guard_pos[1]] = 'X'
            guard_pos = (guard_pos[0] + directions[direction_index][0], guard_pos[1] + directions[direction_index][1])
    return grid


def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        grid = iterate_through_path(grid)
        print(f"part 1: {flatten(grid).count('X')}")
