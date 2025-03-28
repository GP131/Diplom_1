import allure

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient


@allure.feature("Ingredient Types")
class TestIngredientTypes:

    @allure.title("Проверка, что значения типов ингредиентов заданы корректно")
    def test_ingredient_type_values(self):
        assert INGREDIENT_TYPE_SAUCE == "SAUCE"
        assert INGREDIENT_TYPE_FILLING == "FILLING"

    @allure.title("Создание ингредиентов с разными типами")
    def test_ingredient_creation_with_types(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

        assert sauce.get_type() == "SAUCE"
        assert filling.get_type() == "FILLING"
