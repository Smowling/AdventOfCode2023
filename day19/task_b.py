import sys
sys.setrecursionlimit(4000)

with open("input.txt") as file:
    data1, data2 = open("input.txt").read().split("\n\n")


workflows = {}
# process instructions
for line in data1.splitlines():
    name, instructions = line[:-1].split("{")
    instructions = instructions.split(",")
    workflows[name] = ([], instructions.pop())

    for instruction in instructions:
        comparsion, target = instruction.split(":")
        key = comparsion[0]
        symbol = comparsion[1]
        num = int(comparsion[2:])
        workflows[name][0].append((key, symbol, num, target))

def count(ranges, workflow = "in"):
    if workflow == "R":
        return 0

    if workflow == "A":
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1

    instructions, fallback = workflows[name]

    result = 0

    for key, _, num, target in instructions:
        low, high = ranges[key]
        if comparsion == "<":
            T = (low, num - 1)
            F = (num, high)
        else:
            T = (num +1, high)
            F = (low, num)

        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            result += count(copy, target)
        
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        
        else:
            break
    else:
        result += count(ranges, fallback)

    return result


print(count({key: (1, 4000) for key in "xmas"}))