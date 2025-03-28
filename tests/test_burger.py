import praktikum.ingredient_types
import pytest
import allure

from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


@allure.feature("Burger")
class TestBurger:

    @allure.title("Установка булочек")
    def test_set_buns(self):
        with allure.step("Создаем бургер и булочку"):
            burger = Burger()
            bun = Bun('Type_bun', 100.0)
        with allure.step("Устанавливаем булочку в бургер"):
            burger.set_buns(bun)
        with allure.step("Проверяем, что булочка установлена корректно"):
            assert burger.bun == bun

    @allure.title("Добавление ингредиента")
    def test_add_ingredient(self):
        with allure.step("Создаем бургер и мок-объект ингредиента"):
            burger = Burger()
            mock_ingredient = Mock()
            mock_ingredient.get_name.return_value = 'Type_bun'
            mock_ingredient.get_price.return_value = 8.0
            mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        with allure.step("Добавляем ингредиент в бургер"):
            burger.add_ingredient(mock_ingredient)
        with allure.step("Проверяем, что ингредиент добавлен корректно"):
            assert burger.ingredients[0].get_price() == 8.0
            assert burger.ingredients[0].get_name() == 'Type_bun'
            assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    @allure.title("Удаление ингредиента")
    def test_remove_ingredient(self):
        with allure.step("Создаем бургер и мок-ингредиент"):
            burger = Burger()
            mock_ingredient = Mock()
        with allure.step("Добавляем ингредиент и затем удаляем"):
            burger.add_ingredient(mock_ingredient)
            burger.remove_ingredient(0)
        with allure.step("Проверяем, что ингредиентов в бургере не осталось"):
            assert len(burger.ingredients) == 0

    @allure.title("Перемещение ингредиента")
    def test_move_ingredient(self):
        with allure.step("Создаем бургер и добавляем два ингредиента"):
            burger = Burger()
            mock_ingredient1 = Mock()
            mock_ingredient2 = Mock()
            burger.add_ingredient(mock_ingredient1)
            burger.add_ingredient(mock_ingredient2)
        with allure.step("Перемещаем второй ингредиент на первое место"):
            burger.move_ingredient(1, 0)
        with allure.step("Проверяем, что порядок ингредиентов изменился"):
            assert burger.ingredients[0] == mock_ingredient2
            assert burger.ingredients[1] == mock_ingredient1

    @allure.title("Получение цены бургера")
    def test_get_price(self):
        with allure.step("Создаем бургер и получаем данные из базы"):
            burger = Burger()
            database = Database()
            burger.set_buns(database.available_buns()[0])
            burger.add_ingredient(database.available_ingredients()[0])
            burger.add_ingredient(database.available_ingredients()[3])
        with allure.step("Проверяем, что цена бургера рассчитана верно"):
            assert burger.get_price() == 400.0

    @allure.title("Получение чека бургера")
    def test_get_receipt(self):
        with allure.step("Создаем бургер и добавляем ингредиенты"):
            burger = Burger()
            database = Database()
            burger.set_buns(database.available_buns()[0])
            burger.add_ingredient(database.available_ingredients()[0])
            burger.add_ingredient(database.available_ingredients()[3])
        with allure.step("Формируем ожидаемый чек"):
            expected_receipt = (
                "(==== black bun ====)\n"
                "= sauce hot sauce =\n"
                "= filling cutlet =\n"
                "(==== black bun ====)\n\n"
                "Price: 400"
            )
        with allure.step("Проверяем, что чек сформирован корректно"):
            assert expected_receipt == burger.get_receipt()
