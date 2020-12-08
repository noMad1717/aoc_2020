import unittest

from puzzle import executeInstruction, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6']

    def testExecuteInstruction_increaseAcc(self):
        expectedAcc = 5
        expectedNext = 4
        acc = 2
        nextInst = 3
        acc, nextInst = executeInstruction('acc', '+', 3, nextInst, acc)
        self.assertEqual(expectedAcc, acc)
        self.assertEqual(expectedNext, nextInst)

    def testExecuteInstruction_decreaseAcc(self):
        expectedAcc = -10
        expectedNext = 6
        acc = 89
        nextInst = 5
        acc, nextInst = executeInstruction('acc', '-', 99, nextInst, acc)
        self.assertEqual(expectedAcc, acc)
        self.assertEqual(expectedNext, nextInst)

    def testExecuteInstruction_increaseNext(self):
        expectedAcc = -10
        expectedNext = 6
        acc = -10
        nextInst = 2
        acc, nextInst = executeInstruction('jmp', '+', 4, nextInst, acc)
        self.assertEqual(expectedAcc, acc)
        self.assertEqual(expectedNext, nextInst)

    def testExecuteInstruction_decreaseNext(self):
        expectedAcc = -10
        expectedNext = 1
        acc = -10
        nextInst = 4
        acc, nextInst = executeInstruction('jmp', '-', 3, nextInst, acc)
        self.assertEqual(expectedAcc, acc)
        self.assertEqual(expectedNext, nextInst)

    def testExecuteInstruction_nop(self):
        expectedAcc = -10
        expectedNext = 1
        acc = -10
        nextInst = 0
        acc, nextInst = executeInstruction('nop', '+', 0, nextInst, acc)
        self.assertEqual(expectedAcc, acc)
        self.assertEqual(expectedNext, nextInst)

    def testPartOne(self):
        expectedAcc = 5
        acc = partOne(self.data)
        self.assertEqual(acc, expectedAcc)

    def testPartTwo(self):
        expectedAcc = 8
        acc = partTwo(self.data)
        self.assertEqual(acc, expectedAcc)


if __name__ == '__main()__':
    unittest.main()

