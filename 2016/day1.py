directions = [0, 0, 0, 0]
direction = 0

with open('data/day1.txt') as f:
    data = f.read()

tokens = data.split(', ')
for token in tokens:
    letter = token[0]
    number = int(token[1:])
    if letter == 'L':
        direction -= 1
    else:
        direction += 1
    direction %= len(directions)
    directions[direction] += number

print(abs(directions[0] - directions[2]) + abs(directions[1] - directions[3]))