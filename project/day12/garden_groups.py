def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def find_next_plot(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                return (y,x)
    return False

def add_to_side(location, direction, sides_per_direction):
    adjacent_direction = [(abs(direction[1]), abs(direction[0])), (-abs(direction[1]), -abs(direction[0]))]
    adjacents = list(map(lambda adjacent_direction: (adjacent_direction[0] + location[0], adjacent_direction[1] + location[1]), adjacent_direction))
    matches = []
    for side in sides_per_direction[direction]:
        for adjacent in adjacents:
            if adjacent in side:
                matches.append(side)
    if len(matches) == 0:
        sides_per_direction[direction].append([location])
    elif len(matches) == 1:
        matches[0].append(location)
    else:
        for match in matches:
            sides_per_direction[direction].remove(match)
        sides_per_direction[direction].append(matches[0] + matches[1] + [location])

def count_plot(start_point, grid):
    to_explore = {start_point}
    explored = set()
    perimeter = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    sides_per_direction = {(-1, 0): [],  (0, 1): [], (1, 0): [], (0, -1): []}
    while to_explore:
        location = to_explore.pop()
        for direction in directions:
            new_location = (location[0] + direction[0], location[1] + direction[1])
            if is_valid(new_location, grid) and grid[new_location[0]][new_location[1]] == grid[location[0]][location[1]]:
                if new_location not in explored:
                    to_explore.add(new_location)
            else:
                perimeter += 1
                add_to_side(location, direction, sides_per_direction)

        explored.add(location)
    for explored_point in explored:
        grid[explored_point[0]][explored_point[1]] = '.'
    total_sides = [side for sides in sides_per_direction.values() for side in sides ]
    return len(explored) * perimeter, len(explored) * len(total_sides)

def explore_garden(grid):
    total_fence = 0
    total_fence_with_discount = 0
    next_plot = (0,0)
    while next_plot:
        fence, fence_with_discount = count_plot(next_plot, grid)
        total_fence += fence
        total_fence_with_discount += fence_with_discount
        next_plot = find_next_plot(grid)
    return total_fence, total_fence_with_discount

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid = [list(line.strip()) for line in file.readlines()]
        fence, fence_with_discount = explore_garden(grid)

        print(f"part 1: {fence}")

        print(f"part 2: {fence_with_discount}")
