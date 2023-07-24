'''
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''
import random
from random import randint, uniform, shuffle

MIN_LEN_PS = 4
MAX_LEN_PS = 7
STR_VOWEL = 'eyuioa'
STR_CHAR = 'qwrtpsdfghjklzxcvbnm'
MIN_NUM = -1000
MAX_NUM = 1000


def add_number(count: int, name_file: str):
    with open(name_file, 'a', encoding='utf-8') as f:
        for i in range(0, count):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')

def gen_psevdonim(name_file: str):
    spam = random.sample(STR_CHAR, randint(MIN_LEN_PS, MAX_LEN_PS - 1))
    eggs = random.sample(STR_VOWEL, randint(1, len(STR_VOWEL)))
    eggs.extend(spam)
    eggs = eggs[:random.randint(MIN_LEN_PS, MAX_LEN_PS)]
    random.shuffle(eggs)
    print(eggs)
    with open(name_file, 'a', encoding='utf-8') as f:
        f.write(f'{"".join(eggs).title()}\n')


if __name__ == '__main__':
   gen_psevdonim('task01.txt')