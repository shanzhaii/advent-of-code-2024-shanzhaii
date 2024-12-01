from functools import reduce

if __name__ == "__main__":
    with open("input", "r", newline='\n') as lists:
        list_of_ids = [line.strip("\n").split("   ") for line in lists]
        left_ids = [int(left) for left, right in list_of_ids]
        right_ids = [int(right) for left, right in list_of_ids]
        left_ids.sort()
        right_ids.sort()
        print(f"part 1: {reduce(lambda acc, ids: acc + abs(ids[0] - ids[1]), zip(left_ids, right_ids), 0)}")

