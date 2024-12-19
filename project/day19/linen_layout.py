def patterns_possible(pattern:str, towels, storage):
    if pattern in storage:
        return storage[pattern]
    else:
        possible_patterns = []
        for towel in filter(lambda towel: pattern.startswith(towel), towels):
            if len(pattern[len(towel):]) == 0:
                possible_patterns.append([towel])
            else:
                for subpattern in patterns_possible(pattern[len(towel):], towels, storage):
                    possible_patterns.append([towel] + subpattern)
        storage[pattern] = possible_patterns
        return possible_patterns

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        towels, patterns = file.read().split('\n\n')
        towels = list(map(lambda towel: towel.strip(), towels.split(',')))
        patterns = patterns.strip().split('\n')
        storage = {}
        print(patterns_possible('ugurwbbbgrrbbubrurubuwgguurgbbwbrubwbwgwugwbwururrrgg', towels, storage))

        # print(f"part 1: {len(list(filter(lambda pattern: pattern_is_possible(pattern, towels), patterns)))}")

        # print(f"part 2: {sum(map(lambda pattern: len(pattern_is_possible(pattern, towels)), patterns))}")
