def patterns_possible(pattern: str, towels, storage):
    if len(pattern) == 0:
        return 1
    candidates = list(filter(lambda towel: pattern.startswith(towel), towels))
    if len(candidates) == 0:
        return 0
    total_possibilities = 0
    for towel in candidates:
        total_possibilities += patterns_possible(pattern[len(towel):], towels, storage)
    return total_possibilities

# def patterns_possible(pattern: str, towels, storage):
#     if pattern in storage:
#         return storage[pattern]
#     else:
#         count = 1 if pattern in towels else 0
#         for i in range(1, len(pattern)):
#             count += patterns_possible(pattern[:i], towels, storage) * patterns_possible(pattern[i:], towels, storage)
#         storage[pattern] = count
#         return count

# def patterns_possible(pattern: str, towels, storage):
#     if pattern in storage:
#         return storage[pattern]
#     else:
#         possibilites = {(pattern,)} if pattern in towels else set()
#         for i in range(1, len(pattern)):
#             for pattern1 in patterns_possible(pattern[:i], towels, storage):
#                 for pattern2 in patterns_possible(pattern[i:], towels, storage):
#                     possibilites.add(tuple(list(pattern1) + list(pattern2)))
#         storage[pattern] = possibilites
#         return possibilites


if __name__ == "__main__":
    with open("test", "r", newline='\n') as file:
        towels, patterns = file.read().split('\n\n')
        towels = list(map(lambda towel: towel.strip(), towels.split(',')))
        patterns = patterns.strip().split('\n')
        storage = {}
        print(patterns_possible('brwrr', towels, storage))



        # print(f"part 1: {len(list(filter(lambda pattern: pattern_is_possible(pattern, towels), patterns)))}")

        # print(f"part 2: {sum(map(lambda pattern: len(pattern_is_possible(pattern, towels)), patterns))}")
