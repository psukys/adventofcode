def get_coordinates(c, x, y):
    if c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    elif c == '<':
        x -= 1
    elif c == '>':
        x += 1

    return (x, y)

with open('data/day3.txt') as f:
    data = f.read()

visits = []
x = 0
y = 0
visits.append((x, y))
for char in data:
    x, y = get_coordinates(char, x, y)
    visits.append((x, y))

print len(set(visits))
