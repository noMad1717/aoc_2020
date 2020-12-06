import unittest

from puzzle import collectGroups, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['abc\n',
            '\n',
            'a\n',
            'b\n',
            'c\n',
            '\n',
            'ab\n',
            'ac\n',
            '\n',
            'a\n',
            'a\n',
            'a\n',
            'a\n',
            '\n',
            'b']

    def testCollectGroups(self):
        expectedLen = 5
        expectedGroup = [{'a', 'b'}, {'a', 'c'}]
        groups = collectGroups(self.data)
        self.assertEqual(len(groups), expectedLen)
        self.assertEqual(groups[2], expectedGroup)

    def testPartOne(self):
        expected = 11
        result = partOne(self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 6
        result = partTwo(self.data)
        self.assertEqual(result, expected)

if __name__ == '__main()__':
    unittest.main()

