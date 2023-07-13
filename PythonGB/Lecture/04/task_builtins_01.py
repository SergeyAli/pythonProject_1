# Функция map()
# map(function, iterable) — принимает на вход функцию и последовательность.
# Функция применяется к каждому элементу последовательности и возвращает map итератор.
"""map(function, iterable)"""

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)