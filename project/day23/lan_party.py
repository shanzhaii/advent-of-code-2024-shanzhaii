def find_relations_and_nodes(input):
    nodes = set()
    relations = {}
    for pair in input:
        relations.setdefault(pair[0], set()).add(pair[1])
        relations.setdefault(pair[1], set()).add(pair[0])
        nodes.add(pair[0])
        nodes.add(pair[1])
    return relations, nodes

def find_triplets(input, relations):
    triplets = set()
    for pair in input:
        for third in relations[pair[0]].intersection(relations[pair[1]]):
            triplet_list = [pair[0], pair[1], third]
            if any(map(lambda node: node.startswith('t'), triplet_list)):
                triplets.add(tuple(sorted(triplet_list)))
    return len(triplets)
    
def find_lan(nodes, relations):
    lans = []
    largest = 0
    i_largest = -1
    for node in nodes:
        found_match = False
        for i, lan in enumerate(lans):
            if relations[node].intersection(lan) == lan:
                lan.add(node)
                found_match = True
                if len(lan) > largest:
                    largest = len(lan)
                    i_largest = i
        if not found_match:
            lans.append({node})
    return ','.join(sorted(list(lans[i_largest])))

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = list(map(lambda line: line.strip().split('-'), file.readlines()))
        relations, nodes = find_relations_and_nodes(input)
        print(f"part 1: {find_triplets(input, relations)}")

        print(find_lan(nodes, relations))
        