import unittest

from puzzle import parseDirections, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['sesenwnenenewseeswwswswwnenewsewsw',
            'neeenesenwnwwswnenewnwwsewnenwseswesw',
            'seswneswswsenwwnwse',
            'nwnwneseeswswnenewneswwnewseswneseene',
            'swweswneswnenwsewnwneneseenw',
            'eesenwseswswnenwswnwnwsewwnwsene',
            'sewnenenenesenwsewnenwwwse',
            'wenwwweseeeweswwwnwwe',
            'wsweesenenewnwwnwsenewsenwwsesesenwne',
            'neeswseenwwswnwswswnw',
            'nenwswwsewswnenenewsenwsenwnesesenew',
            'enewnwewneswsewnwswenweswnenwsenwsw',
            'sweneswneswneneenwnewenewwneswswnese',
            'swwesenesewenwneswnwwneseswwne',
            'enesenwswwswneneswsenwnewswseenwsese',
            'wnwnesenesenenwwnenwsewesewsesesew',
            'nenewswnwewswnenesenwnesewesw',
            'eneswnwswnwsenenwnwnwwseeswneewsenese',
            'neswnwewnwnwseenwseesewsenwsweewe',
            'wseweeenwnesenwwwswnew']

    def testParseDirections(self):
        expected = ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w', 'se', 'w', 'sw']
        result = parseDirections(self.data)[0]
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 10
        result = partOne(self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 2208
        result = partTwo(self.data)
        self.assertEqual(result, expected)
    

if __name__ == '__main()__':
    unittest.main()

