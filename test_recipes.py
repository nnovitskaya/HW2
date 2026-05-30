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

