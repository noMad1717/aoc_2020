"""
    Advent of Code 2020 - Day 1
"""
import util

def partOne(report):
    for x in report:
        for y in report:
            if x + y == 2020:
               return '%d * %d = %d' % (x, y, x * y)

def partTwo(report):
    for x in report:
        for y in report:
            for z in report:
                if x + y + z == 2020:
                    return '%d * %d * %d = %d' % (x, y, z, x * y * z)

report = util.fileToIntList('input')

print(partOne(report))
print(partTwo(report))

