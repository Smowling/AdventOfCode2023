with open("input.txt") as file:
    lines = file.read().splitlines()

def extrapolate(data):
    values = []
    for i in range(len(data)-1):
        values.append(data[i+1] - data[i])
    
    if all(x== 0 for x in values):
        return data[-1]
    else:
        return data[-1] + extrapolate(values)
    
result = 0
for line in lines:
    data = [int(x) for x in line.split()]
    result += extrapolate(data)

print(result)