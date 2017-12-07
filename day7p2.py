# Advent of code
# day 7 puzzle 2
#
# (C) 2017 Steve Luzynski <steve@luzynski.net>

from collections import defaultdict
import json

def tree(): return defaultdict(tree)


def findBottom():
    programs = tree()
    with open('example.txt', 'rb') as f:
        for row in f:
            children = []
            splitRow = row.partition('->')

            head = splitRow[0].split(' ')
            name = head[0]
            weight = head[1].strip('()\n')

            for inner in splitRow[2].rsplit():
                children.append(inner.strip(','))

            programs[name]['name'] = name
            programs[name]['weight'] = weight
            programs[name]['children'] = children

    print(json.dumps(programs))

# i have no idea where to go from here. or if here is even a valid place to be.
# i may revisit this later but right now i'm stuck.


findBottom()
