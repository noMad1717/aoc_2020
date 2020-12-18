"""
    Advent of Code 2020 - Day 18
"""
import re
import util

def solveLeftToRight(expr):
    ops = [x for x in expr if x == '+' or x == '*']
    nums = re.split(' [\+\*] ', expr)
    lh = nums[0]
    for i, op in enumerate(ops):
        rh = nums[i+1]
        lh = eval(f'{lh}{op}{rh}')
    return int(lh)

def solveParentheses(expr):
    match = re.findall('\([\d \+\*]*\)', expr)
    if not match:
        return expr
    for m in match:
        expr = expr.replace(m, str(solveLeftToRight(m[1:-1])))
    return solveParentheses(expr)

def partOne(data):
    res = 0
    for line in data:
        res += solveLeftToRight(solveParentheses(line))
    return res

homework = util.fileToStringList('input')

print(f'Part one: Sum of all expressions = {partOne(homework)}')

