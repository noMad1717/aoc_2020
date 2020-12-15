import unittest

from puzzle import partOne, partTwo


class TestPuzzle(unittest.TestCase):

    initialState = ['L.LL.LL.LL',
                    'LLLLLLL.LL',
                    'L.L.L..L..',
                    'LLLL.LL.LL',
                    'L.LL.LL.LL',
                    'L.LLLLL.LL',
                    '..L.L.....',
                    'LLLLLLLLLL',
                    'L.LLLLLL.L',
                    'L.LLLLL.LL']

    def testPartOne(self):
        expected = 37
        result = partOne(self.initialState)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 26
        result = partTwo(self.initialState)
        self.assertEqual(result, expected)

if __name__ == '__main()__':
    unittest.main()
