"""
    Advent of Code 2020 - Day 5
"""
seatCodes = []
with open('input') as inputFile:
    for line in inputFile:
        seatCodes.append(line.strip())

def findMatch(codes, arr):
    for code in codes: 
        half = len(arr) // 2
        if code == 'F' or code == 'L':
            arr = arr[:half]
        else:
            arr = arr[half:]
    return arr[0]

def computeSeatId(codes):
    rows = [*range(0, 128)]
    cols = [*range(0, 8)]
    rowCodes = codes[:7]
    colCodes = codes[7:]
    row = findMatch(rowCodes, rows)
    col = findMatch(colCodes, cols)
    return row * 8 + col

def partOne(codesList):
    maxId = 0
    for code in codesList:
        seatId = computeSeatId(code)
        if seatId > maxId:
            maxId = seatId
    return maxId

def partTwo(codesList):
    seatIds = []
    for code in codesList:
        seatIds.append(computeSeatId(code))
    seatIds.sort()
    missingSeatId = [x for x in range(seatIds[0], 975, 1) if x not in seatIds]
    return missingSeatId[0]

print('Part one: Highest seat ID = %d' % partOne(seatCodes))
print('Part two: Missing seat ID = %d' % partTwo(seatCodes))

