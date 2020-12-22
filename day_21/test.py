import unittest

from puzzle import separateIngredients, countAppearances, getAllergenPairs, getCanonicalList


class TestPuzzle(unittest.TestCase):

    data = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
            'trh fvjkl sbzzf mxmxvkd (contains dairy)',
            'sqjhc fvjkl (contains soy)',
            'sqjhc mxmxvkd sbzzf (contains fish)']

    def testSeparateIngredients(self):
        expected = set(['kfcds', 'nhms', 'sbzzf', 'trh'])
        foods, result = separateIngredients(self.data)
        self.assertEqual(result, expected)

    def testCountAppearances(self):
        expected = 5
        foods, nonAllergens = separateIngredients(self.data)
        result = countAppearances(nonAllergens, self.data)
        self.assertEqual(result, expected)

    def testGetAllergenPairs(self):
        expected = {'dairy': 'mxmxvkd', 'fish': 'sqjhc', 'soy': 'fvjkl'}
        foods, nonAllergens = separateIngredients(self.data)
        result = getAllergenPairs(foods)
        self.assertEqual(result, expected)

    def testGetCanonicalList(self):
        expected = 'mxmxvkd,sqjhc,fvjkl'
        allergens, nonAllergens = separateIngredients(self.data)
        allergens = getAllergenPairs(allergens)
        result = getCanonicalList(allergens)
        self.assertEqual(result, expected)


if __name__ == '__main()__':
    unittest.main()

