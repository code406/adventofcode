# Oxy: sweep, keeping number if bit is the most common in position
# CO2: sweep, keeping number if bit is the least common in position

with open("input.txt", "r") as input:
    nums = input.read().splitlines()

oxy, co2 = nums[:], nums[:]
for i in range (len(nums[0])):
    if len(oxy) != 1:
        ones = sum([int(oxy[j][i]) for j in range(len(oxy))])
        common = 1 if ones >= len(oxy)/2 else 0
        valid = [j for j in range(len(oxy)) if int(oxy[j][i]) == common]
        oxy = [n for idx, n in enumerate(oxy) if idx in valid]
    if len(co2) != 1:
        ones = sum([int(co2[j][i]) for j in range(len(co2))])
        common = 1 if ones >= len(co2)/2 else 0
        valid = [j for j in range(len(co2)) if int(co2[j][i]) != common]
        co2 = [n for idx, n in enumerate(co2) if idx in valid]
print(int(oxy[0], 2) * int(co2[0],2))