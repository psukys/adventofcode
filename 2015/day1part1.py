floor = 0
with open('data/day1.txt') as f:
    data = f.read()
    for char in data:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

print floor
