def find_symbol(grid, char):
    y = list(filter(lambda row: char in row[1], enumerate(grid)))[0][0]
    return y, grid[y].index(char)

def run(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start = find_symbol(grid, 'S')
    to_visit = {(start[0], start[1], 1)}
    scores = {(start[0], start[1], 1): 0}
    paths = {(start[0], start[1], 1): {(start[0], start[1])}}
    while to_visit:
        current_pos = to_visit.pop()
        x, y, direction = current_pos
        in_front = (x + directions[direction][0], y + directions[direction][1], direction)
        if grid[in_front[0]][in_front[1]] != '#' and (in_front not in scores or scores[in_front] >= scores[current_pos] + 1):
            to_visit.add(in_front)
            if in_front in scores and scores[in_front] == scores[current_pos] + 1:
                paths[in_front] = paths[in_front].union(paths[current_pos])
            else:
                paths[in_front] = paths[current_pos].union({(in_front[0], in_front[1])})
            scores[in_front] = scores[current_pos] + 1
        for rotation in [1, -1]:
            new_pos = (x, y, len(directions) + direction + rotation if direction + rotation < 0 else (direction+rotation) % len(directions))
            if new_pos not in scores or scores[new_pos] >= scores[current_pos] + 1000:
                to_visit.add(new_pos)
                if new_pos in scores and scores[new_pos] == scores[current_pos] + 1000:
                    paths[new_pos] = paths[new_pos].union(paths[current_pos])
                else:
                    paths[new_pos] = paths[current_pos].union({(new_pos[0], new_pos[1])})
                scores[new_pos] = scores[current_pos] + 1000
    y_end, x_end = find_symbol(grid, 'E')
    scores, endpoints = zip(*[(scores[endpoint], endpoint) for endpoint in [(y_end, x_end, direction) for direction in range(4)]])
    score, endpoint = min(scores), endpoints[scores.index(min(scores))]
    return score, paths[endpoint]


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        score, path = run(grid)
        print(f"part 1: {score}")

        print(f"part 2: {len(path)}")

