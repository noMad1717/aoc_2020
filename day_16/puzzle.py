"""
    Advent of Code 2020 - Day 16
"""
import re
import util

from functools import reduce


def parseNotes(data):
    notesDict = {}
    curKey = ''
    for line in data:
        if line == '':
            continue
        if re.match('^[a-z ]*:', line) and line[-1] != ':':
            parts = line.split(': ')
            ranges = set()
            for r in parts[1].split(' or '):
                ranges = ranges | parseToRange(r)
            notesDict[parts[0]] = ranges
        elif line[-1] == ':':
            curKey = line[:-1]
            notesDict[curKey] = []
        else:
            nums = [int(x) for x in line.split(',')]
            if curKey == 'nearby tickets':
                notesDict[curKey].append(nums)
            else:
                notesDict[curKey] = nums
    return notesDict

def parseToRange(rangeStr):
    parts = rangeStr.split('-')
    minVal = int(parts[0])
    maxVal = int(parts[1]) + 1
    l = [x for x in range(minVal, maxVal)]
    return set(l)

def findInvalidVals(notesDict):
    validNums = set()
    for key in notesDict.keys():
        if key != 'your ticket' and key != 'nearby tickets':
            validNums = validNums | notesDict[key]
    return [x for tickets in notesDict['nearby tickets'] for x in tickets if x not in validNums]

def findValidTickets(notesDict):
    invalidVals = findInvalidVals(notesDict)
    validTickets = []
    for ticket in notesDict['nearby tickets']:
        if not any(val in ticket for val in invalidVals):
            validTickets.append(ticket)
    return validTickets

def decipherTicket(notesDict):
    validTickets = findValidTickets(notesDict)
    keys = list([x for x in notesDict.keys() if x != 'your ticket' and x != 'nearby tickets'])
    decipheredTicket = dict.fromkeys(keys)
    for i in range(len(validTickets[0])):
        indexVals = [ticket[i] for ticket in validTickets]
        for key in notesDict.keys():
            if key != 'your ticket' and key != 'nearby tickets':
                if not decipheredTicket[key]:
                    decipheredTicket[key] = []
                if all(val in notesDict[key] for val in indexVals):
                    decipheredTicket[key].append(i)
    unique = set()
    while len(unique) < len(validTickets[0]):
        for key in decipheredTicket.keys():
            vals = decipheredTicket[key]
            if len(vals) == 1:
                unique.add(vals[0])
            else:
                for uq in unique:
                    if uq in vals: vals.remove(uq)
    return decipheredTicket

def partOne(data):
    parsedNotes = parseNotes(data)
    return sum(findInvalidVals(parsedNotes))

def partTwo(data):
    parsedNotes = parseNotes(data)
    ticketInfo = decipherTicket(parsedNotes)
    departureIndexes = set()
    for key in ticketInfo.keys():
        if key.startswith('departure'):
            departureIndexes.add(ticketInfo[key][0])
    departureVals = []
    for i in departureIndexes:
        departureVals.append(parsedNotes['your ticket'][i])
    res = reduce((lambda x, y: x * y), departureVals)
    return res

notes = util.fileToStringList('input')

print(f'Part one: Ticket scanning error rate: {partOne(notes)}')
print(f'Part two: Product of fields starting with departure: {partTwo(notes)}')

