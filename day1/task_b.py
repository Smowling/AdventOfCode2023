import re


file = 'input.txt'

result = 0
num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open(file) as lines:
    for line in lines:
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        for idx, num in enumerate(numbers):
            if num in num_dict:
                numbers[idx] = num_dict[num]
        print(numbers)
        result += int(numbers[0] + numbers[-1])

print(result)


