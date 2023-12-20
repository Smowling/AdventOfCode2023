with open("input.txt") as file:
    data1, data2 = open("input.txt").read().split("\n\n")


operation = {
    # a < b is the same as a.__lt__(b)
    # in this case its the same as int.__lt__(a,b)

    ">": int.__gt__,
    "<": int.__lt__
}

def process(item, workflow = "in"):
    if workflow == "R":
        return False
    if workflow == "A":
        return True
    
    flow, fallback = workflows[workflow]

    for key, symbol, num, target in flow:
        if operation[symbol](item[key], num):
            return process(item, target)
    
    return process(item, fallback)



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

result = 0

# process items
for line in data2.splitlines():
    item = {}
    for l in line[1:-1].split(","):
        category, value = l.split("=")
        item[category] = int(value)
    
    if process(item):
        result += sum(item.values())

print(result)