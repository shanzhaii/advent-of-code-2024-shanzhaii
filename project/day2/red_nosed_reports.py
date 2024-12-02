import csv

def safe(input):
    safe = True
    precendant = input[0]
    difference = 0
    i = 1
    while (safe and i < len(input)):
        if (abs((input[i]-precendant)) > 3 or (input[i]-precendant == 0) or (difference * (input[i]-precendant) < 0)):
            return False, i
        difference = input[i]-precendant
        precendant = input[i]
        i = i + 1
    return safe, -1

def almost_safe(input):
    is_safe, error_at = safe(input)
    if is_safe:
        return True
    if error_at == 2:
        popped = list(input)
        popped.pop(0)
        if safe(popped)[0]:
            return True

    popped1 = list(input)
    popped1.pop(error_at)
    popped2 = list(input)
    popped2.pop(error_at-1)

    return safe(popped1)[0] or safe(popped2)[0]

    

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        reports = file.readlines()
        print(f"part 1: {[safe([int(value) for value in row.split()])[0] for row in reports].count(True)}")
        print(f"part 2: {[almost_safe([int(value) for value in row.split()]) for row in reports].count(True)}")
            