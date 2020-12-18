import unittest

from puzzle import solveLeftToRight, solveParentheses, partOne


class TestPuzzle(unittest.TestCase):

    data = ['2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']

    def testSolveLeftToRight(self):
        expectedFirst = 26
        expectedSecond = 437
        expectedThird = 12240
        expectedFourth = 13632
        resFirst = solveLeftToRight('2 * 3 + 20')
        resSecond = solveLeftToRight('5 + 432')
        resThird = solveLeftToRight('5 * 9 * 272')
        resFourth = solveLeftToRight('6810 + 2 + 4 * 2')
        self.assertEqual(resFirst, expectedFirst)
        self.assertEqual(resSecond, expectedSecond)
        self.assertEqual(resThird, expectedThird)
        self.assertEqual(resFourth, expectedFourth)

    def testSolveParentheses(self):
        expectedFirst = '2 * 3 + 20'
        expectedSecond = '5 + 432'
        expectedThird = '5 * 9 * 272'
        expectedFourth = '6810 + 2 + 4 * 2'
        resFirst = solveParentheses(self.data[0])
        resSecond = solveParentheses(self.data[1])
        resThird = solveParentheses(self.data[2])
        resFourth = solveParentheses(self.data[3])
        self.assertEqual(resFirst, expectedFirst)
        self.assertEqual(resSecond, expectedSecond)
        self.assertEqual(resThird, expectedThird)
        self.assertEqual(resFourth, expectedFourth)

    def testPartOne(self):
        expected = 26335
        result = partOne(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

