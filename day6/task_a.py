with open("input.txt") as file:
    data = file.read().splitlines()

times, distances = [list(map(int, line.split(":")[1].split())) for line in data]

result = 1

for time, distance in zip(times, distances):
    margin = 0
    for speed in range(time):
        if speed * (time-speed) > distance:
            margin += 1
    result *= margin
    
print(result)