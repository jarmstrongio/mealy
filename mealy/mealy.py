'''
This application reads in a JSON document of possible meals to cook and displays a meal plan for the
week.
'''
from pprint import pprint
from meals_input import read_meals_json
from meals import generate_meal_list
from ingredients import generate_shopping_list

if __name__ == "__main__":
    MEALS = read_meals_json()
    MEAL_LIST = generate_meal_list(MEALS)
    SHOPPING_LIST = generate_shopping_list(MEAL_LIST)

    print('Meal list')
    for meal in MEAL_LIST:
        print(meal['name'])
    print('')
    print('Shopping list')
    pprint(SHOPPING_LIST)
