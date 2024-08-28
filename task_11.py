class Dessert:
    """Класс Dessert c геттерами и сеттерами name и calories"""

    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    def set_name(self, name):
        self.__name = name

    def set_calories(self, calories):
        self.__calories = calories

    def get_name(self):
        return self.__name

    def get_calories(self):
        return self.__calories

    def is_healthy(self):
        return True if self.__calories < 200 else False

    def is_delicious(self):
        return True
