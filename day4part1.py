import hashlib

with open('data/day4.txt') as f:
    data = f.read()

number = 1
md5_hash = hashlib.md5(data + str(number))
while md5_hash.hexdigest()[0:5] != '00000':
    number += 1
    print number
    md5_hash = hashlib.md5(data + str(number))

print 'Solution: {0}'.format(number)
