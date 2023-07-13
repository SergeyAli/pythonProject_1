# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX : int = 16

num: int = int(input('Введите число: '))
def convert_to(number, base, upper=False):
    digits = '0123456789abcdef'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

print(convert_to(num, HEX))

print(hex(num)[2:])