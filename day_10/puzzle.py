"""
    Advent of Code 2020 - Day 10
"""
import util

def getSortedAdapters(startJolt, data):
    adapters = [startJolt] + data
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)
    return adapters

def countDifferences(startJolt, data):
    adapters = getSortedAdapters(startJolt, data)
    diffs = {1: 0, 2: 0, 3: 0}
    for x in adapters[:-1]:
        i = adapters.index(x)
        diff = adapters[i+1] - x
        diffs[diff] += 1
    return diffs

def countCombinations(startJolt, data):
    adapters = getSortedAdapters(startJolt, data)
    elems = {0:1}
    for x in adapters[1:]:
        paths = 0
        for y in adapters:
            if y >= x: break
            diff = x - y
            if diff <= 3:
                paths += elems[y]
        elems.update({x: paths})
    return elems[adapters[len(adapters) - 1]]

def partOne(data):
    diffs = countDifferences(0, data)
    return diffs[1] * diffs[3]

def partTwo(data):
    return countCombinations(0, data)

jolts = util.fileToIntList('input')

print(f'Part one: {partOne(jolts)}')
print(f'Part two: Number of combinations: {partTwo(jolts)}')

