
rule1 = lambda line: any([line[i: i + 2] in line.replace(line[i: i + 2], '-', 1) for i in xrange(len(line)) if i + 1 < len(line)])
rule2 = lambda line: any([char == line[i + 2] for i, char in enumerate(line) if i + 2 < len(line)])

nice_count = 0

with open('data/day5.txt') as f:
    for line in f:
        if rule1(line) and rule2(line):
            nice_count += 1

print nice_count
