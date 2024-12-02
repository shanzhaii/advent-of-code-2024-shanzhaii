import csv

def safe(input):
    safe = True
    precendant = input[0]
    difference = 0
    i = 1
    while (safe and i < len(input)):
        if (abs((input[i]-precendant)) > 3 or (input[i]-precendant == 0) or (difference > 0 and input[i]-precendant < 0) or (difference < 0 and input[i]-precendant > 0)):
            safe = False
        difference = input[i]-precendant
        precendant = input[i]
        i = i + 1
    return safe

def almost_safe(input):
    if safe(input):
        return True
    return any(map(safe, [[input[j] for j in range(len(input)) if i!=j] for i in range(len(input))]))
    

if __name__ == "__main__":
    with open("input", "r", newline='\n') as file:
        reports = csv.reader(file, delimiter=' ')
        print([almost_safe([int(value) for value in row]) for row in reports].count(True))
            