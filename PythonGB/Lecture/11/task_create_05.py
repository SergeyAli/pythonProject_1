'''
Удаление экземпляра класса, __del__
Дандер метод __del__ также редко используется в обычной практике ООП. Он
отвечает за действия при удалении экземпляра класса. Если быть более точным,
метод срабатывает при достижении нуля счётчиком ссылок на объект, но перед его
удалением из памяти сборщиком мусора. Рассмотрим простой пример.
'''

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')

u_1 = User('Спенглер')
u_2 = User('Венкман')
