"""
    Advent of Code 2020 - Day 21
"""
import util

from functools import reduce


def getAllergenPairs(foods):
    unique = set()
    while len(unique) < len(foods.keys()):
        for key, vals in foods.items():
            if len(vals) == 1:
                unique = unique | vals
            else:
                for uq in unique:
                    if uq in vals:
                        vals.remove(uq)
    for key in foods:
        foods[key] = [x for x in foods[key]][0]
    return foods

def separateIngredients(data):
    allIngredients = set()
    foods = {}
    for line in data:
        allergens = [x for x in line.split(' (contains ')[1][:-1].split(', ')]
        ingredients = {x for x in line.split(' (')[0].split()}
        allIngredients = allIngredients | ingredients
        for allergen in allergens:
            try:
                foods[allergen] = foods[allergen] & ingredients
            except KeyError:
                foods[allergen] = ingredients
    allAllergens = set()
    for allergen in foods.values():
        allAllergens = allAllergens | allergen
    return foods, allIngredients - allAllergens

def countAppearances(nonAllergens, data):
    count = dict.fromkeys(nonAllergens, 0)
    for line in data:
        ingredients = {x for x in line.split(' (')[0].split()}
        for ing in ingredients:
            try:
                count[ing] += 1
            except KeyError:
                pass
    return sum(list(count.values()))

def getCanonicalList(allergens):
    keys = list(allergens.keys())
    keys.sort()
    ingredients = [allergens[key] for key in keys]
    return reduce((lambda x,y: x + ',' + y), ingredients)

def partOne(data):
    allergens, nonAllergens = separateIngredients(data)
    return countAppearances(nonAllergens, data)

def partTwo(data):
    allergens, nonAllergens = separateIngredients(data)
    allergens = getAllergenPairs(allergens)
    return getCanonicalList(allergens)

foods = util.fileToStringList('input')

print(f'Part one: Non-allergens appear a total of {partOne(foods)} times!')
print(f'Part two: Canonical list of allergens = {partTwo(foods)}')

