from functools import reduce


def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


def valid(test_value, equation):
    possible_sums = reduce(
        lambda acc, value: flatten(map(lambda previous_sum: (previous_sum + value, previous_sum * value), acc)),
        equation[1:],
        [equation[0]])
    possible_equations = reduce(
        lambda acc, value: flatten(map(lambda previous_equation: (previous_equation + f" + {value}", previous_equation + f" * {value}"), acc)),
        equation[1:],
        [str(equation[0])]
    )
    return test_value in possible_sums


if __name__ == "__main__":
    with open("input", "r") as file:
        lines = [line.strip() for line in file.readlines()]
        equations = [(int(line.split(':')[0].strip()), list(map(int, line.split(':')[1].strip().split(' ')))) for line in lines]
        print(f"part 1: {sum([k for k, v in equations if valid(k, v)])}")
