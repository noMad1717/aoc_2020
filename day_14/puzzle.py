"""
    Advent of Code 2020 - Day 14
"""
import util

def toBinaryArray(val, bitLen):
    binVal = bin(val)[2:].zfill(bitLen)
    binValArr = [c for c in binVal]
    return binValArr

def toDecimalInt(val):
    return int(''.join(val), 2)

def applyMask(mask, val):
    binValArr = toBinaryArray(val, 36)
    i = 0
    while i < 36:
        maskBit = mask[i]
        valBit = binValArr[i]
        if maskBit != 'X':
            if maskBit != valBit:
                valBit = maskBit
                binValArr[i] = valBit
        i += 1
    return toDecimalInt(binValArr)

def applyMask_v2(mask, addr):
    binValArr = toBinaryArray(addr, 36)
    maskXs = []
    i = 0
    while i < 36:
        maskBit = mask[i]
        valBit = binValArr[i]
        if maskBit == '1' and valBit == '0':
           binValArr[i] = '1' 
        elif maskBit == 'X':
            maskXs.append(i)
        i += 1
    floatingBits = len(maskXs)
    permutations = 2 ** floatingBits
    memAddrs = []
    j = 0
    while j < permutations:
        b = bin(j)[2:].zfill(len(maskXs))
        x = 0
        while x < len(maskXs):
            binValArr[maskXs[x]] = b[x]
            x += 1
        j += 1
        temp = ''.join(binValArr)
        memAddrs.append(toDecimalInt(binValArr))
        binValArr = [c for c in temp]
    return memAddrs

def executeInstruction(mem, mask, instruction):
    mask = mask.split(' = ')[1]
    inst = instruction.split(' = ')[0]
    val = int(instruction.split(' = ')[1])
    maskedVal = applyMask(mask, val)
    newInst = f'{inst} = {maskedVal}'
    exec(f'{newInst}')

def executeInstruction_v2(mem, mask, instruction):
    mask = mask.split(' = ')[1]
    inst = instruction.split(' = ')[0]
    val = int(instruction.split(' = ')[1])
    addr = int(inst.split('[')[1][:-1])
    maskedAddrs = applyMask_v2(mask, addr)
    for a in maskedAddrs:
        mem[a] = val

def runInit(mem, data):
    mask = ''
    for line in data:
        if line.startswith('mask = '):
            mask = line
        else:
            executeInstruction(mem, mask, line)

def runInit_v2(mem, data):
    mask = ''
    for line in data:
        if line.startswith('mask = '):
            mask = line
        else:
            executeInstruction_v2(mem, mask, line)

def partOne(data):
    mem = {}
    runInit(mem, data)
    return sum(mem.values())

def partTwo(data):
    mem = {}
    runInit_v2(mem, data)
    return sum(mem.values())

initData = util.fileToStringList('input')

print(f'Part one: Sum = {partOne(initData)}')
print(f'Part two: Sum = {partTwo(initData)}')

