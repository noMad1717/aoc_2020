"""
    Advent of Code 2020 - Day 2
"""
import re

def buildRegexp(val):
    parts = val.split()
    return '%s{%s}' % (parts[1], parts[0].replace("-", ","))

def partOne(passwords):
    print(passwords)
    matches = 0
    for pwd in passwords:
        parts = pwd.split(": ")
        pattern = buildRegexp(parts[0])
        print(pattern + ", " + parts[1])
        result = re.match(pattern, parts[1])
        if result != None:
            print('Match!')
            matches = matches + 1
    return matches

def partTwo(passwords):
    print('hello2')

