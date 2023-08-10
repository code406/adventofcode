# detect a start-of-message marker in the datastream: 14 characters that are all different
# report the # of characters from the beginning of the buffer to the end of the first marker

LEN = 14

with open("input.txt", "r") as input:
    stream = input.read()

for i in range(0, len(stream)-LEN + 1):
    if len(set(stream[i:i+LEN])) == LEN:
        print(i+LEN)
        break
