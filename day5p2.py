# Advent of code
# day 5 puzzle 2
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

lines = []
with open('test.txt') as f:
    for line in f:
        lines.append(int(line))

length = len(lines)

def calc(length):
    pc = 0
    jump = 0
    count = 0

    while pc < length:
        #print("pc ", pc, " count ", count)
        count += 1 # increment instruction counter
        #print lines
        jump = lines[pc] # how far to jump on this run
        if jump >= 3:
            lines[pc] -= 1
        else:
            lines[pc] += 1 # increment value at current position
        pc += jump # add value of current position to pc
    return count

print calc(length)
