"""
    Advent of Code 2020 - Day 1
"""

report = []
with open('input') as inputFile:
    for line in inputFile:
        line.strip()
        report.append(int(line))

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

print(partOne(report))
print(partTwo(report))

