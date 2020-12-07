"""
    Advent of Code 2020 - Day 7
"""
import util

def parseToDict(data):
    bagDict = dict()
    for line in data:
        parts = line.split(' bags contain ')
        key = parts[0]
        vals = parts[1]
        if vals == 'no other bags.':
            bagDict.update({key: dict()})
        else:
            bags = vals.split(',')
            valDict = dict()
            for bag in bags:
                p = bag.split()
                v = p[1] + ' ' + p[2]
                valDict.update({v: int(p[0])})
            bagDict.update({key: valDict})
    return bagDict

def collectContainers(search, dictionary, bagSet):
    for key in dictionary.keys():
        if search in dictionary[key].keys():
            bagSet.add(key)
            collectContainers(key, dictionary, bagSet)

def countContainedBags(search, dictionary):
    c = sum(dictionary[search].values())
    for key in dictionary[search].keys():
        amount = dictionary[search][key]
        c += amount * countContainedBags(key, dictionary)
    return c

def partOne(data):
    bagDict = parseToDict(data)
    s = 'shiny gold'
    bagSet = set()
    collectContainers(s, bagDict, bagSet)
    return len(bagSet)

def partTwo(data):
    bagDict = parseToDict(data)
    s = 'shiny gold'
    return countContainedBags(s, bagDict)

bagRules = util.fileToStringList('input')

print('Part one: %d possible outer bags!' % partOne(bagRules))
print('Part two: %d contained bags!' % partTwo(bagRules))

