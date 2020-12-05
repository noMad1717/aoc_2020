"""
    Advent of Code 2020 - Day 2
"""
import util

def parseRules(string):
    parts = string.split()
    boundsParts = parts[0].split("-")
    return [parts[1], boundsParts[0], boundsParts[1]]

def checkOccurrences(string, char, lowerBound, upperBound):
    occurrences = string.count(char)
    return occurrences >= lowerBound and occurrences <= upperBound

def checkPosition(string, char, firstIndex, lastIndex):
    firstMatches = string[firstIndex] == char
    secondMatches = string[lastIndex] == char
    return (firstMatches and not secondMatches) or (not firstMatches and secondMatches)

def partOne(passwords):
    matches = 0
    for pwd in passwords:
        parts = pwd.split(": ")
        password = parts[1].strip()
        rules = parseRules(parts[0])
        char = rules[0]
        lower = int(rules[1])
        upper = int(rules[2])
        result = checkOccurrences(password, char, lower, upper)
        if (result == True):
            matches = matches + 1
    return matches

def partTwo(passwords):
    matches = 0
    for pwd in passwords:
        parts = pwd.split(": ")
        password = parts[1].strip()
        rules = parseRules(parts[0])
        char = rules[0]
        lower = int(rules[1]) - 1
        upper = int(rules[2]) - 1
        result = checkPosition(password, char, lower, upper)
        if (result == True):
            matches = matches + 1
    return matches

pwds = util.fileToStringList('input')

print(str(partOne(pwds)) + " matches!")
print(str(partTwo(pwds)) + " matches!")

