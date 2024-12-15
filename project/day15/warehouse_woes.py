def find_robot(grid):
    y = list(filter(lambda row: '@' in row[1], enumerate(grid)))[0][0]
    return y, grid[y].index('@')

def run_movements(grid, movements):
    pos = find_robot(grid)
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    movements = [movement for movement in movements]
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

def run_small_movements(grid, movements):
    pos = find_robot(grid)
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    movements = [movement for movement in movements]
    while movements:
        movement = movements.pop(0)
        direction = directions[movement]
        all_in_front = []
        last_checked_positions = {(pos[0], pos[1])}
        new_to_old = {}
        while last_checked_positions == {(pos[0], pos[1])} or all(map(lambda loc: grid[loc[0]][loc[1]] in {'[', ']'}, last_checked_positions)):
            new_in_front = set()
            for previous in last_checked_positions:
                in_front = (previous[0] + direction[0], previous[1] + direction[1])
                new_in_front.add(in_front)
                new_to_old[in_front] = previous
                if direction[0] != 0:
                    if grid[in_front[0]][in_front[1]] == '[':
                        new_in_front.add((in_front[0], in_front[1] + 1))
                    if grid[in_front[0]][in_front[1]] == ']':
                        new_in_front.add((in_front[0], in_front[1] - 1))
            for new in new_in_front:
                all_in_front.append(new)
            last_checked_positions = new_in_front

        if all(map(lambda loc: grid[loc[0]][loc[1]] == '.', last_checked_positions)):
            for new in all_in_front[::-1]:
                if new in new_to_old:
                    grid[new[0]][new[1]] = grid[new_to_old[new][0]][new_to_old[new][1]]
            for uncovered_old in filter(lambda old: old not in new_to_old.keys(), new_to_old.values()):
                grid[uncovered_old[0]][uncovered_old[1]] = '.'
            pos = (pos[0] + direction[0], pos[1] + direction[1])
        print(movement)
        print_grid(grid)
    return grid

def count_gps(grid):
    current_gps_score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in {'O', '['}:
                current_gps_score += 100*y + x
    return current_gps_score

def print_grid(grid):
    for y in range(len(grid)):
        print(''.join(grid[y]))
    print('\n')

def grid_enlarge(grid):
    return [[char for value in row for char in ('##' if value == '#' else '[]' if value == 'O' else '..' if value == '.' else '@.')] for row in grid]


if __name__ == "__main__":
    with open("test4", "r", newline='\n') as file:
        grid, movements = file.read().split("\n\n")
        grid = [list(line.strip()) for line in grid.split('\n')]
        new_grid = grid_enlarge(grid)
        movements = [movement for movement in movements if movement != '\n']
        print(f"part 1: {count_gps(run_movements(grid, movements))}")

        print(f"part 2: {count_gps(run_small_movements(new_grid, movements))}")


