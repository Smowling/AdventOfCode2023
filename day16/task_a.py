from collections import deque

with open("input.txt") as file:
    grid = file.read().splitlines()


# row, col, deltarow, deltacol
a = [(0, -1, 0, 1)]
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
print(len(coords))