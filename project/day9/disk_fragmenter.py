def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]

def decompress(compressed_disk_map):
    return flatten([[int(i/2)]*int(compressed_disk_map[i]) if i % 2 == 0 else ['.']*int(compressed_disk_map[i]) for i in range(len(compressed_disk_map))])

def defragment(uncompressed_disk_map):
    disk_map = [char for char in uncompressed_disk_map]
    new_map = []
    while disk_map:
        front = disk_map[0]
        if front != '.':
            new_map.append(disk_map.pop(0))
        else:
            end = disk_map.pop(len(disk_map)-1)
            if disk_map:
                disk_map[0] = end
    return new_map

def calculate_checksum(disk_map):
    return sum(map(lambda value: value[0] * value[1], enumerate(disk_map)))

if __name__ == "__main__":
    with open("input", "r") as file:
        input = list(file.read().strip())
        print(f"part 1: {calculate_checksum(defragment(decompress(input)))}")
        # print(defragment(decompress(input)))
        