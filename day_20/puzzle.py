"""
    Advent of Code 2020 - Day 20
"""
import util

from functools import reduce


def parseInput(data):
    tiles = {}
    cur = ''
    tileRows = []
    data.append('')
    for line in data:
        if line == '':
            if cur != '' and len(tileRows) > 0:
                maxRow = len(tileRows) - 1
                maxCol = len(tileRows[0]) - 1
                borders = []
                borders.append(tileRows[0])
                borders.append(''.join([r[0] for r in tileRows]))
                borders.append(tileRows[-1])
                borders.append(''.join([r[-1] for r in tileRows]))
                tiles[cur] = borders
                cur = ''
                tileRows = []
            continue
        if line.startswith('Tile '):
            cur = line[5:-1]
            continue
        tileRows.append(line)
    return tiles

def findMatches(tiles):
    matches = {}
    for key, borders in tiles.items():
        m = set()
        for k, b in tiles.items():
            if key == k:
                continue
            try:
                if key in matches[k]:
                    m.add(k)
                    continue
            except KeyError:
                pass
            for border in borders:
                if border in b:
                    m.add(k)
                    continue
                else:
                    reverse = ''.join(reversed(border))
                    if reverse in b:
                        m.add(k)
                        continue
        matches[key] = m
    return matches

def findCornerTiles(tiles):
    corners = {int(x) for x in tiles.keys() if len(tiles[x]) == 2}
    return corners

def partOne(data):
    return reduce((lambda x,y: x*y), findCornerTiles(findMatches(parseInput(data))))

imageData = util.fileToStringList('input')

print(f'Part one: Product of corner tile IDs = {partOne(imageData)}')

