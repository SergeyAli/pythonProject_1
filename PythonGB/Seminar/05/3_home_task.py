'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

number = int(input(f'Введите количество чисел Фибоначчи которое хотите вывести:\n'))
print(*(fib(number)))
