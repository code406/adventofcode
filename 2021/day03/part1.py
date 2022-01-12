# Gamma: most common bit for each position of all numbers
# Epsilon: least common bit for each position of all numbers

with open("input.txt", "r") as input:
    nums = input.read().splitlines()

gamma = ""
for i in range (len(nums[0])):
    ones = sum([int(nums[j][i]) for j in range(len(nums))])
    if ones > len(nums)/2: gamma += "1"
    else: gamma += "0"
epsilon = gamma.replace("1","2").replace("0","1").replace("2","0")
print(int(gamma, 2) * int(epsilon,2))