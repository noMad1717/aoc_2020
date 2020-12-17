import unittest

from puzzle import parseNotes, findInvalidVals, findValidTickets, decipherTicket, partOne, partTwo


class TestPuzzle(unittest.TestCase):

    data = ['class: 1-3 or 5-7',
            'row: 6-11 or 33-44',
            'seat: 13-40 or 45-50',
            '',
            'your ticket:',
            '7,1,14',
            '',
            'nearby tickets:',
            '7,3,47',
            '40,4,50',
            '55,2,20',
            '38,6,12']

    data2 = ['class: 0-1 or 4-19',
            'row: 0-5 or 8-19',
            'seat: 0-13 or 16-19',
            '',
            'your ticket:',
            '11,12,13',
            '',
            'nearby tickets:',
            '3,9,19',
            '15,1,5',
            '5,14,9']

#    def testParseNotes(self):
#        expected = {'class': ['1-3', '5-7'], 'row': ['6-11', '33-44'], 'seat': ['13-40', '45-50'], 'your ticket': [7,1,14], 'nearby tickets': [[7,3,47], [40,4,50], [55,2,20], [38,6,12]]}
#        result = parseNotes(self.data)
#        self.assertEqual(result, expected)

    def testFindInvalidVals(self):
        expected = [4,55,12]
        result = findInvalidVals(parseNotes(self.data))
        self.assertEqual(result, expected)

    def testFindValidTickets(self):
        expected = [[7,3,47]]
        result = findValidTickets(parseNotes(self.data))
        self.assertEqual(result, expected)

    def testDecipherTicket(self):
        expected = {'row': [0], 'class': [1], 'seat': [2]}
        result = decipherTicket(parseNotes(self.data2))
        self.assertEqual(result, expected)

    def testPartOne(self):
        expected = 71
        result = partOne(self.data)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

