import unittest

from puzzle import findLoopSize, partOne


class TestPuzzle(unittest.TestCase):

    data = [5764801, 17807724]

    def testFindLoopSize(self):
        expected = {5764801: 8, 17807724: 11}
        result = findLoopSize(self.data)
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 14897079
        result = partOne(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

