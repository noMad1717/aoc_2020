"""
    Advent of Code 2020 - Day 20
"""
import util

from functools import reduce


def parseInput(data):
    tiles = {}
    cur = ''
    for line in data:
        if line == '':
            continue
        if line.startswith('Tile '):
            cur = line[5:-1]
            tiles[cur] = []
            continue
        tiles[cur].append(line)
    return tiles

def flipVertical(tiles, borders):
    updatedBorders = {}
    if borders:
        updatedBorders = {'top': borders['btm'], 'rgt': borders['rgt'], 'btm': borders['top'], 'lft': borders['lft']}
    return [row for row in reversed(tiles)], updatedBorders

def flipHorizontal(tiles, borders):
    updatedBorders = {}
    if borders:
        updatedBorders = {'top': borders['top'], 'rgt': borders['lft'], 'btm': borders['btm'], 'lft': borders['rgt']}
    return [''.join(reversed(row)) for row in tiles], updatedBorders

def rotateImg(tiles, borders):
    rotated = []
    updatedBorders = {}
    maxCol = len(tiles[0])
    for i in range(0, maxCol):
        t = [row[i] for row in reversed(tiles)]
        rotated.append(''.join(t))
    updatedBorders = {}
    if borders:
        updatedBorders = {'top': borders['lft'], 'rgt': borders['top'], 'btm': borders['rgt'], 'lft': borders['btm']}
    return rotated, updatedBorders

def getBorders(tile):
    borders = {}
    borders['top'] = tile[0]
    borders['lft'] = ''.join([r[0] for r in tile])
    borders['btm'] = tile[-1]
    borders['rgt'] = ''.join([r[-1] for r in tile])
    return borders

def findAdjacentTiles(tiles):
    adjacents = {}
    for tId, pixels in tiles.items():
        tileBorders = {}
        borders = getBorders(pixels)
        for label, border in borders.items():
            tileBorders[label] = None
            for adjTileId, adjPixels in tiles.items():
                if adjTileId == tId:
                    continue
                adjBorders = getBorders(adjPixels)
                borderSet = set(list(adjBorders.values()))
                if border in borderSet or ''.join(reversed(border)) in borderSet:
                    tileBorders[label] = adjTileId
        adjacents[tId] = tileBorders
    return adjacents

def getTilesTopAndLeft(x, y, gridTiles):
    topId = gridTiles[(x,y-1)] if y-1 >= 0 else None
    leftId = gridTiles[(x-1,y)] if x-1 >= 0 else None
    return topId, leftId

def trimAndMerge(tiles, grid, y):
    gridRowLen = len(tiles[1:-1])
    gridLen = len(grid)
    actualLen = (gridLen // gridRowLen) - 1 if gridLen > 0 else 0
    for i, row in enumerate(tiles[1:-1]):
        if y > actualLen or gridLen == 0:
            grid.append(row[1:-1])
        else:
            actualRow = (y * gridRowLen) + i if actualLen > 0 else i
            grid[actualRow] = ''.join([grid[actualRow], row[1:-1]])

def addTileIdToGrid(tileId, x, y, gridTiles):
    gridTiles[(x,y)] = tileId

def updateBorders(borders):
    return borders['top'], borders['lft']

def addToGrid(tileId, x, y, tiles, adjacents, grid, gridTiles):
    topId, leftId = getTilesTopAndLeft(x, y, gridTiles)
    borders = adjacents[tileId]
    adjTop = borders['top']
    adjLeft = borders['lft']
    imgTiles = tiles[tileId]
    while not (adjTop == topId and adjLeft == leftId):
        if topId != leftId:
            if adjTop == topId:
                imgTiles, borders = flipHorizontal(imgTiles, borders)
                adjTop, adjLeft = updateBorders(borders)
            elif adjLeft == leftId:
                imgTiles, borders = flipVertical(imgTiles, borders)
                adjTop, adjLeft = updateBorders(borders)
            else:
                imgTiles, borders = rotateImg(imgTiles, borders)
                adjTop, adjLeft = updateBorders(borders)
        else:
            if adjTop == topId and adjLeft != adjTop:
                imgTiles, borders = flipHorizontal(imgTiles, borders)
                adjTop, adjLeft = updateBorders(borders)
            elif adjLeft == leftId and adjLeft != adjTop:
                imgTiles, borders = flipVertical(imgTiles, borders)
                adjTop, adjLeft = updateBorders(borders)
            else:
                imgTiles, borders = rotateImg(imgTiles, borders)
                adjTop, adjLeft = updateBorders(borders)
    adjacents[tileId] = borders
    trimAndMerge(imgTiles, grid, y)
    addTileIdToGrid(tileId, x, y, gridTiles)

def findCornerTiles(tiles):
    return [int(tId) for tId, borders in tiles.items() if len(list(filter((lambda x: x != None), borders.values()))) == 2]

def buildImage(tiles):
    adjacents = findAdjacentTiles(tiles)
    cornerTiles = findCornerTiles(adjacents)
    processed = set()
    x = y = 0
    grid = []
    gridTiles = {}
    prevTileId = currentTileId = None
    while len(processed) < len(tiles):
        if prevTileId == None:
            currentTileId = str(cornerTiles[0])
        else:
            rightAdj = adjacents[prevTileId]['rgt']
            if rightAdj != None:
                currentTileId = rightAdj
            else:
                bottomAdj = adjacents[gridTiles[(0,y)]]['btm']
                currentTileId = bottomAdj
                x = 0
                y += 1
        addToGrid(currentTileId, x, y, tiles, adjacents, grid, gridTiles)
        processed.add(currentTileId)
        prevTileId = currentTileId
        x += 1
    return grid, gridTiles

def scanGrid(grid, pattern):
    patternLen = len(pattern)
    patternRowLen = len(pattern[0])
    matches = 0
    y = 0
    while y + (patternLen - 1) < len(grid):
        found = False
        offset = 0
        while offset + patternRowLen < len(grid[y]):
            found = True
            for patternY, patternRow in enumerate(pattern):
                if not found:
                    break
                x = 0
                while x < patternRowLen:
                    if patternRow[x] == '#' and grid[y+patternY][x+offset] != '#':
                        found = False
                        break
                    x += 1
            if not found:
                offset += 1
            else:
                matches += 1
                break
        y += 1
    return matches

def findSeaMonster(grid):
    pattern = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']
    totalHashes = 0
    for row in grid:
        totalHashes += row.count('#')
    i = 0
    matches = 0
    while matches == 0 and i < 8:
        matches = scanGrid(grid, pattern)
        if matches == 0:
            grid, b = rotateImg(grid, None)
            if i == 3:
                grid, b = flipVertical(grid, None)
        i += 1
    return totalHashes - (matches * 15)

def partOne(data):
    return reduce((lambda x,y: x*y), findCornerTiles(findAdjacentTiles(parseInput(data))))

def partTwo(data):
    tiles = parseInput(data)
    grid, gridTiles = buildImage(tiles)
    return findSeaMonster(grid)

imageData = util.fileToStringList('input')

print(f'Part one: Product of corner tile IDs = {partOne(imageData)}')
print(f'Part two: Water roughness = {partTwo(imageData)}')

