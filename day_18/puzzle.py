"""
    Advent of Code 2020 - Day 18
"""
import re
import util

from collections import deque

def solveLeftToRight(expr):
    ops = [x for x in expr if x == '+' or x == '*']
    nums = re.split(' [\+\*] ', expr)
    lh = nums[0]
    for i, op in enumerate(ops):
        rh = nums[i+1]
        lh = eval(f'{lh}{op}{rh}')
    return lh

def solveAdditionFirst(expr):
    parts = expr.split(' * ')
    for part in parts:
        expr = expr.replace(part, str(eval(part)))
    return eval(expr)

def solveParentheses(expr, solveFunc):
    match = re.findall('\([\d \+\*]*\)', expr)
    if not match:
        return expr
    for m in match:
        expr = expr.replace(m, str(solveFunc(m[1:-1])))
    return solveParentheses(expr, solveFunc)

def peek(stack):
    try:
        return stack[-1]
    except IndexError:
        return None

def shuntingYard(expr):
    opStack = deque()
    output = deque()
    expr = expr.replace('(', '( ')
    expr = expr.replace(')', ' )')
    expr = expr.split()
    for c in expr:
        if re.match('\d', c):
            output.append(c)
        elif c == '+' or c == '*':
            while len(opStack) > 0:
                topOp = peek(opStack)
                if topOp == '(' or (topOp == '*' and c == '+'):
                    break
                output.append(opStack.pop())
            opStack.append(c)
        elif c == '(':
            opStack.append(c)
        elif c == ')':
            while len(opStack) > 0:
                topOp = opStack.pop()
                if topOp == '(':
                    break
                output.append(topOp)
    while len(opStack) > 0:
        output.append(opStack.pop())
    return output

def evalShuntingYard(output):
    stack = deque()
    for token in output:
        if re.match('\d', token):
            stack.append(int(token))
        elif token == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(stack.pop() * stack.pop())
    return stack.pop()

def partOne(data):
    res = 0
    for line in data:
        res += solveLeftToRight(solveParentheses(line, solveLeftToRight))
    return res

def partTwo(data):
    res = 0
    for line in data:
        res += evalShuntingYard(shuntingYard(line))
    return res

homework = util.fileToStringList('input')

print(f'Part one: Sum of all expressions = {partOne(homework)}')
print(f'Part two: Sum of all expressions = {partTwo(homework)}')

