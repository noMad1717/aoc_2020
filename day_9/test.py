import unittest

from puzzle import trimHigherValues, hasPairSum, findFirstWithoutPair, findContiguousSet, partTwo


class TestPuzzle(unittest.TestCase):

    data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

    def testTrimHigherValues(self):
        expected = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117]
        result = trimHigherValues(127, self.data)
        self.assertEqual(expected, result)

    def testHasPairSum_shouldBeFalse(self):
        preambleSize = 5
        expected = False
        result = hasPairSum(14, preambleSize, self.data)
        self.assertEqual(result, expected)

    def testHasPairSum_shouldBeTrue(self):
        preambleSize = 5
        expected = True
        result = hasPairSum(5, preambleSize, self.data)
        self.assertEqual(result, expected)

    def testFindFirstWithoutPair(self):
        preambleSize = 5
        expected = 127
        result = findFirstWithoutPair(preambleSize, self.data)
        self.assertEqual(result, expected)

    def testFindContiguousSet(self):
        expected = set([15, 25, 47, 40])
        result = findContiguousSet(127, self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 62
        result = partTwo(127, self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

