from functools import reduce
from operator import add, mul

def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]

def concatenation(a, b):
    return int(str(a) + str(b))

def valid(test_value, equation, operators):
    possible_sums = reduce(
        lambda acc, value: flatten(map(lambda previous_sum: [operator(previous_sum, value) for operator in operators], acc)),
        equation[1:],
        [equation[0]])
    return test_value in possible_sums


if __name__ == "__main__":
    with open("input", "r") as file:
        lines = [line.strip() for line in file.readlines()]
        equations = [(int(line.split(':')[0].strip()), list(map(int, line.split(':')[1].strip().split(' ')))) for line in lines]
        print(f"part 1: {sum([k for k, v in equations if valid(k, v, [add, mul])])}")

        print(f"part 2: {sum([k for k, v in equations if valid(k, v, [add, mul, concatenation])])}")
