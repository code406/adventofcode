# jf. only works with prime numbers for buses, but they're always prime so ok
with open("input.txt", "r") as input:
    buses = [int(i) for i in input.read().splitlines()[1].replace("x","0").split(",")]

time = 0
step = 1
for i, bus in enumerate(buses):
    if bus==0: continue
    print(f"bus: {bus}, i: {i}, time: {time}, step: {step}")
    while (time+i)%bus:
        print(f"\t-> time: {time}, time+i: {time+i}")
        time += step
    print(f"\t-> time: {time}, time+i: {time+i} is mult of {bus}!")
    step *= bus
    if i!=len(buses)-1: print(f"\tstep*={bus}: {step*bus}")

print(time)
