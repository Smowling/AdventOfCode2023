with open("input.txt") as file:
    data = tuple(file.read().splitlines())

def roration():
    global data
    for _ in range(4):
        data = tuple(map("".join, zip(*data)))
        data = tuple("#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in data)
        data = tuple(row[::-1] for row in data)

seen = {data}
array = [data]

iteration = 0

while True:
    iteration += 1
    roration()
    if data in seen:
        break
    
    seen.add(data)
    array.append(data)

first = array.index(data)

data = array[(1_000_000_000 - first) % (iteration - first) + first]

#count amount of stones on each line times len-r
result = sum(row.count("O") * (len(data) - r) for r, row in enumerate(data))
    
print(result)