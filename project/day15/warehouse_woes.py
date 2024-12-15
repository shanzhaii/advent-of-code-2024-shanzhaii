def find_robot(grid):
    y = list(filter(lambda row: '@' in row[1], enumerate(grid)))[0][0]
    return y, grid[y].index('@')

def run_movements(grid, movements):
    pos = find_robot(grid)
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    while movements:
        movement = movements.pop(0)
        direction = directions[movement]
        in_front = (pos[0] + direction[0], pos[1] + direction[1])
        number_steps = 1
        while grid[in_front[0]][in_front[1]] == 'O':
            number_steps += 1
            in_front = (in_front[0] + direction[0], in_front[1] + direction[1])
        if grid[in_front[0]][in_front[1]] == '.':
            for i in range(number_steps-1, -1, -1):
                grid[pos[0] + direction[0] * (i + 1)][pos[1] + direction[1] * (i + 1)] = grid[pos[0] + direction[0] * i][pos[1] + direction[1] * i]
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0] + direction[0], pos[1] + direction[1])
    return grid

def count_gps(grid):
    current_gps_score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                current_gps_score += 100*y + x
    return current_gps_score


if __name__ == "__main__":
    with open("test2", "r", newline='\n') as file:
        grid, movements = file.read().split("\n\n")
        grid = [list(line.strip()) for line in grid.split('\n')]
        movements = [movement for movement in movements if movement != '\n']
        print(f"part 1: {count_gps(run_movements(grid, movements))}")
