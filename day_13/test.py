import unittest

from puzzle import parseInput, findNearestDeparture, parseBusIDs, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['939', '7,13,x,x,59,x,31,19']

    def testParseInput(self):
        expectedTimeStamp = 939
        expectedBusIDs = [7, 13, 59, 31, 19]
        timeStamp, busIDs = parseInput(self.data)
        self.assertEqual(timeStamp, expectedTimeStamp)
        self.assertEqual(busIDs, expectedBusIDs)

    def testFindNearestDeparture(self):
        expectedBusId = 59
        expectedDepartureTime = 944
        busId, departureTime = findNearestDeparture(939, [7, 13, 59, 31, 19])
        self.assertEqual(busId, expectedBusId)
        self.assertEqual(departureTime, expectedDepartureTime)

    def testParseBusIDs(self):
        expected = [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]
        result = parseBusIDs(self.data)
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 295
        result = partOne(self.data)
        self.assertEqual(result, expected)
    
    def testPartTwo(self):
        expected = 1068781
        result = partTwo(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

