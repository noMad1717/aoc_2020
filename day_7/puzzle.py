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

def countBags(search, dictionary):
    count = sum(dictionary[search].values())
    for key in dictionary[search].keys():
        amount = dictionary[search][key]
        count += amount * countBags(key, dictionary)
    return count

def partOne(data):
    bagDict = parseToDict(data)
    bag = 'shiny gold'
    bagSet = set()
    collectContainers(bag, bagDict, bagSet)
    return len(bagSet)

def partTwo(data):
    bagDict = parseToDict(data)
    bag = 'shiny gold'
    return countBags(bag, bagDict)

bagRules = util.fileToStringList('input')

print('Part one: %d possible outer bags!' % partOne(bagRules))
print('Part two: %d contained bags!' % partTwo(bagRules))

