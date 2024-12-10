def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def find_all_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trailheads.append((y,x))
    return trailheads

def find_trailhead_score(head, grid):
    location_to_score = {head: 0}
    explored = []
    score = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while location_to_score:
        for location, height in dict(location_to_score).items():
            if height == 9:
                score += 1
            else:
                for direction in directions:
                    new_location = (location[0] + direction[0], location[1] + direction[1])
                    if is_valid(new_location, grid) and new_location not in explored and grid[new_location[0]][new_location[1]] == height + 1:
                        location_to_score[new_location] = height + 1
            explored.append(location)
            location_to_score.pop(location)
    return score


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(map(int, line.strip())) for line in file.readlines()]
        print(f"part 1: {sum(map(lambda trailhead: find_trailhead_score(trailhead, grid), find_all_trailheads(grid)))}")