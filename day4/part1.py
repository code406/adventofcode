# Count number of passports with all required fields
fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open("input.txt", "r") as input:
    lines = input.read().split("\n\n")

valid = 0
for line in lines:
    passport = dict(l.split(":") for l in line.split())
    if fields <= passport.keys(): #if is subset
        valid += 1

print(valid)
