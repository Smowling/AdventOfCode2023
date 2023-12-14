with open("input.txt") as file:
    data = file.read().split("\n\n")

def find_mirror(grid):
    for row in range(1, len(grid)):
        above = grid[:row][::-1] #up to row and flip
        below = grid[row:]
        
        # cut grid length to the shortest one
        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return row
    
    return 0
        

result = 0

for d in data:
    grid = d.splitlines()
    r = find_mirror(grid)

    result += r * 100

    c = find_mirror(list(zip(*grid)))
    result += c


print(result)