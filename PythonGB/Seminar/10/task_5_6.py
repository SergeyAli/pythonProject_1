'''
Задание №5
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
'''

'''
Задание №6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.
'''

class Animals:
    def __init__(self, name):
        self.name = name
    def animal_name(self):
        return f'Имя: {self.name}'

class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth
    def get_info(self):
        return f'Глубина обитания: {self.depth} m '

class Birds(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def get_info(self):
        return f'Размах крыльев: {self.wingspan} sm '

class Reptiles(Animals):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела: {self.length} m '


if __name__ == '__main__':
    fish = Fish('Som', 5)
    bird = Birds('Parrot', 10)
    reptile = Reptiles('Anaconda', 3)
    print(fish.animal_name())
    print(fish.get_info())
    print(bird.animal_name())
    print(bird.get_info())
    print(reptile.animal_name())
    print(reptile.get_info())
