def combo(op2, a, b, c):
    if op2 < 4:
        return op2
    elif op2 == 4:
        return a
    elif op2 == 5:
        return b
    elif op2 == 6:
        return c
    else:
        raise Exception('Invalid Combo op')

def divide(op2, a, b, c):
    return int(a / (2 ** combo(op2, a, b, c)))

def adv(op2, ptr, a, b, c, output):
    a = divide(op2, a, b, c)
    return a, b, c, ptr+2

def bxl(op2, ptr, a, b, c, output):
    b = b ^ op2
    return a, b, c, ptr+2

def bst(op2, ptr, a, b, c, output):
    b = combo(op2, a, b, c) % 8
    return a, b, c, ptr+2

def jnz(op2, ptr, a, b, c, output):
    if a == 0:
        return a, b, c, ptr + 2
    else:
        return a, b, c, op2
    
def bxc(op2, ptr, a, b, c, output):
    b = b ^ c
    return a, b, c, ptr+2

def out(op2, ptr, a, b, c, output):
    output.append(combo(op2, a, b, c) % 8)
    return a, b, c, ptr+2

def bdv(op2, ptr, a, b, c, output):
    b = divide(op2, a, b, c)
    return a, b, c, ptr+2

def cdv(op2, ptr, a, b, c, output):
    c = divide(op2, a, b, c)
    return a, b, c, ptr+2

def run_instruction(op1, op2, ptr, a, b, c, output):
    op_code_to_instr = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }
    return op_code_to_instr[op1](op2, ptr, a, b, c, output)


def run_program(program, a, b, c):
    output = []
    ptr = 0
    while ptr < len(program):
        a, b, c, ptr = run_instruction(program[ptr], program[ptr+1], ptr, a, b, c, output)
    return ','.join(map(str, output))
        

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        registers, program = file.read().split('\n\n')
        a, b, c = map(lambda register_info: int(register_info.strip('Register ABC:')), registers.split('\n'))
        program = list(map(int, program.strip('Program: ').split(',')))
        print(run_program(program, a, b, c))