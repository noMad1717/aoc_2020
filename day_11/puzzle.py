"""
    Advent of Code 2020 - Day 11
"""
import util

def getFloorPoints(data):
    floor = set()
    i = 0
    while i < len(data):
        row = data[i]
        j = 0
        while j < len(row):
            if row[j] == '.':
                floor.add((i, j))
            j += 1
        i += 1
    return floor

def countAdjacentOccupied(cur, occupiedPoints, floorPoints, data):
    count = 0
    checkPoints = set([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    for point in checkPoints:
        check = (cur[0] + point[0], cur[1] + point[1])
        if check in occupiedPoints:
            count += 1
    return count

def getSeat(point, floorPoints, occupiedPoints, maxRow, maxCol):
    if point not in floorPoints:
        return '#' if point in occupiedPoints else 'L'

def getNextPoint(cur, point, i):
    yVal = cur[0] + point[0]
    xVal = cur[1] + point[1]
    if point[0] != 0:
        yVal = yVal + i if point[0] > 0 else yVal + -i
    if point[1] != 0:
        xVal = xVal + i if point[1] > 0 else xVal + -i
    return yVal, xVal

def countVisibleOccupied(cur, occupiedPoints, floorPoints, data):
    checkPoints = set([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    seats = dict.fromkeys(checkPoints, None)
    i = 0
    while len([x for x in seats.values() if x == None]) > 0:
        for point in checkPoints:
            if seats[point] != None:
                continue
            yVal, xVal = getNextPoint(cur, point, i)
            if yVal < 0 or xVal < 0 or yVal > len(data) - 1 or xVal > len(data[0]) - 1:
                seats[point] = 'OoB'
                continue
            seat = getSeat((yVal, xVal), floorPoints, occupiedPoints, len(data) - 1, len(data[0]) - 1)
            if seat != None:
                seats[point] = seat
        i += 1
    occupiedSeats = [x for x in seats.values() if x == '#']
    return len(occupiedSeats)

def runSimulation(data, floorPoints, occupiedPoints, maxOccupied, countOccupiedFunc):
    nextOccupied = set()
    i = 0
    while i < len(data):
        row = data[i]
        j = 0
        while j < len(row):
            cur = (i, j)
            if cur in floorPoints:
                j += 1
                continue
            elif cur in occupiedPoints:
                if countOccupiedFunc(cur, occupiedPoints, floorPoints, data) < maxOccupied:
                    nextOccupied.add(cur)
            else:
                if countOccupiedFunc(cur, occupiedPoints, floorPoints, data) == 0:
                    nextOccupied.add(cur)
            j += 1
        i += 1
    return nextOccupied

def run(data, countOccupiedFunc, maxOccupied):
    floorPoints = getFloorPoints(data)
    prev = cur = set()
    cur = runSimulation(data, floorPoints, cur, maxOccupied, countOccupiedFunc)
    while prev != cur:
        prev = cur
        cur = runSimulation(data, floorPoints, cur, maxOccupied, countOccupiedFunc)
    return len(cur)

def partOne(data):
    return run(data, countAdjacentOccupied, 4)

def partTwo(data):
    return run(data, countVisibleOccupied, 5)

seatData = util.fileToStringList('input')

print(f'Part one: {partOne(seatData)} occupied seats!')
print(f'Part two: {partTwo(seatData)} occupied seats!')

