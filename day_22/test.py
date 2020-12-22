import unittest

from puzzle import splitDeck, playCombat, countScore


class TestPuzzle(unittest.TestCase):

    data = ['Player 1:',
            '9',
            '2',
            '6',
            '3',
            '1',
            '',
            'Player 2:',
            '5',
            '8',
            '4',
            '7',
            '10']

    def testSplitDeck(self):
        expectedOne = [9,2,6,3,1]
        expectedTwo = [5,8,4,7,10]
        resOne, resTwo = splitDeck(self.data)
        self.assertEqual(resOne, expectedOne)
        self.assertEqual(resTwo, expectedTwo)

    def testPlayCombat(self):
        expected = {'Player 2': [3,2,10,6,8,5,9,4,7,1]}
        playerOne, playerTwo = splitDeck(self.data)
        result = playCombat(playerOne, playerTwo, False)
        self.assertEqual(result, expected)

    def testPlayCombat_recursive(self):
        expected = {'Player 2': [7,5,6,2,4,1,10,8,9,3]}
        playerOne, playerTwo = splitDeck(self.data)
        result = playCombat(playerOne, playerTwo, True)
        self.assertEqual(result, expected)

    def testCountScore(self):
        expected = 306
        result = countScore([3,2,10,6,8,5,9,4,7,1])
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

