"""
    Advent of Code 2020 - Day 24
"""
import util

def parseDirections(data):
    directions = []
    for line in data:
        tileRow = []
        buf = ''
        for char in line:
            if buf == '' and (char == 'w' or char == 'e'):
                tileRow.append(char)
            elif buf == '' and (char == 'n' or char == 's'):
                buf = char
            else:
                tileRow.append(buf+char)
                buf = ''
        directions.append(tileRow)
    return directions

def e(qPos, rPos):
    return qPos + 1, rPos

def w(qPos, rPos):
    return qPos - 1, rPos

def ne(qPos, rPos):
    return qPos + 1, rPos - 1

def nw(qPos, rPos):
    return qPos, rPos - 1

def se(qPos, rPos):
    return qPos, rPos + 1

def sw(qPos, rPos):
    return qPos - 1, rPos + 1

def flipTiles(data):
    tiles = {}
    for tile in data:
        qPos = rPos = 0
        for direction in tile:
            qPos, rPos = eval(f'{direction}({qPos}, {rPos})')
        try:
            tiles[(qPos, rPos)] += 1
        except KeyError:
            tiles[(qPos, rPos)] = 1
    return tiles

def getAdjacents(tile):
    dirs = ['e', 'w', 'ne', 'nw', 'se', 'sw']
    adjacents = set()
    for d in dirs:
        adj = eval(f'{d}{tile}')
        adjacents.add(adj)
    return adjacents

def flip(blackTiles):
    nextBlack = set()
    for tile in blackTiles:
        adjBlackCount = 0
        adjWhites = set()
        for adj in getAdjacents(tile):
            if adj not in blackTiles:
                adjWhites.add(adj)
            else:
                adjBlackCount += 1
        if 0 < adjBlackCount and adjBlackCount < 3:
            nextBlack.add(tile)
        for whiteTile in adjWhites:
            bc = 0
            for adj in getAdjacents(whiteTile):
                if adj in blackTiles:
                    bc += 1
            if bc == 2:
                nextBlack.add(whiteTile)
    return nextBlack

def partOne(data):
    flippedTiles = flipTiles(parseDirections(data))
    blackTiles = [x for x in flippedTiles.values() if x % 2 != 0]
    return len(blackTiles)

def partTwo(data):
    flippedTiles = flipTiles(parseDirections(data))
    blackTiles = {x for x, y in flippedTiles.items() if y % 2 != 0}
    for i in range(1, 101):
        blackTiles = flip(blackTiles)
        if i % 10 == 0:
            print(f'({i}) - Black tiles: {len(blackTiles)}')
    return len(blackTiles)

floorTiles = util.fileToStringList('input')

print(f'Part one: Number of tiles left with black side up = {partOne(floorTiles)}')
print(f'Part two: Number of tiles with black side facing up after 100 days: {partTwo(floorTiles)}')

