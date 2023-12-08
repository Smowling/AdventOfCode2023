from itertools import cycle
import re

with open("input.txt", "r") as input_file:
        lines = input_file.read().splitlines()
        directions = [0 if direction == "L" else 1 for direction in lines[0]]
        nodes = {label: (left, right) for line in lines[2:]
                 for label, left, right in [re.findall(r"\w+", line)]}

label = "AAA"

for step, direction in enumerate(cycle(directions)):
        if label == "ZZZ":
            break
        label = nodes[label][direction]

print(step)