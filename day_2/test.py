import unittest

from puzzle import parseRules, checkOccurrences, checkPosition, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

    def testCheckOccurrences(self):
        expected = [True, False, True]
        matches = []
        for x in self.data:
            parts = x.split(": ")
            rules = parseRules(parts[0])
            char = rules[0]
            lower = int(rules[1])
            upper = int(rules[2])
            matches.append(checkOccurrences(parts[1], char, lower, upper))
        self.assertEqual(matches, expected)

    def testCheckPosition(self):
        expected = [True, False, False]
        matches = []
        for x in self.data:
            parts = x.split(": ")
            rules = parseRules(parts[0])
            char = rules[0]
            lower = int(rules[1]) - 1
            upper = int(rules[2]) - 1
            matches.append(checkPosition(parts[1], char, lower, upper))
        self.assertEqual(matches, expected)

    def testPartOne(self):
        expected = 2
        matches = partOne(self.data)
        self.assertEqual(matches, expected)

    def testPartTwo(self):
        expected = 1
        matches = partTwo(self.data)
        self.assertEqual(matches, expected)

if __name__ == '__main()__':
    unittest.main()

