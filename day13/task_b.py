with open("input.txt") as file:
    data = file.read().split("\n\n")

def find_mirror(grid):
    for row in range(1, len(grid)):
        above = grid[:row][::-1] #up to current row and flip
        below = grid[row:]
        
        # for each row of zip (above and below)
        # for each pair of chars in that rows
        # +1 if not equal, than sum it all up
        # if 1 == 1 return row number
        if sum(sum(0 if chabove == chbelow else 1 for chabove, chbelow in zip(lineabove, linebelow)) for lineabove, linebelow in zip(above, below)) == 1:
            return row
    
    return 0
        

result = 0

for d in data:
    grid = d.splitlines()
    
    r = find_mirror(grid)
    result += r * 100
    
    # flip grid rotate 90deg
    c = find_mirror(list(zip(*grid)))
    result += c


print(result)