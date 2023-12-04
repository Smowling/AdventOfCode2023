from collections import defaultdict

with open("input.txt") as file:
    data = file.read().splitlines()

result = 0


for line in data:
    card_res = 0
    d = defaultdict(int)
    card = line[line.find(':'):].split()
    for key in card:
        d[key] += 1
        
    for key in d:
        if d[key] == 2:
            if card_res == 0:
                card_res = 1
            else:
                card_res *= 2
    result += card_res

print(result)