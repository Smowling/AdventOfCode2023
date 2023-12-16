def hash(s):
    value = 0

    for ch in s:
        value += ord(ch) # ord returns ascii value of char
        value *= 17      # ascii x 17
        value %= 256     # mod 256
    return value
# print(hash("HASH")) -> 52   

with open("input.txt") as file:
    data = file.read().split(",")

boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in data:
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)

        focal_lengths[label] = length

total = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(total)

