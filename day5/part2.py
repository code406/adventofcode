# What is my seat? (the only empty one with +1 and -1 taken)
with open("input.txt", "r") as input:
    lines = input.read().splitlines()

taken = []
for l in lines:
    row = int(l[:-3].replace("B","1").replace("F","0"), 2)
    col = int(l[-3:].replace("R","1").replace("L","0"), 2)
    taken.append(row * 8 + col)

seats = [row * 8 + col for row in range(128) for col in range(8)]
empty = set(seats) - set(taken)
for seat in empty:
    if seat-1 in taken and seat+1 in taken:
        print(seat)
