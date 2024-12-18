def is_valid(pos, size):
    return 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]

def traverse_memory(bytes, size):
    to_explore = {(0,0)}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cost = {(0,0):0}
    while to_explore:
        pos = to_explore.pop()
        for direction in directions:
            in_front = (pos[0] + direction[0], pos[1] + direction[1])
            if is_valid(in_front, size) and in_front not in bytes and (in_front not in cost or cost[in_front] > cost[pos] + 1):
                to_explore.add(in_front)
                cost[in_front] = cost[pos] + 1
    end = (size[0]-1, size[1]-1)
    return cost[end] if end in cost else False

def find_blocking_byte(all_bytes, size):
    last_passing = 0
    last_failing = len(all_bytes)-1
    while last_failing-last_passing > 1:
        i = int((last_failing - last_passing) / 2) + last_passing
        if not traverse_memory(all_bytes[:i], size):
            last_failing = i
        else:
            last_passing = i
        print(i)
    return all_bytes[last_passing]

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = list(map(lambda line: tuple(map(int, line.strip().split(','))), file.readlines()))
        size = (71,71)

        print(f"part 1: {traverse_memory(input[:1024], size)}")
        
        print(f"part 2: {find_blocking_byte(input, size)}")