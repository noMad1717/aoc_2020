import unittest

from puzzle import countDifferences, countPermutations, partOne


class TestPuzzle(unittest.TestCase):

    data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    data2 = [28,
             33,
             18,
             42,
             31,
             14,
             46,
             20,
             48,
             47,
             24,
             23,
             49,
             45,
             19,
             38,
             39,
             11,
             1,
             32,
             25,
             35,
             8,
             17,
             7,
             9,
             4,
             2,
             34,
             10,
             3]

    def testCountDifferences(self):
        expected = {1: 7, 2: 0, 3: 5}
        result = countDifferences(0, self.data)
        self.assertEqual(result, expected)

    def testCountPermutations(self):
        expected = 8
        result = countPermutations(0, self.data)
        self.assertEqual(result, expected)

    def testCountPermutations_2(self):
        expected = 19208
        result = countPermutations(0, self.data2)
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 35
        result = partOne(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()
