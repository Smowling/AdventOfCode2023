with open("input.txt") as file:
    data = file.read().splitlines()
    #rotate grid to work on rows instead of cols
    grid = list(map("".join, zip(*data)))

    #split lines on #
    #sort each of those parts
    #join them again on #
    grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]

    #rotate again to origin orientation
    grid = list(map("".join, zip(*grid)))

#count amount of stones on each line times len-r
result = sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))
    
print(result)