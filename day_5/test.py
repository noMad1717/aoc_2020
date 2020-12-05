import unittest

from puzzle import findMatch, computeSeatId


class TestPuzzle(unittest.TestCase):

    data = 'FBFBBFFRLR'

    def testFindRow(self):
        expected = 44
        codes = self.data[:7]
        arr = [*range(0, 128)]
        row = findMatch(codes, arr)
        self.assertEqual(row, expected)

    def testFindColumn(self):
        expected = 5
        codes = self.data[7:]
        arr = [*range(0, 8)]
        col = findMatch(codes, arr)
        self.assertEqual(col, expected)

    def testComputeSeatId(self):
        expected = 357
        result = computeSeatId(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

