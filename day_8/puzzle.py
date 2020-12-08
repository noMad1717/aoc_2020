"""
    Advent of Code 2020 - Day 8
"""
import util

def parseInstruction(inst):
    action = inst[:3]
    op = inst[4]
    val = int(inst[5:])
    return action, op, val

def executeInstruction(action, op, val, nextInst, acc):
    if action == 'nop':
        return acc, nextInst + 1
    elif action == 'jmp':
        nextInst = nextInst + val if op == '+' else nextInst - val
        return acc, nextInst
    else:
        acc = acc + val if op == '+' else acc - val
        return acc, nextInst + 1

def partOne(data):
    executed = []
    acc = 0
    nextInst = 0
    while nextInst not in executed:
        executed.append(nextInst)
        action, op, val = parseInstruction(data[nextInst])
        acc, nextInst = executeInstruction(action, op, val, nextInst, acc)
    return acc

def partTwo(data):
    executed = []
    acc = 0
    prevAcc = acc
    nextInst = 0
    prevInst = nextInst
    changed = False
    while nextInst < len(data):
        executed.append(nextInst)
        action, op, val = parseInstruction(data[nextInst])
        if action != 'acc' and changed == False:
            prevAcc = acc
            prevInst = nextInst
            action = 'nop' if action == 'jmp' else 'jmp'
            changed = True
        acc, nextInst = executeInstruction(action, op, val, nextInst, acc)
        if nextInst in executed:
            changed = False
            i = executed.index(prevInst)
            executed = executed[0:i]
            action, op, val = parseInstruction(data[prevInst])
            acc, nextInst = executeInstruction(action, op, val, prevInst, prevAcc)
    return acc

bootCode = util.fileToStringList('input')

print('Part one: Acc = %d!' % partOne(bootCode))
print('Part two: Acc = %d!' % partTwo(bootCode))

