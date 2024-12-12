def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def find_next_plot(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                return (y,x)
    return False

def count_plot(start_point, grid):
    to_explore = {start_point}
    explored = set()
    perimeter = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while to_explore:
        location = to_explore.pop()
        for direction in directions:
            new_location = (location[0] + direction[0], location[1] + direction[1])
            if is_valid(new_location, grid) and grid[new_location[0]][new_location[1]] == grid[location[0]][location[1]]:
                if new_location not in explored:
                    to_explore.add(new_location)
            else:
                perimeter += 1
        explored.add(location)
    for explored_point in explored:
        grid[explored_point[0]][explored_point[1]] = '.'
    return len(explored) * perimeter

def explore_garden(grid):
    total_fence = 0
    next_plot = (0,0)
    while next_plot:
        total_fence += count_plot(next_plot, grid)
        next_plot = find_next_plot(grid)
    return total_fence

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        print(explore_garden(grid))
