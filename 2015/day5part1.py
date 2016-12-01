rule1 = lambda line: sum([line.count(char) for char in ['a', 'e', 'i', 'o', 'u']]) >= 3
rule2 = lambda line: any([char == line[i + 1] for i, char in enumerate(line) if i + 1 < len(line)])
rule3 = lambda line: not any([substr in line for substr in ['ab', 'cd', 'pq', 'xy']])

nice_count = 0

with open('data/day5.txt') as f:
    for line in f:
        if rule1(line) and rule2(line) and rule3(line):
            nice_count += 1

print nice_count
