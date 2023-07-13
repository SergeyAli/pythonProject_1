# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# texts = sorted(input('Введите несколько слов: ').split())
#
# max_len = 0
# for word in texts:
#     if len(word) > max_len:
#         max_len = len(word)
#
# for i, word in enumerate(texts, 1):
#     print(f'{i}. {word:>{max_len}}')


def task_6(current_txt: str):
    list_work = current_txt.split()
    list_work.sort()
    maxlen = 0

    for item in list_work:
        if maxlen < len(item):
            maxlen = len(item)

    for i, item in enumerate(list_work, start=1):
        print(f'{i}. {item:>{maxlen}}')


txt = 'самые мягкие лапки'
task_6(txt)