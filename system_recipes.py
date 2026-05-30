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


class ShoppingList:
    def __init__(self, _items=None):
        if _items is not None:
            self._items = _items
        else:
            self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if not Recipe.is_valid_ratio(portions):
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        new_items = []

        for item in self._items:
            if item[1] != title:
                new_items.append(item)

        self._items = new_items

    def get_list(self):
        ingredients_dict = {}
        for item in self._items:
            ingredient = item[0]
            key = (ingredient.name, ingredient.unit)

            if key in ingredients_dict:
                ingredients_dict[key] += ingredient.quantity
            else:
                ingredients_dict[key] = ingredient.quantity

        ingredients_list = []
        for (name, unit), quantity in ingredients_dict.items():
            ingredients_list.append(Ingredient(name, quantity, unit))

        ingredients_list.sort(key=lambda x: x.name)
        return ingredients_list

    def __add__(self, other: 'ShoppingList'):
        return ShoppingList(self._items + other._items)


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float):
        new_recipe = super().scale(ratio)

        return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)

    def __str__(self):
        return f"[{self.diet_type}]{self.title}: {', '.join(str(ingredient) for ingredient in self.ingredients)}"