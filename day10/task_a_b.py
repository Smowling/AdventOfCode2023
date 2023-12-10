
array = []
with open("input.txt") as file:
    for line in file.read().splitlines():
        array.append(line)

n, m = len(array), len(array[0])

def travel(pos): # neighbour function
    i, j = pos
    c = array[i][j]

    # SET S as apropriate PIPE shape, in this case | == S
    travelspots = {
        '|': [(i+1, j), (i-1, j)],
        'S': [(i+1, j), (i-1, j)],
        '-': [(i, j-1), (i, j+1)],
        'L': [(i-1, j), (i, j+1)],
        'J': [(i-1, j), (i, j-1)],
        '7': [(i+1, j), (i, j-1)],
        'F': [(i+1, j), (i, j+1)],
    }
    return [(i, j) for (i, j) in travelspots[c] if i >=0 and j >= 0 and i < n and j < m]

for i in range(n): # find starting position
    for j in range(m):
        if array[i][j] == 'S':
            start = (i,j)
            break

# BFS Part 1
data = [start]
dist = {start : 0}
while len(data) > 0:
    nextspot = data.pop(0)
    for s in travel(nextspot):
        if s not in dist:
            data.append(s)
            dist[s] = dist[nextspot] + 1
print('BFS :', max([d for _,d in dist.items()]))

## Part 2
size = 0
for i in range(n):
    for j in range(m):
        if (i,j) not in dist:
            counter = len([(i,l) for l in range(j) if (i,l) in dist and array[i][l] not in {'-','J','L'}]) # if your S is a -, J or L put it here too
            size += counter % 2


print('Size :', size)