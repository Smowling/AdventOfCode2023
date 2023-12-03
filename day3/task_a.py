import re

with open("input.txt") as file:
    data = file.read().splitlines()

test = ['467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..']

def check_symbol(x, x2, y, data):
    grid = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0,1],
            [1, -1], [1, 0], [1, 1]]
    pos = range(x, x2)
    for p in pos:
        for xx, yy in grid:
            try:
                if not data[y+xx][p+yy].isdigit() and data[y+xx][p+yy] != '.':
                    print(f'{y+xx}, {p+yy}: {data[y+xx][p+yy]}')
                    return True
            except:
                pass
    return False

    
result = 0
line_n = 0

for line in data:
    matches = re.finditer(r'\d+', line)
    for match in matches:
        # print (f'{line_n} {match.span()} {match.group()}')
        if check_symbol(*match.span(), line_n, data):
            print(match.group())
            result += int(match.group())
    line_n += 1
    
print(result)

