# Counting only digits in the the part after "|",
# count the number of words with len 2,3,4,7

with open("input.txt", "r") as input:
    words = " ".join(l.split(" | ")[1] for l in input.read().splitlines()).split()

print(sum(len(list(filter(lambda x:len(x)==i, words))) for i in [2,3,4,7]))