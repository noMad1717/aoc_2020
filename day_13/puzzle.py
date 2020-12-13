"""
    Advent of Code 2020 - Day 13
"""
import re
import math
import util

def parseInput(data):
    timeStamp = int(data[0])
    busIDs = [int(x) for x in data[1].split(',') if re.match('\d', x)]
    return timeStamp, busIDs

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

def partOne(data):
    timeStamp, busIDs = parseInput(data)
    busId, departureTime = findNearestDeparture(timeStamp, busIDs)
    diff = departureTime - timeStamp
    return busId * diff

notes = util.fileToStringList('input')

print(f'Part one: BusID * time to wait = {partOne(notes)}')

