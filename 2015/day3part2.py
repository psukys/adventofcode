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
x_santa = 0
y_santa = 0
x_robo = 0
y_robo = 0
visits.append((x_santa, y_santa))
for i, char in enumerate(data):
    if i % 2 == 0:
        x_santa, y_santa = get_coordinates(char, x_santa, y_santa)
        visits.append((x_santa, y_santa))
    else:
        x_robo, y_robo = get_coordinates(char, x_robo, y_robo)
        visits.append((x_robo, y_robo))

print len(set(visits))
