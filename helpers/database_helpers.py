def filter_ingredients_by_type(ingredients, ingredient_type):
    """Фильтрация ингредиентов по типу"""
    return [ingredient for ingredient in ingredients if ingredient.get_type() == ingredient_type]


def get_ingredients_price_dict(ingredients):
    """Получение словаря цен ингредиентов по их названию"""
    return {ingredient.get_name(): ingredient.get_price() for ingredient in ingredients}
