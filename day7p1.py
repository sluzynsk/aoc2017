# Advent of code
# day 7 puzzle 1
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>


def findBottom():
    fieldnames = ['program', 'size', 'haslinks', 'linksare']
    programs = {}
    with open('test.txt', 'rb') as f:
        for row in f:
            items = []
            splitRow = row.partition('->')
            for inner in splitRow[2].rsplit():
                items.append(inner.strip(','))
                programs[splitRow[0].rsplit()[0]]=items

    linked = []
    for program in programs:
        if programs[program]:
            linked.extend(programs[program])

    for program in programs:
        if program not in linked:
            print("the answer is ", program)


findBottom()
