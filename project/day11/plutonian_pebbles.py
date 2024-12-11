def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


def apply_rules(stone):
    if int(stone) == 0:
        return ['1']
    if len(stone) % 2 == 0:
        return [str(int(stone[0: int(len(stone)/2)])), str(int(stone[int(len(stone)/2): len(stone)]))]
    else:
        return [str(int(stone)*2024)]

def apply_n_iters(stones, n):
    for i in range(n):
        stones = list(flatten(map(apply_rules, stones)))
        print(i)
    return stones


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = file.read().strip().split(' ')
        print(f"part 1: {len(apply_n_iters(input, 75))}")
