import unittest

from puzzle import getAdjacentSeats, runSimulation, countFinalOccupied


class TestPuzzle(unittest.TestCase):

    initialState = ['L.LL.LL.LL',
                    'LLLLLLL.LL',
                    'L.L.L..L..',
                    'LLLL.LL.LL',
                    'L.LL.LL.LL',
                    'L.LLLLL.LL',
                    '..L.L.....',
                    'LLLLLLLLLL',
                    'L.LLLLLL.L',
                    'L.LLLLL.LL']

    allOccupied = ['#.##.##.##',
                   '#######.##',
                   '#.#.#..#..',
                   '####.##.##',
                   '#.##.##.##',
                   '#.#####.##',
                   '..#.#.....',
                   '##########',
                   '#.######.#',
                   '#.#####.##']

    someOccupied = ['#.LL.L#.##',
                    '#LLLLLL.L#',
                    'L.L.L..L..',
                    '#LLL.LL.L#',
                    '#.LL.LL.LL',
                    '#.LLLL#.##',
                    '..L.L.....',
                    '#LLLLLLLL#',
                    '#.LLLLLL.L',
                    '#.#LLLL.##']

    def testcountFinalOccupied(self):
        expected = 37
        result = countFinalOccupied(self.initialState)
        self.assertEqual(result, expected)

    def testRunSimulation_first(self):
        expected = self.allOccupied
        result, o = runSimulation(self.initialState)
        self.assertEqual(result, expected)

    def testRunSimulation_second(self):
        expected = self.someOccupied
        result, o = runSimulation(self.allOccupied)
        self.assertEqual(result, expected)

    def testGetAdjacentSeats(self):
        expected = 0
        result = getAdjacentSeats(1, 1, self.initialState)
        self.assertEqual(result, expected)

    def testGetAdjacentSeats_topRow(self):
        expected = 0
        result = getAdjacentSeats(0, 0, self.initialState)
        self.assertEqual(result, expected)

    def testGetAdjacentSeats_bottomRow(self):
        expected = 0
        result = getAdjacentSeats(9, 0, self.initialState)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()
