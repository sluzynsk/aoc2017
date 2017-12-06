# Advent of code
# day 6 puzzle 2
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

# faster test dataset
example = [0,2,7,0]

# real dataset
puzzledata = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

def optimizeBlocks(bank):
    length = len(bank)
    biggest = int(max(bank))
    index = bank.index(biggest)
    bank[index] = 0
    while biggest:
        index += 1
        if index == length: index = 0
        bank[index] += 1
        biggest -= 1
    return bank

previous_tries = []
count = 0
print(puzzledata)
while puzzledata not in previous_tries:
    previous_tries.append(list(puzzledata))
    puzzledata = optimizeBlocks(puzzledata)

# now we need to loop it again

previous_tries = []
print(puzzledata)
while puzzledata not in previous_tries:
    previous_tries.append(list(puzzledata))
    puzzledata = optimizeBlocks(puzzledata)
    count += 1

print count
