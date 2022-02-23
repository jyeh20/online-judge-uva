import sys

case = 1
for line in sys.stdin:
    og_start, limit = [int(x) for x in line.strip().split(' ')]
    if og_start == -1 and limit == -1:
        break

    steps = 0
    start = og_start
    while start <= limit:
        steps += 1
        if start == 1:
            break
        start = start / 2 if start % 2 == 0 else start * 3 + 1
    print("Case {}: A = {}, limit = {}, number of terms = {}".format(case, og_start, limit, steps))
    case += 1
