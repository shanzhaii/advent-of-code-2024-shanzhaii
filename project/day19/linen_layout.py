def patterns_possible(pattern: str, towels, storage):
    if len(pattern) == 0:
        return 1
    if pattern in storage:
        return storage[pattern]
    candidates = list(filter(lambda towel: pattern.startswith(towel), towels))
    if len(candidates) == 0:
        return 0
    total_possibilities = 0
    for towel in candidates:
        total_possibilities += patterns_possible(pattern[len(towel):], towels, storage)
    storage[pattern] = total_possibilities
    return total_possibilities


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        towels, patterns = file.read().split('\n\n')
        towels = list(map(lambda towel: towel.strip(), towels.split(',')))
        patterns = patterns.strip().split('\n')
        storage = {}

        print(f"part 1: {list(map(lambda pattern: patterns_possible(pattern, towels, storage) > 0, patterns)).count(True)}")

        print(f"part 2: {sum(map(lambda pattern: patterns_possible(pattern, towels, storage), patterns))}")
