import re
from math import prod

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

with open("input.txt") as f:
    data = f.read().splitlines()

result = 0
for game, line in enumerate(data, start=1):
    rs = list(map(int, re.findall(r"(\d+) red", line)))
    gs = list(map(int, re.findall(r"(\d+) green", line)))
    bs = list(map(int, re.findall(r"(\d+) blue", line)))
    valid = not any([
        *filter(lambda x: x > RED_LIMIT, rs),
        *filter(lambda x: x > GREEN_LIMIT, gs),
        *filter(lambda x: x > BLUE_LIMIT, bs),
    ])
    result += prod([max(rs), max(gs), max(bs)])

print(f"result: {result}")
