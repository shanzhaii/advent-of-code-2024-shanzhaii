def flatten(list_of_list):
    return [elem for array in list_of_list for elem in array]


def decompress(compressed_disk_map):
    return flatten([[int(i / 2)] * int(length) if i % 2 == 0 else ['.'] * int(length)
                    for i, length in enumerate(compressed_disk_map)])


def defragment(uncompressed_disk_map):
    disk_map = [char for char in uncompressed_disk_map]
    new_map = []
    while disk_map:
        front = disk_map[0]
        if front != '.':
            new_map.append(disk_map.pop(0))
        else:
            end = disk_map.pop(len(disk_map) - 1)
            if disk_map:
                disk_map[0] = end
    return new_map


def calculate_checksum(disk_map):
    return sum(map(lambda value: value[0] * value[1] if value[1] != '.' else 0, enumerate(disk_map)))


def find_files_and_empty(compressed_disk_map):
    index_to_file = {}
    index_to_free_size = {}
    current_index = 0
    for i in range(len(compressed_disk_map)):
        size = int(compressed_disk_map[i])
        if i % 2 == 0:
            index_to_file[current_index] = (int(i/2), size)
        else:
            if size != 0:
                index_to_free_size[current_index] = size
        current_index = current_index + size
    return index_to_file, index_to_free_size

def block_defragment(index_to_file, index_to_free_size):
    new_index_to_file = {}
    for file_index in sorted(index_to_file.keys(), reverse=True):
        file_id, file_size = index_to_file[file_index]
        found_spot = False
        for free_index in sorted(filter(lambda key: key <= file_index, index_to_free_size.keys())):
            free_size = index_to_free_size[free_index]
            if free_size >= file_size:
                found_spot = True
                new_index_to_file[free_index] = (file_id, file_size)
                index_to_free_size.pop(free_index)
                if free_size - file_size > 0:
                    index_to_free_size[free_index + file_size] = free_size - file_size  # does not merge free blocks
                index_to_free_size[file_index] = file_size
                break
        if not found_spot:
            new_index_to_file[file_index] = (file_id, file_size)
    return new_index_to_file

def file_map_to_disk_map(index_to_file):
    disk_map = []
    i = 0
    for index in sorted(index_to_file.keys()):
        if index > i:
            disk_map.append(['.'] * (index - i))
        file_info = index_to_file[index]
        disk_map.append([file_info[0]] * file_info[1])
        i = index + file_info[1]
    return flatten(disk_map)


if __name__ == "__main__":
    with open("input", "r") as file:
        input = list(file.read().strip())
        print(f"part 1: {calculate_checksum(defragment(decompress(input)))}")

        files, free = find_files_and_empty(input)
        print(f"part 2: {calculate_checksum(file_map_to_disk_map(block_defragment(files, free)))}")
