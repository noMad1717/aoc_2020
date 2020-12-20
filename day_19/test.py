import unittest

from puzzle import parseRules


class TestPuzzle(unittest.TestCase):

    data = ['0: 4 1 5',
            '1: 2 3 | 3 2',
            '2: 4 4 | 5 5',
            '3: 4 5 | 5 4',
            '4: "a"',
            '5: "b"',
            '',
            'ababbb',
            'bababa',
            'abbbab',
            'aaabbb',
            'aaaabbb']

    def testParseRules(self):
        expected = '^a((((aa)|(bb))((ab)|(ba)))|(((ab)|(ba))((aa)|(bb))))b$'
        result = parseRules(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

