def subtract(string1, string2):
    string3 = string1
    for char in string1:
        if char in string2: string3 = string3.replace(char, "")
    return string3

def common(strings):
    sets = [set(x) for x in strings] 
    return sets[0].intersection(*sets[1:])

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

suma = 0
for line in lines:
    digits = {'8': 'abcdefg', }
    possible5s = set()
    possible6s = set()
    for word in line.split(" | ")[0].split(): # for word in input side
        if   len(word) == 2: digits['1'] = "".join(sorted(word))
        elif len(word) == 3: digits['7'] = "".join(sorted(word))
        elif len(word) == 4: digits['4'] = "".join(sorted(word))
        elif len(word) == 5: possible5s.add("".join(sorted(word)))
        elif len(word) == 6: possible6s.add("".join(sorted(word)))

    a = subtract(digits['7'], digits['1'])
    d = common((subtract(digits['4'], digits['7']), set([subtract('abcdefg', s) for s in possible6s]))).pop()
    g = subtract("".join(common(possible5s)), a+d)
    digits['0'] = [s for s in possible6s if d not in s][0]
    possible6s.remove(digits['0'])
    digits['9'] = [s for s in possible6s if len(subtract(s, digits['1']))==4][0]
    possible6s.remove(digits['9'])
    digits['6'] = possible6s.pop()
    digits['3'] = [s for s in possible5s if len(subtract(s, digits['1']))==3][0]
    possible5s.remove(digits['3'])
    c = subtract("abcdefg", digits['6'])
    digits['2'] = [s for s in possible5s if c in s][0]
    possible5s.remove(digits['2'])
    digits['5'] = possible5s.pop()
    reversed = {value: key for key, value in digits.items()}
    
    suma += int("".join([reversed["".join(sorted(x))] for x in line.split(" | ")[1].split()]))

print(suma)