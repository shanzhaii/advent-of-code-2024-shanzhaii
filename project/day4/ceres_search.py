import re

def generete_all_orders(rows):
    length = len(rows)
    return [
        rows, # Horizontal
        [[rows[y][x] for y in range(length)] for x in range(length)], # vertical
        [[rows[x][y] for x in range(i) for y in range(i) if ((x+y)==(i-1) and x < length and y < length)] for i in range(1, 2*length)],
        [[rows[length-y-1][x] for x in range(i) for y in range(i) if ((x+y)==(i-1) and x < length and y < length)] for i in range(1, 2*length)]
    ]

def find_xmas_or_samx(rows):
    return sum(map(lambda row: len(re.findall("XMAS", ''.join(row))) + len(re.findall("SAMX", ''.join(row))), rows))

def generate_all_crosses(rows):
    length = len(rows)
    return [
        [rows[y][x], rows[y][x+2], rows[y+1][x+1], rows[y+2][x], rows[y+2][x+2]]
        for x in range(length)
        for y in range(length)
        if (x+2 < length and y+2 < length)
    ]

def count_mas_crosses(crosses):
    return crosses.count('MMASS') + crosses.count('SSAMM') + crosses.count('MSAMS') + crosses.count('SMASM')

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        input = [list(row.strip()) for row in file.readlines()]
        print(f"part 1: {sum(map(find_xmas_or_samx, generete_all_orders(input)))}")
        print(f"part 2: {count_mas_crosses(list(map(''.join ,generate_all_crosses(input))))}")
