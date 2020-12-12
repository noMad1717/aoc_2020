"""
    Advent of Code 2020 - Day 12
"""
import util

def parseAction(actionStr):
    op = actionStr[0]
    amount = int(actionStr[1:])
    return op, amount

def rotateShip(current, op, amount):
    if op == 'R': return (current + amount) % 360
    else: return (current - amount) % 360

def rotateWaypoint(current, op, amount):
    rotation = amount % 360
    if rotation > 0:
        vals = list(current.values())
        if rotation == 90: 
            current['N'] = vals[3] if op == 'R' else vals[1]
            current['E'] = vals[0] if op == 'R' else vals[2]
            current['S'] = vals[1] if op == 'R' else vals[3]
            current['W'] = vals[2] if op == 'R' else vals[0]
        elif rotation == 180:
            current['N'] = vals[2]
            current['E'] = vals[3]
            current['S'] = vals[0]
            current['W'] = vals[1]
        else:
            current['N'] = vals[1] if op == 'R' else vals[3]
            current['E'] = vals[2] if op == 'R' else vals[0]
            current['S'] = vals[3] if op == 'R' else vals[1]
            current['W'] = vals[0] if op == 'R' else vals[2]

def moveShip(currentState, op, amount):
    opposites = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    opposite = opposites[op]
    oppositePos = currentState[opposite]
    if oppositePos > 0 and oppositePos >= amount:
        currentState[opposite] -= amount
    elif oppositePos > 0 and oppositePos < amount:
        currentState[op] = amount - oppositePos
        currentState[opposite] = 0
    else:
        currentState[op] += amount

def executeAction(currentState, currentPos, action):
    op, amount = parseAction(action)
    if op == 'F':
        direction = directions[currentPos]
        moveShip(currentState, direction, amount)
    elif op == 'L' or op == 'R':
        return rotateShip(currentPos, op, amount)
    else:
        moveShip(currentState, op, amount)
    return currentPos

def executeWaypointAction(currentState, currentWaypoint, action):
    op, amount = parseAction(action)
    if op == 'F':
        i = 0
        northSouth = 'N' if currentWaypoint['N'] > 0 else 'S'
        eastWest = 'E' if currentWaypoint['E'] > 0 else 'W'
        while i < amount:
            moveShip(currentState, northSouth, currentWaypoint[northSouth])
            moveShip(currentState, eastWest, currentWaypoint[eastWest])
            i += 1
    elif op == 'L' or op == 'R':
        rotateWaypoint(currentWaypoint, op, amount)
    else:
        moveShip(currentWaypoint, op, amount)

def partOne(actions):
    state = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    facing = 90
    for action in actions:
        facing = executeAction(state, facing, action)
    return (max(state['N'], state['S']) + max(state['E'], state['W']))

def partTwo(actions):
    state = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    for action in actions:
        executeWaypointAction(state, waypoint, action)
    return (max(state['N'], state['S']) + max(state['E'], state['W']))

directions = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

actions = util.fileToStringList('input')

print(f'Part one: Manhattan distance = {partOne(actions)}')
print(f'Part two: Manhattan distance = {partTwo(actions)}')

