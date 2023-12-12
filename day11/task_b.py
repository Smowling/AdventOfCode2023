with open("input.txt") as file:
    grid = file.read().splitlines()

void_rows = [r for r, row in enumerate(grid) if all( char == "." for char in row)]
void_cols = [c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)]

galaxies = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "#"]

result = 0
scale = 1_000_000

for i, (r1, c1) in enumerate(galaxies):
    for (r2, c2) in galaxies[:i]:
        for r in range(min(r1, r2), max(r1, r2)):
            result += scale if r in void_rows else 1
        for c in range(min(c1, c2), max(c1,c2)):
            result += scale if c in void_cols else 1

print(result)