import re


literal_characters = 0
memory_characters = 0
rules = [re.escape(r'\\'), re.escape(r'\"'), '\\\\x[a-f0-9]{2}']
print re.escape(rules[2])
with open('data/day8.txt') as f:
    for line in f:
        print(line)
        literal_characters += len(line)
        for rule in rules:
            line = re.sub(rule, '-', line)
        line = re.sub(r'^"(.+)"$', r'\1', line)
        memory_characters += len(line)
        print(line)
        print('---')

print literal_characters - memory_characters
