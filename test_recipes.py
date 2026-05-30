from system_recipes import Ingredient, Recipe, ShoppingList
import pytest

def test_ingredient_init():
    ingredient = Ingredient("Мука", 500.0, "г")

    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"

def test_ingredient_str():
    ingredient = Ingredient("Мука", 500.0, "г")

    assert str(ingredient) == "Мука: 500.0 г"

def test_ingredient_eq_correctly():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Мука", 400.0, "г")

    assert ingredient1 == ingredient2

def test_ingredient_eq_different_names():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Крахмал", 500.0, "г")

    assert ingredient1 != ingredient2

def test_ingredient_eq_different_units():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Мука", 500.0, "кг")

    assert ingredient1 != ingredient2

def test_recipe_init():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки", ingredients)

    assert recipe.title == "Пирожки"
    assert len(recipe.ingredients) == 3

def test_recipe_add_ingredients():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки", ingredients)

    recipe.add_ingredient(Ingredient("Грибы", 150.0, "г"))
    recipe.add_ingredient(Ingredient("Мука", 100.0, "г"))

    assert len(recipe.ingredients) == 4
    assert recipe.ingredients[0].quantity == 600.0

def test_recipe_scale_correctly():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки", ingredients)

    scaled_recipe = recipe.scale(5)

    assert scaled_recipe.title == "Пирожки"
    assert len(scaled_recipe.ingredients) == 3
    assert scaled_recipe.ingredients[0].quantity == 2500.0
    assert scaled_recipe.ingredients[1].quantity == 1500.0
    assert scaled_recipe.ingredients[2].quantity == 10

def test_recipe_scale_error():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки", ingredients)

    with pytest.raises(ValueError):
        recipe.scale(-5)
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale("str")

def test_recipe_len():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки", ingredients)

    assert len(recipe) == 3

def test_shopping_list_add_recipe_correctly():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки с картошкой", ingredients)

    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 5)
    final_list = shopping_list.get_list()

    assert len(final_list) == 3
    assert final_list[0].name == "Картошка"
    assert final_list[0].quantity == 1500.0
    assert final_list[0].unit == "г"
    assert final_list[1].name == "Мука"
    assert final_list[1].quantity == 2500.0
    assert final_list[1].unit == "г"
    assert final_list[2].name == "Яйца"
    assert final_list[2].quantity == 10
    assert final_list[2].unit == "шт"

def test_shopping_list_add_recipe_error():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки с картошкой", ingredients)

    shopping_list = ShoppingList()

    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, -5)
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, 0)

def test_shopping_list_remove_recipe_exiting():
    ingredients = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe = Recipe("Пирожки с картошкой", ingredients)

    shopping_list = ShoppingList()

    shopping_list.add_recipe(recipe, 5)
    shopping_list.remove_recipe("Котлеты")

    assert len(shopping_list._items) == 3

def test_shopping_list_get_list():
    ingredients1 = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe1 = Recipe("Пирожки с картошкой", ingredients1)
    ingredients2 = [Ingredient("Мука", 200.0, "г"), Ingredient("Грибы", 150.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe2 = Recipe("Пирожки с грибами", ingredients2)

    shopping_list = ShoppingList()

    shopping_list.add_recipe(recipe1, 5)
    shopping_list.add_recipe(recipe2, 3)
    final_list = shopping_list.get_list()

    assert len(final_list) == 4
    assert final_list[0].name == "Грибы"
    assert final_list[0].quantity == 450.0
    assert final_list[0].unit == "г"
    assert final_list[1].name == "Картошка"
    assert final_list[1].quantity == 1500.0
    assert final_list[1].unit == "г"
    assert final_list[2].name == "Мука"
    assert final_list[2].quantity == 3100.0
    assert final_list[2].unit == "г"
    assert final_list[3].name == "Яйца"
    assert final_list[3].quantity == 16
    assert final_list[3].unit == "шт"

def test_shopping_list_add():
    ingredients1 = [Ingredient("Мука", 500.0, "г"), Ingredient("Картошка", 300.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe1 = Recipe("Пирожки с картошкой", ingredients1)
    ingredients2 = [Ingredient("Мука", 200.0, "г"), Ingredient("Грибы", 150.0, "г"), Ingredient("Яйца", 2, "шт")]
    recipe2 = Recipe("Пирожки с грибами", ingredients2)

    shopping_list1 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 5)
    shopping_list2 = ShoppingList()
    shopping_list2.add_recipe(recipe2, 3)

    merge_list = shopping_list1 + shopping_list2
    final_list = merge_list.get_list()

    assert len(final_list) == 4
    assert final_list[0].name == "Грибы"
    assert final_list[0].quantity == 450.0
    assert final_list[1].name == "Картошка"
    assert final_list[1].quantity == 1500.0
    assert final_list[2].name == "Мука"
    assert final_list[2].quantity == 3100.0
    assert final_list[3].name == "Яйца"
    assert final_list[3].quantity == 16

    assert len(shopping_list1._items) == 3
    assert shopping_list1.get_list()[0].name == "Картошка"
    assert shopping_list1.get_list()[0].quantity == 1500.0
    assert shopping_list1.get_list()[1].name == "Мука"
    assert shopping_list1.get_list()[1].quantity == 2500.0
    assert shopping_list1.get_list()[2].name == "Яйца"
    assert shopping_list1.get_list()[2].quantity == 10

    assert len(shopping_list2._items) == 3
    assert shopping_list2.get_list()[0].name == "Грибы"
    assert shopping_list2.get_list()[0].quantity == 450.0
    assert shopping_list2.get_list()[1].name == "Мука"
    assert shopping_list2.get_list()[1].quantity == 600.0
    assert shopping_list2.get_list()[2].name == "Яйца"
    assert shopping_list2.get_list()[2].quantity == 6