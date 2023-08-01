'''
Задание №3
📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
 который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой функции.
'''

from typing import Callable, Any
import json
import os


def fun_decor_file(fun: Callable) -> Callable[..., None]:
    def wrapper(*args, **kwargs):
        spam_dict = dict()

        file_json = f'{fun.__name__}.json'
        if os.path.exists(file_json):
            with open(file_json, 'r', encoding='utf-8') as fj:
                spam_dict = json.load(fj)

        spam_dict[str(args)] = args
        spam_dict.update(**kwargs)
        spam_dict['result'] = fun(*args, **kwargs)

        with open(file_json, 'w', encoding='utf-8') as fj:
            json.dump(spam_dict, fj, indent=2, ensure_ascii=False)

    return wrapper


@fun_decor_file
def get_all(*args, **kwargs) -> tuple[tuple[Any, ...], dict[str, Any]]:
    return args, kwargs


if __name__ == '__main__':
    get_all(2, 'wert', True, reg=8, funs='ewww')
    get_all(233, 'round', False, upper=3699, region='sun')
