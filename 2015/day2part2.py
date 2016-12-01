def calculate_ribbon(l, w, h):
    ribbon = l * w * h  # bow is equal to volume of a present
    half_perimeters = [l + w, w + h, l + h]
    # minimum half perimeter -> minimum perimeter
    ribbon += 2 * min(half_perimeters)
    return ribbon


ribbon = 0
with open('data/day2.txt') as f:
    for line in f:
        items = line.split('x')
        l = int(items[0])
        w = int(items[1])
        h = int(items[2])
        ribbon += calculate_ribbon(l, w, h)

print ribbon
