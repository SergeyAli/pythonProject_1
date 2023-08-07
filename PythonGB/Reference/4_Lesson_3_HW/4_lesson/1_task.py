# ------------------------------------------- 1 -----------------------------
# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки

def func(text: str) -> None:
    text = sorted(text.split())
    max_len = len(max(text, key=len))

    for i, world in enumerate(text, start=1):
        print(f'{i}. {world:>{max_len}}')


func('Каждый охотник желает знать где сидит фазан')