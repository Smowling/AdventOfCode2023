with open("input.txt") as file:
    data = open("input.txt").readlines()

points = [(0, 0)]

directions = {
    "3": (-1,  0),
    "1": ( 1,  0),
    "2": ( 0, -1),
    "0": ( 0,  1)
}

# for pick's theorem
boundry = 0

for line in data:
    _, _, color = line.split()
    color = color[2:-1]
    dr, dc = directions[color[-1]]

    step = int(color[:-1], 16)

    boundry += step
    row, col = points[-1]
    # create list of points to use shoelace formula
    points.append((row + dr * step, col + dc * step))

sholace = abs(sum(points[i][0] * (points[i-1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) / 2

i = sholace - boundry // 2 + 1

print(boundry + i)