from collections import deque

with open("input.txt") as file:
    grid = file.read().splitlines()


# row, col, deltarow, deltacol
def calculate(r, c, dr, dc):
    a = [(r, c, dr, dc)]
    seen = set()
    queue = deque(a)

    while queue:
        # row, col, deltarow, deltacol
        r, c, dr, dc = queue.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        ch = grid[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                queue.append((r, c, dr, dc))
        elif ch == "/":
            # right to up (0, 1) => (-1, 0)
            # down to left(1, 0) => (0, -1) 
            # up to right (-1, 0) => (0, 1)
            # left to down (0, -1) => (1, 0)
            # (dr, dc) => (-dc, -dr)
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                queue.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr # just a value swap
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                queue.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    queue.append((r, c, dr, dc))

    coords = {(r, c) for (r, c, _, _) in seen}
    return len(coords)

max_val = 0

for row in range(len(grid)):
    max_val = max(max_val, calculate(row, -1, 0, 1))
    max_val = max(max_val, calculate(row, len(grid[0]), 0, -1))

for col in range(len(grid)):
    max_val = max(max_val, calculate(-1, col, 1, 0))
    max_val = max(max_val, calculate(len(grid), col, -1, 0))

print(max_val)