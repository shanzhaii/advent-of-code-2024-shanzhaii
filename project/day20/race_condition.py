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

def find_normal_path(obstacles, start, end, size):
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

def traverse_maze(obstacles, start, end, size, max_cost):
    global storage
    to_explore = [start]
    explored = set()
    cost, path = storage
    cost.setdefault((start, start), 0)
    path.setdefault((start, start), [start])
    while to_explore and (max_cost is None or cost[(start, to_explore[0])] <= max_cost):
        if (start, end) in cost:
            return cost[(start, end)]
        pos = to_explore.pop(0)
        for direction in directions:
            in_front = (pos[0] + direction[0], pos[1] + direction[1])
            if (is_valid(in_front, size)
                    and (in_front not in obstacles)
                    and ((start, in_front) not in cost or cost[(start, in_front)] >= cost[(start, pos)] + 1)):
                if in_front not in to_explore or in_front not in explored:
                    to_explore.append(in_front)
                path[(start, in_front)] = path[(start, pos)] + [in_front]
                cost[(start, in_front)] = cost[(start, pos)] + 1
                # full_previous_path = path[(start, pos)]
                # for i in range(min(len(full_previous_path), 3)):
                #     if (full_previous_path[i], in_front) not in cost:
                #         path[(full_previous_path[i], in_front)] = full_previous_path[i:] + [in_front]
                #         cost[(full_previous_path[i], in_front)] = len(full_previous_path) - i
        explored.add(pos)
    return None

def distance(a, b):
    a_y, a_x = a
    b_y, b_x = b
    return abs(a_x - b_x) + abs(a_y - b_y)

def find_cheats(grid, max_cheat_cost, min_cheat):
    obstacles, start, end, size = find_features(grid)
    cheats = {}
    explored_cheats = set()
    normal_path, normal_time = find_normal_path(obstacles, start, end, size)
    for i, step in enumerate(normal_path):
        print(i)
        cheat_start = step
        for j in range(i+min_cheat, len(normal_path)):
            if distance(normal_path[j], cheat_start) <= max_cheat_cost:
                cheat_end = normal_path[j]
                cheat = (cheat_start, cheat_end)
                if cheat not in explored_cheats:
                    cheat_traversal = traverse_maze({}, cheat_start, cheat_end, size, max_cost=max_cheat_cost)
                    if cheat_traversal is not None:
                        cheat_cost = cheat_traversal
                        if cheat_cost < j-i:
                            cheats.setdefault(j-i-cheat_cost, set()).add(cheat)
                    explored_cheats.add(cheat)
    return sum([len(positions) for cheat_save, positions in cheats.items() if cheat_save >= min_cheat])

storage = ({}, {})

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        print(f"part 1: {find_cheats(grid, 20, 100)}")

        # print(f"part 2: {find_cheats(grid, 20, 100)}")
