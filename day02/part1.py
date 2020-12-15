# How many passwords are valid according to their policies?
# Format of each line of input: "<min>-<max> <char>: <password>"
# Password is valid if there are min to max appearances of char in it.

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

valid = 0
for l in lines:
    split1 = l.split("-")
    min = int(split1[0])
    split2 = split1[1].split(" ")
    max = int(split2[0])
    char = split2[1].split(":")[0]
    password = split2[2]

    if password.count(char) in range(min, max+1):
        valid += 1

print(valid)
