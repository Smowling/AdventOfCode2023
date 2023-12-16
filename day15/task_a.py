def hash(s):
    value = 0

    for ch in s:
        value += ord(ch) # ord returns ascii value of char
        value *= 17      # ascii x 17
        value %= 256     # mod 256
    return value
# print(hash("HASH")) -> 52   

with open("input.txt") as file:
    data = file.read().split(",")

result = 0

for s in data:
    result += hash(s)

print(result)