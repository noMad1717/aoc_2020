import unittest

from puzzle import findTreePos, computeTreePos, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#']

    def testFindTreePos(self):
        expected = [2, 3]
        treePos = findTreePos(self.data[0])
        self.assertEqual(treePos, expected)

    def testComputeTreePos_FindMatchWithoutRepetion(self):
        expected = True
        isTreePos = computeTreePos(2, [2, 3], len(self.data[0]))
        self.assertEqual(isTreePos, expected)

    def testComputeTreePos_FindMatchOnRepetition(self):
        expected = True
        isTreePos = computeTreePos(13, [2, 3], len(self.data[0]))
        self.assertEqual(isTreePos, expected)

    def testComputeTreePos_NoMatchWithoutRepetition(self):
        expected = False
        isTreePos = computeTreePos(0, [2, 3], len(self.data[0]))
        self.assertEqual(isTreePos, expected)

    def testComputeTreePos_NoMatchOnRepetition(self):
        expected = False
        isTreePos = computeTreePos(12, [2, 3], len(self.data[0]))
        self.assertEqual(isTreePos, expected)

    def testPartOne(self):
        expected = 7
        foundTrees = partOne(self.data)
        self.assertEqual(foundTrees, expected)

    def testPartTwo(self):
        expected = 336
        foundTrees = partTwo(self.data, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])
        self.assertEqual(foundTrees, expected)

if __name__ == '__main()__':
    unittest.main()

