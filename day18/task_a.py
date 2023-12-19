with open("input.txt") as file:
    data = open("input.txt").readlines()

points = [(0, 0)]

directions = {
    "U": (-1,  0),
    "D": ( 1,  0),
    "L": ( 0, -1),
    "R": ( 0,  1)
}

# for pick's theorem
boundry = 0

for line in data:
    direction, step, color = line.split()
    dr, dc = directions[direction]
    step = int(step)
    boundry += step
    row, col = points[-1]
    # create list of points to use shoelace formula
    points.append((row + dr * step, col + dc * step))

sholace = abs(sum(points[i][0] * (points[i-1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) / 2

i = sholace - boundry // 2 + 1

print(boundry + i)