#recursive solution instead of dp
def count_variants(line, nums):
    if line == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if "#" in line else 1
    
    value = 0

    if line[0] in ".?":
        value += count_variants(line[1:], nums)
    
    if line[0] in "#?":
        if nums[0] <= len(line) and "." not in line[:nums[0]] and (nums[0] == len(line) or line[nums[0]] != "#"):
            value += count_variants(line[nums[0] +1 :], nums[1:])
    return value

result = 0

with open("input.txt") as file:
    for l in file:
        line, nums = l.split()
        nums = tuple(map(int, nums.split(",")))
        result += count_variants(line, nums)


print(result)