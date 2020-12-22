"""
    Advent of Code 2020 - Day 22
"""
import util

def splitDeck(data):
    hands = {}
    player = ''
    for line in data:
        if line == '':
            continue
        if line.startswith('Player'):
            player = line[:-1]
            hands[player] = []
        else:
            hands[player].append(int(line))
    return hands['Player 1'], hands['Player 2']

def countScore(cards):
    score = 0
    factor = len(cards)
    for card in cards:
        score += card * factor
        factor -= 1
    return score

def drawCards(playerOne, playerTwo):
    p1 = playerOne[0]
    playerOne.remove(p1)
    p2 = playerTwo[0]
    playerTwo.remove(p2)
    return p1, p2

def willBeInfinite(playerOne, playerTwo, prevDecks):
    for r, decks in prevDecks.items():
        prevP1 = decks[0]
        prevP2 = decks[1]
        if prevP1 == playerOne and prevP2 == playerTwo:
            return True
    return False

def determineWinner(p1, p2, playerOne, playerTwo):
    if p1 > p2:
        playerOne = playerOne + [p1,p2]
    else:
        playerTwo = playerTwo + [p2,p1]
    return playerOne, playerTwo

def playCombat(playerOne, playerTwo, isRecursiveCombat):
    playRound = 1
    prevDecks = {}
    while len(playerOne) > 0 and len(playerTwo) > 0:
        if isRecursiveCombat:
            if playRound > 1:
                if willBeInfinite(playerOne, playerTwo, prevDecks):
                    return {'Player 1': playerOne}
            prevDecks[playRound] = [[x for x in playerOne], [x for x in playerTwo]]
        p1, p2 = drawCards(playerOne, playerTwo)
        if isRecursiveCombat:
            if len(playerOne) >= p1 and len(playerTwo) >= p2:
                winner = playCombat([x for x in playerOne[:p1]], [x for x in playerTwo[:p2]], True)
                if list(winner.keys())[0] == 'Player 1':
                    playerOne = playerOne + [p1, p2]
                else:
                    playerTwo = playerTwo + [p2, p1]
            else:
                playerOne, playerTwo = determineWinner(p1, p2, playerOne, playerTwo)
        else:
            playerOne, playerTwo = determineWinner(p1, p2, playerOne, playerTwo)
        playRound += 1
    winner = {'Player 1': playerOne} if len(playerOne) > 0 else {'Player 2': playerTwo}
    return winner

def partOne(data):
    playerOne, playerTwo = splitDeck(data)
    winner = playCombat(playerOne, playerTwo, False)
    return countScore(list(winner.values())[0])

def partTwo(data):
    playerOne, playerTwo = splitDeck(data)
    winner = playCombat(playerOne, playerTwo, True)
    return countScore(list(winner.values())[0])

deck = util.fileToStringList('input')

print(f'Part one: Winning score is {partOne(deck)}!')
print(f'Part two: Winning score is {partTwo(deck)}!')

