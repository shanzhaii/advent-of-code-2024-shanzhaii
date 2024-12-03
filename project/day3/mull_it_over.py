import re

def process_muls(muls):
    return sum(map(lambda operands: int(operands[0]) * int(operands[1]), (map(lambda mul_string: mul_string.strip("mul()").split(","), muls))))

with open("input", "r", newline='\n') as file:
    input = file.read()
    all_muls = re.findall("mul\\([0-9]+,[0-9]+\\)", input)
    print(f"part 1: {process_muls(all_muls)}")

    muls_and_instructions = re.findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)", input)
    enabled = True
    filtered_muls = list()
    for value in muls_and_instructions:
        if (value == "do()"):
            enabled = True
        elif (value == "don't()"):
            enabled = False
        elif (enabled):
            filtered_muls.append(value)
    print(f"part 2: {process_muls(filtered_muls)}")
