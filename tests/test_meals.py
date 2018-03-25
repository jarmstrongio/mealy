from mealy import meals
import unittest

class TestMeals(unittest.TestCase):
    def test_expand_list_one(self):
        meal = {
            "name": "test",
            "weighting": 2
        }

        meal_list = [meal]

        result = meals.expand_list(meal_list)

        self.assertEqual(2, len(result), "The list should be the sum of the combined weightings in length")

    def test_expand_list_multiple(self):
        meal1 = {
            "name": "test1",
            "weighting": 2
        }

        meal2 = {
            "name": "test2",
            "weighting": 3
        }

        meal_list = [meal1, meal2]

        result = meals.expand_list(meal_list)

        self.assertEqual(5, len(result), "The list should be the sum of the combined weightings in length")

    def test_select_meals_default_length(self):
        meal1 = {"name": "test1"}
        meal2 = {"name": "test2"}
        meal3 = {"name": "test3"}
        meal4 = {"name": "test4"}
        meal5 = {"name": "test5"}
        meal6 = {"name": "test6"}

        meal_list = [meal1, meal2, meal3, meal4, meal5, meal6]

        result = meals.select_meals(meal_list)

        self.assertEqual(5, len(result), "By default five meals should be chosen")

        all_unique = True
        names = []

        for meal in result:
            name = meal['name']
            if name in names:
                all_unique = False
            
            names.append(name)

        self.assertTrue(all_unique, "There shouldn't be any repeated meals returned")

    def test_select_meals_chosen_length(self):
        meal1 = {"name": "test1"}
        meal2 = {"name": "test2"}
        meal3 = {"name": "test3"}
        meal4 = {"name": "test4"}
        meal5 = {"name": "test5"}
        meal6 = {"name": "test6"}

        meal_list = [meal1, meal2, meal3, meal4, meal5, meal6]

        result = meals.select_meals(meal_list, 3)

        self.assertEqual(3, len(result), "The specified number of meals should be returned")
        
        all_unique = True
        names = []

        for meal in result:
            name = meal['name']
            if name in names:
                all_unique = False
            
            names.append(name)

        self.assertTrue(all_unique, "There shouldn't be any repeated meals returned")
        
if __name__ == '__main__':
    unittest.main()
