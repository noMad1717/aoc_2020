import unittest

from puzzle import parseAction, rotateShip, moveShip, executeAction, partOne, rotateWaypoint, executeWaypointAction, partTwo


class TestPuzzle(unittest.TestCase):

    def testParseAction(self):
        expectedOp = 'R'
        expectedAmount = 90
        resultOp, resultAmount = parseAction('R90')
        self.assertEqual(resultOp, expectedOp)
        self.assertEqual(resultAmount, expectedAmount)

    def testRotateShip_clockwise(self):
        expected = 180
        result = rotateShip(90, 'R', 90)
        self.assertEqual(result, expected)

    def testRotateShip_counterClockwise(self):
        expected = 90
        result = rotateShip(180, 'L', 90)
        self.assertEqual(result, expected)

    def testMoveShip_shouldIncrease(self):
        initialState = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        expected = {'N': 0, 'E': 10, 'S': 0, 'W': 0}
        moveShip(initialState, 'E', 10)
        self.assertEqual(initialState, expected)

    def testMoveShip_shouldDecrease(self):
        initialState = {'N': 0, 'E': 10, 'S': 0, 'W': 0}
        expected = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        moveShip(initialState, 'W', 10)
        self.assertEqual(initialState, expected)

    def testMoveShip_shouldDecreaseAndIncrease(self):
        initialState = {'N': 0, 'E': 10, 'S': 0, 'W': 0}
        expected = {'N': 0, 'E': 0, 'S': 0, 'W': 10}
        moveShip(initialState, 'W', 20)
        self.assertEqual(initialState, expected)

    def testExecuteAction(self):
        initialState = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        expectedPos = 90
        expectedState = {'N': 0, 'E': 10, 'S': 0, 'W': 0}
        resultDir = executeAction(initialState, 90, 'F10')
        self.assertEqual(initialState, expectedState)
        self.assertEqual(resultDir, expectedPos)

    def testPartOne(self):
        expected = 25
        actions = ['F10', 'N3', 'F7', 'R90', 'F11']
        result = partOne(actions)
        self.assertEqual(result, expected)

    def testRotateWaypoint_clockwise(self):
        initialState = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
        expected = {'N': 0, 'E': 1, 'S': 10, 'W': 0}
        rotateWaypoint(initialState, 'R', 90)
        self.assertEqual(initialState, expected)

    def testRotateWaypoint_counterClockWise(self):
        initialState = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
        expected = {'N': 10, 'E': 0, 'S': 0, 'W': 1}
        rotateWaypoint(initialState, 'L', 90)
        self.assertEqual(initialState, expected)

    def testExecuteWaypointAction(self):
        initWaypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
        initialState = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        expectedWaypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
        expectedState = {'N': 10, 'E': 100, 'S': 0, 'W': 0}
        executeWaypointAction(initialState, initWaypoint, 'F10')
        self.assertEqual(expectedWaypoint, initWaypoint)
        self.assertEqual(expectedState, initialState)

    def testPartTwo(self):
        expected = 286
        actions = ['F10', 'N3', 'F7', 'R90', 'F11']
        result = partTwo(actions)
        self.assertEqual(result, expected)

if __name__ == '__main()__':
    unittest.main()

