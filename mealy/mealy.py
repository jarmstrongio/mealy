'''
This application reads in a JSON document of possible meals to cook and displays a meal plan for the
week.
'''
from meals_input import read_meals_json
from meals import generate_meal_list
from ingredients import generate_shopping_list
from view import render

import web

urls = (
    '/', 'display',
    '/raw', 'raw'
)

class raw:
    def GET(self):
        MEALS = read_meals_json()
        MEAL_LIST = generate_meal_list(MEALS)
        SHOPPING_LIST = generate_shopping_list(MEAL_LIST)

        result = {'meals':MEAL_LIST, 'shopping':SHOPPING_LIST}

        # Prevents an No 'Access-Control-Allow-Origin' warning
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')

        return render.raw(result)

class display:
    def GET(self):
        MEALS = read_meals_json()
        MEAL_LIST = generate_meal_list(MEALS)

        return render.meals(MEAL_LIST)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()