import pytest
import allure

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from praktikum.database import Database


@allure.feature("Ingredient")
class TestIngredient:

    @allure.title("Проверка, что цена ингредиента устанавливается корректно")
    def test_get_price_correct_price(self):
        database = Database()
        ingredient = database.available_ingredients()[0]  # Берем первый ингредиент
        assert ingredient.get_price() == 100

    @allure.title("Проверка, что имя ингредиента устанавливается корректно")
    def test_get_name_correct_name(self):
        database = Database()
        ingredient = database.available_ingredients()[1]
        assert ingredient.get_name() == "sour cream"

    @pytest.mark.parametrize(
        "ingredient_index",
        [0, 1, 2, 3, 4, 5]
    )
    @allure.title("Проверка, что тип ингредиента корректно определяется для {ingredient_index}-го ингредиента")
    def test_get_type_correct_type(self, ingredient_index):
        database = Database()
        ingredient = database.available_ingredients()[ingredient_index]
        assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
