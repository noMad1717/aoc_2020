import util
import unittest

from puzzle import parseInput, findMatches, findCornerTiles, partOne


class TestPuzzle(unittest.TestCase):

    data = util.fileToStringList('testinput')

    def testParseInput(self):
        expected = ['..##.#..#.', '.#####..#.', '..###..###', '...#.##..#']
        result = parseInput(self.data)['2311']
        self.assertEqual(result, expected)

    def testFindMatches(self):
        expected = set(['1951', '3079', '1427'])
        result = findMatches(parseInput(self.data))['2311']
        self.assertEqual(result, expected)

    def testFindCornerTiels(self):
        expected = set([1951, 3079, 2971, 1171])
        result = findCornerTiles(findMatches(parseInput(self.data)))
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 20899048083289
        result = partOne(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

