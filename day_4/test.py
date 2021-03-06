import unittest

from puzzle import separatePassports, parseKeyVals, containsRequiredKeys, isValidFormatAndRange, isValidHeight, isValidFormat, partOne


class TestPuzzle(unittest.TestCase):

    data = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
            'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
            '\n',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
            'hcl:#cfa07d byr:1929\n',
            '\n',
            'hcl:#ae17e1 iyr:2013\n',
            'eyr:2024\n',
            'ecl:brn pid:760753108 byr:1931\n',
            'hgt:179cm\n',
            '\n',
            'hcl:#cfa07d eyr:2025 pid:166559648\n',
            'iyr:2011 ecl:brn hgt:59in']

    keyRules = {'byr': [['^\d{4}$', 1920, 2002], isValidFormatAndRange],
                'iyr': [['^\d{4}$', 2010, 2020], isValidFormatAndRange],
                'eyr': [['^\d{4}$', 2020, 2030], isValidFormatAndRange],
                'hgt': [['^\d{1,3}(cm|in)$', {'cm': [150, 193], 'in': [59, 76]}], isValidHeight],
                'hcl': ['^#[0-9a-f]{6}$', isValidFormat],
                'ecl': ['^(amb|blu|brn|gry|grn|hzl|oth)$', isValidFormat],
                'pid': ['^\d{9}$', isValidFormat]}

    def testSeparatePassports(self):
        expectedLen = 4
        expectedStr = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n'
        result = separatePassports(self.data)
        self.assertEqual(len(result), expectedLen)
        self.assertEqual(result[0], expectedStr)

    def testParseKeyVals(self):
        expected = ['ecl:gry', 'pid:860033327', 'eyr:2020', 'hcl:#fffffd', 'byr:1937', 'iyr:2017', 'cid:147', 'hgt:183cm']
        result = parseKeyVals('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n')
        self.assertEqual(result, expected)

    def testContainsRequiredKeys_shouldBeValid(self):
        keyVals = ['ecl:gry', 'pid:860033327', 'eyr:2020', 'hcl:#fffffd', 'byr:1937', 'iyr:2017', 'cid:147', 'hgt:183cm']
        expected = True
        isValid = containsRequiredKeys(keyVals, self.keyRules)
        self.assertEqual(isValid, expected)

    def testContainsRequiredKeys_shouldBeInvalid(self):
        keyVals = ['ecl:gry', 'eyr:2020', 'hcl:#fffffd', 'byr:1937', 'iyr:2017', 'cid:147', 'hgt:183cm']
        expected = False
        isValid = containsRequiredKeys(keyVals, self.keyRules)
        self.assertEqual(isValid, expected)

    def testPartOne(self):
        expected = 2
        result = partOne(self.data, self.keyRules)
        self.assertEqual(result, expected)

if __name__ == '__main()__':
    unittest.main()

