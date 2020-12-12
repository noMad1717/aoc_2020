"""
    Advent of Code 2020 - Day 11
"""
import util

def getSeatAtPos(row, col, seats):
    if row < 0 or row > len(seats) - 1 or col < 0 or col > len(seats[0]) - 1:
        return '.'
    return seats[row][col]

def getAdjacentSeats(row, col, seats):
    occupied = 0
    curRow = row - 1
    while curRow <= row + 1:
        curCol = col - 1
        while curCol <= col + 1:
            if curRow == row and curCol == col:
                curCol += 1
                continue
            seat = getSeatAtPos(curRow, curCol, seats)
            if seat == '#': occupied += 1
            curCol += 1
        curRow += 1
    return occupied

def runSimulation(seats):
    updatedSeats = []
    seatsOccupied = 0
    r = 0
    for row in seats:
        rowSeats = ''
        c = 0
        for col in row:
            if col == '.':
                rowSeats += col
                c += 1
                continue
            occupied = getAdjacentSeats(r, c, seats)
            if col == 'L':
                if occupied == 0: 
                    rowSeats += '#'
                    seatsOccupied += 1
                else: 
                    rowSeats += 'L'
            else:
                if occupied >= 4: 
                    rowSeats += 'L'
                else: 
                    rowSeats += '#'
                    seatsOccupied += 1
            c += 1
        r += 1
        updatedSeats.append(rowSeats)
    return updatedSeats, seatsOccupied
                
def countFinalOccupied(seats):
    prevRun = []
    curRun, occupiedSeats = runSimulation(seats)
    while prevRun != curRun:
        prevRun = curRun
        curRun, occupiedSeats = runSimulation(prevRun)
    return occupiedSeats

seatData = util.fileToStringList('input')

print(f'Part one: {countFinalOccupied(seatData)} occupied seats!')

