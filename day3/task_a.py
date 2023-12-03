import re

with open("input.txt") as file:
    data = file.read().splitlines()

def check_symbol(x, x2, y, data):
    grid = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0,1],
            [1, -1], [1, 0], [1, 1]]
    pos = range(x, x2)
    for p in pos:
        for xx, yy in grid:
            try:
                if not data[y+xx][p+yy].isdigit() and data[y+xx][p+yy] != '.':
                    return True
            except:
                pass
    return False

    
result = 0

for line_idx, line in enumerate(data):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        if check_symbol(*match.span(), line_idx, data):
            result += int(match.group())
    
print(result)

