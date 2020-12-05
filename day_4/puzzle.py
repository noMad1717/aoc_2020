"""
    Advent of Code 2020 - Day 4
"""
import re
import util

def separatePassports(data):
    passports = []
    passport = ''
    for line in data:
        if line == '\n':
            passports.append(passport)
            passport = ''
        passport += line
    passports.append(passport)
    return passports

def parseKeyVals(string):
    keyVals = []
    newlineParts = string.split('\n')
    for part in newlineParts:
        parts = part.split()
        for p in parts:
            keyVals.append(p)
    return keyVals

def containsRequiredKeys(keyVals, keyRules):
    keys = [kvp.split(':')[0] for kvp in keyVals]
    required = list(keyRules.keys())
    for rq in required:
        if rq not in keys:
            return False
    return True

def isValidField(keyVals, keyRules):
    if containsRequiredKeys(keyVals, keyRules):
        for kvp in keyVals:
            if not isValidPassportData(kvp, keyRules):
                return False
        return True
    return False

def collectValidPassports(passports, keyRules, func):
    validPassports = []
    for passport in passports:
        keyVals = parseKeyVals(passport)
        if func(keyVals, keyRules):
            validPassports.append([keyVals])
    return validPassports

def isValidFormat(val, rule):
    return re.match(rule, val)

def isWithinRange(val, minVal, maxVal):
    return val >= minVal and val <= maxVal

def isValidFormatAndRange(val, rules):
    rule = rules[0]
    minVal = rules[1]
    maxVal = rules[2]
    if isValidFormat(val, rule):
        return isWithinRange(int(val), int(minVal), int(maxVal))
    return False

def isValidHeight(val, rules):
    rule = rules[0]
    if isValidFormat(val, rule):
        unit = val[-2:]
        kr = rules[1]
        subRules = [int(r) for r in kr[unit]]
        length = int(val[:-2])
        return isWithinRange(length, subRules[0], subRules[1])
    return False

def isValidPassportData(kvp, kr):
    kvpParts = kvp.split(':')
    key = kvpParts[0]
    val = kvpParts[1]
    if key == 'cid':
        return True
    ruleSet = kr[key]
    if ruleSet:
        params = ruleSet[0]
        func = ruleSet[1]
        return func(val, params)
    return True

def partOne(passportBatch, kr):
    passports = separatePassports(passportBatch)
    return len(collectValidPassports(passports, kr, containsRequiredKeys))

def partTwo(passportBatch, kr):
    passports = separatePassports(passportBatch)
    valid = collectValidPassports(passports, kr, isValidField)
    return len(valid)

keyRules = {'byr': [['^\d{4}$', 1920, 2002], isValidFormatAndRange],
            'iyr': [['^\d{4}$', 2010, 2020], isValidFormatAndRange],
            'eyr': [['^\d{4}$', 2020, 2030], isValidFormatAndRange],
            'hgt': [['^\d{1,3}(cm|in)$', {'cm': [150, 193], 'in': [59, 76]}], isValidHeight],
            'hcl': ['^#[0-9a-f]{6}$', isValidFormat],
            'ecl': ['^(amb|blu|brn|gry|grn|hzl|oth)$', isValidFormat],
            'pid': ['^\d{9}$', isValidFormat]}

data = util.fileToStringListNoStrip('input')

print('Part one: Found %d valid passports!' % partOne(data, keyRules))
print('Part two: Found %d valid passports!' % partTwo(data, keyRules))

