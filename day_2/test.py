import unittest

from puzzle import buildRegexp, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

    def testBuildRegexp(self):
        expected = 'a{1,3}'
        pattern = buildRegexp(self.data[0].split(":")[0])
        self.assertEqual(pattern, expected)

    def testPartOne(self):
        expected = 2
        matches = partOne(self.data)
        self.assertEqual(matches, expected)

if __name__ == '__main()__':
    unittest.main()

