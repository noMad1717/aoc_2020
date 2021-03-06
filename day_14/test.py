import unittest

from puzzle import applyMask, applyMask_v2, execValInst, execAddrInst, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0']
    data_v2 = ['mask = 000000000000000000000000000000X1001X', 'mem[42] = 100', 'mask = 00000000000000000000000000000000X0XX', 'mem[26] = 1']

    def testApplyMask(self):
        expected = 73
        result = applyMask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11)
        self.assertEqual(result, expected)

    def testApplyMask_v2(self):
        expected = [26, 27, 58, 59]
        result = applyMask_v2('000000000000000000000000000000X1001X', 42)
        self.assertEqual(result, expected)

    def testExecValInst(self):
        expected = 73
        mem = {}
        execValInst(mem, self.data[0], self.data[1])
        self.assertEqual(mem[8], expected)

    def testExecAddrInst(self):
        expected = 100
        mem = {}
        execAddrInst(mem, self.data_v2[0], self.data_v2[1])
        self.assertEqual(mem[26], expected)
        self.assertEqual(mem[27], expected)
        self.assertEqual(mem[58], expected)
        self.assertEqual(mem[59], expected)

    def testPartOne(self):
        expected = 165
        result = partOne(self.data)
        self.assertEqual(result, expected)

    def testPartTwo(self):
        expected = 208
        result = partTwo(self.data_v2)
        self.assertEqual(result, expected)

if __name__ == '__main()__':
    unittest.main()

