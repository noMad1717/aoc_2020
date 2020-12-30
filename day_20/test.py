import util
import unittest

from puzzle import findCornerTiles, rotateImg, parseInput, findAdjacentTiles, addToGrid, buildImage, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = util.fileToStringList('testinput')
    data2 = ['#..',
             '..#',
             '.##']
    borders = {'top': 1, 'rgt': 2, 'btm': 3, 'lft': 4}

    def testFindAdjacentTiles(self):
        expected = {'top': '1427', 'lft': '1951', 'btm': None, 'rgt': '3079'}
        result = findAdjacentTiles(parseInput(self.data))['2311']
        self.assertEqual(result, expected)

    def testFindCornerTiles(self):
        expected = [1951, 1171, 2971, 3079]
        result = findCornerTiles(findAdjacentTiles(parseInput(self.data)))
        self.assertEqual(result, expected)

    def testRotateImg(self):
        expectedTiles = ['..#',
                         '#..',
                         '##.']
        expectedBorders = {'top': 4, 'rgt': 1, 'btm': 2, 'lft': 3}
        resTiles, resBorders = rotateImg(self.data2, self.borders)
        self.assertEqual(resTiles, expectedTiles)
        self.assertEqual(resBorders, expectedBorders)

    def testAddToGrid(self):
        expectedGrid = ['.#.#..#.',
                        '###....#',
                        '##.##.##',
                        '###.####',
                        '##.#....',
                        '...#####',
                        '....#..#',
                        '.####...']
        expectedGridTiles = {(0,0): '1951'}
        grid = []
        gridTiles = {}
        allTiles = parseInput(self.data)
        adjacents = findAdjacentTiles(allTiles)
        addToGrid('1951', 0, 0, allTiles, adjacents, grid, gridTiles)
        self.assertEqual(grid, expectedGrid)
        self.assertEqual(gridTiles, expectedGridTiles)

    def testAddToGrid_withExisting(self):
        expectedGrid = ['.#.#..#.##...#.#',
                        '###....#.#....#.',
                        '##.##.###.#.#..#',
                        '###.#####...#.##',
                        '##.#....#.##.###',
                        '...########.#...',
                        '....#..#...##..#',
                        '.####...#..#....']
        expectedGridTiles = {(0,0): '1951', (1,0): '2311'}
        grid = ['.#.#..#.',
                '###....#',
                '##.##.##',
                '###.####',
                '##.#....',
                '...#####',
                '....#..#',
                '.####...']
        gridTiles = {(0,0): '1951'}
        allTiles = parseInput(self.data)
        adjacents = findAdjacentTiles(allTiles)
        addToGrid('2311', 1, 0, allTiles, adjacents, grid, gridTiles)
        self.assertEqual(grid, expectedGrid)
        self.assertEqual(gridTiles, expectedGridTiles)

    def testBuildImage(self):
        expectedGrid = ['.#.#..#.##...#.##..#####',
                        '###....#.#....#..#......',
                        '##.##.###.#.#..######...',
                        '###.#####...#.#####.#..#',
                        '##.#....#.##.####...#.##',
                        '...########.#....#####.#',
                        '....#..#...##..#.#.###..',
                        '.####...#..#.....#......',
                        '#..#.##..#..###.#.##....',
                        '#.####..#.####.#.#.###..',
                        '###.#.#...#.######.#..##',
                        '#.####....##..########.#',
                        '##..##.#...#...#.#.#.#..',
                        '...#..#..#.#.##..###.###',
                        '.#.#....#.##.#...###.##.',
                        '###.#...#..#.##.######..',
                        '.#.#.###.##.##.#..#.##..',
                        '.####.###.#...###.#..#.#',
                        '..#.#..#..#.#.#.####.###',
                        '#..####...#.#.#.###.###.',
                        '#####..#####...###....##',
                        '#.##..#..#...#..####...#',
                        '.#.###..##..##..####.##.',
                        '...###...##...#...#..###']
        expectedGridTiles = {(0,0): '1951', (1,0): '2311', (2,0): '3079',
                             (0,1): '2729', (1,1): '1427', (2,1): '2473',
                             (0,2): '2971', (1,2): '1489', (2,2): '1171'}
        resGrid, resGridTiles = buildImage(parseInput(self.data))
        self.assertEqual(resGrid, expectedGrid)
        self.assertEqual(resGridTiles, expectedGridTiles)

    def testPartOne(self):
        expected = 20899048083289
        result = partOne(self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 273
        result = partTwo(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

