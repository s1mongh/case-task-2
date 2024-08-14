class Animal:
    """Базовый класс, представляющий животное."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Метод, который будет переопределяться в дочерних классах."""
        return f"{self.name} издает звук."


class Dog(Animal):
    """Производный класс, представляющий собаку."""

    def speak(self):
        """Переопределение метода speak для класса Dog."""
        return f"{self.name} лает."


class Cat(Animal):
    """Производный класс, представляющий кошку."""

    def speak(self):
        """Переопределение метода speak для класса Cat."""
        return f"{self.name} мяукает."


# Тестовая программа для демонстрации работы базового и производного классов
if __name__ == "__main__":
    # Создаем объекты классов
    generic_animal = Animal("Животное")
    dog = Dog("Бобик")
    cat = Cat("Мурзик")

    # Демонстрируем работу методов
    print(generic_animal.speak())  # Вывод: Животное издает звук.
    print(dog.speak())             # Вывод: Бобик лает.
    print(cat.speak())             # Вывод: Мурзик мяукает.
