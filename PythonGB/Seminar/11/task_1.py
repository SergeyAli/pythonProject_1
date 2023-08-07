'''
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)
'''

import datetime

class MyString(str):

    def __new__(cls, current_str, autor):
        instance = super().__new__(cls, current_str)
        instance.autor = autor
        instance.time_create = datetime.datetime.today()


        print(instance)
        return instance


spam = MyString('чудный день', 'сурок')

print(f'{spam.autor = }, {spam.time_create}')
