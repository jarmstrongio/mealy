'''
This module is responsible for parsing a given list of meal dicts and generating a shopping list.
'''

def generate_shopping_list(meals):
    '''
    Accepts a meals list and returns a dict of ingredient to number of times it occurs.
    '''
    ingredients = flatten_ingredients(meals)
    grouped_ingredients = group_ingredients(ingredients)

    return grouped_ingredients

def flatten_ingredients(meals):
    '''
    Accepts the meal list and returns the list of all the ingredients mentioned.
    '''
    ingredients = []

    for meal in meals:
        try:
            ingredients.extend(meal['ingredients'])
        except KeyError:
            pass

    return ingredients

def group_ingredients(ingredients):
    '''
    Accepts the given list of ingredients and counts how many times each is mentioned - returning
    the result as a dict of ingredient - count.
    '''
    grouped_ingredients = {}

    for ingredient in ingredients:
        try:
            grouped_ingredients[ingredient] = grouped_ingredients[ingredient] + 1
        except KeyError:
            grouped_ingredients[ingredient] = 1

    return grouped_ingredients
