def find_symbol(grid, char):
    y = list(filter(lambda row: char in row[1], enumerate(grid)))[0][0]
    return y, grid[y].index(char)

def run(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start = find_symbol(grid, 'S')
    to_visit = {(start[0], start[1], 1)}
    scores = {(start[0], start[1], 1): 0}
    while to_visit:
        current_pos = to_visit.pop()
        x, y, direction = current_pos
        in_front = (x + directions[direction][0], y + directions[direction][1], direction)
        if grid[in_front[0]][in_front[1]] != '#' and (in_front not in scores or scores[in_front] > scores[current_pos] + 1):
            to_visit.add(in_front)
            scores[in_front] = scores[current_pos] + 1
        for rotation in [1, -1]:
            new_pos = (x, y, len(directions) + direction + rotation if direction + rotation < 0 else (direction+rotation) % len(directions))
            if new_pos not in scores or scores[new_pos] > scores[current_pos] + 1000:
                to_visit.add(new_pos)
                scores[new_pos] = scores[current_pos] + 1000
    y_end, x_end = find_symbol(grid, 'E')
    end_scores = [scores[end_point] for end_point in [(y_end, x_end, direction) for direction in range(4)]]
    return min(end_scores)


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        print(f"part 1: {run(grid)}")
