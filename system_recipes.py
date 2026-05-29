import copy

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):

        for current_ingredient in self.ingredients:
            if current_ingredient.name == ingredient.name and current_ingredient.unit == ingredient.unit:
                current_ingredient.quantity += ingredient.quantity
                return

        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен являться числом и быть положительным")

        new_recipe = copy.deepcopy(self)

        for ingredient in new_recipe.ingredients:
            ingredient.quantity *= ratio

        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return f"{self.title}: {', '.join(str(ingredient) for ingredient in self.ingredients)}"