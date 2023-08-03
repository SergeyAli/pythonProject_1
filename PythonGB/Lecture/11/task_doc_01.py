'''
2. Строка документации
Как и при создании функции, при создании классов принято оставлять документацию к нему. Для этого достаточно
использовать многострочный комментарий сразу после определения класса — строки class ClassName: Посмотрите на пример
'''

class User:
    """A User training class for demonstrating class documentation.
    Shows the operation of the help(cls) and the dander method __doc__"""

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_1 = User('Спенглер')
print('Справка класса User ниже', '*' * 50)
help(User)
print('Справка экземпляра u_1 ниже', '*' * 50)
help(u_1)

