# Функция filter()
# filter(function, iterable) — принимает на вход функцию и последовательность.
# Если функция возвращает истину, элемент остаётся в последовательности. Как и map возвращает объект итератор.

"""filter(function, iterable)"""

numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)