def grid_deep_copy(grid):
    return [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]


def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


def get_antennas(grid):
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                antennas.setdefault(grid[y][x], []).append((y, x))
    return antennas


def add_antinode_to_grid(grid, antenna1, antenna2, n):
    antinode = (n * antenna2[0] - n * antenna1[0] + antenna1[0],
                n * antenna2[1] - n * antenna1[1] + antenna1[1])
    if is_valid(antinode, grid):
        grid[antinode[0]][antinode[1]] = '#'
        return True
    else:
        return False


def compute_antinodes(grid, antennas, part1=False):
    grid = grid_deep_copy(grid)
    for antenna_list in antennas.values():
        for antenna1 in antenna_list:
            for antenna2 in filter(lambda antenna: antenna != antenna1, antenna_list):
                if part1:
                    add_antinode_to_grid(grid, antenna1, antenna2, 2)
                else:
                    n = 1
                    is_still_in_grid = True
                    while is_still_in_grid:
                        is_still_in_grid = add_antinode_to_grid(grid, antenna1, antenna2, n)
                        n = n + 1
    return grid


def print_grid(grid):
    current_string = ""
    for row in grid:
        current_string = current_string + ''.join(row) + '\n'
    return current_string


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        antennas = get_antennas(grid)
        print(f"part 1: {flatten(compute_antinodes(grid, antennas, True)).count('#')}")

        print(f"part 2: {flatten(compute_antinodes(grid, antennas)).count('#')}")
