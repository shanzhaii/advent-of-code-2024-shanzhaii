from typing import List, Dict

def printable(row: List[int], comes_after: Dict[int, List[int]], comes_before: Dict[int, List[int]]):
    for i in range(len(row)):
        for i_before in range(i):
            if (row[i] not in comes_before or not row[i_before] in comes_before.get(row[i])):
                return False
        for i_after in range(i+1, len(row)):
            if (row[i] not in comes_after or not row[i_after] in comes_after.get(row[i])):
                return False
    return True

def reorder(row: List[int], comes_after: Dict[int, List[int]], comes_before: Dict[int, List[int]]):
    values_left = list(row)
    ordered = []
    while values_left:
        for value in values_left:
            values_before_correct = list(map(lambda value_before: value in comes_before and value_before in comes_before.get(value), ordered))
            values_after_correct = list(map(lambda value_after: value in comes_after and value_after in comes_after.get(value), filter(lambda value_left: value != value_left, values_left)))
            if all(values_after_correct) and all(values_before_correct):
                ordered.append(value)
                values_left.remove(value)
                break
    return ordered



if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        rules, prints = file.read().split("\n\n")
        rules = list(map(lambda rule: tuple(map(int, rule.split('|'))) , rules.split('\n')))
        prints = list(map(lambda print: list(map(int, print.split(','))) , prints.split('\n')))
        comes_after = {}
        comes_before = {}
        for rule in rules:
            comes_after.setdefault(rule[0], []).append(rule[1])
            comes_before.setdefault(rule[1], []).append(rule[0])

        print(f"part 1: {sum([print[int(len(print)/2)] for print in prints if printable(print, comes_after, comes_before)])}")

        non_printable = list(filter(lambda print: not printable(print, comes_after, comes_before), prints))
        reorderd = list(map(lambda print: reorder(print, comes_after, comes_before), non_printable))

        print(f"part 2: {sum([print[int(len(print)/2)] for print in reorderd])}")
