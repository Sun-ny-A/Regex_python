#REGEX


import re
with open('./user_records.txt') as f:
    data = f.readlines() 
    print(data)

group_pattern = re.compile('^([^Invalid\sdata|Record][A-z]+\s[A-z]+)\W*([0-9]{2})\W*([A-z]+\s[A-z]*)\W*$')

valid_records = 0 #always outside of loop
invalid_records = 0

for x in data:
    result = group_pattern.match(x)
    if result:
        valid_records += 1
        print(f'name: {result.group(1)}, age: {result.group(2)}, country: {result.group(3)}')
    else:
        invalid_records += 1
        print("invalid record")

print(f'There are {valid_records} valid records.')
print(f'There are {invalid_records} invalid records.')
        

    







