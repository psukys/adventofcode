def calculate_surface(l, w, h):
    sides = [l * w, w * h, l * h]

    return 2 * sum(sides) + min(sides)


surface_sum = 0
with open('data/day2.txt') as f:
    for line in f:
        items = line.split('x')
        l = int(items[0])
        w = int(items[1])
        h = int(items[2])
        surface_sum += calculate_surface(l, w, h)

print surface_sum
