"""
    Advent of Code 2020 - Day 17
"""
import util

def findActiveCubes(data, z, *args):
    active = set()
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '#': 
                if not args: active.add((x,y,z))
                else: active.add((x,y,z,args[0]))
    return active

def countNeighbors(cur, activeCubes):
    noActiveNeighbors = 0
    for z in range(-1,2):
        for y in range(-1,2):
            for x in range(-1,2):
                point = (cur[0]+x, cur[1]+y, cur[2]+z)
                if point == cur:
                    continue
                if point in activeCubes:
                    noActiveNeighbors += 1
    return noActiveNeighbors

def countNeighborsHypercube(cur, activeCubes):
    noActiveNeighbors = 0
    for w in range(-1,2):
        for z in range(-1,2):
            for y in range(-1,2):
                for x in range(-1,2):
                    point = (cur[0]+x, cur[1]+y, cur[2]+z, cur[3]+w)
                    if point == cur:
                        continue
                    if point in activeCubes:
                        noActiveNeighbors += 1
    return noActiveNeighbors

def iterateCubes(minYX, maxYX, activeCubes, countNeighborsFunc, z, *args):
    nextActive = set()
    for y in range(minYX, maxYX + 1):
        for x in range(minYX, maxYX + 1):
            point = (x,y,z) if not args else (x,y,z,args[0])
            c = countNeighborsFunc(point, activeCubes)
            shouldStayActive = point in activeCubes and (c == 2 or c ==3)
            shouldBecomeActive = point not in activeCubes and c == 3
            if shouldStayActive or shouldBecomeActive:
                nextActive.add(point)
    return nextActive

def iterateSlice(minYX, maxYX, activeCubes, cycle):
    nextActive = set()
    minZ = cycle * -1
    maxZ = cycle
    for z in range(minZ, maxZ+1):
        nextActive = nextActive | iterateCubes(minYX, maxYX, activeCubes, countNeighbors, z)
    return nextActive

def iterateSliceHypercube(minYX, maxYX, activeCubes, cycle):
    nextActive = set()
    minZ = minW = cycle * -1
    maxZ = maxW = cycle
    for w in range(minW, maxW+1):
        for z in range(minZ, maxZ+1):
            nextActive = nextActive | iterateCubes(minYX, maxYX, activeCubes, countNeighborsHypercube, z, w)
    return nextActive

def partOne(data):
    cycle = 1
    activeCubes = findActiveCubes(data, 0)
    while cycle <= 6:
        minYX = cycle * -1
        maxYX = (len(data) - 1) + cycle
        activeCubes = iterateSlice(minYX, maxYX, activeCubes, cycle)
        cycle += 1
    return len(activeCubes)

def partTwo(data):
    cycle = 1
    activeHypercubes = findActiveCubes(data, 0, 0)
    while cycle <= 6:
        minYX = cycle * -1
        maxYX = (len(data) - 1) + cycle
        activeHypercubes = iterateSliceHypercube(minYX, maxYX, activeHypercubes, cycle)
        cycle += 1
    return len(activeHypercubes)

cubes = util.fileToStringList('input')

print(f'Part one: Cubes left in active state = {partOne(cubes)}')
print(f'Part two: Cubes left in active state = {partTwo(cubes)}')

