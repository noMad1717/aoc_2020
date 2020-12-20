"""
    Advent of Code 2020 - Day 19
"""
import re
import util

def getExpression(rule, rules, regexes, exprList, isTopRule):
    if rule.startswith('"'):
        exprList.append(rule.replace('"', ''))
        return
    if isTopRule:
        exprList.append('^')
    else:
        exprList.append('(')
    alternatives = rule.split(' | ')
    for i, alt in enumerate(alternatives):
        if len(alternatives) > 1:
            exprList.append('(')
        for subRule in alt.split():
            getExpression(rules[int(subRule)], rules, regexes, exprList, False)
        if len(alternatives) > 1:
            if i < len(alternatives) - 1:
                exprList.append(')|')
            else:
                exprList.append(')')
    if isTopRule:
        exprList.append('$')
    else:
        exprList.append(')')

def parseRules(data):
    rules = {}
    regexes = {}
    for line in data:
        if line == '':
            break
        parts = line.split(': ')
        rules[int(parts[0])] = parts[1]
    exprList = []
    getExpression(rules[0], rules, regexes, exprList, True)
    ruleExpression = ''.join(exprList)
    return ruleExpression

def partOne(data):
    pattern = parseRules(data)
    startIndex = data.index('') + 1
    validMessages = 0
    for line in data[startIndex:]:
        if re.match(pattern, line):
            validMessages += 1
    return validMessages

puzzleInput = util.fileToStringList('input')

print(f'Part one: Found {partOne(puzzleInput)} valid messages!')

