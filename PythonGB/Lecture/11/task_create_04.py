'''
Шаблон Одиночка, Singleton
Ещё один вариант использования дандре __new__ — паттерн Singleton. Он
позволяет создавать лишь один экземпляр класса. Вторая и последующие попытки
будут возвращать ранее созданый экземпляр.
'''

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, name: str):
        self.name = name


a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')
