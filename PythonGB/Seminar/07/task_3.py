'''
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
'''

import random
from random import randint, uniform, shuffle

MIN_LEN_PS = 4
MAX_LEN_PS = 7
STR_VOWEL = 'eyuioa'
STR_CHAR = 'qwrtpsdfghjklzxcvbnm'
MIN_NUM = -1000
MAX_NUM = 1000


def gen_psevdonim(name_file: str):
    spam = random.sample(STR_CHAR, randint(MIN_LEN_PS, MAX_LEN_PS - 1))
    eggs = random.sample(STR_VOWEL, randint(1, len(STR_VOWEL)))
    eggs.extend(spam)
    eggs = eggs[:random.randint(MIN_LEN_PS, MAX_LEN_PS)]
    random.shuffle(eggs)
    print(eggs)
    with open(name_file, 'a', encoding='utf-8') as f:
        f.write(f'{"".join(eggs).title()}\n')

