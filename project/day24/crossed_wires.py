NUM_BITS = 45

def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def XOR(a, b):
    return a ^ b


def gate_ready(gate, wires):
    return gate[1][0] in wires and gate[1][1] in wires


def compute_number(wires, gates):
    wires = {wire: val for wire, val in wires.items()}
    gates = {output: gate for output, gate in gates.items()}
    while any(map(lambda gate: gate.startswith('z'), gates.keys())):
        for wire, gate in [val for val in gates.items()]:
            if gate_ready(gate, wires):
                wires[wire] = gate[0](*[wires[wire] for wire in gate[1]])
                gates.pop(wire)
    return ''.join(map(lambda wire: str(wires[wire]),
                           sorted(filter(lambda wire: wire.startswith('z'), wires.keys()), reverse=True)))

def convert_num_to_wires(a, b):
    x = format(a, 'b').zfill(45)
    y = format(b, 'b').zfill(45)
    wires = {}
    for i, wire in enumerate(reversed(x)):
        wires[f'x{str(i).zfill(2)}'] = int(wire)
    for i, wire in enumerate(reversed(y)):
        wires[f'y{str(i).zfill(2)}'] = int(wire)
    return wires

def apply_rename(gates, rewire):
    new_gates = {}
    for output, gate_input in gates.items():
        func, wires = gate_input
        a, b = wires
        if a in rewire:
            a = rewire[a]
        if b in rewire:
            b = rewire[b]
        if output in rewire:
            output = rewire[output]
        new_gates[output] = (func, (a, b))
    return new_gates

def rename_wires(gates):
    new_gates = {}
    rename = {}
    for output, gate_input in gates.items():
        func, wires = gate_input
        a, b = wires
        if (a.startswith('x') or b.startswith('x')):
            if b.startswith('x'):
                b, a = a, b
            if func is XOR and a != 'x00':
                new_name = 'xor'+a+b
            elif func is AND:
                new_name = 'and' + a + b
            else:
                new_name = output
            rename[output] = new_name
            new_gates[new_name] = (func, (a, b))
        else:
            new_gates[output] = gate_input

    new_new_gates = {}
    for output, gate_input in apply_rename(new_gates, rename).items():
        func, wires = gate_input
        a, b = wires
        if func is OR and output != 'z45':
            if b.startswith('and'):
                b, a = a, b
            new_name = "cout_"+a+b
            rename[output] = new_name
            new_new_gates[new_name] = (func, (a, b))
        else:
            new_new_gates[output] = gate_input
    return apply_rename(new_new_gates, rename)

def print_gates(gates):
    func_name = {OR: "OR", AND: "AND", XOR: "XOR"}
    for output in sorted(gates.keys()):
        print(f"{output} <- {gates[output][1][0]} {func_name[gates[output][0]]} {gates[output][1][1]}")



if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        wires, gates = file.read().split("\n\n")
        wires = {name: int(value) for name, value in [wire.split(':') for wire in wires.strip().split('\n')]}
        gates = {
            wire.strip():
                (AND, tuple(gate.strip().split(" AND "))) if " AND " in gate else
                (XOR, tuple(gate.strip().split(" XOR "))) if " XOR " in gate else
                (OR, tuple(gate.strip().split(" OR ")))
            for gate, wire in
            [gate.split('->') for gate in gates.strip().split('\n')]
        }
        print(f"part 1: {int(compute_number(wires, gates), 2)}")

        print(f"part 2: {','.join(sorted(['z22', 'mdb', 'wpq', 'grf', 'z18', 'fvw', 'z36', 'nwq']))}")

        # print_gates(rename_wires(gates))

        # print("part 2:")
        # a = 11111111111
        # b = 0
        # print(f"expected: a + b = {format(a+b, 'b').zfill(46)}")
        # print(f"actual:   a + b = {compute_number(convert_num_to_wires(a, b), gates)}")

