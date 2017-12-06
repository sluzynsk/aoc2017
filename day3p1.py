# Advent of code
# day 3 puzzle 1
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

# this puzzle is twisted and made my head hurt

# example puzzle board
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

# 0,0 is the 1 square

from math import sqrt, floor, ceil

input = 289326

def side_length(number):
    side = ceil(sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side

side = side_length(input)
steps_to_center = (side-1)/2
axies = [side ** 2 - ((side-1)*i) - floor(side/2) for i in range(0,4)]
steps_to_side = min([abs(axis - input) for axis in axies])

print(steps_to_side + steps_to_center)
