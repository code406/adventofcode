# detect a start-of-packet marker in the datastream: 4 characters that are all different
# report the # of characters from the beginning of the buffer to the end of the first marker

LEN = 4

with open("input.txt", "r") as input:
    stream = input.read()

for i in range(0, len(stream)-LEN + 1):
    if len(set(stream[i:i+LEN])) == LEN:
        print(i+LEN)
        break
