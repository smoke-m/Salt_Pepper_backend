class Dessert:
    """Класс Dessert c геттерами и сеттерами name и calories"""

    def __init__(self, name: str = "", calories: int = 0):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self) -> bool:
        if isinstance(self.__calories, (int, float)):
            return self.__calories < 200
        return False

    @staticmethod
    def is_delicious() -> bool:
        return True
