import re

grid = [[False for a in xrange(1000)] for b in xrange(1000)]


def turn(p1, p2, action):
    for i in range(int(p1[0]), int(p2[0]) + 1):
        for j in range(int(p1[1]), int(p2[1]) + 1):
            if action == 'on':
                grid[i][j] = True
            elif action == 'off':
                grid[i][j] = False
            elif action == 'toggle':
                grid[i][j] = not grid[i][j]
            else:
                print 'Uknown action!'

with open('data/day6.txt') as f:
    for line in f:
        coordinates_search = re.search('(\d+,\d+) through (\d+,\d+)', line)
        point1 = coordinates_search.group(1).split(',')
        point2 = coordinates_search.group(2).split(',')
        if 'turn on' in line:
            turn(point1, point2, 'on')
        elif 'turn off' in line:
            turn(point1, point2, 'off')
        elif 'toggle' in line:
            turn(point1, point2, 'toggle')

light_sum = 0
for row in grid:
    light_sum += sum(row)

print light_sum
