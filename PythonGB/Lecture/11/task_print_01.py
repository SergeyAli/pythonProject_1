'''
3. Представления экземпляра
При работе с классами, а точнее с их экземплярами бывает необходимо вывести их содержимое в консоль. С этим отлично
справляется функция print, но есть одно но. Попробуем “запринтить” класс из примера выше.
'''

class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

user = User('Спенглер')
print(user)



