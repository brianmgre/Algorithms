#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches=None

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0
    numBatches = ingredients[ingredient] // amount
    if batches == None or numBatches < batches:
      batches = numBatches
  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 132, 'butter': 50, 'flour': 51 }
  ingredients = { 'milk': 1000, 'butter': 58, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))