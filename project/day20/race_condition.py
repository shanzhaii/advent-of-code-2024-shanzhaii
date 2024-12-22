def is_valid(pos, size):
    return 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]

def find_features(grid):
    obstacles = set()
    size = (len(grid)-2, len(grid[0])-2)
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            value = grid[y][x]
            pos = (y-1, x-1)
            if value == '#':
                obstacles.add(pos)
            elif value == 'S':
                start = pos
            elif value == 'E':
                end = pos
    return obstacles, start, end, size

def traverse_maze(obstacles, start, end, size, cheat_time = None):
    to_explore = {start}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cost = {start: 0}
    cheat_start, cheat_end = (-1, -1), (-1, -1)
    while to_explore:
        pos = to_explore.pop()
        for direction in directions:
            in_front = (pos[0] + direction[0], pos[1] + direction[1])
            if is_valid(in_front, size) and (in_front not in obstacles or (cheat_time is not None and cost[pos] + 1 == cheat_time)) and (in_front not in cost or cost[in_front] >= cost[pos] + 1):
                if cheat_time is not None:
                    if in_front in obstacles:
                        cheat_start = in_front
                    if pos == cheat_start:
                        cheat_end = in_front
                to_explore.add(in_front)
                cost[in_front] = cost[pos] + 1
    if cheat_time is not None:
        return cost[end], (cheat_start, cheat_end)
    return cost[end] if end in cost else False

def find_cheats(grid):
    obstacles, start, end, size = find_features(grid)
    normal_time = traverse_maze(obstacles, start, end, size)
    times = {}

    for i in range(normal_time):
        cheated_time, cheat = traverse_maze(obstacles, start, end, size, i)
        times.setdefault(cheated_time, set()).add(cheat)
    print(times)

if __name__ == "__main__":
    with open("test", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        find_cheats(grid)
