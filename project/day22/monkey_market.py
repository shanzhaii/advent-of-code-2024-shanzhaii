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

def calculate_prices_and_changes(secret_number, n):
    price = int(str(secret_number)[-1])
    prices = [price]
    changes = []
    last_price = price
    for _ in range(n):
        secret_number = calculate(secret_number)
        price = int(str(secret_number)[-1])
        prices.append(price)
        changes.append(price - last_price)
        last_price = price
    return prices, changes

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = list(map(lambda line: int(line.strip()), file.readlines()))
        # print(f"part 1: {sum(map(lambda secret_number: calculate_nth(secret_number, 2000), input))}")
        print(calculate_prices_and_changes(123, 10))
