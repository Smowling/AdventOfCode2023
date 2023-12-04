from collections import defaultdict

#diff approach to get length of cards to copy

with open("input.txt") as file:
    data = file.read().splitlines()

num_of_cards = defaultdict(int)

for i, line in enumerate(data):
    num_of_cards[i] += 1
    left, right = line.split('|')
    _, cards = left.split(':')
    
    left_nums = [int(x) for x in cards.split()]
    right_nums = [int(x) for x in right.split()]
    
    rl_val = len(set(left_nums) & set(right_nums))
    
    for j in range(rl_val):
        num_of_cards[i+1+j] += num_of_cards[i]

print(sum(num_of_cards.values()))