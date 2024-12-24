def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def XOR(a, b):
    return a ^ b


def gate_ready(gate, wires):
    return gate[1][0] in wires and gate[1][1] in wires


def compute_number(wires, gates):
    while any(map(lambda gate: gate.startswith('z'), gates.keys())):
        for wire, gate in [val for val in gates.items()]:
            if gate_ready(gate, wires):
                wires[wire] = gate[0](*[wires[wire] for wire in gate[1]])
                gates.pop(wire)
    return int(''.join(map(lambda wire: str(wires[wire]),
                           sorted(filter(lambda wire: wire.startswith('z'), wires.keys()), reverse=True))), 2)


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
        print(compute_number(wires, gates))
