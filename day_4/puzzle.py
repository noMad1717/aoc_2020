"""
    Advent of Code 2020 - Day 4
"""
import re

data = []
with open('input') as inputFile:
    for line in inputFile:
        data.append(line)

def separatePassports(data):
    passports = []
    passport = ''
    for line in data:
        if line == '\n':
            passports.append(passport)
            passport = ''

        passport = passport + line

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

def checkValid(params):
    keyVals = params[0]
    required = params[1]
    keys = []
    for kvp in keyVals:
        keys.append(kvp.split(':')[0])

    for rq in required:
        if rq not in keys:
            return False
    return True

def checkValidKeyVal(params):
    if checkValid(params):
        keyVals = params[0]
        ruleSets = params[2]
        for kvp in keyVals:
            if not parseKeyRules(kvp, ruleSets):
                return False
        return True
    return False

def collectValidPassports(passports, params, func):
    validPassports = []
    for passport in passports:
        keyVals = parseKeyVals(passport)
        args = [keyVals] + params
        if func(args):
            validPassports.append([keyVals])
    return validPassports

def checkRule(val, rule):
    return re.match(rule, val)

def checkMinMax(val, minVal, maxVal):
    return val >= minVal and val <= maxVal

def checkRuleMinMax(val, rules):
    rule = rules[0]
    minVal = rules[1]
    maxVal = rules[2]
    if checkRule(val, rule):
        return checkMinMax(int(val), int(minVal), int(maxVal))
    return False

def checkHeight(val, rules):
    rule = rules[0]
    if checkRule(val, rule):
        unit = val[len(val) - 2:]
        kr = rules[1]
        subRules = kr[unit]
        return checkMinMax(int(val[:len(val) - 2]), int(subRules[0]), int(subRules[1]))
    return False

def parseKeyRules(kvp, kr):
    key = kvp.split(':')[0]
    val = kvp.split(':')[1]
    rs = [i for i in kr if i['key'] == key]
    if rs:
        ruleSet = rs[0]['val']
        params = ruleSet[0]
        func = ruleSet[1]
        return func(val, params)
    return True

def partOne(passportBatch, required):
    passports = separatePassports(passportBatch)
    return len(collectValidPassports(passports, [required], checkValid))

def partTwo(passportBatch, required, kr):
    passports = separatePassports(passportBatch)
    valid = collectValidPassports(passports, [required, kr], checkValidKeyVal)
    return len(valid)

requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
keyRules = [{'key': 'byr', 'val': [['^\d{4}$', 1920, 2002], checkRuleMinMax]},
            {'key': 'iyr', 'val': [['^\d{4}$', 2010, 2020], checkRuleMinMax]},
            {'key': 'eyr', 'val': [['^\d{4}$', 2020, 2030], checkRuleMinMax]},
            {'key': 'hgt', 'val': [['^\d{1,3}(cm|in)$', {'cm': [150, 193], 'in': [59, 76]}], checkHeight]},
            {'key': 'hcl', 'val': ['^#[0-9a-f]{6}$', checkRule]},
            {'key': 'ecl', 'val': ['^(amb|blu|brn|gry|grn|hzl|oth)$', checkRule]},
            {'key': 'pid', 'val': ['^\d{9}$', checkRule]}]

print('Part one: Found %d valid passports!' % partOne(data, requiredKeys))
print('Part two: Found %d valid passports!' % partTwo(data, requiredKeys, keyRules))

