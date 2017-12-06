# Advent of code
# day 2 puzzle 2
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

thisRow = []
sum = 0
with open('test.txt', 'rb') as f:
    for row in f:
        print row
        for index, val in enumerate(row.split()):
            thisRow.append(int(val))
        for num in thisRow:
            for num2 in thisRow:
                if num != num2:
                    if num % num2 == 0:
                        print(num, num2)
                        sum += num/num2
        thisRow = []

print sum
