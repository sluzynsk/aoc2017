# Advent of code
# day 4 puzzle 1
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

lines = list(open("test.txt"))

phrase = []
valid = True
count = 0
for line in lines:
    for index, val in enumerate(line.split()):
        print val
        if val not in phrase:
            phrase.append(val)
        else:
            print(val, " was a dupe")
            valid = False
        print phrase
    phrase = []
    if valid: count += 1
    valid = True
print count
