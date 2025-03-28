import pytest
import allure

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from helpers.database_helpers import filter_ingredients_by_type, get_ingredients_price_dict


@allure.feature("Database")
class TestDataBase:

    @allure.title("Проверка количества доступных булок")
    def test_get_available_buns(self, database_instance):
        available_buns = database_instance.available_buns()
        assert len(available_buns) == 3

    @allure.title("Проверка количества доступных ингредиентов")
    def test_get_available_ingredients(self, database_instance):
        available_ingredients = database_instance.available_ingredients()
        assert len(available_ingredients) == 6

    @pytest.mark.parametrize("ingredient_type, expected_count", [
        (INGREDIENT_TYPE_SAUCE, 3),
        (INGREDIENT_TYPE_FILLING, 3),
    ])
    @allure.title("Проверка количества доступных {ingredient_type}")
    def test_get_quantity_available_ingredients(self, database_instance, ingredient_type, expected_count):
        ingredients = database_instance.available_ingredients()
        filtered_ingredients = filter_ingredients_by_type(ingredients, ingredient_type)
        assert len(filtered_ingredients) == expected_count

    @allure.title("Сравнение цен ингредиентов в базе данных")
    def test_get_available_ingredients_prices(self, database_instance):
        ingredients = database_instance.available_ingredients()
        price_dict = get_ingredients_price_dict(ingredients)
        assert price_dict == {
            'hot sauce': 100,
            'sour cream': 200,
            'chili sauce': 300,
            'cutlet': 100,
            'dinosaur': 200,
            'sausage': 300,
        }
