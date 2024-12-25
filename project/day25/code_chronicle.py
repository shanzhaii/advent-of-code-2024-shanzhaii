def convert_char_to_height(lock_or_keys):
    return [
        [[lock_or_key[y][x] for y in range(len(lock_or_key))].count('#')
         for x in range(len(lock_or_key[0]))]
        for lock_or_key in lock_or_keys
    ]

def find_fitting_pairs(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            if all(map(lambda key_lock: key_lock[0] + key_lock[1] < 6, zip(key, lock))):
                count += 1
    return count

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        keys_and_locks = file.read().strip().split('\n\n')
        locks = [lock.split('\n')[1:]
            for lock in filter(lambda key_or_lock: key_or_lock.startswith('#'), keys_and_locks)
        ]
        keys = [keys.split('\n')[:-1]
            for keys in filter(lambda key_or_lock: key_or_lock.startswith('.'), keys_and_locks)
        ]
        locks = convert_char_to_height(locks)
        keys = convert_char_to_height(keys)
        print(f"part 1: {find_fitting_pairs(locks, keys)}")
