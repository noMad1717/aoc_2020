"""
    Advent of Code 2020 - Day 13
"""
import re
import math
import util

def parseInput(data):
    timeStamp = int(data[0])
    busIDs = parseBusIDs(data)
    return timeStamp, [x[0] for x in busIDs]

def parseBusIDs(data):
    ids = data[1].split(',')
    return [(int(x), ids.index(x)) for x in ids if re.match('\d', x)]

def findNearestDeparture(timeStamp, busIDs):
    foundBusID = departureTime = -1
    for busId in busIDs:
        dt = busId * math.ceil(timeStamp / busId)
        if departureTime < 0 or departureTime > dt:
            foundBusID = busId
            departureTime = dt
    return foundBusID, departureTime

def findDeparture(t, busIds, step):
    if not busIds:
        return t
    busId, offset = busIds[0]
    while True:
        if (t + offset) % busId == 0:
            return findDeparture(t, busIds[1:], step * busId)
        t += step

def partOne(data):
    timeStamp, busIDs = parseInput(data)
    busId, departureTime = findNearestDeparture(timeStamp, busIDs)
    diff = departureTime - timeStamp
    return busId * diff

def partTwo(data):
    busIDs = parseBusIDs(data)
    return findDeparture(busIDs[0][0], busIDs, 1)

notes = util.fileToStringList('input')

print(f'Part one: BusID * time to wait = {partOne(notes)}')
print(f'Part two: Earliest timestamp = {partTwo(notes)}')

