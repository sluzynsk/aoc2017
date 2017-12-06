# Advent of code
# day 1
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

example1 = "1122" # expected output is 3
example2 = "1111" # expected output is 4
example3 = "1234" # expected output is 0
example4 = "91212129" # expected output is 9

with open('test.txt') as f:
    teststring = f.read().rstrip()


print ("length is ", len(teststring))
total = 0
for index in range(len(teststring)):
    if index == len(teststring) - 1:
        nextDigit = teststring[0]
    else:
        nextDigit = teststring[index+1]
    print("index ", index, " digit ", teststring[index], " nextDigit ", nextDigit)
    if teststring[index] == nextDigit:
        total += int(teststring[index])

print(total)
