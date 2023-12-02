import re


file = 'in.txt'

result = 0

with open(file) as lines:
    for line in lines:
        num = re.findall(r'\d', line)
        result = result + int(num[0] + num[-1])

print(result)


