'''
Кроме выборочного импорта можно создавать псевдонимы для объектов через
зарезервированное слово as. При этом доступ к объекту будет возможен только
через псевдоним. Один объект — одно имя.
'''

import random as rnd
from sys import builtin_module_names as bmn, path as p

print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
print(path) # NameError: name 'path' is not defined
print(sys.path) # NameError: name 'sys' is not defined