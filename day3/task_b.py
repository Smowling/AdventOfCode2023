import re
from collections import defaultdict

star_dict = defaultdict(list)

with open("input.txt") as file:
    data = file.read().splitlines()


def check_symbol(x, x2, y, value, data):
    grid = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0,1],
            [1, -1], [1, 0], [1, 1]]
    pos = range(x, x2)
    for p in pos:
        for xx, yy in grid:
            try:
                if not data[y+xx][p+yy].isdigit() and data[y+xx][p+yy] != '.':
                    if data[y+xx][p+yy] == '*':
                        star_dict[f'{y+xx}:{p+yy}'].append(int(value))
                    return True
            except:
                pass
    return False

result = 0

for line_idx, line in enumerate(data):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        check_symbol(*match.span(), line_idx, match.group(), data)


for key in star_dict:
    if len(star_dict[key]) == 2:
        result += star_dict[key][0] * star_dict[key][1]

print(result)

