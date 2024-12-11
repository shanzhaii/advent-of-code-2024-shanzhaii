def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


def apply_rules(stone):
    if int(stone) == 0:
        return ['1']
    if len(stone) % 2 == 0:
        return [str(int(stone[: int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))]
    else:
        return [str(int(stone)*2024)]

def apply_n_iters(stones, n):
    for i in range(n):
        stones = list(flatten(map(apply_rules, stones)))
    return stones

storage = {}

def recursively_solve(stone, iterations_left):
    if iterations_left == 0:
        return 1
    elif ((stone, iterations_left) in storage):
        return storage[(stone, iterations_left)]
    elif int(stone) == 0:
        result = recursively_solve('1', iterations_left-1)
        storage[(stone, iterations_left)] = result
        return result
    elif len(stone) % 2 == 0:
        result = recursively_solve(str(int(stone[: int(len(stone)/2)])), iterations_left-1) + recursively_solve(str(int(stone[int(len(stone)/2): ])), iterations_left-1)
        storage[(stone, iterations_left)] = result
        return result
    else:
        result = recursively_solve(str(int(stone)*2024), iterations_left-1)
        storage[(stone, iterations_left)] = result
        return result



if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = file.read().strip().split(' ')
        print(f"part 1: {len(apply_n_iters(input, 25))}")

        print(f"part 2: {sum(map(lambda pebble: recursively_solve(pebble, 75), input))}")
