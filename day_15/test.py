import unittest

from puzzle import partOne, partTwo


class TestPuzzle(unittest.TestCase):

    def testPartOne(self):
        firstExpected = 436
        firstData = [0, 3, 6]

        secondExpected = 1
        secondData = [1, 3, 2]

        thirdExpected = 10
        thirdData = [2, 1, 3]

        fourthExpected = 27
        fourthData = [1, 2, 3]

        fifthExpected = 78
        fifthData = [2, 3, 1]

        sixthExpected = 438
        sixthData = [3, 2, 1]

        seventhExpected = 1836
        seventhData = [3, 1, 2]

        self.assertEqual(partOne(firstData), firstExpected)
        self.assertEqual(partOne(secondData), secondExpected)
        self.assertEqual(partOne(thirdData), thirdExpected)
        self.assertEqual(partOne(fourthData), fourthExpected)
        self.assertEqual(partOne(fifthData), fifthExpected)
        self.assertEqual(partOne(sixthData), sixthExpected)
        self.assertEqual(partOne(seventhData), seventhExpected)
        
#    def testPartTwo(self):
#        firstExpected = 175594
#        firstData = [0, 3, 6]
#
#        secondExpected = 2578
#        secondData = [1, 3, 2]
#
#        thirdExpected = 3544142
#        thirdData = [2, 1, 3]
#
#        fourthExpected = 261214
#        fourthData = [1, 2, 3]
#
#        fifthExpected = 6895259
#        fifthData = [2, 3, 1]
#
#        sixthExpected = 18
#        sixthData = [3, 2, 1]
#
#        seventhExpected = 362
#        seventhData = [3, 1, 2]
#
#        self.assertEqual(partTwo(firstData), firstExpected)
#        self.assertEqual(partTwo(secondData), secondExpected)
#        self.assertEqual(partTwo(thirdData), thirdExpected)
#        self.assertEqual(partTwo(fourthData), fourthExpected)
#        self.assertEqual(partTwo(fifthData), fifthExpected)
#        self.assertEqual(partTwo(sixthData), sixthExpected)
#        self.assertEqual(partTwo(seventhData), seventhExpected)
    

if __name__ == '__main()__':
    unittest.main()

