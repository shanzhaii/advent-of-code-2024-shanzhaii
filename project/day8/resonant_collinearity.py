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


def compute_antinodes(grid, antennas):
    for antenna_list in antennas.values():
        for antenna1 in antenna_list:
            for antenna2 in filter(lambda antenna: antenna != antenna1, antenna_list):
                antinode = (2 * antenna2[0] - antenna1[0], 2 * antenna2[1] - antenna1[1])
                if is_valid(antinode, grid):
                    grid[antinode[0]][antinode[1]] = '#'

def print_grid(grid):
    current_string = ""
    for row in grid:
        current_string = current_string + ''.join(row) + '\n'
    return current_string

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        compute_antinodes(grid, get_antennas(grid))
        print(f"part 1: {flatten(grid).count('#')}")
        # print(print_grid(grid))
