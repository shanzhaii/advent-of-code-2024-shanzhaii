def mix(value, secret_number):
    return value ^ secret_number


def prune(secret_number):
    return secret_number % 16777216


def calculate(secret_number):
    secret_number = prune(mix(secret_number * 64, secret_number))
    secret_number = prune(mix(int(secret_number / 32), secret_number))
    return prune(mix(secret_number * 2048, secret_number))


def calculate_nth(secret_number, n):
    for _ in range(n):
        secret_number = calculate(secret_number)
    return secret_number


def calculate_sequence_to_price(secret_number, n, sequences):
    price = int(str(secret_number)[-1])
    changes = []
    last_price = price
    sequence_to_price = {}
    for _ in range(n):
        secret_number = calculate(secret_number)
        price = int(str(secret_number)[-1])
        changes.append(price - last_price)
        if len(changes) >= 4:
            sequence = (changes[-4], changes[-3], changes[-2], changes[-1])
            if sequence not in sequence_to_price:
                sequences.add(sequence)
                sequence_to_price[sequence] = price
        last_price = price
    return sequence_to_price


def find_best_sequence(input, n):
    all_sequences = set()
    sequence_to_prices = list(
        map(lambda secret_number: calculate_sequence_to_price(secret_number, n, all_sequences), input))
    max_bananas = 0
    for sequence in all_sequences:
        bananas = sum(map(lambda sequence_to_price: sequence_to_price.get(sequence, 0), sequence_to_prices))
        max_bananas = max(max_bananas, bananas)
    return max_bananas


if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = list(map(lambda line: int(line.strip()), file.readlines()))
        print(f"part 1: {sum(map(lambda secret_number: calculate_nth(secret_number, 2000), input))}")

        print(f"part 2: {find_best_sequence(input, 2000)}")
