def find_guard(grid):
    y = list(filter(lambda row: '^' in row[1], enumerate(grid)))[0][0]
    return (y, grid[y].index('^'))

def iterate_through_path(grid):
    guard_pos = find_guard(grid)
    directions = [(-1, 0), (0,1), (1,0), (0,-1)]
    direction_index = 0
    grid[guard_pos[0]][guard_pos[1]] = 'X'
    while True:
        if guard_pos[0] + directions[direction_index][0] >= len(grid) or guard_pos[1] + directions[direction_index][1] >= len(grid) or guard_pos[0] + directions[direction_index][0] < 0 or guard_pos[1] + directions[direction_index][1] < 0:
            grid[guard_pos[0]][guard_pos[1]] = 'X'
            return grid
        elif grid[guard_pos[0] + directions[direction_index][0]][guard_pos[1] + directions[direction_index][1]] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            grid[guard_pos[0]][guard_pos[1]] = 'X'
            guard_pos = (guard_pos[0] + directions[direction_index][0], guard_pos[1] + directions[direction_index][1])

def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        grid = iterate_through_path(grid)
        print(f"part 1: {flatten(grid).count('X')}")