# Advent of code
# day 1 puzzle 2
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

example1 = "1212" # expected output is 6
example2 = "1221" # expected output is 0
example3 = "123425" # expected output is 4
example4 = "123123" # expected output is 12
example5 = "12131415" # expected output is 4

with open('test.txt') as f:
    teststring = f.read().rstrip()

#teststring = example5

print ("length is ", len(teststring))
total = 0
skipFactor = len(teststring) / 2
print ("skipFactor is ", skipFactor)
for index in range(len(teststring)):
    if index + skipFactor > len(teststring) - 1:
        nextDigit = teststring[index + skipFactor - len(teststring)]
    else:
        nextDigit = teststring[index + skipFactor]
    print("index ", index, " digit ", teststring[index], " nextDigit ", nextDigit)
    if teststring[index] == nextDigit:
        total += int(teststring[index])

print(total)
