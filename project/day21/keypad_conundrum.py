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

def robot(sequences, pad, starting_pos, length_only = False):
    robot_sequence = []
    min_length = 10000000000000
    last_pos = starting_pos
    for sequence in sequences:
        current_sequences = [[]]
        for key in sequence:
            last_pos, possible_paths = shortest_path(pad, last_pos, key)
            current_sequences = [
                current_sequence + possible_path
                for possible_path in possible_paths
                for current_sequence in current_sequences
            ]
        for current_sequence in current_sequences:
            if length_only:
                min_length = min(min_length, len(current_sequence))
            else:
                robot_sequence.append(current_sequence)
    if length_only:
        return min_length
    min_length = min(map(len, robot_sequence))
    return list(filter(lambda sequence: len(sequence) == min_length, robot_sequence))


def shortest_path(pad, starting_pos, value):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    directions_to_key = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
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
    return value_pos, [list(map(lambda direction: directions_to_key[direction], possible_path)) + ['A'] for possible_path in steps[value_pos]]

def calculate_complexity(line):
    robot1 = robot([line], numeric_keypad, (3, 2))
    robot2 = robot(robot1, direction_keypad, (0, 2))
    length = robot(robot2, direction_keypad, (0, 2), True)
    return length * int(line.strip('A'))


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = list(map(lambda line: line.strip(), file.readlines()))
        print(f"part 1 {sum(map(calculate_complexity, input))}")
