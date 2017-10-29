'''
This application reads in a JSON document of possible meals to cook and displays a meal plan for the
week.
'''
from pprint import pprint
import os
import json
import random

def read_meals_json():
    '''
    Reads in the meals.json file in the same folder this is found in and returns a list of dicts of
    the contents.

    Example:
    An example meal dict:
    {'ingredients': ['TBD'],
     'name': 'Chicken in White Sauce',
     'recipe': ['TBD'],
     'weighting': 3
    }
    '''
    # Get the meals.json file in the same directory this is running from
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # Convert the contents of the json file to dicts
    with open(os.path.join(__location__, 'meals.json')) as data_file:
        meals = json.load(data_file)

    return meals['meals']

def generate_meal_list(meals):
    '''Generates the meal list for the week.
    meals: The initial unexpanded list of meals from which the meal list for the week should be
    generated.
    '''
    expanded_meals = expand_list(meals)
    weeks_meals = select_meals(expanded_meals)

    return weeks_meals

def expand_list(meals):
    '''Creates an expanded version of the given meal list with each item appearing as many times as
    its weighting declares.
    meals: The list of meals to expand.
    '''
    expanded_meals = []

    for meal in meals:
        try:
            for _m in range(0, meal['weighting']):
                expanded_meals.append(meal)
        except KeyError:
            # If it's missing a weighting just add it once
            expanded_meals.append(meal)

    return expanded_meals

def select_meals(expanded_meals, number_of_meals=5):
    '''Randomly selects the given number of meals from the expanded meals list and returns a list
    of meals of that length.
    expanded_meals: The expanded list of meals to create the meal list from.
    number_of_meals: The number of meals to be included (Default 5).
    '''
    weeks_meals = []

    for _m in range(0, number_of_meals):
        meal = random.choice(expanded_meals)

        # We only want to add each meal once unless there are fewer possible meals than
        # required_meal_numner which would cause an infinate loop otherwise.
        while number_of_meals < len(expanded_meals) and meal in weeks_meals:
            meal = random.choice(expanded_meals)

        weeks_meals.append(meal)

    return weeks_meals

if __name__ == "__main__":
    MEALS = read_meals_json()
    MEAL_LIST = generate_meal_list(MEALS)

    pprint(MEAL_LIST, width=300)
