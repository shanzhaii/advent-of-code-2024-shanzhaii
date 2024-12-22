directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def is_valid(pos, size):
    return 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]


def find_features(grid):
    obstacles = set()
    size = (len(grid) - 2, len(grid[0]) - 2)
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            value = grid[y][x]
            pos = (y - 1, x - 1)
            if value == '#':
                obstacles.add(pos)
            elif value == 'S':
                start = pos
            elif value == 'E':
                end = pos
    return obstacles, start, end, size


def traverse_maze(obstacles, start, end, size):
    to_explore = {start}
    cost = {start: 0}
    path = {start: [(start)]}
    while to_explore:
        pos = to_explore.pop()
        for direction in directions:
            in_front = (pos[0] + direction[0], pos[1] + direction[1])
            if (is_valid(in_front, size)
                    and (in_front not in obstacles)
                    and (in_front not in cost or cost[in_front] > cost[pos] + 1)):
                to_explore.add(in_front)
                cost[in_front] = cost[pos] + 1
                path[in_front] = path[pos] + [in_front]
    return path[end], cost[end]


def find_cheats(grid):
    obstacles, start, end, size = find_features(grid)
    # cheats = {}
    cheat_count = 0
    normal_path, normal_time = traverse_maze(obstacles, start, end, size)
    for i, step in enumerate(normal_path):
        for direction in directions:
            in_front = (step[0] + direction[0], step[1] + direction[1])
            if is_valid(in_front, size) and (in_front in obstacles):
                for next_direction in directions:
                    next_in_front = (in_front[0] + next_direction[0], in_front[1] + next_direction[1])
                    if next_in_front in normal_path and normal_path.index(next_in_front) - i - 2 >= 100:
                        cheat_count += 1
    return cheat_count



if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        print(find_cheats(grid))
