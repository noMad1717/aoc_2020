"""
    Advent of Code 2020 - Day 19
"""
import regex
import util

def getExpression(rule, ruleId, rules, exprList, isTopRule):
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
            if subRule == ruleId:
                if subRule == '8':
                    exprList.append('(?<eight>(')
                    getExpression(rules[42], '42', rules, exprList, False)
                    exprList.append('|')
                    getExpression(rules[42], '42', rules, exprList, False)
                    exprList.append('(?&eight)))')
                elif subRule == '11':
                    exprList.append('(?<eleven>(')
                    getExpression(rules[42], '42', rules, exprList, False)
                    getExpression(rules[31], '31', rules, exprList, False)
                    exprList.append('|')
                    getExpression(rules[42], '42', rules, exprList, False)
                    exprList.append('(?&eleven)')
                    getExpression(rules[31], '31', rules, exprList, False)
                    exprList.append('))')
            else:
                getExpression(rules[int(subRule)], subRule, rules, exprList, False)
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
    for line in data:
        if line == '':
            break
        parts = line.split(': ')
        rules[int(parts[0])] = parts[1]
    exprList = []
    getExpression(rules[0], '0', rules, exprList, True)
    ruleExpression = ''.join(exprList)
    return ruleExpression

def partOne(data):
    pattern = parseRules(data)
    startIndex = data.index('') + 1
    validMessages = 0
    for line in data[startIndex:]:
        if regex.match(pattern, line):
            validMessages += 1
    return validMessages

def partTwo(data):
    data[data.index('8: 42')] = '8: 42 | 42 8'
    data[data.index('11: 42 31')] = '11: 42 31 | 42 11 31'
    pattern = parseRules(data)
    startIndex = data.index('') + 1
    validMessages = 0
    for line in data[startIndex:]:
        if regex.match(pattern, line):
            validMessages += 1
    return validMessages

puzzleInput = util.fileToStringList('input')

#print(f'Part one: Found {partOne(puzzleInput)} valid messages!')
print(f'Part two: Found {partTwo(puzzleInput)} valid messages!')

