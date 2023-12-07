from collections import Counter


with open("input.txt") as file:
    table = str.maketrans('AKQJT', 'EDCBA')
    data = tuple([(pair := line.split())[0].translate(table),
                  int(pair[1])] for line in file.readlines())


types = {key: [] for key in ['11111', '2111', '221', '311', '32', '41', '5']}
for hand in data:
    if 'B' in hand[0]:
      hand[0] = hand[0].replace('B', '1')
    wild = 0
    counts = Counter(hand[0])
    if '1' in counts and len(counts) > 1:
        wild = counts.pop('1')
    counts = sorted(counts.values(), reverse=True)
    counts[0] += wild
    current_type = ''.join(str(ch) for ch in counts)
    types[current_type].append(hand)
for key in types:
    types[key].sort()
winners = sum(types.values(), [])
result = sum(hand[1] * (idx + 1) for idx, hand in enumerate(winners))

print(result)