# recursive solution
# task_a solution works (slooooowly), requires optimalization
# best way is to do it with memorising already calculated values
# and check if we have solution for current problem before calculating it again

values_cache = {}

def count_variants(line, nums):
    if line == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if "#" in line else 1
    
    value_key = (line, nums)
    value = 0

    #check if value for current key was calculated already
    if value_key in values_cache:
        return values_cache[value_key]

    if line[0] in ".?":
        value += count_variants(line[1:], nums)
    
    if line[0] in "#?":
        if nums[0] <= len(line) and "." not in line[:nums[0]] and (nums[0] == len(line) or line[nums[0]] != "#"):
            value += count_variants(line[nums[0] +1 :], nums[1:])
    #store value
    values_cache[value_key] = value    

    return value

result = 0

with open("input.txt") as file:
    for l in file:
        line, nums = l.split()
        nums = tuple(map(int, nums.split(",")))

        line = "?".join([line] * 5)
        nums *= 5

        result += count_variants(line, nums)


print(result)