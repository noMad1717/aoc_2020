"""
    Advent of Code 2020 - Day 15
"""
import util

def getNextNum(num, turn, prev):
    try:
        last = prev[num]
        return turn - last
    except KeyError:
        return 0

def runGame(data, stopIter):
    prev = {}
    for num in data:
        prev[num] = data.index(num) + 1
    cur = data[-1]
    turn = len(data)
    while True:
        nextNum = getNextNum(cur, turn, prev)
        prev[cur] = turn
        turn += 1
        cur = nextNum
        if turn == stopIter:
            return cur

def partOne(data):
    return runGame(data, 2020)

def partTwo(data):
    return runGame(data, 30000000)

print(f'Part one: Number spoken on turn 2020: {partOne([19, 20, 14, 0, 9, 1])}')
print(f'Part two: Number spoken on turn 30M: {partTwo([19, 20, 14, 0, 9, 1])}')

