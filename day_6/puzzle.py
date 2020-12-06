"""
    Advent of Code 2020 - Day 6
"""
import util

def collectGroups(data):
    groups = []
    group = []
    for line in data:
        if line == '\n':
            groups.append(group)
            group = []
            continue
        group.append({char for char in line.strip()})
    groups.append(group)
    return groups

def getSetUnionCounts(groups):
    return [len(set.union(*group)) for group in groups]

def getSetIntersectionCounts(groups):
    return [len(set.intersection(*group)) for group in groups]

def partOne(data):
    groups = collectGroups(data)
    return sum(getSetUnionCounts(groups))

def partTwo(data):
    groups = collectGroups(data)
    return sum(getSetIntersectionCounts(groups))

groupBatch = util.fileToStringListNoStrip('input')

print('Part one: Sum of counts = %d' % partOne(groupBatch))
print('Part two: Sum of counts = %d' % partTwo(groupBatch))

