floor = 0
position = 0
with open('data/day1.txt') as f:
    data = f.read()
    for pos, char in enumerate(data):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if floor == -1:
            position = pos
            break

print position + 1  # enumerate gives indices starting from 0; part 2 indices start from 1
