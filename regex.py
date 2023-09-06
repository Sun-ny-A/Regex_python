#Week 3 HW 1 REGEX


import re
with open('./user_records.txt') as f:
    data = f.readlines() 
    print(data)

group_pattern = re.compile('^([^Invalid\sdata|Record][A-z]+\s[A-z]+)\W*([0-9]{2})\W*([A-z]+\s[A-z]*)\W*$')

for x in data:
    valid = 0
    invalid = 0
    result = group_pattern.match(x)
    if result:
        print(f'name: {result.group(1)}, age: {result.group(2)}, country: {result.group(3)}')
        valid += 1
    else:
        invalid += 1
        print("invalid record")
        

    







