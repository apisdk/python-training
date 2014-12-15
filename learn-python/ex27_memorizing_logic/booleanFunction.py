from enum import Enum


class Taste(Enum):
    unknown = 0
    sweet = 1
    bitter = 2
    sour = 3
    salty = 4
    hot = 5


class Food(Enum):
    apple = 0
    orange = 1
    snack = 2
    cake = 3


def isSweet(food):
    if food == Food.apple:
        return True
    return False


result = isSweet(Food.apple)
print("%s isSweet=%s" % (Food.apple, result))

result = isSweet(Food.orange)
print("%s isSweet=%s" % (Food.orange, result))

apple = Food.apple
print("%r" % apple)
print(repr(apple))
print(type(apple))

print("apple is instance of Food = %s" % isinstance(apple, Food))

print("print item name = %s" % apple.name)
