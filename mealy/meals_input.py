'''
This module is responsible for parsing input and converting it into dictoinaries to be easily used
by the rest of the application.
Currently it only supports reading in the provided meals.json file.
'''
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
