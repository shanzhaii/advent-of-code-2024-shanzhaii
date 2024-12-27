numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A']
]

direction_keypad = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
]


def is_valid(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] != '#'


def remote_control(sequence, pad, starting_pos):
    robot_sequence = []
    last_pos = starting_pos
    for key in sequence:
        last_pos, path = shortest_path(pad, last_pos, key)
        robot_sequence = robot_sequence + path
    return robot_sequence


def prepare_steps(steps):
    directions_to_key = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
    keys = list(map(lambda direction: directions_to_key[direction], steps))
    return keys + ['A']


def shortest_path(pad, starting_pos, value):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    sorted_directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    to_explore = [starting_pos]
    explored = set()
    steps = {starting_pos: [[]]}
    while to_explore:
        pos = to_explore.pop(0)
        if pad[pos[0]][pos[1]] == value:
            value_pos = pos
        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if is_valid(new_pos, pad) and new_pos not in explored:
                for path in steps[pos]:
                    steps.setdefault(new_pos, []).append(path + [direction])
                if new_pos not in to_explore:
                    to_explore.append(new_pos)
        explored.add(pos)
    possible_paths = sorted(steps[value_pos],
                            key=lambda steps: sorted_directions.index(steps[0]) if len(steps) > 0 else -1,
                            reverse=False)
    best_steps = list(filter(no_interleaving, possible_paths))[0]
    return value_pos, prepare_steps(best_steps)


def no_interleaving(steps):
    previous = set()
    last_seen = None
    for step in steps:
        if step in previous and step != last_seen:
            return False
        previous.add(step)
        last_seen = step
    return True


def calculate_sequence(line, num_directional=2):
    sequence = remote_control(line, numeric_keypad, (3, 2))

    storage = {}
    length = process_iteration(sequence, num_directional, storage)
    return length * int(line.strip('A'))


def process_iteration(pattern, iterations_left, storage):
    if iterations_left == 0:
        return len(pattern)
    elif (tuple(pattern), iterations_left) in storage:
        return storage[(tuple(pattern), iterations_left)]
    else:
        total = 0
        for sub_pattern in ''.join(pattern).split('A')[:-1]:
            total += process_iteration(
                remote_control(list(sub_pattern) + ['A'], direction_keypad, (0, 2)),
                                       iterations_left - 1, storage)
        storage[(tuple(pattern), iterations_left)] = total
        return total


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = list(map(lambda line: line.strip(), file.readlines()))
        print(f"part 1: {sum(map(calculate_sequence, input))}")

        print(f"part 1: {sum(map(lambda sequence: calculate_sequence(sequence, 25), input))}")
