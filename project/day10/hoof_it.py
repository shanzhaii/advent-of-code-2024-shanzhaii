def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def find_all_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trailheads.append((y,x))
    return trailheads

def find_trailhead_score_and_rating(head, grid):
    path_to_explore = [([head], 0)]
    path_to_end = []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while path_to_explore:
        for path_height_tuple in path_to_explore:
            path, height = path_height_tuple[0], path_height_tuple[1]
            if height == 9:
                if path not in path_to_end:
                    path_to_end.append(path)
            else:
                for direction in directions:
                    new_location = (path[-1][0] + direction[0], path[-1][1] + direction[1])
                    if is_valid(new_location, grid) and grid[new_location[0]][new_location[1]] == height + 1:
                        new_path = list(path)
                        new_path.append(new_location)
                        path_to_explore.append((new_path, height + 1))
            path_to_explore.remove((path, height))
    return len(set(map(lambda path: path[-1], path_to_end))), len(path_to_end)


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(map(int, line.strip())) for line in file.readlines()]
        score, rating = zip(*map(lambda trailhead: find_trailhead_score_and_rating(trailhead, grid), find_all_trailheads(grid)))
        print(f"part 1: {sum(score)}")

        print(f"part 2: {sum(rating)}")