import re


def detect_straight(positions, number_in_straight):
    for position in positions:
        diag = [(position[0] - i, position[1]) for i in range(number_in_straight)]
        if all(map(lambda pos: pos in positions, diag)):
            return True
    return False


def print_robots(positions, grid_size):
    string = ''
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if (x, y) in positions:
                string += '#'
            else:
                string += '.'
        string += '\n'
    string += '\n'
    print(string)


def teleport(x, y, grid_x, grid_y):
    return grid_x + x if x < 0 else x % grid_x, grid_y + y if y < 0 else y % grid_y


def move_robot(robot_position, robot_speed, grid_size):
    return teleport(robot_position[0] + robot_speed[0], robot_position[1] + robot_speed[1], grid_size[0], grid_size[1])


def run_simulation(robots_info, time, grid_size):
    for i in range(time):
        robots_info = list(map(lambda robot_info: (move_robot(*robot_info, grid_size), robot_info[1]), robots_info))
    return list(robots_info)


def calculate_safety_factor(positions, grid_size):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for position in positions:
        if position[0] < int(grid_size[0] / 2) and position[1] < int(grid_size[1] / 2):
            q1 += 1
        elif position[0] >= int(grid_size[0] / 2) + 1 and position[1] < int(grid_size[1] / 2):
            q2 += 1
        elif position[0] < int(grid_size[0] / 2) and position[1] >= int(grid_size[1] / 2) + 1:
            q3 += 1
        elif position[0] >= int(grid_size[0] / 2) + 1 and position[1] >= int(grid_size[1] / 2) + 1:
            q4 += 1
    return q1 * q2 * q3 * q4


def run_until_straight(robots_info, grid_size):
    i = 1
    while True:
        robots_info = list(map(lambda robot_info: (move_robot(*robot_info, grid_size), robot_info[1]), robots_info))
        positions, speeds = zip(*robots_info)
        if detect_straight(positions, 8):
            return i
        i += 1


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        grid_size = (101, 103)
        input = list(map(lambda robot: ((int(robot[0]), int(robot[1])), (int(robot[2]), int(robot[3]))),
                         map(lambda line: re.findall(r"-?\d+", line), file.readlines())))

        positions, speeds = zip(*run_simulation(input, 100, grid_size))

        print(f"part 1: {calculate_safety_factor(positions, grid_size)}")

        print(f"part 2: {run_until_straight(input, grid_size)}")
