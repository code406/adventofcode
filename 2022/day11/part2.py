# Follow instructions from input. Results are no longer divided by 3. Find another way to keep numbers small.
# After 10000 rounds, find the two monkes with highest number of inspections ("Test") and multiply those two numbers
from dataclasses import dataclass

@dataclass
class Monke:
    id: int
    items: list[int]
    operation: str
    test_divider: int
    receiver_true: int
    receiver_false: int
    test_count: int = 0

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

# Create monkes
monkes = []
modulo = 1
for i in range(0, len(lines), 7):
    monke_id = int(lines[i].split()[1][:-1])
    starting_items = [int(x) for x in lines[i+1].replace(',','').split()[2:]]
    operation = lines[i+2].split('new = ')[1]
    test_divider = int(lines[i+3].split()[3])
    modulo *= test_divider
    receiver_true = int(lines[i+4].split()[5])
    receiver_false = int(lines[i+5].split()[5])
    monkes.append(Monke(monke_id, starting_items, operation, test_divider, receiver_true, receiver_false))

# Run 10000 rounds
for i in range(10000):
    for monke in monkes:
        for i in range(len(monke.items)):
            old = monke.items[i]
            # We can use mcm of all dividers to keep our numbers small without affecting any tests
            new = eval(monke.operation) % modulo
            receiver = monke.receiver_false if new % monke.test_divider else monke.receiver_true
            monkes[receiver].items.append(new)
            monke.test_count += 1
        monke.items = []
    
# Find two monkes with highest test count and multiply their test counts
monkes.sort(key=lambda x: x.test_count, reverse=True)
print(monkes[0].test_count * monkes[1].test_count)
