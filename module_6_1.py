# Родительские классы:
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True   # Атрибут экземпляра
        self.fed = False    # Атрибут экземпляра

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # Атрибут экземпляра

# Классы наследники:

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределение атрибута экземпляра

# Пример результата выполнения программы:

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Имена объектов
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Начальные состояния
print(a1.alive)  # True
print(a2.fed)    # False

# Кормим животных
a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин

# Конечные состояния
print(a1.alive)  # False
print(a2.fed)    # True
