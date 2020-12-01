import unittest

from puzzle import partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = [1721, 979, 366, 299, 675, 1456]

    def testPartOne(self):
        expected = '1721 * 299 = 514579'
        self.assertEqual(partOne(self.data), expected)

    def testPartTwo(self):
        expected = '979 * 366 * 675 = 241861950'
        self.assertEqual(partTwo(self.data), expected)

if __name__ == '__main()__':
    unittest.main()

