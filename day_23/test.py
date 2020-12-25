import unittest

from puzzle import partOne


class TestPuzzle(unittest.TestCase):

    data = [3,8,9,1,2,5,4,6,7]

    def testPartOne(self):
        expected = '67384529'
        result = partOne(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

