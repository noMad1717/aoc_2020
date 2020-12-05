"""
    Advent of Code 2020 - Day 5
"""
import util

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
    return max([computeSeatId(code) for code in codesList])

def partTwo(codesList):
    seatIds = [computeSeatId(code) for code in codesList]
    missingSeatId = [x for x in range(min(seatIds), max(seatIds)+1, 1) if x not in seatIds]
    return missingSeatId[0]

seatCodes = util.fileToStringList('input')

print('Part one: Highest seat ID = %d' % partOne(seatCodes))
print('Part two: Missing seat ID = %d' % partTwo(seatCodes))

