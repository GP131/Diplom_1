import pytest
import allure
from praktikum.bun import Bun


@allure.feature("Bun")
class TestBun:

    @allure.title("Получение наименования булочки")
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_get_correct_name(self, name, price):
        with allure.step(f"Создаем булочку с именем '{name}' и ценой {price}"):
            bun = Bun(name, price)
        with allure.step(f"Проверяем, что имя булочки равно '{name}'"):
            assert bun.get_name() == name

    @allure.title("Получение цены булочки")
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_get_correct_price(self, name, price):
        with allure.step(f"Создаем булочку с именем '{name}' и ценой {price}"):
            bun = Bun(name, price)
        with allure.step(f"Проверяем, что цена булочки равна {price}"):
            assert bun.get_price() == price
