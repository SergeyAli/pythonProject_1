'''
Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов.
'''

import random
import json


def save_params(func):
    def wrapper(*args, **kwargs):
        params = {
            "args": args,
            "kwargs": kwargs
        }

        filename = func.__name__ + "_params.json"
        with open(filename, "w") as file:
            json.dump(params, file, indent=4)

        result = func(*args, **kwargs)
        return result

    return wrapper


def validate_values(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Аргументы должны быть целыми числами")
        for value in kwargs.values():
            if not isinstance(value, int):
                raise ValueError("Аргументы ключевого слова должны иметь целочисленные значения")

        result = func(*args, **kwargs)
        return result

    return wrapper


def repeat_func(repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeats):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat_func(3)
@validate_values
@save_params

def guess_number(number):
    guess = random.randint(1, 10)
    if number == guess:
        return "Поздравляю, вы угадали!"
    else:
        return "Мои соболезнования, но вам не повезло с ответом"

if __name__ == '__main__':
    guess_number(5)
