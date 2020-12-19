import unittest

from puzzle import solveLeftToRight, solveAdditionFirst, solveParentheses, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
            '1 + (2 * 3) + (4 * (5 + 6))']

    def testSolveLeftToRight(self):
        expectedFirst = 26
        expectedSecond = 437
        expectedThird = 12240
        expectedFourth = 13632
        expectedFifth = 51
        resFirst = solveLeftToRight('2 * 3 + 20')
        resSecond = solveLeftToRight('5 + 432')
        resThird = solveLeftToRight('5 * 9 * 272')
        resFourth = solveLeftToRight('6810 + 2 + 4 * 2')
        resFifth = solveLeftToRight('1 + 6 + 44')
        self.assertEqual(resFirst, expectedFirst)
        self.assertEqual(resSecond, expectedSecond)
        self.assertEqual(resThird, expectedThird)
        self.assertEqual(resFourth, expectedFourth)
        self.assertEqual(resFifth, expectedFifth)

    def testSolveAdditionFirst(self):
        expectedFirst = 46
        expectedSecond = 1445
        expectedThird = 669060
        expectedFourth = 23340
        expectedFifth = 51
        resFirst = solveAdditionFirst('2 * 3 + 20')
        resSecond = solveAdditionFirst('5 + 1440')
        resThird = solveAdditionFirst('5 * 9 * 14868')
        resFourth = solveAdditionFirst('11664 + 2 + 4 * 2')
        resFifth = solveAdditionFirst('1 + 6 + 44')
        self.assertEqual(resFirst, expectedFirst)
        self.assertEqual(resSecond, expectedSecond)
        self.assertEqual(resThird, expectedThird)
        self.assertEqual(resFourth, expectedFourth)
        self.assertEqual(resFifth, expectedFifth)

    def testSolveParentheses(self):
        expectedFirst = '2 * 3 + 20'
        expectedSecond = '5 + 432'
        expectedThird = '5 * 9 * 272'
        expectedFourth = '6810 + 2 + 4 * 2'
        expectedFifth = '1 + 6 + 44'
        resFirst = solveParentheses(self.data[0], solveLeftToRight)
        resSecond = solveParentheses(self.data[1], solveLeftToRight)
        resThird = solveParentheses(self.data[2], solveLeftToRight)
        resFourth = solveParentheses(self.data[3], solveLeftToRight)
        resFifth = solveParentheses(self.data[4], solveLeftToRight)
        self.assertEqual(resFirst, expectedFirst)
        self.assertEqual(resSecond, expectedSecond)
        self.assertEqual(resThird, expectedThird)
        self.assertEqual(resFourth, expectedFourth)
        self.assertEqual(resFifth, expectedFifth)

    def testPartOne(self):
        expected = 26386
        result = partOne(self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 693942
        result = partTwo(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

