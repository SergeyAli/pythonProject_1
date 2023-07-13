# Доступ через метод get
# Если ли мы хотим гарантировать отсутствие ошибки KeyError при обращении к элементу словаря, можно обратиться
# к значению через метод get, а не квадратные скобки.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))