'''
This module is responsible for parsing the the given meals input into generate_meal_list and
returning a random selection.
This can then be consumed by other modules to generate shopping lists, formatted outputs etc.
'''
import random

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
