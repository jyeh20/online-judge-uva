import sys

for line in sys.stdin:
    line = line.strip()
    if line == "0":
        break
    new_val = 0

    for index, digit in enumerate(line[::-1]):
        new_val += int(digit) * (2 ** (index + 1) - 1)
    print(new_val)
