"""
    Advent of Code 2020 - Day 3
"""
treeMap = []
with open('input') as inputFile:
    for line in inputFile:
        line.strip()
        treeMap.append(line)

def findTreePos(string):
    treePos = []
    for i in range(len(string)):
        if string[i] == "#":
            treePos.append(i)
    return treePos

def computeTreePos(col, treePos, rowLength):
    if col < rowLength:
        return col in treePos

    factor = int(col / rowLength)
    for pos in treePos:
        res = pos + factor * rowLength
        if res == col:
            return True
    return False

def countTrees(data, colIncrease, rowIncrease):
    matches = 0
    rowIndex = rowIncrease
    colIndex = colIncrease
    while rowIndex < len(data):
        row = data[rowIndex].strip()
        treePos = findTreePos(row)
        isTree = computeTreePos(colIndex, treePos, len(row))
        if isTree == True:
            matches = matches + 1
        rowIndex = rowIndex + rowIncrease
        colIndex = colIndex + colIncrease
    return matches

def partOne(data):
    rowIncrease = 1
    colIncrease = 3
    return countTrees(data, colIncrease, rowIncrease)

def partTwo(data, slopes):
    res = 1
    for slope in slopes:
        colIncrease = slope[0]
        rowIncrease = slope[1]
        foundTrees = countTrees(data, colIncrease, rowIncrease)
        res = res * foundTrees
    return res

print('Part one: Collided with %d trees!' % partOne(treeMap))
print('Part two: Collided with %d trees!' % partTwo(treeMap, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))

