# Count number of passports with all required fields (checking format)
import re

fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
                     (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.fullmatch(r"#[\da-f]{6}", x),
    "ecl": lambda x: x in ("amb","blu","brn","gry","grn","hzl","oth"),
    "pid": lambda x: re.fullmatch(r"\d{9}", x),
}

with open("input.txt", "r") as input:
    lines = input.read().split("\n\n")

valid = 0
for line in lines:
    passport = dict(l.split(":") for l in line.split())
    if not fields.keys() <= passport.keys(): #if not a subset
        continue

    valid_fields = [lamb(passport[field]) for field,lamb in fields.items()]
    if all(valid_fields):
        valid += 1

print(valid)
