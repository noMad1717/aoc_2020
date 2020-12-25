"""
    Advent of Code 2020 - Day 23
"""
import util

def playCups(moves, cups, isPartTwo):
    move = 1
    cupsLen = len(cups)
    current = cups[0]
    while move <= moves:
        currIndex = cups.index(current) + 1
        pickedUp = []
        while len(pickedUp) < 3:
            if currIndex > cupsLen - 1:
                currIndex = 0
            cup = cups[currIndex]
            pickedUp.append(cup)
            currIndex += 1
        for cup in pickedUp:
            cups.remove(cup)
        destinationCup = None
        while not destinationCup:
            cupNo = current - 1
            while not cupNo in cups:
                cupNo -= 1
                if cupNo < min(cups):
                    cupNo = max(cups)
            destinationCup = cups[cups.index(cupNo)]
        nextIndex = cups.index(destinationCup) + 1
        while len(pickedUp) > 0:
            cup = pickedUp[0]
            if nextIndex < cupsLen:
                cups.insert(nextIndex, cup)
                nextIndex += 1
            else:
                cups.insert(0, cup)
            pickedUp.remove(cup)
        if cups.index(current) == cupsLen - 1:
            current = cups[0]
        else:
            current = cups[cups.index(current) + 1]
        move += 1
    return cups

def partOne(data):
    cups = playCups(100, data, False)
    onesIndex = cups.index(1)
    cups = [str(x) for x in cups]
    right = cups[onesIndex + 1:]
    left = cups[:onesIndex]
    return ''.join(right + left)

def partTwo(data):
    cups = playCups(100, data, True)
    onesIndex = cups.index(1)
    nextIndex = onesIndex + 1
    nextCups = []
    while len(nextCups) < 2:
        if nextIndex > len(cups) - 1:
            nextIndex = 0
        nextCups.append(cups[nextIndex])
        nextIndex += 1
    return nextCups[0] * nextCups[1]

puzzleInput = [5,3,8,9,1,4,7,6,2]

print(f'Part one: Labels on the cups after "1": {partOne(puzzleInput)}')
#print(f'Part two: Product of cup labels immediately clockwise of "1": {partTwo(puzzleInput)}')

