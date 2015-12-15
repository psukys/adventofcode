encoded_characters = 0
original_characters = 0
rules = ['\\', '"']
with open('data/day8.txt') as f:
    for line in f:
        print line
        original_characters += len(line)
        for rule in rules:
            line = line.replace(rule, '\\' + rule)
        line = '"' + line + '"'
        encoded_characters += len(line)
        print line
        print '---'

print encoded_characters - original_characters
