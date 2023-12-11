from itertools import combinations
grid = []


with open("input.txt") as file:
    for line in file.readlines():
        row = list(line.strip())
        grid.append(row)

        if "#" not in row:
            grid.append(row)

# Find the empty columns and insert them.
empty_columns = [x for x in range(len(grid[0])) if all(row[x] == "." for row in grid)]

for y in range(len(grid)):
    for i, x in enumerate(empty_columns):
        grid[y].insert(i + x, ".")


# Find the galaxies.
galaxies = []

for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == "#":
            galaxies.append((x, y))

pairs = list(combinations(galaxies, 2))

count = 0

for p1, p2 in pairs:
    # Manhattan distance (https://en.wikipedia.org/wiki/Taxicab_geometry)
    count += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print(count)