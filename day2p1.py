# Advent of code
# day 2 puzzle 1
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

thisRow = []
sum = 0
with open('test.txt', 'rb') as f:
    for row in f:
        #print row
        for index, val in enumerate(row.split()):
            thisRow.append(int(val))
        highest = int(max(thisRow))
        lowest = int(min(thisRow))
        diff = highest - lowest
        sum += diff
        #print("highest ", highest, " lowest ", lowest, " diff ", diff, " sum ", sum)
        thisRow = []

print sum
