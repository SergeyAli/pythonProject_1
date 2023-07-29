# Второй параметр функции iter — sentinel передают для вызываемых объектов-итераторов.
# Параметр указывает в какой момент должна быть завершена итерация,
# при совпадении возвращаемого значения со значением sentinel.

data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()
