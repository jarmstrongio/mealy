'''
This application reads in a JSON document of possible meals to cook and displays a meal plan for the
week.
'''
from pprint import pprint
import os
import json

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

if __name__ == "__main__":
    MEALS = read_meals_json()
    pprint(MEALS, width=300)
