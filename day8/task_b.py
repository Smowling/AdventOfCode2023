from itertools import cycle
from math import lcm
import re

with open("input.txt", "r") as input_file:
        lines = input_file.read().splitlines()
        directions = [0 if direction == "L" else 1 for direction in lines[0]]
        nodes = {label: (left, right) for line in lines[2:]
                 for label, left, right in [re.findall(r"\w+", line)]}

starting_labels = [label for label in nodes.keys() if label.endswith("A")]
steps = []

for label in starting_labels:
    for step, direction in enumerate(cycle(directions)):
        if label.endswith("Z"):
            steps.append(step)
            break
        label = nodes[label][direction]

print(lcm(*steps))