"""
    Advent of Code 2020 - Day 23
"""
import util

def initCups(cupsList, isPartTwo):
    cups = {}
    maxLbl = max(cupsList) if not isPartTwo else 1000000
    for i, cup in enumerate(cupsList):
        if i == len(cupsList) - 1:
            lbl = cupsList[0] if not isPartTwo else max(cupsList) + 1
            cups[cup] = lbl
        else:
            cups[cup] = cupsList[i + 1]
    if isPartTwo:
        for i in range(max(cupsList) + 1, maxLbl + 1):
            if i == maxLbl:
                cups[i] = cupsList[0]
            else:
                cups[i] = i + 1
    return cups, cupsList[0], maxLbl

def pickUp(current, cups):
    pickedUp = []
    nextCup = current
    while len(pickedUp) < 3:
        pickedUp.append(cups[nextCup])
        nextCup = cups[nextCup]
    cups[current] = cups[nextCup]
    return pickedUp

def setDestination(current, cups, pickedUp, maxLbl):
    dst = current - 1
    if dst <= 0:
        dst = maxLbl
    while dst in pickedUp:
        dst -= 1
        if dst <= 0:
            dst = maxLbl
    return dst

def insertPickedUp(cups, pickedUp, dst):
    oldNext = cups[dst]
    for i, cup in enumerate(pickedUp):
        if i == 0:
            cups[dst] = cup
        elif i == 2:
            cups[cup] = oldNext

def playCups(moves, cupsList, isPartTwo):
    move = 1
    cups, current, maxLbl = initCups(cupsList, isPartTwo)
    while move <= moves:
        pickedUp = pickUp(current, cups)
        dst = setDestination(current, cups, pickedUp, maxLbl)
        insertPickedUp(cups, pickedUp, dst)
        current = cups[current]
        move += 1
    return cups

def partOne(data):
    cups = playCups(100, data, False)
    labels = []
    cur = cups[1]
    while cur != 1:
        labels.append(str(cur))
        cur = cups[cur]
    return ''.join(labels)

def partTwo(data):
    cups = playCups(10000000, data, True)
    firstCup = cups[1]
    secondCup = cups[firstCup]
    return firstCup * secondCup

puzzleInput = [5,3,8,9,1,4,7,6,2]

print(f'Part one: Labels on the cups after "1": {partOne(puzzleInput)}')
print(f'Part two: Product of cup labels immediately clockwise of "1": {partTwo(puzzleInput)}')

