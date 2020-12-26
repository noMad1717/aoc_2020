"""
    Advent of Code 2020 - Day 25
"""
import util

def transform(val, subjectNo):
    return (val * subjectNo) % 20201227

def getEncryptionKey(val, subjectNo, loopSize):
    for i in range(0, loopSize):
        val = transform(val, subjectNo)
    return val

def findLoopSize(pubKeys):
    loopSizes = {}
    subjectNo = 7
    for key in pubKeys:
        ls = 0
        val = 1
        while val != key:
            val = transform(val, subjectNo)
            ls += 1
        loopSizes[key] = ls
    return loopSizes

def partOne(data):
    loopSizes = findLoopSize(data)
    pubKey = list(loopSizes.keys())[0]
    loopSize = list(loopSizes.values())[1]
    return getEncryptionKey(1, pubKey, loopSize)

pubKeys = util.fileToIntList('input')

print(f'Part one: Encryption key: {partOne(pubKeys)}')

