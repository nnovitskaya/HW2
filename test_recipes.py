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
