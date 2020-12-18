import unittest

from puzzle import findActiveCubes, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['.#.',
            '..#',
            '###']

    def testFindActiveCubes(self):
        expected = set([(1,0,0), (2,1,0), (0,2,0), (1,2,0), (2,2,0)])
        result = findActiveCubes(self.data, 0)
        self.assertEqual(result, expected)

    def testFindActiveHypercubes(self):
        expected = set([(1,0,0,0), (2,1,0,0), (0,2,0,0), (1,2,0,0), (2,2,0,0)])
        result = findActiveCubes(self.data, 0, 0)
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 112
        result = partOne(self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 848
        result = partTwo(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

