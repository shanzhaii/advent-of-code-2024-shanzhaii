FP_ERROR = 0.000000001

def parse_machine(input):
    properties = input.split('\n')
    output = {
        'A': tuple(map(lambda value: int(value.strip('ButtonABXY+: ')), properties[0].split(','))),
        'B': tuple(map(lambda value: int(value.strip('ButtonABXY+: ')), properties[1].split(','))),
        'Prize': tuple(map(lambda value: int(value.strip('PrizeXY=: ')), properties[2].split(',')))
    }
    return output

def parse_erroneous_machine(input):
    properties = input.split('\n')
    output = {
        'A': tuple(map(lambda value: int(value.strip('ButtonABXY+: ')), properties[0].split(','))),
        'B': tuple(map(lambda value: int(value.strip('ButtonABXY+: ')), properties[1].split(','))),
        'Prize': tuple(map(lambda value: int(value.strip('PrizeXY=: ')) + 10000000000000, properties[2].split(',')))
    }
    return output

def calculate_tokens(machine):
    a = 0
    b = 0
    tokens_necessary = 0
    while a < 100 and a * machine['A'][0] <= machine['Prize'][0] and machine['A'][1] <= machine['Prize'][1]:
        b = 0
        while b < 100 and a * machine['A'][0] + b * machine['B'][0] <= machine['Prize'][0] and a * machine['A'][1] + b * machine['B'][1] <= machine['Prize'][1]:
            if a * machine['A'][0] + b * machine['B'][0] == machine['Prize'][0] and a * machine['A'][1] + b * machine['B'][1] == machine['Prize'][1] and (tokens_necessary == 0 or 3*a + b < tokens_necessary):
                tokens_necessary = 3*a + b
            b += 1
        a += 1
    return tokens_necessary

# triple a and its values

def solve_system(machine): 
    a = (machine['Prize'][0] * machine['B'][1] - machine['Prize'][1] * machine['B'][0]) / (machine['A'][0] * machine['B'][1] - machine['A'][1] * machine['B'][0])
    if abs(int(a) - a) < FP_ERROR:
        b = (machine['Prize'][1] - int(a) * machine['A'][1]) / machine['B'][1]
        if abs(int(b) - b) < FP_ERROR:
            return 3*int(a) + int(b)
    return 0

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = file.read().split('\n\n')
        print(f"part 1: {sum(map(calculate_tokens, list(map(lambda machine: parse_machine(machine), input))))}")

        print(f"part 2: {sum(map(solve_system, list(map(lambda machine: parse_erroneous_machine(machine), input))))}")
