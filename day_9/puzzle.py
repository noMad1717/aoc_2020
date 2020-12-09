"""
    Advent of Code 2020 - Day 9
"""
import util

def trimHigherValues(val, nums):
    return [x for x in nums if x < val]

def hasPairSum(index, preambleSize, nums):
    precedingNums = nums[index - preambleSize:index]
    precedingNums = trimHigherValues(nums[index], precedingNums)
    found = False
    while not found and len(precedingNums) > 1:
        num = precedingNums[0]
        precedingNums = precedingNums[1:]
        match = [x for x in precedingNums if x != num and x + num == nums[index]]
        found = len(match) > 0
    return found

def findFirstWithoutPair(preambleSize, nums):
    index = preambleSize
    found = True
    while found:
        found = hasPairSum(index, preambleSize, nums)
        index += 1
    return nums[index - 1]

def findContiguousSet(val, nums):
    res = set()
    startIndex = 0
    setLen = 2
    s = 0
    while s != val:
        if s > val:
            setLen = 2
            s = 0
            startIndex += 1
        res = set(nums[startIndex:startIndex + setLen])
        s = sum(res)
        setLen += 1
    return res

def partOne(data):
    preambleSize = 25
    return findFirstWithoutPair(preambleSize, data)

def partTwo(val, data):
    contigSet = findContiguousSet(val, data)
    minVal = min(contigSet)
    maxVal = max(contigSet)
    return minVal + maxVal

numbers = util.fileToIntList('input')

print('Part one: First number with no matching pair: %d!' % partOne(numbers))
print('Part two: Sum of min and max: %d!' % partTwo(138879426, numbers))

