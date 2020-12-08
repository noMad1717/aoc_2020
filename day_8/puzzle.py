"""
    Advent of Code 2020 - Day 8
"""
import util

def parseInstruction(inst):
    parts = inst.split()
    return parts[0], int(parts[1])

def executeInstruction(action, offset, nextInst, acc):
    if action == 'nop':
        return acc, nextInst + 1
    elif action == 'jmp':
        return acc, nextInst + offset
    else:
        return acc + offset, nextInst + 1

def partOne(data):
    executed = []
    acc = nextInst = 0
    while nextInst not in executed:
        executed.append(nextInst)
        action, offset = parseInstruction(data[nextInst])
        acc, nextInst = executeInstruction(action, offset, nextInst, acc)
    return acc

def partTwo(data):
    executed = []
    acc = prevAcc = nextInst = prevInst = 0
    changed = False
    while nextInst < len(data):
        executed.append(nextInst)
        action, offset = parseInstruction(data[nextInst])
        if action != 'acc' and changed == False:
            prevAcc, prevInst, changed = acc, nextInst, True
            action = 'nop' if action == 'jmp' else 'jmp'
        acc, nextInst = executeInstruction(action, offset, nextInst, acc)
        if nextInst in executed:
            changed = False
            executed = executed[0:executed.index(prevInst)]
            action, offset = parseInstruction(data[prevInst])
            acc, nextInst = executeInstruction(action, offset, prevInst, prevAcc)
    return acc

bootCode = util.fileToStringList('input')

print('Part one: Acc = %d!' % partOne(bootCode))
print('Part two: Acc = %d!' % partTwo(bootCode))

